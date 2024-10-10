# Module 3 : Network Layer
> - Network Layer Services
- Packet Switching
- Network Layer Performance
- IPv4 Addressing (classful and classless)
- Subnetting
- Supernetting
- IPv4 Protocol
- DHCP
<p id="L10"></p>
### Network Address Translation (NAT).
Objectives :
>- The network layer is responsible for the source-to-destination delivery of a packet, possibly across multiple networks (links). Whereas the data link layer oversees the delivery of the packet between two systems on the same network (links), the network layer ensures that each packet gets from its point of origin to its final destination.
- The network layer adds a header that includes the logical addresses of the sender and receiver to the packet corning from the upper layer. If a packet travels through the Internet, we need this addressing system to help distinguish the source and destination. 
- When independent networks or links are connected together to create an internetwork, routers or switches route packets to their final destination. One of the functions of the network layer is to provide a routing mechanism.


Thus, Network layer is majorly focused on getting packets from the source to the destination, routing error handling and congestion control.

<p id="L20"></p>
Various functions of network layer:
>- Addressing:
Maintains the address at the frame header of both source and destination and performs addressing to detect various devices in the network.
- Packeting:
This is performed by Internet Protocol. The network layer converts the packets from its upper layer.
- Routing:
It is the most important functionality. The network layer chooses the most relevant and best path for the data transmission from source to destination.
- Inter-networking:
It works to deliver a logical connection across multiple devices.
<p id="L30"></p>

##Network layer design issues:
The network layer comes with some design issues they are described as follows:


1. Store and Forward packet switching:
The host sends the packet to the nearest router. This packet is stored there until it has fully arrived once the link is fully processed by verifying the checksum then it is forwarded to the next router till it reaches the destination. This mechanism is called “Store and Forward packet switching.”


<p id="L40"></p>
2. Services provided to Transport Layer:
Through the network/transport layer interface, the network layer transfers it’s services to the transport layer. These services are described below.
But before providing these services to the transfer layer following goals must be kept in mind :-


Offering services must not depend on router technology.
The transport layer needs to be protected from the type, number and topology of the available router.
The network addresses for the transport layer should use uniform numbering patterns also at LAN and WAN connections.
Based on the connections there are 2 types of services provided :
<p id="L50"></p>

Connectionless – The routing and insertion of packets into subnet is done individually. No added setup is required.
Connection-Oriented – Subnet must offer reliable service and all the packets must be transmitted over a single route.


3. Implementation of Connectionless Service:
Packet are termed as “datagrams” and corresponding subnet as “datagram subnets”. When the message size that has to be transmitted is 4 times the size of the packet, then the network layer divides into 4 packets and transmits each packet to router via. a few protocol.Each data packet has destination address and is routed independently irrespective of the packets.


<p id="L60"></p>
4. Implementation of Connection Oriented service:
To use a connection-oriented service, first we establishes a connection, use it and then release it. In connection-oriented services, the data packets are delivered to the receiver in the same order in which they have been sent by the sender.







<p id="L70"></p>
It can be done in either two ways :


- Circuit Switched Connection – A dedicated physical path or a circuit is established between the communicating nodes and then data stream is transferred.
- Virtual Circuit Switched Connection – The data stream is transferred over a packet switched network, in such a way that it seems to the user that there is a dedicated path from the sender to the receiver. A virtual path is established here. While, other connections may also be using the same path.


###Packet switching-
Packet switching is a connectionless network switching technique. Here, the message is divided and grouped into a number of units called packets that are individually routed from the source to the destination. There is no need to establish a dedicated circuit for communication.
<p id="L80"></p>
Process
>1. Each packet in a packet switching technique has two parts: a header and a payload. The header contains the addressing information of the packet and is used by the intermediate routers to direct it towards its destination. The payload carries the actual data.
2. A packet is transmitted as soon as it is available in a node, based upon its header information. The packets of a message are not routed via the same path. So, the packets in the message arrive at the destination out of order. It is the responsibility of the destination to reorder the packets in order to retrieve the original message.
3. The process is diagrammatically represented in the following figure. Here the message comprises four packets, A, B, C and D, which may follow different routes from the sender to the receiver.


  

###Advantages and Disadvantages of Packet Switching
<p id="L90"></p>
####Advantages
* Delay in delivery of packets is less, since packets are sent as soon as they are available.


* Switching devices don’t require massive storage, since they don’t have to store the entire messages before forwarding them to the next node.


* Data delivery can continue even if some parts of the network faces link failure. Packets can be routed via other paths.

<p id="L100"></p>
* It allows simultaneous usage of the same channel by multiple users.


* It ensures better bandwidth usage as a number of packets from multiple sources can be transferred via the same link.


####Disadvantages
* They are unsuitable for applications that cannot afford delays in communication like high quality voice calls.

<p id="L110"></p>
* Packet switching high installation costs.


* They require complex protocols for delivery.


* Network problems may introduce errors in packets, delay in delivery of packets or loss of packets. If not properly handled, this may lead to loss of critical information.


<p id="L120"></p>

###Network Layer Performance
Performance of a network pertains to the measure of service quality of a network as perceived by the user. There are different ways to measure the performance of a network, depending upon the nature and design of the network. The characteristics that measure the performance of a network are : 
* Bandwidth
* Throughput
* Latency (Delay)
* Bandwidth – Delay Product
* Jitter

<p id="L130"></p>
- BANDWIDTH: One of the most essential conditions of a website’s performance is the amount of bandwidth allocated to the network. Bandwidth determines how rapidly the webserver is able to upload the requested information. While there are different factors to consider with respect to a site’s performance, bandwidth is every now and again the restricting element.
- THROUGHPUT 
Throughput is the number of messages successfully transmitted per unit time. It is controlled by available bandwidth, the available signal-to-noise ratio and hardware limitations. The maximum throughput of a network may be consequently higher than the actual throughput achieved in everyday consumption. The terms ‘throughput’ and ‘bandwidth’ are often thought of as the same, yet they are different. Bandwidth is the potential measurement of a link, whereas throughput is an actual measurement of how fast we can send data.
- LATENCY 
In a network, during the process of data communication, latency(also known as delay) is defined as the total time taken for a complete message to arrive at the destination, starting with the time when the first bit of the message is sent out from the source and ending with the time when the last bit of the message is delivered at the destination. The 
network connections where small delays occur are called “Low-Latency-Networks” and the network connections which            suffer from long delays are known as “High-Latency-Networks”.
- BANDWIDTH – DELAY PRODUCT 
Bandwidth and delay are two performance measurements of a link. However, what is significant in data communications is the product of the two, the bandwidth-delay product.
- JITTER 
<p id="L140"></p>
>>Jitter is another performance issue related to delay. In technical terms, jitter is a “packet delay variance”. It can simply mean that jitter is considered as a problem when different packets of data face different delays in a network and the data at the receiver application is time-sensitive, i.e. audio or video data. Jitter is measured in milliseconds(ms). It is defined as an interference in the normal order of sending data packets. For example: if the delay for the first packet is 10 ms, for the second is 35 ms, and for the third is 50 ms, then the real-time destination application that uses the packets experiences jitter.


###IPv4 Addressing (classful and classless)


An IPv4 address is a 32-bit address that uniquely and universally defines the connection of a device (for example, a computer or a router) to the Internet. IPv4 addresses are unique. They are unique in the sense that each address defines one, and only one, connection to the Internet. Two devices on the Internet can never have the same address at the same time. The IPv4 addresses are unique and universal.


<p id="L150"></p>

####Address Space
A protocol such as IPv4 that defines addresses has an address space. An address space is the total number of addresses used by the protocol. If a protocol uses N bits to define an address, the address space is 2N because each bit can have two different values (0 or 1) and N bits can have 2N values. IPv4 uses 32-bit addresses, which means that the address space is 232 or 4,294,967,296 (more than 4 billion). This means that, theoretically, if there were no restrictions, more than 4 billion devices could be connected to the Internet. We will see shortly that the actual number is much less because of the restrictions imposed on the addresses


####Notations
There are two prevalent notations to show an IPv4 address: binary notation and dotteddecimal notation. 
- Binary Notation: In binary notation, the IPv4 address is displayed as 32 bits. Each octet is often referred to as a byte. So it is common to hear an IPv4 address referred to as a 32-bit address or a 4-byte address. The following is an example of an IPv4 address in binary notation: 01110101 10010101 00011101 00000010 
- Dotted-Decimal Notation: To make the IPv4 address more compact and easier to read, Internet addresses are usually written in decimal form with a decimal point (dot) separating the bytes. The following is the dotted~decimal notation of the above address: 117.149.29.2.
<p id="L160"></p>

####Classful Addressing
IPv4 addressing, at its inception, used the concept of classes. This architecture is called classful addressing. Although this scheme is becoming obsolete, we briefly discuss it here to show the rationale behind classless addressing. In classful addressing, the address space is divided into five classes: A, B, C, D, and E. Each class occupies some part of the address space.
We can find the class of an address when given the address in binary notation or dotted-decimal notation. If the address is given in binary notation, the first few bits can immediately tell us the class of the address. If the address is given in decimal-dotted notation, the first byte defines the class. Both methods are shown in Figure.


  


<p id="L170"></p>
####Classes and Blocks
One problem with classful addressing is that each class is divided into a fixed number of blocks with each block having a fixed size as shown in Table
  



####Netid and Hostid
In classful addressing, an IP address in class A, B, or C is divided into netid and hostid. These parts are of varying lengths, depending on the class of the address. Figure 19.2 shows some netid and hostid bytes. The netid is in color, the hostid is in white. Note that the concept does not apply to classes D and E. In class A, one byte defines the netid and three bytes define the hostid. In class B, two bytes define the netid and two bytes define the hostid. In class C, three bytes define the netid and one byte defines the hostid.

<p id="L180"></p>
####Mask 
Although the length of the netid and hostid (in bits) is predetermined in classful addressing, we can also use a mask (also called the default mask), a 32-bit number made of contiguous Is followed by contiguous 0s. The concept does not apply to classes D and E.


  

The mask can help us to find the netid and the hostid. For example, the mask for a class A address has eight 1s, which means the first 8 bits of any address in class A define the netid; the next 24 bits define the hostid.


<p id="L190"></p>









<p id="L200"></p>
###Subnetting:
*  During the era of classful addressing, subnetting was introduced. If an organization was granted a large block in class A or B, it could divide the addresses into several contiguous groups and assign each group to smaller networks (called subnets).Subnetting means dividing your single network region into more than one region.
*  As we already know that IP address is the combination of network ID and host ID. Depending upon the class its network and host ID is decided. In subnetting the regions can be decided by borrowing a few bits from host ID.
* For. e.g. If you borrowed 1 bit from host ID you can divide your region into two parts. This way the division of regions can be decided. Subnetting helps to reduce the network traffic and conceals network complexity. Subnets were initially designed for solving the shortage of IP addresses over the Internet.
* The subnetting process allows the administrator to divide a single Class A, Class B, or Class C network number into smaller portions. The subnets can be subnetted again into sub-subnets. Dividing the network into a number of subnets provides the following benefits:
• Reduces the network traffic by reducing the volume of broadcasts
• Helps to surpass the constraints in a local area network (LAN), for example, the maximum
number of permitted hosts.
• Enables users to access a work network from their homes; there is no need to open the complete network.
<p id="L210"></p>

Each class of IP address has its default mask like :
- A class: 255.0.0.0
- B class: 255.255.0.0
- C class: 255.255.255.0


 But subnetting takes its own mask by taking or borrowing bits from the host and the new mask is called as subnet mask, which will be different from the default mask.
  
<p id="L220"></p>


  






<p id="L230"></p>
For. example
IP address 192.168.25.1 is a C class IP address and C class can form 254 possible hosts excluding the first IP address and the broadcast IP address. Now if any organisation has a requirement of less IP address than 254 then all the remaining IP address will be wasted. So in order to avoid that we can use the subnetting concept. Because it allows you to divide your network into sub networks with its own subnet mask.
11111111.11111111.11111111.00000000 (C class --> network ID is 24 bits, Host ID is 8 bits)






<p id="L240"></p>
Using subnetting:
11111111.11111111.11111111.10000000 (here one bit is borrowed from host)
1 bit borrowed means 2^1=2 regions
So we can divide the c class network into two sub regions where each will have a 25 bits subnet mask.
1st region is from 192.168.25.0 to 192.168.25.127
2nd region is from 192.168.25.128 to 192.168.25.254



<p id="L250"></p>
###Supernetting 


* The time came when most of the class A and class B addresses were depleted; however, there was still a huge demand for midsize blocks. The size of a class C block with a maximum number of 256 addresses did not satisfy the needs of most organizations. Even a midsize organization needed more addresses. One solution was supernetting.
*  In supernetting, an organization can combine several class C blocks to create a larger range of addresses. In other words, several networks are combined to create a supernetwork or a supemet. An organization can apply for a set of class C blocks instead of just one.
*  For example, an organization that needs 1000 addresses can be granted four contiguous class C blocks. The organization can then use these addresses to create one supernetwork. Supernetting decreases the number of Is in the mask. For example, if an organization is given four class C addresses, the mask changes from /24 to /22. 
  

####Classless Addressing 
<p id="L260"></p>
To overcome address depletion and give more organizations access to the Internet, classless addressing was designed and implemented. In this scheme, there are no classes, but the addresses are still granted in blocks. Address Blocks In classless addressing, when an entity, small or large, needs to be connected to the Internet, it is granted a block (range) of addresses. The size of the block (the number of addresses) varies based on the nature and size of the entity. For example, a household may be given only two addresses; a large organization may be given thousands of addresses. An ISP, as the Internet service provider, may be given thousands or hundreds of thousands based on the number of customers it may serve. Restriction To simplify the handling of addresses, the Internet authorities impose three restrictions on classless address blocks: 1. The addresses in a block must be contiguous, one after another. 2. The number of addresses in a block must be a power of 2 (I, 2, 4, 8, ... ). 3. The first address must be evenly divisible by the number of addresses.
Mask
 A better way to define a block of addresses is to select any address in the block and the mask. As we discussed before, a mask is a 32-bit number in which the n leftmost bits are Is and the 32 - n rightmost bits are Os. However, in classless addressing the mask for a block can take any value from 0 to 32. It is very convenient to give just the value of n preceded by a slash (CIDR notation).


In IPv4 addressing, a block of addresses can be defined as x.y.z.t/n in which x.y.z.t defines one of the addresses and the /n defines the mask.


###IPv6 ADDRESSES 
<p id="L270"></p>
Despite all short-term solutions, such as classless addressing, Dynamic Host Configuration Protocol (DHCP), discussed in Chapter 21, and NAT, address depletion is still a long-term problem for the Internet. This and other problems in the IP protocol itself, such as lack of accommodation for real-time audio and video transmission, and encryption and authentication of data for some applications, have been the motivation for IPv6. In this section, we compare the address structure of IPv6 to IPv4. In Chapter 20, we discuss both protocols.
            Structure 
An IPv6 address consists of 16 bytes (octets); it is 128 bits long.
            Hexadecimal Colon Notation
To make addresses more readable, IPv6 specifies hexadecimal colon notation. In this notation, 128 bits is divided into eight sections, each 2 bytes in length. Two bytes in hexadecimal notation requires four hexadecimal digits. Therefore, the address consists of 32 hexadecimal digits, with every four digits separated by a colon.
            Address Space
IPv6 has a much larger address space; 2^128 addresses are available. The designers of IPv6 divided the address into several categories. A few leftmost bits, called the type prefix, in each address define its category. The type prefix is variable in length, but it is designed such that no code is identical to the first part of any other code. In this way, there is no ambiguity; when an address is given, the type prefix can easily be determined.
           

<p id="L280"></p>



  





<p id="L290"></p>
###IPv4 Protocol
* IPv4 is an unreliable and connectionless datagram protocol-a best-effort delivery service. The term best-effort means that IPv4 provides no error control or flow control (except for error detection on the header).
* IPv4 assumes the unreliability of the underlying layers and does its best to get a transmission through to its destination, but with no guarantees. If reliability is important, IPv4 must be paired with a reliable protocol such as TCP. An example of a more commonly understood best-effort delivery service is the post office. The post office does its best to deliver the mail but does not always succeed. If an unregistered letter is lost, it is up to the sender or would-be recipient to discover the loss and rectify the problem. The post office itself does not keep track of every letter and cannot notify a sender of loss or damage. 
* IPv4 is also a connectionless protocol for a packet-switching network that uses the datagram approach (see Chapter 8). This means that each datagram is handled independently, and each datagram can follow a different route to the destination. This implies that datagrams sent by the same source to the same destination could arrive out of order. Also, some could be lost or corrupted during transmission. Again, IPv4 relies on a higher-level protocol to take care of all these problems.
* Packets in the IPv4 layer are called datagrams.


IPv4 Header
  
<p id="L300"></p>


A datagram is a variable-length packet consisting of two parts: header and data. The header is 20 to 60 bytes in length and contains information essential to routing and delivery. It is customary in TCP/IP to show the header in 4-byte sections. A brief description of each field is in order.
Version (VER). This 4-bit field defines the version of the IPv4 protocol. Currently the version is 4. However, version 6 (or IPng) may totally replace version 4 in the future. This field tells the IPv4 software running in the processing machine that the datagram has the format of version 4. All fields must be interpreted as specified in the fourth version of the protocol. If the machine is using some other version of IPv4, the datagram is discarded rather than interpreted incorrectly.
Header length (HLEN). This 4-bit field defines the total length of the datagram header in 4-byte words. This field is needed because the length of the header is variable (between 20 and 60 bytes). When there are no options, the header length is 20 bytes, and the value of this field is 5 (5 x 4 = 20). When the option field is at its maximum size, the value of this field is 15 (15 x 4 = 60).
Type of Services. IETF has changed the interpretation and name of this 8-bit field. This field, previously called service type, is now called differentiated services.
1. Service Type In this interpretation, the first 3 bits are called precedence bits. The next 4 bits are called type of service (TOS) bits, and the last bit is not used. Type of service is an 8-bit field that is used for Quality of Service (QoS). The datagram is marked for giving a certain treatment using this field.
2. Differentiated Services In this interpretation, the first 6 bits make up the codepoint subfield, and the last 2 bits are not used.
Total Length: This 16-bit field defines the total length of the datagram header in 4-byte words. Total length = Header length + Payload length
<p id="L310"></p>
Since the field length is 16 bits, the total length of the IPv4 datagram is limited to 65,535 (2^16 - 1) bytes, of which 20 to 60 bytes are the header and the rest is data from the upper layer.


- Identification: Unique Packet Id for identifying the group of fragments of a single IP datagram (16 bits).


- Flags: 3 flags of 1 bit each : reserved bit (must be zero), do not fragment flag, more fragments flag .


<p id="L320"></p>
- Fragment Offset: (13bits)Represents the number of Data Bytes ahead of the particular fragment in the particular Datagram. Specified in terms of number of 8 bytes. Maximum fragment offset possible = (65535 – 20)  = 65515 


- Time to live: Datagram’s lifetime (8 bits), It prevents the datagram to loop through the network by restricting the number of Hops taken by a Packet before delivering to the Destination.


- Protocol:  This 8-bit field defines the higher-level protocol that uses the services of the IPv4 layer.An IPv4 datagram can encapsulate data from several higher-level protocols such as TCP, UDP, ICMP, and IGMP. This field specifies the final destination protocol to which the IPv4 datagram is delivered. In other words, since the IPv4 protocol carries data from different other protocols, the value of this field helps the receiving network layer know to which protocol the data belong 


<p id="L330"></p>
- Header Checksum: 16 bits header checksum for checking errors in the datagram header


- Source IP address: 32 bits IP address of the sender


- Destination IP address: 32 bits IP address of the receiver


<p id="L340"></p>
- Option: Optional information such as source route, record route. Used by the Network administrator to check whether a path is working or not. Due to the presence of options, the size of the datagram header can be of variable length (20 bytes to 60 bytes).


##Network Address Translation (NAT)
* With the increasing number of internet users requiring an unique IP address for each host, there is an acute shortage of IP addresses (until everybody moves to IPV6). The Network Address Translation (NAT) approach is a quick interim solution to this problem. NAT allows a large set of IP addresses to be used in an internal (private) network and a handful of addresses to be used for the external internet. 
* The internet authorities has set aside three sets of addresses to be used as private addresses as shown in Table 6.2.1. It may be noted that these addresses can be reused within different internal networks simultaneously, which in effect has helped to increase the lifespan of the IPV4. However, to make use of the concept, it is necessary to have a router to perform the operation of address translation between the private network and the internet. 
* As shown in Fig., the NAT router maintains a table with a pair of entries for private and internet addresses. The source address of all outgoing packets passing through the NAT router gets replaced by an internet address based on table look up. Similarly, the destination address of all incoming packets passing through the NAT router gets replaced by the corresponding private address, as shown in the figure. The NAT can use a pool of internet addresses to have internet access by a limited number of stations of the private network at a time.


<p id="L350"></p>


###Address Resolution Protocol (ARP) 
It may be noted that the knowledge of hosts’ IP address is not sufficient for sending packets, because data link hardware does not understand internet addresses. For example, in an Ethernet network, the Ethernet controller card can send and receive using 48-bit Ethernet addresses. The 32-bit IP addresses are unknown to these cards. This requires a mapping of the IP addresses to the corresponding Ethernet addresses. This mapping is accomplished by using a technique known as Address Resolution Protocol (ARP).


One possible approach is to have a configuration file somewhere in the system that maps IP addresses onto the Ethernet addresses. Although this approach is straightforward, maintaining an up-to0-date table has a high overhead on the system. Another elegant approach is to broadcast packet onto the Ethernet asking “who owns the destination IP address?”. The destination node responds with its Ethernet address after hearing the request. This protocol of asking the question and getting the reply is called ARP (Addressing Resolution Protocol), which is widely used. ARP is a dynamic mapping approach for finding a physical address for a known IP address. It involves following two basic steps as shown in Fig..


<p id="L360"></p>
• An ARP request is broadcast to all stations in the network 
 • An ARP reply is an unicast to the host requesting the mapping


Various optimizations are commonly used to improve the efficiency of the ARP protocol. One possible approach is to use cache memory to hold the recently acquired frame containing the physical address. As a consequence, no broadcasting is necessary in near future. Figure 6.2.10 shows how an ARP packet is encapsulated into the data field of a MAC frame.




<p id="L370"></p>

###Reverse ARP (RARP)
* The TCP/IP protocols include another related protocol known as reverse ARP, which can be used by a computer such as a diskless host to find out its own IP address.
* It involves the following steps:
 • Diskless host A broadcasts a RARP request specifying itself as the target 
 • RARP server responds with the reply directly to host A 
 • Host A preserves the IP address in its main memory for future use until it reboots


<p id="L380"></p>
* Routers can not forward RARP broadcast, so a RARP server is needed on each network. 
* The primary limitations of RARP are that each MAC must be manually configured on a central (RARP) server, and that the protocol only conveys an IP address and this leaves configuration of subnetting, gateways, and other information to other protocols or the user. RARP does not use IP/UDP.


####Reverse ARP (RARP):Limitations


* Routers can not forward RARP broadcast, so a RARP server is needed on each network. 

<p id="L390"></p>
* The primary limitations of RARP are that each MAC must be manually configured on a central (RARP) server, and that the protocol only conveys an IP address and this leaves configuration of subnetting, gateways, and other information to other protocols or the user. 


* RARP does not use IP/UDP.


###Dynamic Host Configuration Protocol(DHCP)
It is an application layer protocol which is used to provide: 
 
<p id="L400"></p>
* Subnet Mask (Option 1 – e.g., 255.255.255.0)
* Router Address (Option 3 – e.g., 192.168.1.1)
* DNS Address (Option 6 – e.g., 8.8.8.8)
* Vendor Class Identifier (Option 43 – e.g., ‘unifi’ = 192.168.1.9 ##where unifi = controller)
DHCP is based on a client-server model and based on discovery, offer, request, and ACK. The DHCP port number for the server is 67 and for the client is 68. It is a Client server protocol which uses UDP services. IP address is assigned from a pool of addresses. In DHCP, the client and the server exchange mainly 4 DHCP messages in order to make a connection, also called DORA process, but there are 8 DHCP messages in the process. 

These messages are given as below:


<p id="L410"></p>
- DHCP discover message – 
This is the first message generated in the communication process between server and client. This message is generated by the Client host in order to discover if there is any DHCP server/servers present in a network or not. This message is broadcasted to all devices present in a network to find the DHCP server. This message is 342 or 576 bytes long 
 
As shown in the figure, source MAC address (client PC) is 08002B2EAF2A, destination MAC address(server) is FFFFFFFFFFFF, source IP address is 0.0.0.0(because PC has no IP address till now) and destination IP address is 255.255.255.255 (IP address used for broadcasting). As the discovery message is broadcast to find out the DHCP server or servers in the network therefore broadcast IP address and MAC address is used. 
 


- DHCP offer message – 
The server will respond to the host in this message specifying the unleased IP address and other TCP configuration information. This message is broadcasted by the server. Size of the message is 342 bytes. If there are more than one DHCP servers present in the network then the client host will accept the first DHCP OFFER message it receives. Also a server ID is specified in the packet in order to identify the server. 
<p id="L420"></p>
Now, for the offer message, source IP address is 172.16.32.12 (server’s IP address in the example), destination IP address is 255.255.255.255 (broadcast IP address) ,source MAC address is 00AA00123456, destination MAC address is FFFFFFFFFFFF. Here, the offer message is broadcast by the DHCP server therefore destination IP address is broadcast IP address and destination MAC address is FFFFFFFFFFFF and the source IP address is server IP address and MAC address is server MAC address. 


Also the server has provided the offered IP address 192.16.32.51 and lease time of 72 hours(after this time the entry of host will be erased from the server automatically) . Also the client identifier is the PC MAC address (08002B2EAF2A) for all the messages. 
 


- DHCP request message – 
When a client receives an offer message, it responds by broadcasting a DHCP request message. The client will produce a  gratuitous ARP in order to find if there is any other host present in the network with the same IP address. If there is no reply by another host, then there is no host with the same TCP configuration in the network and the message is broadcasted to server showing the acceptance of IP address .A Client ID is also added in this message. 
<p id="L430"></p>
Now, the request message is broadcast by the client PC therefore source IP address is 0.0.0.0(as the client has no IP right now) and destination IP address is 255.255.255.255 (broadcast IP address) and source MAC address is 08002B2EAF2A (PC MAC address) and destination MAC address is FFFFFFFFFFFF. 
Note – This message is broadcast after the ARP request broadcast by the PC to find out whether any other host is not using that offered IP. If there is no reply, then the client host broadcasts the DHCP request message for the server showing the acceptance of IP address and Other TCP/IP Configuration. 
 


- DHCP acknowledgement message – 
In response to the request message received, the server will make an entry with specified client ID and bind the IP address offered with lease time. Now, the client will have the IP address provided by server. 
Now the server will make an entry of the client host with the offered IP address and lease time. This IP address will not be provided by server to any other host. The destination MAC address is FFFFFFFFFFFF and the destination IP address is 255.255.255.255 and the source IP address is 172.16.32.12 and the source MAC address is 00AA00123456 (server MAC address).

<p id="L440"></p>
####Routing Algorithms


* The main function of the network layer is routing packets from the source machine to the destination machine.

* The routing algorithm is that part of the network layer software responsible for deciding which output line an incoming packet should be transmitted on.

* If the subnet uses datagrams internally, this decision must be made anew for every arriving data packet since the best route may have changed since last time. 

<p id="L450"></p>
* If the subnet uses virtual circuits internally, routing decisions are made only when a new virtual circuit is being set up. This is also called session routing because a route remains in force for an entire user session.

* There is a difference between routing and forwarding.

* Routing algorithms can be grouped into two major classes: nonadaptive and adaptive. Modern computer networks generally use dynamic routing algorithms as it do not take into account current network load.

* Two dynamic algorithms in particular, distance vector routing and link state routing, are the most popular.
   * * Distance vector routing algorithms operate by having each router maintain a table.

<p id="L460"></p>
* These tables are updated by exchanging information with the neighbors.


* The distance vector routing algorithm is sometimes called by distributed Bellman-Ford routing algorithm and the Ford-Fulkerson algorithm, after the researchers who developed it (Bellman, 1957; and Ford and Fulkerson, 1962).

###Distance vector routing algorithms



<p id="L470"></p>
* Distance vector routing algorithms operate by having each router maintain a table (i.e, a vector) giving the best known distance to each destination and which line to use to get there. These tables are updated by exchanging information with the neighbors. 
* The distance vector routing algorithm is sometimes called by other names, most commonly the distributed Bellman-Ford routing algorithm and the Ford-Fulkerson algorithm, after the researchers who developed it (Bellman, 1957; and Ford and Fulkerson, 1962). 
* It was the original ARPANET routing algorithm and was also used on the Internet under the name RIP. In distance vector routing, each router maintains a routing table indexed by, and containing one entry for, each router in the subnet. This entry contains two parts: the preferred outgoing line to use for that destination and an estimate of the time or distance to that destination. The metric used might be number of hops, time delay in milliseconds, total number of packets queued along the path, or something similar. 
* The router is assumed to know the ''distance'' to each of its neighbors. If the metric is hops, the distance is just one hop. If the metric is queue length, the router simply examines each queue. If the metric is delayed, the router can measure it directly with special ECHO packets that the receiver just timestamps and sends back as fast as it can. As an example, assume that delay is used as a metric and that the router knows the delay to each of its neighbors. Once every T msec each router sends to each neighbor a list of its estimated delays to each destination. It also receives a similar list from each neighbor. 
* Imagine that one of these tables has just come in from neighbor X, with Xi being X's estimate of how long it takes to get to router i. If the router knows that the delay to X is m msec, it also knows that it can reach router i via X in Xi + m msec. By performing this calculation for each neighbor, a router can find out which estimate seems the best and use that estimate and the corresponding line in its new routing table. Note that the old routing table is not used in the calculation.
* This updating process is illustrated in Fig. 5-9. Part (a) shows a subnet. The first four columns of part (b) show the delay vectors received from the neighbors of router J. A claims to have a 12-msec delay to B, a 25-msec delay to C, a 40-msec delay to D, etc. Suppose that J has measured or estimated its delay to its neighbors, A, I, H, and K as 8, 10, 12, and 6 msec, respectively.

  

<p id="L480"></p>
Consider how J computes its new route to router G. It knows that it can get to A in 8 msec, and A claims to be able to get to G in 18 msec, so J knows it can count on a delay of 26 msec to G if it forwards packets bound for G to A. Similarly, it computes the delay to G via I, H, and K as 41 (31 + 10), 18 (6 + 12), and 37 (31 + 6) msec, respectively. The best of these values
is 18, so it makes an entry in its routing table that the delay to G is 18 msec and that the route to use is via H. The same calculation is performed for all the other destinations, with the new routing table shown in the last column of the figure.




###The Count-to-Infinity Problem 
Distance vector routing works in theory but has a serious drawback in practice: although it converges to the correct answer, it may do so slowly. In particular, it reacts rapidly to good news, but leisurely to bad news. Consider a router whose best route to destination X is large.If on the next exchange neighbor A suddenly reports a short delay to X, the router just switches over to using the line to A to send traffic to X. In one vector exchange, the good news is processed. To see how fast good news propagates, consider the five-node (linear) subnet of Fig. 5-10, where the delay metric is the number of hops. Suppose A is down initially and all the other routers know this. In other words, they have all recorded the delay to A as infinity.

<p id="L490"></p>

* When A comes up, the other routers learn about it via the vector exchanges. For simplicity we will assume that there is a gigantic gong somewhere that is struck periodically to initiate a vector exchange at all routers simultaneously. At the time of the first exchange, B learns that its left neighbor has zero delay to A. B now makes an entry in its routing table that A is one hop away to the left. All the other routers still think that A is down. 
* At this point, the routing table entries for A are as shown in the second row of Fig. 5-10(a). On the next exchange, Clearns that B has a path of length 1 to A, so it updates its routing table to indicate a path of length 2, but D and E do not hear the good news until later. Clearly, the good news is spreading at the rate of one hop per exchange. In a subnet whose longest path is of length N Hops, within N exchanges everyone will know about newly-revived lines and routers.Now let us consider the situation of Fig. 5-10(b), in which all the lines and routers are initially up. Routers B, C, D, and E have distances to A of 1, 2, 3, and 4, respectively. Suddenly A goes down, or alternatively, the line between A and B is cut, which is effectively the same thing from B's point of view. At the first packet exchange, B does not hear anything from A. Fortunately, C says: Do not worry; I have a path to A of length 2. Little does B know that C's path runs through B itself.For all B knows, C might have ten lines all with separate paths to A of length 2. As a result, B thinks it can reach A via C, with a path length of 3. D and E do not update their entries for A on the first exchange. On the second exchange, C notices that each of its neighbors claims to have a path to A of length 3. It picks one of them at random and makes its new distance to A 4.
* From this figure, it should be clear why bad news travels slowly: no router ever has a value more than one higher than the minimum of all its neighbors. Gradually, all routers work their way up to infinity, but the number of exchanges required depends on the numerical value used for infinity. For this reason, it is wise to set infinity to the longest path plus 1. If the metric is time delay, there is no well-defined upper bound, so a high value is needed to prevent a path with a long delay from being treated as down. Not entirely surprisingly, this problem is known as the count-to-infinity problem.


####Disadvantage of DVR
* Distance vector routing was used in the ARPANET until 1979, when it was replaced by link state routing.

<p id="L500"></p>
* Two primary problems caused its demise.


* First, since the delay metric was queue length, it did not take line bandwidth into account when choosing routes. Initially, all the lines were 56 kbps, so line bandwidth was not an issue, but after some lines had been 272 upgraded to 230 kbps and others to 1.544 Mbps, not taking bandwidth into account was a major problem.


* Second problem was namely, the algorithm often took too long to converge (the count-to-infinity problem.

* For these reasons, it was replaced by an entirely new algorithm, now called link state routing.
<p id="L510"></p>


###Link State Routing
The idea behind link state routing is simple and can be stated as five parts. Each router must do the following: 
1. Discover its neighbors and learn their network addresses. 
2. Measure the delay or cost to each of its neighbors. 
3. Construct a packet telling all it has just learned. 
4. Send this packet to all other routers. 
5. Compute the shortest path to every other router. 
<p id="L520"></p>
In effect, the complete topology and all delays are experimentally measured and distributed to every router. Then Dijkstra's algorithm can be run to find the shortest path to every other router. Below we will consider each of these five steps in more detail.
Learning about the Neighbors
When a router is booted, its first task is to learn who its neighbors are. It accomplishes this goal by sending a special HELLO packet on each point-to-point line. The router on the other end is expected to send back a reply telling who it is. These names must be globally unique because when a distant router later hears that three routers are all connected to F, it is essential that it can determine whether all three mean the same F. When two or more routers are connected by a LAN, the situation is slightly more complicated. Fig. 5-11(a) illustrates a LAN to which three routers, A, C, and F, are directly connected. Each 
of these routers is connected to one or more additional routers, as shown.


####Measuring Line Cost 
The link state routing algorithm requires each router to know, or at least have a reasonable estimate of, the delay to each of its neighbors. The most direct way to determine this delay is to send over the line a special ECHO packet that the other side is required to send back immediately. By measuring the round-trip time and dividing it by two, the sending router can get a reasonable estimate of the delay. For even better results, the test can be conducted several times, and the average used. Of course, this method implicitly assumes the delays are symmetric, which may not always be the case.

<p id="L530"></p>
####Building Link State Packets 
Once the information needed for the exchange has been collected, the next step is for each Router to build a packet containing all the data. The packet starts with the identity of the sender, followed by a sequence number and age (to be described later), and a list of neighbors. For each neighbor, the delay to that neighbor is given. An example subnet is given in Fig. 5-13(a) with delays shown as labels on the lines. The corresponding link state packets for all six routers.

* Building the link state packets is easy. The hard part is determining when to build them. One possibility is to build them periodically, that is, at regular intervals. Another possibility is to build them when some significant event occurs, such as a line or neighbor going down or coming back up again or changing its properties appreciably.

####Distributing the Link State Packets. 
* The trickiest part of the algorithm is distributing the link state packets reliably. As the packets are distributed and installed, the routers getting the first ones will change their routes. Consequently, the different routers may be using different versions of the topology, which can lead to inconsistencies, loops, unreachable machines, and other problems. First we will describe the basic distribution algorithm. Later we will give some refinements.
*  The fundamental idea is to use flooding to distribute the link state packets. To keep the flood in check, each packet contains a sequence number that is incremented for each new packet sent. Routers keep track of all the (source router, sequence) pairs they see. When a new link state packet comes in, it is checked against the list of packets already seen. If it is new, it is forwarded on all lines except the one it arrived on.
*  If it is a duplicate, it is discarded. If a packet with a sequence number lower than the highest one seen so far ever arrives, it is rejected as being obsolete since the router has more recent data.
<p id="L540"></p>

####Computing the New Routes
Once a router has accumulated a full set of link state packets, it can construct the entire subnet graph because every link is represented. Every link is, in fact, represented twice, once for each direction. The two values can be averaged or used separately. Now Dijkstra's algorithm can be run locally to construct the shortest path to all possible destinations. The results of this algorithm can be installed in the routing tables, and normal operation resumed.


####Problems with Link State Routing
* First, if the sequence numbers wrap around, confusion will reign. The solution here is to use a 32-bit sequence number.

* Second, if a router ever crashes, it will lose track of its sequence number. If it starts again at 0, the next packet will be rejected as a duplicate. 
<p id="L550"></p>

* Third, if a sequence number is ever corrupted and 65,540(10000000000000100 ) is received instead of 4(0000000000000100)(a 1-bit error), packets 5 through 65,540 will be rejected as obsolete, since the current sequence number is thought to be 65,540. 


* The solution to all these problems is to include the age of each packet after the sequence number and decrement it once per second. 


###Path  Vector  Routing
It  is  a  routing  algorithm  in the unicast  routing  protocol  of the network layer, and it is useful for interdomain routing. The principle of path vector routing is similar  to  that  of  distance  vector  routing.  It  assumes  that  there  is  one  node  in  each autonomous  system  that  acts  on  behalf  of  the  entire  autonomous  system  is  called  Speaker node .The speaker node in an AS(autonomous System) creates a routing cable and advertises to the speaker node  in the neighbouring ASs  .A speaker node advertises the path, not the metrics  of the nodes, in its autonomous system or other  autonomous systems
<p id="L560"></p>


It is the initial table for each speaker node in a system made four ASs. Here Node A1 is the speaker node for AS1, B1 for AS2, C1 for AS3 and D1 for AS4, Node A1 creates an initial table that shows A1 to A5 and these are located in AS1, it can be reached through it.
A  speaker  in  an  autonomous  system  shares  its  table  with immediate neighbours ,here  Node A1 share its table with nodes B1 and C1 , Node C1 share its table with nodes A1,B1 and D1 , Node B1 share its table with nodes A1 and C1 , Node D1 share its table with node  C1                                                   
If router A1 receives a packet for nodes A3 , it knows that  the path is in  AS1,but  if  it receives  a  packet  for  D1,it  knows  that    the  packet should go from AS1,to AS2 and then to AS3 ,then the routing table shows that path completely on the  other hand    if  the  node  D1  in  AS4  receives  a  packet  for  node  A2,it  knows it  should  go  through AS4,AS3,and AS1


- FUNCTIONS :
####PREVENTION OF LOOP  
<p id="L570"></p>        
* The  creation  of  loop  can  be  avoided  in  path  vector  routing  .A router receives a message it checks to see if its autonomous system is in the path list to the destination if it is looping is involved and the message is ignored  
####POLICY ROUTING                                                     
* When a router receives   a messages    it  can  check the  path,  if one of the autonomous system listed in the path against its policy, it can ignore its path and destination it does not update its routing table with this path or it does not send the messages to its neighbours. 
####OPTIMUM PATH                                    
*  A path to a destination that is the best for the organization that runs the autonomous system

##Protocols –RIP,OSPF,BGP.

###RIP
<p id="L580"></p>
* Routing Information Protocol (RIP) is a dynamic routing protocol that uses hop count as a routing metric to find the best path between the source and the destination network
*  RIP is another interior gateway protocol.
* RIP is used for updating routing table. The routing updates are exchanged between neighboring nodes.
* RIP is based upon distance vector routing protocol.
* In this protocol each router periodically shares its knowledge about the whole internet with its neighboring router.


####Hop Count 
Hop count is the number of routers occurring in between the source and destination network. The path with the lowest hop count is considered as the best route to reach a network and therefore placed in the routing table. RIP prevents routing loops by limiting the number of hops allowed in a path from source and destination. The maximum hop count allowed for RIP is 15 and a hop count of 16 is considered as network unreachable. 
<p id="L590"></p>

####Features of RIP 
1. Updates of the network are exchanged periodically. 
2. Updates (routing information) are always broadcast. 
3. Full routing tables are sent in updates. 
4. Routers always trust routing information received from neighbor routers. This is also known as Routing on rumors.
  


<p id="L600"></p>
Above table shows the typical routing table. Here the destination column consists of the destination address. Hop count column consists of the shortest distance to reach the destination. Next router column contains the address of next router to which the packet is to be forwarded.The routing table is updated when a RIP response message is received. When a new router is added to a network it initializes its routing table.


- Border Gateway Protocol:
* It is used to Exchange routing information for the internet and is the protocol used between ISP which are different ASes. 
* The protocol can connect together any internetwork of autonomous system using an arbitrary topology. The only requirement is that each AS have at least one router that is able to run BGP and that is router connect to at least one other AS’s BGP router. BGP’s main function is to exchange network reach-ability information with other BGP systems. Border Gateway Protocol constructs an autonomous systems’ graph based on the information exchanged between BGP routers. 


####Characteristics of Border Gateway Protocol (BGP):
<p id="L610"></p>
* Inter-Autonomous System Configuration: The main role of BGP is to provide communication between two autonomous systems.
* BGP supports Next-Hop Paradigm.
* Coordination among multiple BGP speakers within the AS (Autonomous System).
* Path Information: BGP advertisement also include path information, along with the reachable destination and next destination pair.
* Policy Support: BGP can implement policies that can be configured by the administrator. For ex:- a router running BGP can be configured to distinguish between the routes that are known within the AS and that which are known from outside the AS.
* Runs Over TCP.
* BGP conserve network Bandwidth.
* BGP supports CIDR.
* BGP also supports Security.
<p id="L620"></p>

####Functionality of Border Gateway Protocol (BGP): 


BGP peers performs 3 functions, which are given below.
* The first function consist of initial peer acquisition and authentication. both the peers established a TCP connection and perform message exchange that guarantees both sides have agreed to communicate.
* The second function mainly focus on sending negative or positive reach-ability information.
* The third function verifies that the peers and the network connection between them are functioning correctly.

<p id="L630"></p>
####BGP Route Information Management Functions:


* Route Storage: Each BGP stores information about how to reach other networks.
* Route Update: In this task, Special techniques are used to determine when and how to use the information received from peers to properly update the routes.
* Route Selection: Each BGP uses the information in its route databases to select good routes to each network on the internet network.
* Route advertisement: Each BGP speaker regularly tells its peer what is known about various networks and methods to reach them.


<p id="L640"></p>

- OSPF(Open shortest Path First)Open Shortest Path First
(OSPF) is a link-state routing protocol that is used to find the best path between the source and the destination router using its own Shortest Path First). OSPF is developed by Internet Engineering Task Force (IETF) as one of the Interior Gateway Protocol (IGP), i.e, the protocol which aims at moving the packet within a large autonomous system or routing domain. It is a network layer protocol which works on protocol number 89 and uses AD value 110. OSPF uses multicast address 224.0.0.5 for normal communication and 224.0.0.6 for update to designated router(DR)/Backup Designated Router (BDR).


####Features:
* Interior gateway routing protocol
* Based on Bellman-Ford algorithm

<p id="L650"></p>
* Supports three kind of connection
   * Point to Point lines between exactly two router
   * Multiaccess network with broadcasting
   * Multiaccess network without broadcasting
* Here the model of the network is created in the form of a graph and each arc in the graph  is assigned a cost.
* Shortest path between source and destination is calculated based upon this cost
* OSPF allows a network to be divided into numerous areas. Area 0 is called backbone area and router in this area are known as backbone router
* Each router which is connected to two or more area is called area border router
* Area border router summarizes the information in one area and provides this information to another area.
<p id="L660"></p>
* Router which lies wholly within an area is called an internal router.
* OSPF operates by abstracting the collection of actual networks, routers, and lines into a directed graph in which each arc is assigned a cost (distance, delay, etc.).
*  It then computes the shortest path based on the weights on the arcs.
*  A serial connection between two routers is represented by a pair of arcs, one in each direction.
* Their weights may be different. A multiaccess network is represented by a node for the network itself plus a node for each router.
* The arcs from the network node to the routers have weight 0 and are omitted from the graph.

  

<p id="L670"></p>	

###Traffic Shaping
In the network layer, before the network can make Quality of service guarantees, it must know what traffic is being guaranteed. One of the main causes of congestion is that traffic is often bursty. 
To understand this concept first we have to know little about traffic shaping. Traffic Shaping is a mechanism to control the amount and the rate of traffic sent to the network. Approach of congestion management is called Traffic shaping. Traffic shaping helps to regulate the rate of data transmission and reduces congestion.
There are 2 types of traffic shaping algorithms: 
1. Leaky Bucket
2. Token Bucket
Suppose we have a bucket in which we are pouring water, at random points in time, but we have to get water at a fixed rate, to achieve this we will make a hole at the bottom of the bucket. This will ensure that the water coming out is at some fixed rate, and also if the bucket gets full, then we will stop pouring water into it.
The input rate can vary, but the output rate remains constant. Similarly, in networking, a technique called leaky bucket can smooth out bursty traffic. Bursty chunks are stored in the bucket and sent out at an average rate.
<p id="L680"></p>  



In the above figure, we assume that the network has committed a bandwidth of 3 Mbps for a host. The use of the leaky bucket shapes the input traffic to make it conform to this commitment. In the above figure, the host sends a burst of data at a rate of 12 Mbps for 2s, for a total of 24 Mbits of data. The host is silent for 5 s and then sends data at a rate of 2 Mbps for 3 s, for a total of 6 Mbits of data. In all, the host has sent 30 Mbits of data in 10 s. The leaky bucket smooths out the traffic by sending out data at a rate of 3 Mbps during the same 10 s. 
Without the leaky bucket, the beginning burst may have hurt the network by consuming more bandwidth than is set aside for this host. We can also see that the leaky bucket may prevent congestion.
A simple leaky bucket algorithm can be implemented using the FIFO queue. A FIFO queue holds the packets. If the traffic consists of fixed-size packets (e.g., cells in ATM networks), the process removes a fixed number of packets from the queue at each tick of the clock. If the traffic consists of variable-length packets, the fixed output rate must be based on the number of bytes or bits.



<p id="L690"></p>
The following is an algorithm for variable-length packets:  
1. Initialize a counter to n at the tick of the clock.
2. Repeat until n is smaller than the packet size of the packet at the head of the queue.
   1. Pop a packet out of the head of the queue, say P.
   2. Send the packet P, into the network 
   3. Decrement the counter by the size of packet P.
3. Reset the counter and go to step 1.
