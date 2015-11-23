## SOCKET

### 什么是socket?

在普通英语里，墙上你用来插电吹风插头的那个孔叫socket。  

Socket构成要素：

1. 地址  
    一个互联网上的socket地址，是一个IP地址加上一个port。  

2. 协议（TCP, UDP, raw IP)，TCP53 和UDP53 是两个不同的socket。


### Socket的属性
一台TCP服务器可能同时与若干个客户端建立socket连接。服务器给每个客户端创建一个socket.  
这些socket在服务器上的地址是相同的，而在远端的客户端上的地址则各不相同(IP不同了嘛，端口也可能不一样）

使用`netstat > socket_info` 可以查看本机当前建立的所有socket的信息，以下是一个样例的截取文本：

    Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
    tcp4       0      0  bogon.60443            117.121.26.197.32930   ESTABLISHED
    tcp4       0      0  bogon.60442            117.121.26.197.32930   ESTABLISHED
    tcp4       0      0  bogon.60441            117.121.26.197.32930   ESTABLISHED
    tcp4       0      0  bogon.60440            117.121.26.197.32930   ESTABLISHED
    tcp4       0      0  bogon.60427            42.81.5.76.http        CLOSE_WAIT 

我们可以看到本机与`117.121.26.197.32930`建立了多个基于`tcp4`协议的socket. 状态是`ESTABLISHED`。  
也就是说本地机器也可以针对服务器的同一个端口，建立多个socket连接。  
此外，最下面的一个socket连接的是`42.81.5.76`的http(80)端口，状态是`CLOSE_WAIT`

### Socket连接类型

* 使用UDP的socket
* 使用TCP的socket
* 使用Raw IP的socket，通常用于路由器或其他网路设备，会绕过传输层，packet header对application可见
* 用于内部进程沟通的Socket

在同一个本地IP地址和本地端口号上一台服务器可以建立多个TCP sockets，其中的每一个socket都被对应到每一个服务器上的子进程上，来服务相对应的客户端进程。  
操作系统会把这些sockets当做不同的socket处理，因为这些socket的socket pair元组不同（远程客户端的IP地址和端口号是不同的）。  

所以一个server能开启的最大sockets数，会受到其最大process数的限制。  
你可以使用`ulimit -u`来查看当前用户的process开启上限数量。  
根据`广州-阿杜`的观点，每个端口能开的最大socket数会收到`ulimit -u`命令里所显示的，单进程能开启最大file-descriptor数量的影响。  
此命令的参数，决定了在某一个端口上能同时开启多少个socket.  
不过我现在不确定，在同一个端口上开新的socket连接，socket和map子进程是各消耗一个file descriptor还是一起消耗一个，所以还不确定这个值是否要除以2。


而对于UDP协议而言，服务器端口不与各个客户端端口建立单独的连接。共用端口的客户端的消息，会按到达时间的先后顺序被处理。  


### 什么是Websocket?
Websocket 置身于 HTTP协议的框架内，通过80端口完成通信。  
`ws` 和 `wss`是websocket里新的uri词缀，分别对应不加密连接和加密连接。  
当有机密信息通过websocket传输时，最好使用token加密。  
如果用户用了Proxy，而proxy不支持websocket时，可能导致websocket连接失败。  
不加密的websocket连接通过透明的代理服务器时，几乎一定会传输失败，所以不加密的websocket连接只能用在非常简单的拓扑关系中。  


[websocket原理详解](http://www.zhihu.com/question/20215561)


## IP

### 什么是IP?
IP实际上是`Internet Protocol`的缩写，互联网协议！简单明了吧。  


### IP协议干什么的
IP协议对addressing hosts和从一个源host传到另一个target host的routing datagram(packets)负责。  

换而言之，IP协议负责给互联网上所有host分配地址，同时尽力使从一个地址往另一个地址发送信息得以实现。  

假设我的Internet Protocol Address地址是`1.2.3.4`，我要用最原始的IP协议（不附加TCP协议）发送一段消息"Ululu"到`5.6.7.8`这台机器。中间会发生什么呢？  

我写了一封信，收件人地址和寄件人地址都有了，内容封在里面。谁来递信？routers(路由器）  
routers是互联网里实际上的消息转发者。

> [关于互联网协议运作机理的文章](http://www.ruanyifeng.com/blog/2012/05/internet_protocol_suite_part_i.html)


### 什么是NAT?

### 信息如何在不同的计算机之间传输？
互联网世界分为很多层。 我们接下来讲的涉及其中的两个层：Link层和network层。  
我现在要发送一段信息给汪爹爹，我需要怎么做？  
我直接拿一根网线把我和汪爹的机器连起来，我和汪爹就在同一个局域网了（现代网卡具备端口翻转功能）。  
这个网，是根据以太网(Ethernet)协议建立起来的，我们现在能见到的局域网，可以说，全是根据以太网协议建立起来的。  
以太网根据什么东西传送信息呢？根据你网卡上的MAC地址。每块网卡在出厂时都拥有地球上独一无二的MAC地址(其实是散列足够大，可认为近似为独一无二)。  
MAC地址的一部分是厂商编号，另一部分是厂商流水号。  
以太网里最底层的机制叫broadcasting（广播），在以太网里传输的信息由两个部分组成，`Headers`和`data`。  
`Headers`里的信息主要是，我是哪个mac地址，我要发到哪个mac地址去。  
最原始的以太网交换机怎么发送消息呢，当你选择发送一条消息时，它会给当前局域网里所有机器发送该消息。  
局域网里的机器收到该消息，一看`header`里写着`致李冬梅`，扭头看看自己脸上，写着`秦刚`, biaji就把消息扔了。  
只有看见自己脸上写有`李冬梅`的机器，才会读该消息。当然这都靠机器自觉。你可以把机器教坏，让它啥都读。这样别人广播传送的数据你就都知道了。  
当然现在的交换机比较先进，会缓存一个ip和mac地址的映射表，发送广播的机会不多。

如果汪爹爹和我离得很远，我们又该如何传递信息呢？  
互联网实际上是由许多大小不一的子网络(subnet)组成的。子网内每台机器上都有一个子网掩码，子网掩码会指明你的ip地址里哪些是subnet的host抬头，哪些是本机子网编号。  
当你尝试向一个IP发送信息时，消息先到达的是gateway机器，以太网协议发送者是本机，接受者是gateway的MAC地址。  
gateway会拿你的IP, 目标IP与你的子网掩码做计算，看这个IP是否在内网里，如果在内网里，将Ether协议header里发送者MAC地址改写为gateway，目的地写该内网机器MAC地址，数据部分不动。。  
如果经过对比，发现目标IP不在同一子网里，你就会把这个包发给你的gateway, gateway收到这个包之后，将包转发给router(一说gateway和router本质上是相同的！）。  
router里面有内置的静态表(ISP管理员提供）和一个动态表，根据这两个表它会找到一条通往目标IP的路由路径，然后沿着这条路径转发这个包，如果找不到路径，它直接就把包扔掉。  
最后的目的地router接到这个包后，会找到目标IP对应的MAC地址，把包转发给那台机器。

> [路由器原理解释](http://tw.18dao.net/%E8%B7%AF%E7%94%B1%E8%BF%BD%E8%B9%A4/%E8%B7%AF%E7%94%B1%E5%99%A8%E5%8E%9F%E7%90%86)

## TCP

### 什么是TCP?
TCP 的全称是Transmission Control Protocol.  它处在在`Transmission layer`，  
TCP的结构是比较复杂的。总的说起来，它能实现稳定的数据传输，保证数据传送的内容完整度和正确顺序(通过校验和要求重发机制）。  
这是纯IP协议难以做到的（互联网环境太复杂。包损坏或丢失的情况很容易发生，而且很可能出现后发包先到的情况）  
在TCP协议里，有一个sequnce number，它有两个角色,  
当`SYN`flag被设置为1的时候，实际的第一个数据字节的sequence number和对应端返回的`ACK`包的acknowledge number是此数字+1；  
如果`SYN`flag是0，则此sequnce number用来表示当前会话里的累积序列号。  
在传输数据前，TCP协议会要求传输双方进行连接，在进行连接的过程中会进行著名的“三次握手”：  
1. 客户端将自己的sequence number设为随机值A，发送一个`SYN`包给服务器。  
2. 服务器发送一个`SYN-ACK`包回去，`SYN`部分的sequence number是另一个随机值B，`ACK`部分的acknowledge number是`A+1`.  
3. 客户端发送`ACK`包返还给服务器，acknowledge number是B+1，sequence number是A+1.

## UDP

### 什么是UDP
UDP的全称是User Datagram Protocol.  
UDP在传输时并不建立连接。  
当你不需要数据的可靠性而想尽可能减少数据的延迟，你可能会需要用到UDP协议。


## HTTP

### 什么是HTTP?
HTTP 的全称是 Hypertext Transfer Protocol，它属于应用层。  
HTTP是无状态协议，也就是说服务器不为user保留任何状态和属性值。  
我们经常用HTTP传输HTML文件。  


### HTTP METHODS
GET: 请求特定资源
HEAD: 和GET效果一样，但是不需要返回message body
POST: 将特定资源递交给服务器
PUT: 请求将特定资源放在指定URI下，如果指定URI下已有资源，替换之
DELETE: 请求删除指定资源
TRACE: DEBUG用
OPTIONS: 问一个服务器它对于特定URL支持哪些methods
CONNECT: 将一个请求变成透明的TCP/IP通道，通常用来利用HTTP Proxy服务器进行HTTPS通信
PATCH: 请求对一个资源进行修改

### HTTP 消息格式
请求消息格式：
* request line, e.g. `GET /logo.png HTTP/1.1`
* [Resquest Head Fields](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Request_fields)
* An empty line
* An optional message body

在HTTP/1.1协议里，除了 Host 以外的Head Fields都是Optional的。


返回消息格式：
* Status-Line, 包括status code和一条status message, 如`HTTP/1.1 200 OK`
* [Response Header Fields](https://en.wikipedia.org/wiki/HTTP_response_header_field)
* An empty line
* An optional message body

在Response里并没有强制使用的header，比较常用的header是content-type, 如`Content-Type: text/html`

另外，在Header里面，我们也可以使用自己创造的Header field，就像websocket所做的那样。

### HTTP返回状态
1XX     Informational
2XX     Successful
3XX     Redirection
4XX     Client Error
5XX     Server Error

[HTTP 所有返回状态详解](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

## Jargons
Ethernet:   Frame
IP:         Datagram
TCP:        Segment


## 什么是互联网7 layers?
https://en.wikipedia.org/wiki/OSI_model

如果要分成五层我会分为：
Application层：     Data
Transmission层：    TCP, UDP
Network层：         IP
Link层：            Ethernet
Physics层：         Bit



