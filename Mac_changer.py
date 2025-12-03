#!/usr/bin/python3
import argparse
import subprocess
import shlex
import re

def get_arguments():
    parser=argparse.ArgumentParser(description="mac changer") 
    parser.add_argument("-i","--interface",dest="iface",help="network_interface",metavar="",required=True)
    parser.add_argument("-m ","--mac",dest="New_Mac",help="New MAC address",metavar="",required=True)
    parser.add_argument("-os","--os", choices=["linux"], help="eg: -os linux", metavar="",required=True)
    args=parser.parse_args()
    return args
    

def chane_mac(iface,New_Mac):
    print(f"[+] Changing the mac address for {iface} to {New_Mac}")
    down=shlex.split(f"ifconfig {iface} down")
    up=shlex.split(f"ifconfig {iface} up")
    change=shlex.split(f"ifconfig {iface} hw ether {New_Mac}")
    subprocess.call(down)
    subprocess.call(change)
    subprocess.call(up)
    

def current_mac(iface):
    result=subprocess.check_output(shlex.split(f"ifconfig {iface}"),text=True) 
    mac_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",result)
    return mac_result.group(0)



options=get_arguments()
chane_mac(options.iface,options.New_Mac)

curr_mac=current_mac(options.iface)
print(f"current mac is {curr_mac}")


if curr_mac==options.New_Mac:
    print(f"[+] MAC address successfully changed to {options.New_Mac}")
else:
    print(f"[-] MAC address did not changed")

