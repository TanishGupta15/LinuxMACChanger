import subprocess  # to run terminal commands from python script
import optparse  # to read arguments from terminal commands
import re  # regular expression


def get_arguments():
    parser = optparse.OptionParser()
    # This library is used to get in-line arguments from command line.
    # First create an object of the class optparse
    parser.add_option("-i", "--interface", dest="interface", help="interface to change MAC address")
    # The add_option function is used to add the type of arguments that can be specified
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()
    # Finally parse the arguments. Returns a pair, of arguments and their inputs(options).
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify an interface, use --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing mac address for " + interface + " to " + new_mac)
    # The subprocess module is used to execute terminal commands from python script
    # To change the mac address, use ifconfig commands on LINUX.
    subprocess.call(["ifconfig", interface, "down"])
    # interface specifies which network's MAC has to be changed (eg: eth0 or wlan0).
    # For more details on this, first type ifconfig on your system.
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # This command captures the output of the terminal command - "ifconfig $interface"
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode('utf-8'))
    # regex expression that finds the mac address. \w stands for alphanumeric character.
    # Decode the ifconfig_result into UTF-8 string, to be compatible for finding regex.
    if mac_address_search_result:
        return mac_address_search_result.group(0)
        # If there are a number of matches, they are put in groups. Interested in only first occurance.
    else:
        # Error in reading MAC address
        print("[-] Could not read MAC address")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")
