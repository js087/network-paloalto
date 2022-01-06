#build proxy id from palo alto firewall to juniper srx via existing ipsec tunnel
#modules
import datetime

#mark start timestamp
begin_time = datetime.datetime.now()

#traffic-selector counting
ts_counter = 0
pa_vpn = '<pa_vpn_name>'

#traffic-selector ip subnets to be built
firewall_routes_pa = [
'10.2.1.0/24',
'10.2.2.0/24',
'10.2.3.0/24',
'10.2.4.0/24',
'10.2.5.0/24',
'10.2.6.0/24'
]

firewall_routes_srx = [
'10.0.1.0/24',
'10.0.2.0/24',
'10.0.3.0/24',
'10.0.4.0/24',
'10.0.5.0/24',
'10.0.6.0/24'
]



for route_pa in firewall_routes_pa:
    for route_srx in firewall_routes_srx:
        config_output = f"""
set network tunnel ipsec {pa_vpn} auto-key proxy-id ts{ts_counter:03} protocol any 
set network tunnel ipsec {pa_vpn} auto-key proxy-id ts{ts_counter:03} local {route_pa}
set network tunnel ipsec {pa_vpn} auto-key proxy-id ts{ts_counter:03} remote {route_srx}"""
        print(config_output)
        ts_counter += 1

#timestamping
print(f"***** Generated: {datetime.datetime.now()} || Runtime: {datetime.datetime.now() - begin_time} ***** ")
