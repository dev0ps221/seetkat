import tkinter as tk
from scapy.all import ARP, Ether, srp
from tkinter import messagebox

def scan_network():
    target_ip = ip_entry.get()
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, "Appareils disponibles sur le réseau:\n")
    result_text.insert(tk.END, "IP" + " "*18+"MAC\n")
    for device in devices:
        result_text.insert(tk.END, "{:16}    {}\n".format(device['ip'], device['mac']))

root = tk.Tk()
root.title("SEET-KAT")

welcome_label = tk.Label(root, text="Welcome to SEET-KAT\n-----------by Seybatou Mbengue °*.. .\n")
welcome_label.pack()

ip_label = tk.Label(root, text="Enter target IP/ IP range (e.g. '192.168.1.1/24'):")
ip_label.pack()

ip_entry = tk.Entry(root)
ip_entry.pack()

scan_button = tk.Button(root, text="Start Network Scan", command=scan_network)
scan_button.pack()

result_text = tk.Text(root)
result_text.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()