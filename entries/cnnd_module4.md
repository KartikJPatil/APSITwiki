# Module 4:Transport Layer & Session Layer
## Transport Layer: 
- Transport Layer Services, 
- Connectionless & Connection-oriented Protocols,
- Transport Layer protocols: User Datagram Protocol: UDP Services, UDP Applications,
- Transmission Control Protocol: TCP Services, TCP Features, Segment, A TCP Connection, Windows in TCP, 
- Flow Control, Error Control, 
- TCP Congestion Control, 
- TCP Timers. 
<p id="L10"></p>
## Session Layer: 
- Session layer design issues, 
- Session Layer protocol - Remote Procedure Call (RPC)


## Transport Layer: 

Transport Layer is the second layer in the TCP/IP model and the fourth layer in the OSI model. It is an end-to-end layer used to deliver messages to a host. It is termed an end-to-end layer because it provides a point-to-point connection rather than hop-to- hop, between the source host and destination host to deliver the services reliably. The unit of data encapsulation in the Transport Layer is a segment. 

<p id="L20"></p>
#### Working of Transport Layer:
The transport layer takes services from the Network layer and provides services to the Application layer.
>- At the sender’s side: The transport layer receives data (message) from the Application layer and then performs Segmentation, divides the actual message into segments, adds source and destination’s port numbers into the header of the segment, and transfers the message to the Network layer. 
- At the receiver’s side: The transport layer receives data from the Network layer, reassembles the segmented data, reads its header, identifies the port number, and forwards the message to the appropriate port in the Application layer.

### Responsibilities of a Transport Layer:
> ***Process to process delivery:*** While Data Link Layer requires the MAC address (48 bits address contained inside the Network Interface Card of every host machine) of source-destination hosts to correctly deliver a frame and the Network layer requires the IP address for appropriate routing of packets, in a similar way Transport Layer requires a Port number to correctly deliver the segments of data to the correct process amongst the multiple processes running on a particular host. A port number is a 16-bit address used to identify any client-server program uniquely.

***End-to-end Connection between hosts/Process-To-Process Delivery:*** The transport layer is also responsible for creating the end-to-end Connection between hosts for which it mainly uses TCP and UDP. TCP is a secure, connection-orientated protocol that uses a handshake protocol to establish a robust connection between two end hosts. TCP ensures reliable delivery of messages and is used in various applications. UDP, on the other hand, is a stateless and unreliable protocol that ensures best-effort delivery. It is suitable for applications that have little concern with flow or error control and requires sending the bulk of data like video conferencing. It is often used in multicasting protocols.
<p id="L30"></p>
### Addressing
Although there are several ways to achieve process-to-process communication, the most common one is through the client/server paradigm. A process on the local host, called a client, needs services from a process usually on the remote host, called a server.
Whenever we need to deliver something to one specific destination among many, we need an address. At the data link layer, we need a MAC address to choose one node among several nodes, at the network layer, we need an IP address to choose one host among millions. Similarly at the transport layer, we need a transport layer address, called a port number, to choose among multiple processes running on the destination host.
### Port Number
In the Internet model, the port numbers are 16-bit integers between 0 and 65,535. The client program defines itself with a port number, chosen randomly by the transport layer software running on the client host. This is the ephemeral port number. The server process must also define itself with a port number. This port number, however, cannot be chosen randomly.
If the computer at the server site runs a server process and assigns a random number as the port number, the process at the client site that wants to access that server and use its services will not know the port number.
The Internet has decided to use universal port numbers for servers; these are called well-known port numbers. There are some exceptions to this rule; for example, there are clients that are assigned well-known port numbers. Every client process knows the well-known port number of the corresponding server process. For example, while the Daytime client process can use an ephemeral (temporary) port number 52,000 to identify itself, the Daytime server process must use the well-known (permanent) port number 13.


<p id="L40"></p>
#### lANA Ranges: 
The lANA (Internet Assigned Number Authority) has divided the port numbers into three ranges: well known, registered, and dynamic (or private), as shown in Figure 23.4.
>1.  Well-known ports. The ports ranging from 0 to 1023 are assigned and controlled by lANA. These are the well-known ports.
2. Registered ports. The ports ranging from 1024 to 49,151 are not assigned or controlled by lANA. They can only be registered with lANA to prevent duplication.
3. Dynamic ports. The ports ranging from 49,152 to 65,535 are neither controlled nor registered. They can be used by any process. These are the ephemeral ports. 

#### Socket Addresses
Process-to-process delivery needs two identifiers, IP address and the port number, at each end to make a connection. The combination of an IP address and a port number is called a socket address. The client socket address defines the client process uniquely just as the server socket address defines the server process uniquely (see Figure 23.5). A transport layer protocol needs a pair of socket addresses: the client socket address and the server socket address. These four pieces of information are part of the IP header and the transport layer protocol header. The IP header contains the IP addresses; the UDP or TCP header contains the port numbers.

<p id="L50"></p>
***Multiplexing and Demultiplexing:*** Multiplexing(many to one) is when data is acquired from number of processes from the sender and merged into one packet along with headers and sent as a single packet. Multiplexing allows simultaneous use of different processes over a network that is running on a host.  The processes are differentiated by their port numbers. Similarly, Demultiplexing(one to many is required at the receiver side when the message is distributed into different processes. Transport receives the segments of data from the network layer distributes and delivers it to the appropriate process running on the receiver’s machine.

***Congestion Control:*** Congestion is a situation in which too many sources over a network attempt to send data and the router buffers start overflowing due to which loss of packets occur. As a result retransmission of packets from the sources increases the congestion further. In this situation, the Transport layer provides Congestion Control in different ways. It uses open loop congestion control to prevent the congestion and closed-loop congestion control to remove the congestion in a network once it occurred. TCP provides AIMD- additive increase multiplicative decrease, leaky bucket technique for congestion control.

***Data integrity and Error correction:*** The transport layer checks for errors in the messages coming from the application layer by using error detection codes, computing checksums, it checks whether the received data is not corrupted and uses the ACK and NACK services to inform the sender if the data has arrived or not and checks for the integrity of data.

***Flow control:*** The transport layer provides a flow control mechanism between the adjacent layers of the TCP/IP model. TCP also prevents data loss due to a fast sender and slow receiver by imposing some flow control techniques. It uses the method of sliding window protocol which is accomplished by the receiver by sending a window back to the sender informing the size of data it can receive.
### Connectionless & Connection-oriented Protocols
Both Connection-oriented service and Connection-less service are used for the connection establishment between two or more two devices. These types of services are offered by the network layer. 
<p id="L60"></p>
- Connection-oriented service is related to the telephone system. It includes connection establishment and connection termination. In a connection-oriented service, the Handshake method is used to establish the connection between sender and receiver.

- Connection-less service is related to the postal system. It does not include any connection establishment and connection termination. Connection-less Service does not give a guarantee of reliability. In this, Packets do not follow the same path to reach their destination.

## Transport Layer protocols:

A transport layer protocol can be either connectionless or connection-oriented. A connectionless transport layer treats each segment as an independent packet and delivers it to the transport layer at the destination machine. A connection-oriented transport layer makes a connection with the transport layer at the destination machine first before delivering the packets. After all the data is transferred, the connection is terminated. In the transport layer, a message is normally divided into transmittable segments. A connectionless protocol, such as UDP, treats each segment separately. A connection oriented protocol, such as TCP and SCTP, creates a relationship between the segments using sequence numbers.


<p id="L70"></p>
#### USER DATAGRAM PROTOCOL (UDP)
The User Datagram Protocol (UDP) is called a connectionless, unreliable transport protocol. It does not add anything to the services of IP except to provide process-toprocess communication instead of host-to-host communication. Also, it performs very limited error checking.
<img src ="https://img.brainkart.com/imagebk14/MJImkQP.jpg">

- User Datagram
UDP packets, called user datagrams, have a fixed-size header of 8 bytes.

- Source port number. 
This is the port number used by the process running on the source host. It is 16 bits long, which means that the port number can range from 0 to 65,535. Ifthe source host is the client (a client sending a request), the port number, in most cases, is an ephemeral port number requested by the process and chosen by the UDP software running on the source host. If the source host is the server (a server sending a response), the port number, in most cases, is a well-known port number. 
<p id="L80"></p>
- Destination port number. 
This is the port number used by the process running on the destination host. It is also 16 bits long. If the destination host is the server (a client sending a request), the port number, in most cases, is a well-known port number. If the destination host is the client (a server sending a response), the port number, in most cases, is an ephemeral port number. In this case, the server copies the ephemeral port number it has received in the request packet. 
- Length. 
This is a 16-bit field that defines the total length of the user datagram, header plus data. The 16 bits can define a total length of 0 to 65,535 bytes. However, the total length needs to be much less because a UDP user datagram is stored in an IP datagram with a total length of 65,535 bytes.
- Checksum.
Here the checksum includes three sections: a pseudoheader, the UDP header, and the data coming from the application layer.

#### UDP Services

<p id="L90"></p>
1. Connectionless Services
As mentioned previously, UDP provides a connectionless service. This means that each user datagram sent by UDP is an independent datagram. There is no relationship between the different user datagrams even ifthey are coming from the same source process and going to the same destination program. The user datagrams are not numbered. Also, there is no connection establishment and no connection termination, as is the case for TCP. This means that each user datagram can travel on a different path. One of the ramifications of being connectionless is that the process that uses UDP cannot send a stream of data to UDP and expect UDP to chop them into different related user datagrams. Instead each request must be small enough to fit into one user datagram. Only those processes sending short messages should use UDP.

2. Flow and Error Control
UDP is a very simple, unreliable transport protocol. There is no flow control and hence no window mechanism. The receiver may overflow with incoming messages. There is no error control mechanism in UDP except for the checksum. This means that the sender does not know if a message has been lost or duplicated. When the receiver detects an error through the checksum, the user datagram is silently discarded. The lack of flow control and error control means that the process using UDP should provide these mechanisms.

3. Encapsulation and Decapsulation 
To send a message from one process to another, the UDP protocol encapsulates and decapsulates messages in an IP datagram.

<p id="L100"></p>

#### Queuing
In UDP, queues are associated with ports. At the client site, when a process starts, it requests a port number from the operating system. Some implementations create both an incoming and an outgoing queue associated with each process. Other implementations create only an incoming queue associated with each process. At the server site, the mechanism of creating queues is different. In its simplest form, a server asks for incoming and outgoing queues, using its well-known port, when it starts running. The queues remain open as long as the server is running.

#### UDP Applications
The following lists some uses of the UDP protocol:

- UDP is suitable for a process that requires simple request-response communication with little concern for flow and error control. It is not usually used for a process such as FrP that needs to send bulk data.
- UDP is suitable for a process with internal flow and error control mechanisms. For example, the Trivial File Transfer Protocol (TFTP) process includes flow and error control. It can easily use UDP.
<p id="L110"></p>
- UDP is a suitable transport protocol for multicasting. Multicasting capability is embedded in the UDP software but not in the TCP software. o UDP is used for management processes such as SNMP.
- UDP is used for some route updating protocols such as Routing Information Protocol (RIP).

### Transmission Control Protocol (TCP)
TCP, like UDP, is a process-to-process (program-to-program) protocol. TCP, therefore, like UDP, uses port numbers. Unlike UDP, TCP is a connection oriented protocol; it creates a virtual connection between two TCPs to send data. In addition, TCP uses flow and error control mechanisms at the transport level. In brief, TCP is called a connection-oriented, reliable transport protocol. It adds connection-oriented and reliability features to the services of IP.

#### TCP Services:
Before we discuss TCP in detail, let us explain the services offered by TCP to the processes at the application layer.
Process-to-Process Communication Like UDP, TCP provides process-to-process communication using port numbers. Table 23.2 lists some well-known port numbers used by TCP. 
<p id="L120"></p>

#### Stream Delivery Service
TCP, on the other hand, allows the sending process to deliver data as a stream of bytes and allows the receiving process to obtain data as a stream of bytes. TCP creates an environment in which the two processes seem to be connected by an imaginary "tube" that carries their data across the Internet. 
- ***Sending and Receiving Buffer:*** Because the sending and the receiving processes may not write or read data at the same speed, TCP needs buffers for storage. There are two buffers, the sending buffer and the receiving buffer, one for each direction. 
>- ***Segments:*** Although buffering handles the disparity between the speed of the producing and consuming processes, we need one more step before we can send data. The IP layer, as a service provider for TCP, needs to send data in packets, not as a stream of bytes. the transport layer, TCP groups a number of bytes together into a packet called a segment. TCP adds a header to each segment (for control purposes) and delivers the segment to the IP layer for transmission. The segments are encapsulated in IP datagrams and transmitted. This entire operation is transparent to the receiving process. Later we will see that segments may be received out of order, lost, or corrupted and resent. All these are handled by TCP with the receiving process unaware of any activities. Note that the segments are not necessarily the same size.
- ***Full-Duplex Communication:*** TCP offers full-duplex service, in which data can flow in both directions at the same time. Each TCP then has a sending and receiving buffer, and segments move in both directions.
- ***Connection-Oriented Service:*** TCP, unlike UDP, is a connection-oriented protocol. When a process at site A wants to send and receive data from another process at site B, the following occurs:
> 1. The two TCPs establish a connection between them. 
2. Data are exchanged in both directions.
<p id="L130"></p>
> 3. The connection is terminated
- ***Reliable Service:***  TCP is a reliable transport protocol. It uses an acknowledgment mechanism to check the safe and sound arrival of data. We will discuss this feature further in the section on error control.

### TCP Features
To provide the services mentioned in the previous section, TCP has several features that are briefly summarized:
>- Numbering System: Although the TCP software keeps track of the segments being transmitted or received, there is no field for a segment number value in the segment header. Instead, there are two fields called the sequence number and the acknowledgment number. These two fields refer to the byte number and not the segment number. 
- Byte Number: TCP numbers all data bytes that are transmitted in a connection. Numbering is independent in each direction. When TCP receives bytes of data from a process, it stores them in the sending buffer and numbers them. The numbering does not necessarily start from O. 
 - Note: The bytes of data being transferred in each connection are numbered by TCP. The numbering starts with a randomly generated number.
- Sequence Number: After the bytes have been numbered, TCP assigns a sequence number to each segment that is being sent. The sequence number for each segment is the number of the first byte carried in that segment.
<p id="L140"></p>
- Acknowledgement Number: As we discussed previously, communication in TCP is full duplex; when a connection is established, both parties can send and receive data at the same time. Each party numbers the bytes, usually with a different starting byte number. The sequence number in each direction shows the number of the first byte carried by the segment. Each party also uses an acknowledgment number to confirm the bytes it has received. However, the acknowledgment number defines the number of the next byte that the party expects to receive.
- Flow Control: TCP, unlike UDP, provides flow control. The receiver of the data controls the amount of data that are to be sent by the sender. This is done to prevent the receiver from being overwhelmed with data. The numbering system allows TCP to use a byte-oriented flow control. 
- Error Control: To provide reliable service, TCP implements an error control mechanism. Although error control considers a segment as the unit of data for error detection (loss or corrupted segments), error control is byte-oriented, as we will see later. 
- Congestion Control: TCP, unlike UDP, takes into account congestion in the network. The amount of data sent by a sender is not only controlled by the receiver (flow control), but is also determined by the level of congestion in the network.


###Segment


<p id="L150"></p>
The segment consists of a 20- to 60-byte header, followed by data from the application program. 
The header is 20 bytes if there are no options and up to 60 bytes if it contains options. We will discuss some of the header fields in this section. 
>- Source port address.
This is a 16-bit field that defines the port number of the application program in the host that is sending the segment. This serves the same purpose as the source port address in the UDP header.
- Destination port address. 
This is a 16-bit field that defines the port number of the application program in the host that is receiving the segment. This serves the same purpose as the destination port address in the UDP header. 
- Sequence number. 
This 32-bit field defines the number assigned to the first byte of data contained in this segment. As we said before, TCP is a stream transport protocol. To ensure connectivity, each byte to be transmitted is numbered. The sequence number tells the destination which byte in this sequence comprises the first byte in the segment. During connection establishment, each party uses a random number generator to create an initial sequence number (ISN), which is usually different in each direction. 
- Acknowledgment number.
This 32-bit field defines the byte number that the receiver of the segment is expecting to receive from the other party. If the receiver of the segment has successfully received byte number x from the other party, it defines x + I as the acknowledgment number. Acknowledgment and data can be piggybacked together.
<p id="L160"></p>
- Header length.
This 4-bit field indicates the number of 4-byte words in the TCP header. The length of the header can be between 20 and 60 bytes. Therefore, the value of this field can be between 5 (5 x 4 =20) and 15 (15 x 4 =60). 
- Reserved. 
This is a 6-bit field reserved for future use. 
- Control. 
This field defines 6 different control bits or flags. One or more of these bits can be set at a time.
 - URG: Urgent pointer is valid
 - RST: Reset the connection
 - ACK: Acknowledgment is valid
 - SYN: Synchronize sequence numbers
 <p id="L170"></p>
 - PSH: Request for push
 - FIN: Terminate the connection
- Window size. This field defines the size of the window, in bytes, that the other party must maintain. Note that the length of this field is 16 bits, which means that the maximum size of the window is 65,535 bytes. This value is normally referred to as the receiving window (rwnd) and is determined by the receiver. The sender must obey the dictation of the receiver in this case.
- Checksum. This 16-bit field contains the checksum. The calculation of the checksum for TCP follows the same procedure as the one described for UDP. However, the inclusion of the checksum in the UDP datagram is optional, whereas the inclusion of the checksum for TCP is mandatory. The same pseudo header, serving the same purpose, is added to the segment. For the TCP pseudo header, the value for the protocol field is 6.
- Urgent pointer. This l6-bit field, which is valid only if the urgent flag is set, is used when the segment contains urgent data. It defines the number that must be added to the sequence number to obtain the number of the last urgent byte in the data section of the segment.
- Options. There can be up to 40 bytes of optional information in the TCP header. We will not discuss these options here; please refer to the reference list for more information.

<p id="L180"></p>
### A TCP Connection
TCP is connection-oriented. A connection-oriented transport protocol establishes a virtual path between the source and destination. All the segments belonging to a message are then sent over this virtual path. Using a single virtual pathway for the entire message facilitates the acknowledgment process as well as retransmission of damaged or lost frames. You may wonder how TCP, which uses the services of IP, a connectionless protocol, can be connection-oriented. The point is that a TCP connection is virtual, not physical. TCP operates at a higher level. TCP uses the services of IP to deliver individual segments to the receiver, but it controls the connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is unaware of this retransmission. If a segment arrives out of order, TCP holds it until the missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented transmission requires three phases: connection establishment, data transfer, and connection termination.
> - Connection Establishment:
TCP transmits data in full-duplex mode. When two TCPs in two machines are connected, they are able to send segments to each other simultaneously. This implies that each party must initialize communication and get approval from the other party before any data are transferred.
- Three-Way Handshaking:
>The connection establishment in TCP is called three way handshaking. In our example, an application program, called the client, wants to make a connection with another application program, called the server, using TCP as the transport layer protocol. The process starts with the server. The server program tells its TCP that it is ready to accept a connection. This is called a request for a passive open. Although the server TCP is ready to accept any connection from any machine in the world, it cannot make the connection itself. The client program issues a request for an active open. A client that wishes to connect to an open server tells its TCP  that it needs to be connected to that particular server. TCP can now start the three-way handshaking process as shown in Figure.
The process starts with the server. The server program tells its TCP that it is ready to accept a connection. This is called a request for a passive open. Although the server TCP is ready to accept any connection from any machine in the world, it cannot make the connection itself. The client program issues a request for an active open. A client that wishes to connect to an open server tells its TCP that it needs to be connected to that particular server. TCP can now start the three-way handshaking process.


<p id="L190"></p>
The three steps in this phase are as follows.
>1. The client sends the first segment, a SYN segment, in which only the SYN flag is set. This segment is for synchronization of sequence numbers. It consumes one sequence number. When the data transfer starts, the sequence number is incremented by 1. We can say that the SYN segment carries no real data, but we can think of it as containing 1 imaginary byte. 
2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set: SYN and ACK. This segment has a dual purpose. It is a SYN segment for communication in the other direction and serves as the acknowledgment for the SYN segment. It consumes one sequence number.             
3. The client sends the third segment. This is just an ACK segment. It acknowledges the receipt of the second segment with the ACK flag and acknowledgment number field. Note that the sequence number in this segment is the same as the one in the SYN segment; the ACK segment does not consume any sequence numbers.

#### Data Transfer
After connection is established, bidirectional data transfer can take place. The client and server can both send data and acknowledgments.
The data segments sent by the client have the PSH (push) flag set so that the server TCP knows to deliver data to the server process as soon as they are received.

<p id="L200"></p>
#### Connection Termination
- (FIN From Client) –
Suppose that the client application decides it wants to close the connection. (Note that the server could also choose to close the connection). This causes the client to send a TCP segment with the FIN bit set to 1 to the server and to enter the FIN_WAIT_1 state. While in the FIN_WAIT_1 state, the client waits for a TCP segment from the server with an acknowledgment (ACK).

- (ACK From Server) – 
When the Server received the FIN bit segment from Sender (Client), Server Immediately sends acknowledgement (ACK) segment to the Sender (Client).
(Client waiting) – 
While in the FIN_WAIT_1 state, the client waits for a TCP segment from the server with an acknowledgment. When it receives this segment, the client enters the FIN_WAIT_2 state. While in the FIN_WAIT_2 state, the client waits for another segment from the server with the FIN bit set to 1.

<p id="L210"></p>
- (FIN from Server) – 
The server sends the FIN bit segment to the Sender(Client) after some time when the Server sends the ACK segment (because of some closing process in the Server).
- (ACK from Client) – 
When the Client receives the FIN bit segment from the Server, the client acknowledges the server’s segment and enters the TIME_WAIT state. The TIME_WAIT state lets the client resend the final acknowledgment in case the ACK is lost. The time spent by clients in the TIME_WAIT state depends on their implementation, but their typical values are 30 seconds, 1 minute, and 2 minutes. After the wait, the connection formally closes and all resources on the client-side (including port numbers and buffer data) are released.



### Windows in TCP
There are three TCP windows used in a TCP connection:
<p id="L220"></p>
* Receive Window (RWIN)
* Send Window (SWIN)
* Congestion Window (CWIN)
 
 
> The RWIN dictates how much data a TCP receiver is willing to accept before sending an acknowledgement (ACK) back to the TCP sender. The receiver will advertise its RWIN to the sender and thus the sender knows it can’t send more than an RWINs worth of data before receiving and ACK from receiver.
 
> The SWIN dictates how much data a TCP sender will be allowed send before it must receive an ACK from the TCP receiver.
 
<p id="L230"></p> 
> The CWIN is a variable that changes dynamically according to the conditions of the network. If data is lost or delivered out-of-order the CWIN is typically reduced.

### Flow Control
> TCP uses a sliding window. The sliding window protocol used by TCP, however, is something between the Go-Back-N and Selective Repeat sliding window.
The sliding window protocol in TCP looks like the Go-Back-N protocol because it does not use NAKs; it looks like Selective Repeat because the receiver holds the out-of-order segments until the missing ones arrive. There are two big differences between this sliding window and the one we used at the data link layer. First, the sliding window of TCP is byte-oriented; the one we discussed in the data link layer is frame-oriented. Second, the TCP's sliding window is of variable size; the one we discussed in the data link layer was of fixed size The bytes inside the window are the bytes that can be in transit; they can be sent without worrying about acknowledgment.
> The imaginary window has two walls: one left and one right. The window is opened, closed, or shrunk. These three activities, as we will see, are in the control of the receiver (and depend on congestion in the network), not the sender. The sender must obey the commands of the receiver in this matter. Opening a window means moving the right wall to the right. This allows more new bytes in the buffer that are eligible for sending. Closing the window means moving the left wall to the right. This means that some bytes have been acknowledged and the sender need not worry about them anymore.
> The size of the window at one end is determined by the lesser of two values: receiver window (rwnd) or congestion window (cwnd). The receiver window is the value advertised by the opposite end in a segment containing acknowledgment. It is the number of bytes the other end can accept before its buffer overflows and data are discarded. The congestion window is a value determined by the network to avoid congestion.

### Error Control
<p id="L240"></p>
Error control in TCP includes a mechanism for detecting corrupted segments with the help of the checksum field. If the segment is corrupted, it is discarded by the destination TCP and is considered as lost. TCP uses a 16-bit checksum that is mandatory in every segment.
An Acknowledgement method is used to confirm the receipt of uncorrupted data. If the acknowledgment is not received before the timeout, it is assumed that the data or the acknowledgment has been corrupted or lost.
The heart of the error control mechanism is the retransmission of segments. When a segment is corrupted, lost, or delayed, it is retransmitted. In modern implementations, a segment is retransmitted on two occasions: when a retransmission timer expires or when the sender receives three duplicate ACKs.
Note that no retransmission occurs for segments that do not consume sequence numbers. In particular, there is no retransmission for an ACK segment

It may be noted that there is no negative acknowledgment in TCP. To keep track of lost or discarded segments and to perform the operations smoothly, the following four timers are used by TCP: 
>- Retransmission: it is dynamically decided by the round trip delay time. To retransmit lost segments, TCP uses retransmission timeout (RTO). When TCP sends a segment the timer starts and stops when the acknowledgment is received. If the timer expires timeout occurs and the segment is retransmitted. RTO (retransmission timeout is for 1 RTT) to calculate retransmission timeout we first need to calculate the RTT(round trip time).
- Persistence: To deal with a zero-window-size deadlock situation, TCP uses a persistence timer. When the sending TCP receives an acknowledgment with a window size of zero, it starts a persistence timer. When the persistence timer goes off, the sending TCP sends a special segment called a probe. This segment contains only 1 byte of new data. It has a sequence number, but its sequence number is never acknowledged; it is even ignored in calculating the sequence number for the rest of the data. The probe causes the receiving TCP to resend the acknowledgment which was lost. This is used to deal with window-size advertisement.
- Keep-alive: commonly used in situations where there is long idle connection between two processes. A keepalive timer is used to prevent a long idle connection between two TCPs. If a client opens a TCP connection to a server transfers some data and becomes silent the client will crash. In this case, the connection remains open forever. So a keepalive timer is used. Each time the server hears from a client, it resets this timer. The time-out is usually 2 hours. If the server does not hear from the client after 2 hours, it sends a probe segment. If there is no response after 10 probes, each of which is 75 s apart, it assumes that the client is down and terminates the connection.
<p id="L250"></p>
- Time-waited: it is used during connection terminations. This timer is used during tcp connection termination. The timer starts after sending the last Ack for 2nd FIN and closing the connection. After a TCP connection is closed, it is possible for datagrams that are still making their way through the network to attempt to access the closed port. 



### Congestion policy in TCP 

TCP uses a congestion window and a congestion policy that avoid congestion. Previously, we assumed that only the receiver can dictate the sender’s window size. We ignored another entity here, the network. If the network cannot deliver the data as fast as it is created by the sender, it must tell the sender to slow down. In other words, in addition to the receiver, the network is a second entity that determines the size of the sender’s window.

#### Congestion policy in TCP –
<p id="L260"></p>
- Slow Start Phase: starts slowly increment is exponential to threshold
- Congestion Avoidance Phase: After reaching the threshold increment is by 1
- Congestion Detection Phase: Sender goes back to Slow start phase or Congestion avoidance phase.

1. **Slow Start Phase :** exponential increment – In this phase after every RTT the congestion window size increments exponentially.
```Initially cwnd = 1
After 1 RTT, cwnd = 2^(1) = 2
2 RTT, cwnd = 2^(2) = 4
3 RTT, cwnd = 2^(3) = 8```
<p id="L270"></p>
2. **Congestion Avoidance Phase :** additive increment – This phase starts after the threshold value also denoted as ssthresh. The size of cwnd(congestion window) increases additive. After each RTT cwnd = cwnd + 1.
```Initially cwnd = i
After 1 RTT, cwnd = i+1
2 RTT, cwnd = i+2
3 RTT, cwnd = i+3```

3. **Congestion Detection Phase :** multiplicative decrement – If congestion occurs, the congestion window size is decreased. The only way a sender can guess that congestion has occurred is the need to retransmit a segment. Retransmission is needed to recover a missing packet that is assumed to have been dropped by a router due to congestion. Retransmission can occur in one of two cases: when the RTO timer times out or when three duplicate ACKs are received.
 - Case 1 : Retransmission due to Timeout – In this case congestion possibility is high.
 
 <p id="L280"></p>
 ```(a) ssthresh is reduced to half of the current window size.
 (b) set cwnd = 1
 (c) start with slow start phase again.```
 - Case 2 : Retransmission due to 3 Acknowledgement Duplicates – In this case congestion possibility is less.
  (a) ssthresh value reduces to half of the current window size.
  (b) set cwnd= ssthresh
  (c) start with congestion avoidance phase
  - Example – Assume a TCP protocol experiencing the behavior of slow start. At 5th transmission round with a threshold (ssthresh) value of 32 goes into congestion avoidance phase and continues till 10th transmission. At 10th transmission round, 3 duplicate ACKs are received by the receiver and enter into additive increase mode. Timeout occurs at 16th transmission round. Plot the transmission round (time) vs congestion window size of TCP segments.

<p id="L290"></p>
## Session Layer:
### Functions of Session Layer:
 
- Dialog Control –
Session layer allows two systems to enter into a dialog exchange mechanism which can either be full or half-duplex.

- Managing Tokens –
The communicating systems in a network try to perform some critical operations and it is Session Layer which prevents collisions which might occur while performing these operations which would otherwise result in a loss.
 
<p id="L300"></p>
- Synchronization –
Checkpoints are the midway marks that are added after a particular interval during stream of data transfer. These points are also referred to as synchronization points. The Session layer permits process to add these checkpoints. For example, suppose a file of 400 pages is being sent over a network, then it is highly beneficial to set up a checkpoint after every 50 pages so that next 50 pages are sent only when previous pages are received and acknowledged.

### Design Issues with Session Layer :
 
1. Establish sessions between machines –
The establishment of session between machines is an important service provided by session layer. This session is responsible for creating a dialog between connected machines. The Session Layer provides mechanism for opening, closing and managing a session between end-user application processes, i.e. a semi-permanent dialogue. This session consists of requests and responses that occur between applications.


<p id="L310"></p>
2. Enhanced Services –
Certain services such as checkpoints and management of tokens are the key features of session layer and thus it becomes necessary to keep enhancing these features during the layer’s design.

3. To help in Token management and Synchronization – 
The session layer plays an important role in preventing collision of several critical operation as well as ensuring better data transfer over network by establishing synchronization points at specific intervals. Thus it becomes highly important to ensure proper execution of these services.

### Remote Procedure Call
A remote procedure call is an interprocess communication technique that is used for client-server based applications. It is also known as a subroutine call or a function call.

<p id="L320"></p>
A client has a request message that the RPC translates and sends to the server. This request may be a procedure or a function call to a remote server. When the server receives the request, it sends the required response back to the client. The client is blocked while the server is processing the call and only resumed execution after the server is finished.

The sequence of events in a remote procedure call are given as follows −
>1. The client stub is called by the client.
2. The client stub makes a system call to send the message to the server and puts the parameters in the message.
3. The message is sent from the client to the server by the client’s operating system.
4. The message is passed to the server stub by the server operating system.
5. The parameters are removed from the message by the server stub.
6. Then, the server procedure is called by the server stub.
<p id="L330"></p>
#### Advantages of Remote Procedure Call

Some of the advantages of RPC are as follows −
>- Remote procedure calls support process oriented and thread oriented models.
- The internal message passing mechanism of RPC is hidden from the user.
- The effort to re-write and re-develop the code is minimum in remote procedure calls.
- Remote procedure calls can be used in distributed environment as well as the local environment.
- Many of the protocol layers are omitted by RPC to improve performance.

<p id="L340"></p>
#### Disadvantages of Remote Procedure Call
Some of the disadvantages of RPC are as follows −
>- The remote procedure call is a concept that can be implemented in different ways. It is not a standard.
- There is no flexibility in RPC for hardware architecture. It is only interaction based.
- There is an increase in costs because of remote procedure call.

### Session Layer Protocols :
Session Layer uses some protocols which are required for safe, secure and accurate communication which exists between two-ender user applications.
Following are some of the protocols provided or used by the Session Layer –
<p id="L350"></p>
- ***AppleTalk Data Stream Protocol (ADSP):*** ADSP is that type of protocol which was developed by Apple Inc. and it includes a number of features that allow local area networks to be connected with no prior setup. This protocol was released in 1985. 
This protocol rigorously followed the OSI model of protocol layering. ADSP itself has two protocols named: AppleTalk Address Resolution Protocol (AARP) and Name Binding Protocol (NBP), both aimed at making system self-configuring.
- ***Real-time Transport Control Protocol (RTCP):*** RTCP is a protocol which provides out-of-band statistics and control information for an RTP (Real-time Transport Protocol) session. RTCP’s primary function is to provide feedback on the quality of service (QoS) in media distribution by periodically sending statistical information such as transmitted octet and packet counts or packet loss to the participants in the streaming multimedia session.
- ***Password Authentication Protocol (PAP):*** Password Authentication Protocol is a password-based authentication protocol used by Point to Point Protocol (PPP) to validate users. Almost all network operating systems, remote servers support PAP. PAP authentication is done at the time of the initial link establishment and verifies the identity of the client using a two-way handshake (Client-sends data and server in return sends Authentication-ACK (Acknowledgement) after the data sent by client is verified completely).
- ***Remote Procedure Call Protocol (RPCP):*** Remote Procedure Call Protocol (RPCP) is a protocol that is used when a computer program causes a procedure (or a sub-routine) to execute in a different address space without the programmer explicitly coding the details for the remote interaction. This is basically the form of client-server interaction, typically implemented via a request-response message-passing system.
- ***Sockets Direct Protocol (SDP):*** Sockets Direct Protocol (SDP) is a protocol that supports streams of sockets over Remote Direct Memory Access (RDMA) network fabrics. The purpose of SDP is to provide an RDMA-accelerated alternative to the TCP protocol. The primary goal is to perform one particular thing in such a manner which is transparent to the application