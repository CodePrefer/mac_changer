#! usr/bin/env python3

import subprocess
import optparse
import re

def optionParameters():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface", help="Enter interfce which you want to change")
	parser.add_option("-m","--mac_address",dest="new_mac", help="Enter new mac")
	(options,arguments)=parser.parse_args()
	return options


parameters = optionParameters()

interface = parameters.interface
mac = parameters.new_mac

if not interface:
    print("Please check help using '--help'")
else:
    subprocess.call(["sudo","ifconfig", interface, "down"])
    Old_Mac_add = str(subprocess.check_output(["sudo","ifconfig", interface]))
    show_old = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", Old_Mac_add)
    subprocess.call(["sudo","ifconfig", interface,"hw","ether", mac])
    subprocess.call(["sudo","ifconfig", interface, "up"])
    New_Mac_add = str(subprocess.check_output(["ifconfig", interface]))
    show_new = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", New_Mac_add)
    print("Welcome to Mac Address Changer")
    print("Your old MAC Address :",show_old.group(0))
    print("The new MAC Address has been updated", ":", show_new.group(0))
    print("Thanks for using \n CodePrefer")
