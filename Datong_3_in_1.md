Datong Token 3-in-1 Module

Original App + Phos ( WebSocket + RSA )

三生萬物

The user identity (UID) that is most widely used in social media applications today is largely a direct descendant of the Unix user identity, primarily based on symmetric encryption, i.e. the encryption and decryption for authentication use the same key derived from the password string supplied by the user. The password file is a single file in the /etc directory in most of the Linux operating system in use today. This practice dates back to the 1970 where a large number of users accessed a central server, which ironically were much less powerful than today's Android phone. As such, radically different ways of manageing user identities could have been implemented but unfortunately bad habits die hard.

It was also during the 1970s, asymmetric encryption (encryption using public key, decryption using private key) was proposed. It is now being widely used in various applications, e.g. [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) in network connections. 

As the number of social media apps and cryptocurrencies increase, users generally finds it increasingly cumbersome to manage passwords for diffrent apps.

Cryptocurrencies and the blockchain technologies have been the literal black horse in the past decade. Despite its upheavals in the past few years, Bitcoin has firmly established the viability of cryptocurrencies with about USD130 billion market capitalization. Nevertheless, the complications arising from user identity management may become a bottleneck for its continued growth.

Another area where novel methods in user identity management will be critical  is ___CLOUDLESS COMPUTING___, i.e. utilizing the computing power of mobile devices instead of those of the servers in the fixed line networks.


### WebSocket + RSA

The following is an example for Datong Token using WebSocket and RSA.

https://dev.to/spukas/learn-websockets-by-building-simple-chat-app-dee



<img src="https://github.com/udexon/DatongToken/blob/master/Party_A.png" width=700>

<img src="https://github.com/udexon/DatongToken/blob/master/Party_B.png" width=700>


#### Phos Stack Machine Shell (Smashlet) Programming

Stack Machine Shell (Smashlet) is similar to C++-to-Python, C++-to-Java or other application programming interface involving different programming languages. In this case, C++ is the "upstream" programming language and Python and Java are the "downstream" programming language, using analogy from supply chain model.

In smashlet, the upstream programming language can be any of JavaScript, Java, PHP, C++ etc, while the downstream programming language is an implementation of Forth like Reverse Polish Notation called Phos.

The basic operations of the Phos smashlet include:
- parse a space delimited string into a list of tokens;
- push non-fuction token onto the stack;
- map function token to target function in host programming language and execute it.

1. In figure 1, Party A sends its public key to the WebSocket server:
- `F("exkey: wss:")`

Each token is mapped to a JavaScript function as shown in figure 3. The Phos word (function token) `exkey:` is mapped to function `fgl_exkey()`, etc.

2. In figure 2, Party B imports the public key from Party A (PUBKEY_A):
- `S.push("-----BEGIN PUBLIC KEY----- MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKMbgVsxfz4De98F1Ba02klrAf+bLzOt RCxSY3IpwWpa3Mg1AOiiQ/sPxtDUs+oLiZci4Rh9x4+RMc4GWuGCWa0CAwEAAQ== -----END PUBLIC KEY-----")`
- `F("imkey: hello_phos ecr: wss:")`

and encrypt a message ("hello__phos"), then sends it to the WebSocket server.

3. In figure 1, Paty A decrypts the encrypted message:
- `S.push("EQsUAvAC87EYthks4TQDoTqVmKx9ziDN/80l9Z0GcLQrMri1VgTuJ3Jz/SpxflCPlveZ2p5yDhxB3eD4bNvCIQ==")`
- `F("dcr:")`


```JavaScript
ws = connection;

function fgl_wss() // websocket send
{   ws.send( S.pop() ); }

function fgl_exkey()
{    S.push( key.exportKey('pkcs8-public-pem') ); }

function fgl_imkey()
{    key.importKey( S.pop() );  }

function fgl_dcr() // decrypt
{    S.push( key.decrypt( S.pop(), 'utf-8') );  }

function fgl_ecr() // encrypt
{    S.push( key.encrypt( S.pop(), 'base64') );  }
```
