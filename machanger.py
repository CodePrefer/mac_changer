#! usr/bin/env python3

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface", help="Interface name for changing Mac address")
parser.add_option("-m","--mac_address",dest="new_mac", help="New Mac address for selected interface")
(options,arguments)=parser.parse_args()

interface = options.interface
mac = options.new_mac

if not interface:
    print("please show help")
else:
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("End ............")
