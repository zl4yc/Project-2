# DS 3002 Project-2
Author: Shining Wang and Lily Lin (computing id: zl4yc)

Project: YahooFinance API Twitter Bot  

In this project, we created a twitter bot using python and deployed it to a Amazon EC2 intance using docker to run the application automatic and continuous backstage. The twitter bot (@YahooTwitBot) can be used to find useful information regarding to companies' stock ticker value when using the right command. @YahooTwitBot will respond to mentions from Twitter users requesting stock ticker value using a certain company's symbol. The twitter bot can also say hello. If user requests help or enters an unsupported command, the bot will guide user to user instruction.

This repository contains the necessary files to write a python application that can be run to execute the Twitter API, reading and writing information from the remote YahooFinance API. 

# User Instruction
**1. Get stock ticker value** (Benchmark )
 - When sending a tweet to bot @YahooTwitBot with a certain company's symbol (i.e. @YahooTwitBot AMZN), the twitter bot will reply with that company's stock ticker, company's full name, and time at which the price is set. 
 - A complete and searchable list of all companies supported by this bot and the symbol-name conversion can be found at this link (https://finance.yahoo.com/lookup).
 - The 

**2. Hello**
 - When sending a tweet to bot @YahooTwitBot that contains "hello", the twitter will respond "Hello back to you!" 

**3. Help! (Benchmark #2)**
 - When sending a tweet to bot @YahooTwitBot that contains "help!" or "info!", the twitter will respond with a link to this page which contains the user instruction.
 - Please always add "!" at the end for amusement reasons. 
