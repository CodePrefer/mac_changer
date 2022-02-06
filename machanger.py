#! usr/bin/env python3

import subprocess
import optparse
import re

def optionParameters():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface", help="Enter interfce which you want to change")
	parser.add_option("-m","--mac_address",dest="new_mac", help="For New Mac Address")
	(options,arguments)=parser.parse_args()
	return options


parameters = optionParameters()

interface = parameters.interface
mac = parameters.new_mac

if not interface:
    print("Please check help using '--help'")
else:
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface,"hw","ether", mac])
    subprocess.call(["ifconfig", interface, "up"])
    New_Mac_add = str(subprocess.check_output(["ifconfig", interface]))
    show = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", New_Mac_add)
    print("The new MAC address has been updated. ", "\nMac_Address :", show.group(0))
    print("End ............")
