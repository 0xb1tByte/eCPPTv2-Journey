"""
pythoNMAP : a simple script that automates some of nmap scanning options
Version : 1.0
Pyhton Version : 3.7
License : GNU LESSER GENERAL PUBLIC LICENSE Version 3
"""
import nmap
import ipaddress
from prettytable import PrettyTable


# TODO :
#       1 - Validating address/netmask =====> DONE
#       2 - Host Discovery =================> DONE
#       3 - List all OPEN Ports ============> DONE
#       4 - Extract all DNS Servers ========> DONE
#       5 - Extract all WEB Servers ========> UNDER DEV.
#       6 - Extract all FTP Servers ========> DONE
#       7 - Extract all DB Servers =========> UNDER DEV.
#       8 - Scan certain Port/s ============> UNDER DEV.


def Banner():
    print("""
\033[37m+-----------------------------------------------+
         _   _      \033[1;31m _____ _____ _____ _____ \033[0m
 ___ _ _| |_| |_ ___\033[1;31m|   | |     |  _  |  _  |\033[0m
| . | | |  _|   | . \033[1;31m| | | | | | |     |   __|\033[0m
|  _|_  |_| |_|_|___\033[1;31m|_|___|_|_|_|__|__|__|\033[0m   
|_| |___|

\033[0mBy: \033[1;31mAlaa , aka: b1tByte\033[0m | github: 0xb1tByte\033[0m
\033[37m+-----------------------------------------------+                                     
""")

class pythoNMAP :

    #  ----- Class Variables ----- #
    # Instantiate the nmap port scanner
    ns = nmap.PortScanner()
    # Colors
    red = '\033[1;31m'
    green = '\033[92m'
    reset = '\033[0m'
    # ----------- END ------------ #

    # --------------------- Class Methods --------------------- #
    def Menu(self):
        # Validating address/netmask
        try:
            network = ipaddress.IPv4Network(input("Please Enter address/netmask : "))
            print ("+------ "+self.red+"+Host Discovery " +self.reset+ " ------+ ")
            self.HostDiscovery(str(network))
            print("\n")
            print("+------ "+self.red+"OpenPorts" +self.reset+ " ------+ ")
            self.OpenPorts(str(network))
            print("\n")
            print("+------ "+self.red+"DNS Servers" +self.reset+ " ------+ ")
            self.ExtractDNServers(str(network))
            print("\n")
            print("+------ "+self.red+"FTP Servers" +self.reset+ " ------+ ")
            self.ExtractFTPServers(str(network))
        except ValueError:
            print('address/netmask is invalid for IPv4')

    def HostDiscovery (self,network):
        # Set options:
        options = '-sn -n'
        # Starting the Scan
        self.ns.scan(hosts=network, arguments=options)
        counter = 0
        # Counting the number of live hosts
        for host in self.ns.all_hosts():
             if (self.ns[host].state() == 'up'):
                 counter+=1
        # Pass the result to the table
        table = PrettyTable(['Host', 'State'])
        for host in self.ns.all_hosts():
            table.add_row([host,self.ns[host].state()])
        # Printing the results
        print (table.get_string(title="HostDiscovery"))
        print("Number of live Hosts : "+self.green+str(counter)+self.reset)

    def OpenPorts (self,network):
        # Set options
        options = '-sS -p-'
        # Starting the Scan
        self.ns.scan(hosts=network, arguments=options)
        table = PrettyTable(['Host','Open Port'])
        for host in self.ns.all_hosts():
            for protocol in self.ns[host].all_protocols():
                portsList = list(self.ns[host][protocol].keys())
                portsList.sort()
                # Pass the result to the table
                table.add_row([host, portsList])
        # Printing the results
        print(table)

    def ExtractDNServers(self, network):
        # Set options
        options = '-sS -sU -p 53'
        # Starting the Scan
        self.ns.scan(hosts=network, arguments=options)
        table = PrettyTable(['Host','Protocol','Port'])
        counter = 0
        for host in self.ns.all_hosts():
            # Check if Both TCP & UDP ports are 'open'
            if ((self.ns[host]['tcp'][53]['state'] == 'open') & (self.ns[host]['udp'][53]['state'] == 'open')):
                table.add_row([host,'TCP & UDP','53'])
                counter+=1
            # if not, Check if TCP port is 'open'
            elif (self.ns[host]['tcp'][53]['state'] == 'open'):
                table.add_row([host, 'TCP','53'])
                counter += 1
            # if not, Check if UDP port is 'open'
            elif (self.ns[host]['udp'][53]['state'] == 'open'):
                table.add_row([host, 'UDP','53'])
                counter += 1
        print(table)
        print("Number of DNS Server/s : " +self.green+ str(counter)+self.reset)

    def ExtractFTPServers(self, network):
        # Set options
        options = '-sS -p 20,21'
        # Starting the Scan
        self.ns.scan(hosts=network, arguments=options)
        table = PrettyTable(['Host','Protocol','Port'])
        counter = 0
        for host in self.ns.all_hosts():
            # Check if 20 port is 'open'
            if (self.ns[host]['tcp'][20]['state'] == 'open'):
                table.add_row([host, 'TCP', '20'])
                counter+=1
            # if not, Check if 21 port is 'open'
            elif (self.ns[host]['tcp'][21]['state'] == 'open'):
                table.add_row([host, 'TCP','21'])
                counter += 1
        print(table)
        print("Number of FTP Server/s : " +self.green+str(counter)+self.reset)

    # --------------------- END --------------------- #


def main():
    Banner()
    nm = pythoNMAP()
    nm.Menu()


if __name__ == "__main__":
    main()

