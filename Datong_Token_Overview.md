### Datong Token Overview

[Datong Token Examples](https://github.com/udexon/EMYL/blob/master/E003_Online_Tipping.md) illustrates several issues concerning identity management, cryptocurrencies as well as conventional financial transactions.

Consider the following scenarios.

Scenario I: Online Tipping with Datong Token via Datong Agents using Western Union

<img src="https://github.com/udexon/DatongToken/blob/master/pay_wu_agents.png" width=400>

Scenario II: Online Tipping with Datong Token via Datong Agents using Bitcoin Cash

<img src="https://github.com/udexon/DatongToken/blob/master/pay_bch_agents.png" width=400>

Scenario III: Direct Money Transfer using Western Union without Agents

<img src="https://github.com/udexon/DatongToken/blob/master/pay_wu_direct.png" width=400>

Scenario IV: Direct Money Transfer using Bitcoin without Agents

<img src="https://github.com/udexon/DatongToken/blob/master/pay_bch_direct.png" width=400>


Describe the roles and functions of transactions, identity management and cryptography in each of Scenarios I II III IV.

A transaction is defined as the transfer of an amount in currency CP by party A in country P to the equivalent in currency CQ for party B in country Q, minus commission fees.

For now, we ignore the special cases where a legal person may own bank accounts in different countries, or a user may own more than one accounts of the same cryptocurrency.

In Scenario III (Direct Money Transfer using Western Union without Agents), identity management is carried out by the Western Union Agents and Systems (software and hardware), utilizing national identity documents and transaction code sent by Sender A to Recipient B.

In Scenario IV (Direct Money Transfer using Bitcon Cash without Agents), identity management and transaction are carried out by a series of operations described in the following document as well as other related resources:

https://en.bitcoin.it/wiki/Transaction

Bitcoin and code represent one of the most comprehensive documentation and code for financial transactions. 


By comparing Scenarios I, II and III, we may conclude that Datong Token minimizes the costs of transactions for international money transfer, as well as enables a much greater number of people to act as money transfer agents.

This is a new area in law --- rules on tipping? Possible to control source code export? What if source code is broken down into pieces? How to enforce? 20 years problem?


- Compare Scenarios I II III -- this is high level perspective, how to link to RSA? Explore identity management?
- From the technical perspective, what are the roles of RSA in both scenarios?
- Minimizing agent fees
- (Non)-Adoption of Cryptocurrencies
- Datong app -- meaning?
- Punchline? Linux and Datong Token both being simple but has great impact?

Transaction: 
- --( is a high level function of )--> Identity Management
- --( is a high level function of )--> Cryptography

Start with DT applied to face to face payments and Western Union. Describe its abstract significance.

Redefine user identity, money, national supervision, person vs. government rights, banking system, financial institution etc.


Explain: how to develop network of agents.


Scenario IV: Bitcoin users C to Do

Let us attempt to describe a generalized model for Scenarios I to IV.

https://en.wikipedia.org/wiki/Legal_person

Transaction: (is defined as) ... accounts in different countries owned by the same person?
