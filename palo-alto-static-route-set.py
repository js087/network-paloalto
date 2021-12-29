#modules
import datetime

#route counting
route_counter = 1 #{route_counter:03} is a way to 'zfill' place values

#firewall specifics
firewall_virtual_router = '<virtual_router>' #'company'
firewall_tunnel = <tunnel_id> #e.g. 1000

#static routes to be built and other parameters
firewall_routes = [
'10.0.0.0/16',
'10.1.0.0/16',
'10.2.0.0/16',
'10.3.0.0/16'
]

firewall_routes_metric = 10
firewall_routes_install = 'unicast' #'no-install'

#To apply these commands via CLI, you need CLI access and will need to change the config-out to 'cli'
#set cli config-output-format set
#https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClHoCAK

for route in firewall_routes:
    config_output = f"""
set network virtual-router {firewall_virtual_router} routing-table ip static-route tun{firewall_tunnel}-route{route_counter:03} path-monitor failure-condition any
set network virtual-router {firewall_virtual_router} routing-table ip static-route tun{firewall_tunnel}-route{route_counter:03} path-monitor hold-time 2
set network virtual-router {firewall_virtual_router} routing-table ip static-route tun{firewall_tunnel}-route{route_counter:03} bfd profile None
set network virtual-router {firewall_virtual_router} routing-table ip static-route tun{firewall_tunnel}-route{route_counter:03} interface tunnel.{firewall_tunnel}
set network virtual-router {firewall_virtual_router} routing-table ip static-route tun{firewall_tunnel}-route{route_counter:03} metric {firewall_routes_metric}
set network virtual-router {firewall_virtual_router} routing-table ip static-route tun{firewall_tunnel}-route{route_counter:03} destination {route}
set network virtual-router {firewall_virtual_router} routing-table ip static-route tun{firewall_tunnel}-route{route_counter:03} route-table {firewall_routes_install}
    """
    
    #print meat and potatoes of config
    print(config_output)
    route_counter += 1

#timestamping
print(f"***** Generated: {datetime.datetime.now()} ***** ")
