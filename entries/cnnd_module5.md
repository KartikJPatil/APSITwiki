# Module 5: Presentation layer & Application layer

### Presentation layer:
- Compression: Comparison between Lossy Compression and Lossless Compression
- Huffman Coding
- LZW
- RLE
- Image Compression – GIF,JPEG
- Speech Compression
<p id="L10"></p>
### Application layer:
- Standard Client-Server Protocols:
  - World Wide Web
  - HTTP
  - FTP
  - Electronic Mail
  - Domain Name System (DNS)
  - SNMP

<p id="L20"></p>
## Presentation layer: 
#### Design Issues in Presentation Layer:
The syntax and the semantics of the information exchanged between two communication systems is managed by the presentation layer of the OSI Model.
Before going through the design issues in the presentation layer, some of its main functions are:
>1. Translation –
It is necessary that the information which is in the form of numbers, characters and symbols needs to be changed to the bit streams. The presentation layer handles the different encoding methods used by different machines .It manages the translation of data between the format of network requires and computer.
2. Encryption –
 The data encryption at the transmission end as well as the decryption at the receiver end is managed by the presentation layer.

<p id="L30"></p>
3. Compression –
 In order to reduce the number of bits to be transmitted, the presentation layer performs the data compression. It increases efficiency in case of multimedia files such as audio, video etc.




#### Compression:

Data compression is the function of presentation layer in OSI reference model. Compression is often used to maximize the use of bandwidth across a network or to optimize disk space when saving data.
<p id="L40"></p>
There are two general types of compression algorithms:

1. Lossless compression

2. Lossy compression

#### Lossless Compression
Lossless compression compresses the data in such a way that when data is decompressed it is exactly the same as it was before compression i.e. there is no loss of data.
A lossless compression is used to compress file data such as executable code, text files, and numeric data, because programs that process such file data cannot tolerate mistakes in the data.
<p id="L50"></p>
Lossless compression will typically not compress file as much as lossy compression techniques and may take more processing power to accomplish the compression.

##### Lossless Compression Algorithms
The various algorithms used to implement lossless data compression are :
>1. Run length encoding

2. Huffman Coding

3. Dictionary based encoding: Lempel–Ziv–Welch (LZW)
<p id="L60"></p>

**1.Run length encoding**
This method replaces the consecutive occurrences of a given symbol with only one copy of the symbol along with a count of how many times that symbol occurs. Hence the names ‘run length’.
It is supported by most bitmap file formats, such as TIFF, BMP, and PCX. RLE is suited for compressing any type of data regardless of its information content
The general idea behind this method is to replace consecutive repeating occurrences of a symbol by one occurrence of the symbol followed by the number of occurrences.
The method can be even more efficient if the data uses only two symbols (for example 0 and 1) in its bit pattern and one symbol is more frequent than the other.
>- For example, the string AAABBCDDDD would be encoded as 3A2BIC4D.


<p id="L70"></p>

A real life example where run-length encoding is quite effective is the fax machine. Most faxes are white sheets with the occasional black text. So, a run-length encoding scheme can take each line and transmit a code for while then the number of pixels, then the code for black and the number of pixels and so on.
This method of compression must be used carefully. If there is not a lot of repetition in the data then it is possible the run length encoding scheme would actually increase the size of a file.

**2.Huffman Coding**
Huffman coding is a lossless data compression algorithm. 
The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters. 
The variable-length codes assigned to input characters are Prefix Codes, means the codes (bit sequences) are assigned in  such a way that the code assigned to one character is not the prefix of code assigned to any other character. 
This is how Huffman Coding makes sure that there is no ambiguity when decoding the generated bitstream. 
<p id="L80"></p>

**3.Dictionary based encoding**
• One of the best known dictionary based encoding algorithms is Lempel-Ziv (LZ) compression algorithm.

• This method is also known as substitution coder.

• In this method, a dictionary (table) of variable length strings (common phrases) is built.

• This dictionary contains almost every string that is expected to occur in data.
<p id="L90"></p>
• When any of these strings occur in the data, then they are replaced with the corresponding index to the dictionary.

• In this method, instead of working with individual characters in text data, we treat each word as a string and output the index in the dictionary for that word.

• For example, let us say that the word “compression” has the index 4978 in one particular dictionary; it is the 4978th word is usr/share/dict/words. To compress a body of text, each time the string “compression” appears, it would be replaced by 4978.

#### Lempel–Ziv–Welch (LZW) 


<p id="L100"></p>
Lempel–Ziv–Welch (LZW) is a universal lossless data compression algorithm created by Abraham Lempel, Jacob Ziv, and Terry Welch.
The algorithm is simple to implement and has the potential for very high throughput in hardware implementations.
It is the algorithm of the widely used Unix file compression utility compress and is used in the GIF image format.
LZW compression uses a code table. A common choice is to provide 4096 entries in the table. In this case, the LZW encoded data consists entirely of 12 bit codes, each referring to one of the entries in the code table.
Uncompression is achieved by taking each code from the compressed file, and translating it through the code table to find what character or characters it represents.
Codes 0-255 in the code table are always assigned to represent single bytes from the input file.

#### Lossy Compression

<p id="L110"></p>
Lossy compression is the one that does not promise that the data received is exactly the same as data send i.e. the data may be lost.
This is because a lossy algorithm removes information that it cannot later restore.
Lossy algorithms are used to compress still images, video and audio.
Lossy algorithms typically achieve much better compression ratios than the lossless algorithms.

#### Audio Compression/ Speech Compression
• Audio compression is used for speech or music.

• For speech, we need to compress a 64-KHz digitized signal; For music, we need to compress a 1.411.MHz signal
<p id="L120"></p>
• Two types of techniques are used for audio compression:

1. Predictive encoding

2. Perceptual encoding




<p id="L130"></p>
**Predictive encoding**
>- In predictive encoding, the differences between the samples are encoded instead of encoding all the sampled values.
- This type of compression is normally used for speech.
- Several standards have been defined such as GSM (13 kbps), G. 729 (8 kbps), and G.723.3 (6.4 or 5.3 kbps).

**Perceptual encoding**
>- Perceptual encoding scheme is used to create a CD-quality audio that requires a transmission bandwidth of 1.411 Mbps.
- MP3 (MPEG audio layer 3), a part of MPEG standard uses this perceptual encoding.
- Perceptual encoding is based on the science of psychoacoustics, a study of how people perceive sound.
<p id="L140"></p>
- The perceptual encoding exploits certain flaws in the human auditory system to encode a signal in such a way that it sounds the same to a human listener, even if it looks quite different on an oscilloscope.
- The key property of perceptual coding is that some sounds can mask other sound. For example, imagine that you are broadcasting a live flute concert and all of a sudden someone starts striking a hammer on a metal sheet. You will not be able to hear the flute any more. Its sound has been masked by the hammer.
- Such a technique explained above is called frequency masking-the ability of a loud sound in one frequency band to hide a softer sound in another frequency band that would have been audible in the absence of the loud sound.
- Masking can also be done on the basis of time. For example: Even if the hammer is not striking on a metal sheet, the flute will be inaudible for a short period of time because the ears turn down its gain when they start and take a finite time to turn up again.
- Thus, a loud sound can numb our ears for a short time even after the sound has stopped. This effect is called temporal masking.

**MP3**
- MP3 uses these two phenomena, i.e. frequency masking and temporal masking to compress audio signals.
- In such a system, the technique analyzes and divides the spectrum into several groups. Zero bits are allocated to the frequency ranges that are totally masked.
<p id="L150"></p>
- A small number of bits are allocated to the frequency ranges that are partially masked.
- A larger number. of bits are allocated to the frequency ranges that are not masked.
- Based on the range of frequencies in the original analog audio, MP3 produces three data rates: 96kbps, 128 kbps and 160 kbps.


## Application layer:
It is the top most layer of OSI Model. The Application Layer contains a variety of protocols that are commonly needed by users. One widely-used application protocol is HTTP(HyperText TransferProtocol), which is the basis for the World Wide Web. When a browser wants a web page, it sends the name of the page it wants to the server using HTTP. The server then sends the page back. Other Application protocols that are used are: File Transfer Protocol(FTP), Trivial File Transfer Protocol(TFTP), Simple Mail Transfer Protocol(SMTP), TELNET, Domain Name System(DNS) etc.


<p id="L160"></p>
#### Standard Client-Server Model 
 - Server send the reply to the client request and provides the service to the client.
 - In order to achieve smooth communication there are certain protocols to follow.
 - Client usually blocks until server responds to its request.
 - Client usually invoked by end users when they require service.
 - Server usually waits for incoming requests .
 - Server can have many clients making concurrent requests.
- A server, generally speaking, is a program which provides some service to other (client) programs. The connection between client and server is normally by means of message passing(request & reply), often over a network, and uses some protocol to encode the client's requests and the server's responses. The server may run continuously (as a daemon), waiting for requests to arrive. Often clients and servers communicate over a computer network on separate hardware, but both client and server may reside in the same system .

<p id="L170"></p>
**Client server paradigm** is a way to explain how a client communicates with the server in order to avail the services/applications present at the server side. It is assumed that client and server are present in the same network. From the above diagram we can see that one server is fetching required information to two clients using network. One client can serve the services to multiple clients at the same time. There should be a proper scenario where client and server should follow in order to achieve expected communication between them, which is given as follows:
Clients and servers exchange messages in a request-response messaging pattern. The client sends a request, and the server returns a response. This exchange of messages is an example of inter-process communication.
>- Example:1
Client sends the request for connection or to use the service that is present on server.
For.e.g. Student communicating with IT server in order to get their IT login screen using TELNET service:
First students sends request to IT server using command telnet 192.168.200.238
Then server sends the response in the form of login screen asking for username and password
once student/client put their valid username and password on the screen, thay will get access of the TELNET service which is present on the IT server.
-   Example:2      An ATM is actually a client programmed to connect you with your bank's servers.
<p id="L180"></p>

###The World Wide Web
The World Wide Web or Web is basically a collection of information that is linked together from points all over the world. It is also abbreviated as WWW.
World wide web provides flexibility, portability, and user-friendly features.
It mainly consists of a worldwide collection of electronic documents (i.e, Web Pages).
It is basically a way of exchanging information between computers on the Internet.
The WWW is mainly the network of pages consists of images, text, and sounds on the Internet which can be simply viewed on the browser by using the browser software.
It was invented by Tim Berners-Lee.

<p id="L190"></p>
#### Components of WWW

The Components of WWW mainly falls into two categories:
>1. Structural Components

2. Semantic Components

#### Architecture of WWW
The WWW is mainly a distributed client/server service where a client using the browser can access the service using a server. The Service that is provided is distributed over many different locations commonly known as sites/websites.
<p id="L200"></p>
Each website holds one or more documents that are generally referred to as web pages.
Where each web page contains a link to other pages on the same site or at other sites.
These pages can be retrieved and viewed by using browsers.
>1. Client/Browser
 - The Client/Web browser is basically a program that is used to communicate with the webserver on the Internet.
   Each browser mainly comprises of three components and these are:
  - Controller
  - Interpreter
  - Client Protocols
<p id="L210"></p>
The Controller mainly receives the input from the input device, after that it uses the client programs in order to access the documents. After accessing the document, the controller makes use of an interpreter in order to display the document on the screen.
An interpreter can be Java, HTML, javascript mainly depending upon the type of the document.
The Client protocol can be FTP, HTTP, TELNET.
>2. Server
- The Computer that is mainly available for the network resources and in order to provide services to the other computer upon request is generally known as the server.
- The Web pages are mainly stored on the server.
   Whenever the request of the client arrives then the corresponding document is sent to the client.
   The connection between the client and the server is TCP.
   It can become more efficient through multithreading or multiprocessing. Because in this case, the server can answer more than one request at a time.
<p id="L220"></p>
3. URL
URL is an abbreviation of the Uniform resource locator.
It is basically a standard used for specifying any kind of information on the Internet.
In order to access any page the client generally needs an address.
To facilitate the access of the documents throughout the world HTTP generally makes use of Locators.

-  URL mainly defines the four things:

   - ***Protocol***
<p id="L230"></p>
   It is a client/server program that is mainly used to retrieve the document. A commonly used protocol is HTTP.

   - ***Host Computer***
It is the computer on which the information is located. It is not mandatory because it is the name given to any computer that hosts the web page.

   - ***Port***
The URL can optionally contain the port number of the server. If the port number is included then it is generally inserted in between the host and path and is generally separated from the host by the colon.
   - ***Path***
It indicates the pathname of the file where the information is located.
<p id="L240"></p>
>4. HTML

HTML is an abbreviation of Hypertext Markup Language.
It is generally used for creating web pages.
It is mainly used to define the contents, structure, and organization of the web page.
>5. XML
XML is an abbreviation of Extensible Markup Language. It mainly helps in order to define the common syntax in the semantic web.

#### HTTP
<p id="L250"></p>
HTTP stands for HyperText Transfer Protocol.
It is a protocol used to access the data on the World Wide Web (www).
The HTTP protocol can be used to transfer the data in the form of plain text, hypertext, audio, video, and so on.
This protocol is known as HyperText Transfer Protocol because of its efficiency that allows us to use in a hypertext environment where there are rapid jumps from one document to another document.
HTTP is similar to the FTP as it also transfers the files from one host to another host. But, HTTP is simpler than FTP as HTTP uses only one connection, i.e., no control connection to transfer the files.
HTTP is similar to SMTP as the data is transferred between client and server. The HTTP differs from the SMTP in the way the messages are sent from the client to the server and from server to the client. SMTP messages are stored and forwarded while HTTP messages are delivered immediately.
##### Features of HTTP:
- Connectionless protocol: HTTP is a connectionless protocol. HTTP client initiates a request and waits for a response from the server. When the server receives the request, the server processes the request and sends back the response to the HTTP client after which the client disconnects the connection. The connection between client and server exist only during the current request and response time only.
- Media independent: HTTP protocol is a media independent as data can be sent as long as both the client and server know how to handle the data content. It is required for both the client and server to specify the content type in MIME-type header.
<p id="L260"></p>
- Stateless: HTTP is a stateless protocol as both the client and server know each other only during the current request. Due to this nature of the protocol, both the client and server do not retain the information between various requests of the web pages.

##### HTTP Transactions

The above figure shows the HTTP transaction between client and server. The client initiates a transaction by sending a request message to the server. The server replies to the request message by sending a response message.

#### Messages
HTTP messages are of two types: request and response. Both the message types follow the same message format.

<p id="L270"></p>
###### Uniform Resource Locator (URL)
A client that wants to access the document in an internet needs an address and to facilitate the access of documents, the HTTP uses the concept of Uniform Resource Locator (URL).
The Uniform Resource Locator (URL) is a standard way of specifying any kind of information on the internet.

The URL defines four parts: method, host computer, port, and path.


- Method: The method is the protocol used to retrieve the document from a server. For example, HTTP.
- Host: The host is the computer where the information is stored, and the computer is given an alias name. Web pages are mainly stored in the computers and the computers are given an alias name that begins with the characters "www". This field is not mandatory.
<p id="L280"></p>
- Port: The URL can also contain the port number of the server, but it's an optional field. If the port number is included, then it must come between the host and path and it should be separated from the host by a colon.
- Path: Path is the pathname of the file where the information is stored. The path itself contain slashes that separate the directories from the subdirectories and files.

### FTP
FTP stands for File transfer protocol.
FTP is a standard internet protocol provided by TCP/IP used for transmitting the files from one host to another.
It is mainly used for transferring the web page files from their creator to the computer that acts as a server for other computers on the internet.
It is also used for downloading the files to computer from other servers.

<p id="L290"></p>
#### Objectives of FTP
- It provides the sharing of files.
- It is used to encourage the use of remote computers.
- It transfers the data more reliably and efficiently.

#### Why FTP?
Although transferring files from one system to another is very simple and straightforward, sometimes it can cause problems. For example, two systems may have different file conventions. Two systems may have different ways to represent text and data. Two systems may have different directory structures. FTP protocol overcomes these problems by establishing two connections between hosts. One connection is used for data transfer, and another connection is used for the control connection.
>1. Control Connection: For sending control information like user identification, password, commands to change the remote directory, commands to retrieve and store files, etc., FTP makes use of a control connection. The control connection is initiated on port number 21.
2. Data connection: For sending the actual file, FTP makes use of a data connection. A data connection is initiated on port number 20. FTP sends the control information out-of-band as it uses a separate control connection. Some protocols send their request and response header lines and the data in the same TCP connection. For this reason, they are said to send their control information in-band. HTTP and SMTP are such examples. 
<p id="L300"></p>
#### FTP Clients
FTP client is a program that implements a file transfer protocol which allows you to transfer files between two hosts on the internet.
It allows a user to connect to a remote host and upload or download the files.
It has a set of commands that we can use to connect to a host, transfer the files between you and your host and close the connection.
The FTP program is also available as a built-in component in a Web browser. This GUI based FTP client makes the file transfer very easy and also does not require to remember the FTP commands.

#### Advantages of FTP:
- Speed: One of the biggest advantages of FTP is speed. The FTP is one of the fastest way to transfer the files from one computer to another computer.
- Efficient: It is more efficient as we do not need to complete all the operations to get the entire file.
<p id="L310"></p>
- Security: To access the FTP server, we need to login with the username and password. Therefore, we can say that FTP is more secure.
- Back & forth movement: FTP allows us to transfer the files back and forth. Suppose you are a manager of the company, you send some information to all the employees, and they all send information back on the same server.

#### Disadvantages of FTP:
The standard requirement of the industry is that all the FTP transmissions should be encrypted. However, not all the FTP providers are equal and not all the providers offer encryption. So, we will have to look out for the FTP providers that provides encryption.
FTP serves two operations, i.e., to send and receive large files on a network. However, the size limit of the file is 2GB that can be sent. It also doesn't allow you to run simultaneous transfers to multiple receivers.
Passwords and file contents are sent in clear text that allows unwanted eavesdropping. So, it is quite possible that attackers can carry out the brute force attack by trying to guess the FTP password.
It is not compatible with every system.

<p id="L320"></p>
#### Electronic mail (E-mail):
E-mail (electronic mail) is the exchange of computer-stored messages by telecommunication.E-mail messages are usually encoded in ASCII text. However, you can also send non-text files, such as graphic images and sound files, as attachments sent
in binary streams. A large percentage of the total traffic over the Internet is e-mail. Email can also be exchanged between online service provider users and in networks other than the Internet, both public and private.E-mail can be distributed to lists of people as well as to individuals

Email messages are comprised of three components, as follows:
>- Message envelope: Describes the email’s electronic format
- Message header: Includes sender/recipient information and email subject line
- Message body: Includes text, image and file attachments

<p id="L330"></p>
E-mail is one of the protocols included with the Transport Control Protocol/Internet Protocol (TCP/IP) suite of protocols.
One of the way of sending and receiving e-mail (and the more popular solution for most people) is an online e-mail service or webmail. Examples include Hotmail (now Outlook.com), Gmail, and Yahoo Mail. To send and receive e-mail messages, you can use an e-mail program, also known as an e-mail client. When using an e-mail client, you must have a server that stores and delivers your messages, which is provided by your ISP or in some cases, another company. An e-mail client needs to connect to a server to download new e-mail, whereas email stored online updates automatically when you visit the site.
A popular protocol for sending e-mail is Simple Mail Transfer Protocol and a popular protocol for receiving it is POP3.


#### SMTP:
Simple Mail Transfer Protocol (SMTP) is the standard protocol for email services on a TCP/IP network. SMTP provides the ability to send and receive email messages.
SMTP is an application-layer protocol that enables the transmission and delivery of email over the Internet.

<p id="L340"></p>
##### SMTP working:
- When we send an email, our computer connects to our email service’s mail server. A server is a centralized computer which manages a specific type of service. An email server for instance, handles emails. The email server responsible for sending emails is called the SMTP (Simple Mail Transfer Protocol) server. One SMTP server can pass on the mail to another SMTP server and relay it to the destination through several hops.
- Every email has the sender’s address (e.g. sender@sendermail.com) and the recipient’s in the To field (e.g. recipient@recipientmail.com). When an email is sent, the email client connects to the SMTP server of the sender’s email service (e.g. mailserver.sendermail.com). The client transmits the address of the sender, the address of the recipient and the content of the message.
- The SMTP server goes to work at locating the whereabouts of the recipient. Using the recipient’s mail ID (i.e. recipient@recipientmail.com) it locates the domain name –e.g.recipientmail.com.
- If the recipient’s mail ID had the same domain name as the sender, then the process would be simpler. The SMTP server would have transferred the mail to its local outgoing mail server (POP3 or IMAP).• Each domain name represents a unique Web address, called an Internet protocol (IP) address. Think of it as postal addresses of the internet. The link between domain names to their IP addresses is stored in the Domain Name Registry. The SMTP server then contacts the server where the registry is kept (The DNS Server). The DNS server sends back the address to the SMTP server.
- The SMTP server then proceeds to hand over the email to the SMTP server of the recipient’s email service. This SMTP server checks and confirms that the mail addressed to recipient@recipientmail.com belongs to it and hands it over to its counterpart – the POP3 server.



<p id="L350"></p>

### DNS
An application layer protocol defines how the application processes running on different systems, pass the messages to each other.

DNS stands for Domain Name System.
DNS is a directory service that provides a mapping between the name of a host on the network and its numerical address.
DNS is required for the functioning of the internet.
Each node in a tree has a domain name, and a full domain name is a sequence of symbols specified by dots.
DNS is a service that translates the domain name into IP addresses. This allows the users of networks to utilize user-friendly names when looking for other hosts instead of remembering the IP addresses.
<p id="L360"></p>
For example, suppose the FTP site at EduSoft had an IP address of 132.147.165.50, most people would reach this site by specifying ftp.EduSoft.com. Therefore, the domain name is more reliable than IP address.
DNS is a TCP/IP protocol used on different platforms. The domain name space is divided into three different sections: generic domains, country domains, and inverse domain.

##### Generic Domains
It defines the registered hosts according to their generic behavior.
Each node in a tree defines the domain name, which is an index to the DNS database.
It uses three-character labels, and these labels describe the organization type.


<p id="L370"></p>

##### Country Domain
The format of country domain is same as a generic domain, but it uses two-character country abbreviations (e.g., us for the United States) in place of three character organizational abbreviations.

##### Inverse Domain
The inverse domain is used for mapping an address to a name. When the server has received a request from the client, and the server contains the files of only authorized clients. To determine whether the client is on the authorized list or not, it sends a query to the DNS server and ask for mapping an address to the name.

### Working of DNS
DNS is a client/server network communication protocol. DNS clients send requests to the. server while DNS servers send responses to the client.
<p id="L380"></p>
Client requests contain a name which is converted into an IP address known as a forward DNS lookups while requests containing an IP address which is converted into a name known as reverse DNS lookups.
DNS implements a distributed database to store the name of all the hosts available on the internet.
If a client like a web browser sends a request containing a hostname, then a piece of software such as DNS resolver sends a request to the DNS server to obtain the IP address of a hostname. If DNS server does not contain the IP address associated with a hostname, then it forwards the request to another DNS server. If IP address has arrived at the resolver, which in turn completes the request over the internet protocol.

### SNMP
SNMP stands for Simple Network Management Protocol. It is a popular protocol for network managemnet.
It is used for collecting information from, and configuring network devices, such as servers, printers, hubs, switches, and routers on the network. As well as services such as DHCP.
SNMP requires only a couple of basic components to work: a management station, an agent and MIB.
>- First, a management station is required. The management station is simply software that collects information from your network. 
<p id="L390"></p>
- Second, the hardware or software that you want to monitor must have an agent running. The agent collects information and then sends it to the monitoring station when polled. Agents can also send notifications to the management station without being polled, for example, if an error is detected.
Management Information Base – MIB consists of information on resources that are to be managed. This information is organized hierarchically. It consists of objects instances which are essentially variables.

SNMP is very simple, yet powerful. It has the ability to help you manage your network by: 





<p id="L400"></p>
- Collect information on how much bandwidth is being used. 
- Collect error reports into a log, useful for troubleshooting and identifying trends. 
- Email an alert when your server is low on disk space. 
- Monitor your servers’ CPU and Memory use, alert when thresholds are exceeded.
- Page or send an SMS text-message when a device fails. 
- Can perform active polling, i.e. Monitoring station asks devices for status every few minutes. 
- Passive SNMP – devices can send alerts to a monitoring station on error conditions. 


<p id="L410"></p>
Realtime example of SNMP :
If printers are available in network, SNMP gathers and monitors the information and make that information available to PC for printing facility using CUPS service(if PC are connected to that network).







<p id="L420"></p>
##### Strength of SNMP:
>1. It is simple to implement.
2. Agents are widely implemented.
3. Agent level overhead is minimal. 
4. It is robust and extensible.
5. Polling approach is good for LAN based managed objects.
6. It offers the best direct manager agent interface.
7. SNMP meets a critical need.

