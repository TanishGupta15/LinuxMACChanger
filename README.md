# Linux MAC Changer
A simple python script that can be run in Linux environment to change default MAC address to any desired  MAC address.

Usage:

  Run the script in your terminal by using "python mac_changer.py --help" to get different arguments that can be used.
  
  Command: python mac_changer.py --interface your_interface --mac new_mac
  
  where your_interface and new_mac are the interface you want to change MAC for and the MAC you want to set.
 
 
I have used 3 python modules:
  1. Subprocess - To execute terminal commands from python script
  2. optparse   - To read command-line arguments
  3. re         - To identify MAC address using regular expressions



PS: You can only change the MAC address to a Unicast MAC Address i.e. the first octet has to have an even value.


