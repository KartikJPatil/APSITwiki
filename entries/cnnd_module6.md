
# Module 6: Network Design Concepts
We will cover the following topics:
>- Introduction to VLAN 
- VPN A case study to design a network for an organization meeting the following guidelines: Networking Devices
- IP addressing: Subnetting, Supernetting, Routing Protocols to be used
- Services to be used: TELNET, SSH, FTP server, Web server, File server, DHCP server and DNS server


<p id="L10"></p>
### Virtual LAN :
Virtual Local Area Networks or Virtual LANs (VLANs) are a logical group of computers that appear to be on the same LAN irrespective of the configuration of the underlying physical network. 
Network administrators partition the networks to match the functional requirements of the VLANs so that each VLAN comprises a subset of ports on single or multiple switches or bridges. 
This allows computers and devices in a VLAN to communicate in the simulated environment as if it is a separate LAN.





<p id="L20"></p>
#### Features of VLANs
A VLAN forms a sub-network grouping together devices on separate physical LANs.
VLANs help the network manager to segment LANs logically into different broadcast domains.
VLANs function at layer 2, i.e. Data Link Layer of the OSI model.
There may be one or more network bridges or switches to form multiple, independent VLANs.

Using VLANs, network administrators can easily partition a single switched network into multiple networks depending upon the functional and security requirements of their systems.
VLANs eliminate the requirement to run new cables or reconfigure physical connections in the present network infrastructure.
VLANs help large organizations to re-partition devices aiming for improved traffic management.
<p id="L30"></p>
VLANs also provide better security management allowing the partitioning of devices according to their security criteria and also ensuring a higher degree of control over connected devices.
VLANs are more flexible than physical LANs since they are formed by logical connections. This aids is a quicker and cheaper reconfiguration of devices when the logical partitioning needs to be changed.
#### Types of VLANs
1. Protocol VLAN − 
 Here, the traffic is handled based on the protocol used. A switch or bridge segregates, forwards or discards frames the come to it based upon the traffics protocol.
2. Port-based VLAN − 
 This is also called static VLAN. Here, the network administrator assigns the ports on the switch / bridge to form a virtual network.
3. Dynamic VLAN − 
 Here, the network administrator simply defines network membership according to device characteristic
<p id="L40"></p>
### VPN(Virtual Private Network): 
Information traveling between a connected device (computer, smartphone, tablet) and a VPN server is encrypted, and as a result, any applications running on the VPN network benefit from the security, functionality, and strength of the private network. 
Internet Protocol Security (IPSec) is a framework of open standards for ensuring private, secure communications over Internet Protocol (IP) networks, through the use of cryptographic security services.
IPSec supports network-level peer authentication, data origin authentication, data integrity, data confidentiality (encryption), and replay protection. 
Internet protocol security (IPsec) is a set of protocols that provides security for Internet Protocol. It can use cryptography to provide security. IPsec can be used for the setting up of virtual private networks (VPNs) in a secure manner. 

IPsec involves two security services: 


<p id="L50"></p>
- Authentication Header (AH): This authenticates the sender and it discovers any changes in data during transmission.
- Encapsulating Security Payload (ESP): This not only performs authentication for the sender but also encrypts the data being sent.
- There are two modes of IPsec:
 - Tunnel Mode: This will take the whole IP packet to form secure communication between two places, or gateways.
 - Transport Mode: This only encapsulates the IP payload (not the entire IP packet as in tunnel mode) to ensure a secure channel of communication.




<p id="L60"></p>

### VPN connections are used in two important ways −

1. To establish WAN connections using VPN technology between two distant networks that may be thousands of miles apart, but where each has some way of accessing the internet.
2. To establish remote access connections that enable remote users to access a private network through a public network like the internet.

##### Types of VPNs
The types of VPNs are as follows −
>1. Router VPN
<p id="L70"></p>
The first type uses a router with added VPN capabilities. A VPN router cannot only handle normal routine duties, but it can also be configured to form VPNs over the internet to other similar routers located in remote networks.
>2. Firewall VPN

The second type of VPN is one built into a firewall device. Firewall VPN can be used both to support remote users and also to provide VPN links.
3. Network Operating System
The third type of VPNs include those offered as part of a network operating system like Windows NT, Windows 2000, and Netware 5. These VPNs are commonly used to support remote access, and they are generally the least expensive to purchase and install.



<p id="L80"></p>
## TELNET
The main task of the internet is to provide services to users. For example, users want to run different application programs at the remote site and transfers a result to the local site. This requires a client-server program such as FTP, SMTP. But this would not allow us to create a specific program for each demand.
The better solution is to provide a general client-server program that lets the user access any application program on a remote computer. Therefore, a program that allows a user to log on to a remote computer. A popular client-server program Telnet is used to meet such demands. Telnet is an abbreviation for Terminal Network. 
Telnet provides a connection to the remote computer in such a way that a local terminal appears to be at the remote side.Telnet is a network protocol used to virtually access a computer and to provide a two-way, collaborative and text-based communication channel between two machines. It follows a user command Transmission Control Protocol/Internet Protocol (TCP/IP) networking protocol for creating remote sessions.

In order to access the system the user logs in to the system by the user-id.The system also includes password checking in order to prevent unauthorized access to the resources of a system.
There are two types of login:
>1. Local Login

<p id="L90"></p>
When a user logs into a local computer, then it is known as local login.
When the workstation running terminal emulator, the keystrokes entered by the user are accepted by the terminal driver. The terminal driver then passes these characters to the operating system which in turn, invokes the desired application program.
However, the operating system has special meaning to special characters. For example, in UNIX some combination of characters have special meanings such as control character with "z" means suspend. Such situations do not create any problem as the terminal driver knows the meaning of such characters. But, it can cause the problems in remote login.

2. Remote login

When the user wants to access an application program on a remote computer, then the user must perform remote login.
How remote login occurs
- At the local site
<p id="L100"></p>
The user sends the keystrokes to the terminal driver, the characters are then sent to the TELNET client. The TELNET client which in turn, transforms the characters to a universal character set known as network virtual terminal characters and delivers them to the local TCP/IP stack
- At the remote site

The commands in NVT forms are transmitted to the TCP/IP at the remote machine. Here, the characters are delivered to the operating system and then pass to the TELNET server. The TELNET server transforms the characters which can be understandable by a remote computer. However, the characters cannot be directly passed to the operating system as a remote operating system does not receive the characters from the TELNET server. Therefore it requires some piece of software that can accept the characters from the TELNET server. The operating system then passes these characters to the appropriate application program.

### SSH
SSH stands for Secure Shell or Secure Socket Shell. It is a cryptographic network protocol that allows two computers to communicate and share the data over an insecure network such as the internet. It is used to login to a remote server to execute commands and data transfer from one machine to another machine.
The SSH protocol was developed by SSH communication security Ltd to safely communicate with the remote machine.
Secure communication provides a strong password authentication and encrypted communication with a public key over an insecure channel. It is used to replace unprotected remote login protocols such as Telnet, rlogin, rsh, etc., and insecure file transfer protocol FTP.
<p id="L110"></p>
Its security features are widely used by network administrators for managing systems and applications remotely.The SSH protocol protects the network from various attacks such as DNS spoofing, IP source routing, and IP spoofing.
A simple example can be understood, such as suppose you want to transfer a package to one of your friends. Without SSH protocol, it can be opened and read by anyone. But if you will send it using SSH protocol, it will be encrypted and secured with the public keys, and only the receiver can open it.

#### How does SSH Works?
The SSH protocol works in a client-server model, which means it connects a secure shell client application (End where the session is displayed) with the SSH server (End where session executes).

As discussed above, it was initially developed to replace insecure login protocols such as Telnet, rlogin, and hence it performs the same function.


<p id="L120"></p>
The basic use of SSH is to connect a remote system for a terminal session and to do this, following command is used:

```ssh UserName@SSHserver.test.com ``` 

The above command enables the client to connect to the server, named server.test.com, using the ID UserName.