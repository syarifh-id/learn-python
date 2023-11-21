import nmap

nm = nmap.PortScanner()
host = "192.168.1.1"

nm.scan(host, "1-1024")

for host in nm.all_hosts():
    print("host : %s (%s)" (host, nm[host].hostname()))
    print("State : %s " % nm[host].state())
    for proto in nm[host].all_protocols():
        print("---------")
        print("Protocol :%s " % proto)
