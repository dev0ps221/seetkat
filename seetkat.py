import os
import sys
from termcolor import colored
from pyfiglet import figlet_format

def banner():
    os.system('clear')
    print(colored(figlet_format('seet-kat', font='standard'), 'green'))
    print(colored('Welcome to SEET-KAT\n', 'green'))
    print(colored("-----------by Seybatou Mbengue °*.. .\n", 'white'))
banner()

def menu():
    print(colored('1. Start Network Scan', 'blue'))
    print(colored('2. Exit', 'blue'))

def scan_network():
    target_ip = input(colored('\nEnter target IP/ IP range (e.g. "192.168.1.1/24"): ', 'blue'))
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("Appareils disponibles sur le réseau:")
    print("IP" + " "*18+"MAC")
    for device in devices:
        print("{:16}    {}".format(device['ip'], device['mac']))

def main():
    from scapy.all import ARP, Ether, srp

    while True:
        menu()
        choice = input(colored('\nChoisissez une option: ', 'blue'))
        if choice == '1':
            scan_network()
        elif choice == '2':
            print(colored('Au revoir...', 'red'))
            sys.exit(0)
        else:
            print(colored('Option invalide. Choisissez une option valide.', 'red'))
        input("Appuyer sur une touche...")

if __name__ == '__main__':
    main()
