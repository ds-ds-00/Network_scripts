#!/usr/bin/python3
import argparse
import subprocess
import shlex

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
    print(change)


options=get_arguments()
chane_mac(options.iface,options.New_Mac)
