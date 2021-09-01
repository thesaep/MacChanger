import subprocess
import optparse                                           # Kullanıcının dışarıdan input girebilmesini ve ona karşı programın bir output dökmesini sağlar. Örneğin, "macchanger -help" gibi..
import re


def get_user_input():

    parse_object = optparse.OptionParser()                                                   # Kullanıcının girdiği argümanlarla input alma.
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")

    return parse_object.parse_args()

def change_mac_address(user_interface,user_mac_address):                       # MAC Adresi değişme.
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig", user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):                                                # Değişen MAC adresini kontrol etme.

    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))        # str kısmı python3 uyumluluğu için eklendi.

    if new_mac:                                                                
        return new_mac.group(0)                                                # Yeni Mac'i gösteriyor.
    else:
        return None

print("MyMacChanger started!")
(user_input,arguments) = get_user_input()
change_mac_address(user_input.interface,user_input.mac_address)
finalized_mac = control_new_mac(str(user_input.interface))                     # str kısmı python3 uyumluluğu için eklendi.

if finalized_mac == user_input.mac_address:
    print("Success!")
else:
    print("Error!")