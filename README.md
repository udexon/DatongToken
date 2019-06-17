# Datong Token 大同币

> Datong Token 大同币: a simple yet extensible and revolutionary cryptocurrency framework based on
RSA cryptosystem, developed using Homogenet. Datong is taken from Confucius’ legendary
teaching 礼运大同篇 Liyun Datong chapter, where a utopian worldview is depicted. Datong
Token can be used to interface to all national currencies, bullions and other cryptocurrencies,
as well as serving the unbanked population, estimated to be more than 1/3 of world
population.

Datong 大同 literally means Grand Harmony or Grand Unifying Token. We envision it to be the token that would unify all tokens.

The name Datong is inspired by a legendary classic text by Confucius 礼运大同篇 Liyun Datong Chapter, where a utopian world view is depicted. In fact, we believe that Datong Token can become something revolutionary just like HTML and Linux, where technology accelerate the cycle of wealth and value creation, helping us making the world better faster.

https://wk.baidu.com/view/40b64923f5335a8102d220db?pcf=2

Ever since the Bretton Woods Treaty initiated the movement to abolish gold and silver bullions as primary currencies around the world, we now have numerous national currencies as well as a myraid of cryptocurrencies.

Is it possible to create a token to unify them all? The solution appears to be so simple. Mathematically speaking, when a simple solution is discovered for a difficult problem, then we are actually discovering something great.

Consider a scenario where Sender A who lives in country P wishes to send an amount X in currency K to Recipient B who lives in country Q.

Sender A requests Recipient B's public key. A encrypts message MA (Datong payment token) and sends token to B. Recipient B decrypts message using own private key. 

Sender A must include own public key in payment token, so that Recipient B can encrypt message MB and send it to Agent C, who lives in the same country Q as B.

Then Agent C can send an encrypted message to Agent D, who lives in the same country P as Sender A, to verify payment.

Once the payment chain is verified, Agent D may collect cash from Sender A physically or use the national banking system in country P to collect the payment. Agent D will pay Agent C using their own international payment method. Agent C can then pay Recipient B cash physically in person, or using the national banking system in country Q.


### (Non)-Adoption of Cryptocurrencies

Datong Token immediately solves the adoption problem of cryptocurrencies. In order for a particular cryptocurrency to be useful, by definition, the sender and the recipient both have to create a personal account for the cryptocurrency concerned.

In Datong Token, the mechanisms involved in a cryptocurrency transaction are broken down to the bare minimum. In the scenario described above for payment using Datong Token, the sender and recipient do not need to create personal accounts on Datong system. 

After A sends the token to B, presumably via a mobile chat service such as WhatsApp, B will use a Datong app to process then token, then send a new token to agent C. Agent C again will use a Datong app to process the token, and send a new token to Agent D. Agent D will also use a Datong app to process the token, and send a new token to Sender A.

(We use the term "a Datong app" to imply the fact that third parties may produce apps that comply to the Datong protocols.)

All the transmissions of token can be done by sending text messages on chat apps like WhatsApp.

Finally, A will use a Datong app to verify then token from D, to confirm that D is an authorized agent who will send money via conventional means to C, and C will send money via conventional means to B. After this confirmation, A may send money to D via conventional means, to initiate the transaction. 

Now consider this variation:

-- Agent D sends money using cryptocurrency L to Agent C.

Let's illustrate the two scenarios in diagrams:

Scenario 1:

<img src="https://github.com/udexon/DatongToken/blob/master/pay_wu.png" width="400"  />


Scenario 2:

<img src="https://github.com/udexon/DatongToken/blob/master/pay_bch.png" width="400"  />




We now have sufficient understanding to compare and analyse various fundamental issues concerning international financial transactions, cryptocurrencies and Datong Token.

From the technical perspective, what are the roles of RSA in both scenarios?


Firstly, as with Bitcoin, we use RSA cryptosystem to authenticate the users (Sender, Recipient, Agents). 

However, in Bitcoin, after the sender and recipient identities are authenticated, the programs concerned automatically carry out a series of operations to deduct the balance from the wallet of the sender and add the exact same amount in the recipient's wallet (which can be either in software or hardware).

In Datong Token, it is the human users (Sender, Recipient, Agents) who will perform the operations as specified in the token.





Just like HTML and Linux, something small and simple can replicate worldwide and become revolutionary.

Consider a simple act of tipping an Instamgrammer in a developing country like Vietnam using Datong Token.

The Sender A only has to send the Recipient B a text message M, consisting of A's public key APBK, and tip amount X in a local currency, e.g. Vietnam Dong (VND).

At this point, B does not have a Datong account yet. She (he) received the message M from A via private message, or possibly in an Instagram comment, which is publicly viewable. This might be done for promotional purposes, i.e. to show off to other followers.

B only has to download a Datong app and use it to generate her (his) own public key BPBK.

B will then send her public key BPBK to an agent C, together with message M, using the Datong app.

C would need to find an Agent D in the home country of Sender A, who would then collect the payment from A in their national currency using their national banking system. C would pass the message from B to D. D would send the message to A to verify the transaction. The chain of payments as described above will be performed to complete the transaction.

Datong network would have many agents in each country, so that they would compete with each other to lower their commission fees.

As a result, agents using cryptocurrencies will have much greater demand for international money transfer, which in turn improve the adoption of cryptocurrencies.


#### Follow Up:

[ Datong Token Demo Code ](https://github.com/udexon/DatongToken/blob/master/RSA.md)

[ Datong Token Single Agent Use Case #1 ](https://github.com/udexon/DatongToken/blob/master/2_1_Single_Agent.md)

#### Further Reading:

https://en.bitcoin.it/wiki/How_bitcoin_works

> First is public key cryptography. Each coin is associated with its current owner's public ECDSA key. When you send some bitcoins to someone, you create a message (transaction), attaching the new owner's public key to this amount of coins, and sign it with your private key. When this transaction is broadcast to the bitcoin network, this lets everyone know that the new owner of these coins is the owner of the new key. Your signature on the message verifies for everyone that the message is authentic. The complete history of transactions is kept by everyone, so anyone can verify who is the current owner of any particular group of coins.

https://www.dummies.com/software/other-software/bitcoin-public-private-keys/

https://coinsutra.com/bitcoin-private-key/

https://www.reddit.com/r/programming/

https://www.reddit.com/r/crypto/
