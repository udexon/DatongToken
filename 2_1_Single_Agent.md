<h2> Single Agent Use Case #1 </h2>

Let us consider a "trivial" (in fact, not so trivial) case of a Sender A tipping Recipient B, involving a single Agent C, all living in the same country.

As described previously, Datong Token is useful when the tippee (party receiving the tip) does not have a common online payment system as Sender A, or A does not know about B's payment details, a very common situation we encounter daily on social media.

<img src="https://github.com/udexon/DatongToken/blob/master/one_agent.png" width=300>

1. As described previously, A may send B a message containing the payment details (amount in local currency, e.g. Malaysian Ringgit MYR10), togetherr with A's public key APBK. This message is generated through a Datong app, and may be sent to B via private chat, or in an Instagram comment section, visible to other users, for promotional purposes -- i.e. A is a fan of B, and he (she) would like the world to know that he is tipping B with MYR10.

2. At this point, B can download a Datong app to realize the transaction.

3. B then uses the Datong app to generate encrypted text message T, contain her (his) own public key BPBK, APBK and Agent C's public key CPBK, together with original message from A.

4. Agent C receives the message from B, then uses Datong app to process the incoming message, and to produce an authorization message to be sent to A.

5. Sender A recieves the message from Agent C and authorizes the payment. 

6. C will send A his (her) online banking details.

7. A pays C via online banking system.

8. C pays B via online banking system.


Accenture reported that there are more the underbanked or unbanked persons made up more than one third of the world's population than.

https://www.accenture.com/my-en/insight-billion-reasons-bank-inclusively

Much of Asia including Chinese territories (mainland China and overseas) still actively use something similar to the traditional Hawala system.

https://en.wikipedia.org/wiki/Hawala

Consider the scenario described above, Sender A would deposit MYR 200 with the Agent C, who would allow him to remit up to MYR 100 using Datong Token, while earning interests from A's deposit.
