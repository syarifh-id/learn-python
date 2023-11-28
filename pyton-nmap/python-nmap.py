import nmap

nm = nmap.PortScanner()
host = "192.168.1.1"

nm.scan(host, "1-1024")

for host in nm.all_hosts():
    print("host : %s (%s)" % (host, nm[host].hostname()))
    print("State : %s " % nm[host].state())
    for proto in nm[host].all_protocols():
        print("---------")
        print("Protocol :%s " % proto)


# import nmap


# def scan_ports(target):
#     # Membuat objek nm dari kelas PortScanner
#     nm = nmap.PortScanner()

#     # Melakukan pemindaian port terhadap target
#     nm.scan(target, arguments='-p 1-1000')

#     # Menampilkan hasil pemindaian
#     for host, result in nm.all_hosts().items():
#         print(f"Host: {host}")
#         print(f"State: {result['status']['state']}")
#         print("Open Ports:")

#         for protocol, ports in result['tcp'].items():
#             for port, state in ports.items():
#                 print(f"    {protocol.upper()} Port {port}: {state['state']}")


# if __name__ == "__main__":
#     target_ip = input("Masukkan alamat IP target: ")
#     scan_ports(target_ip)
