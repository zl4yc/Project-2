# DS 3002 Project-2
**Author: Shining Wang (sw9uf) and Lily Lin (zl4yc)**

**Project: YahooFinance API Twitter Bot**  

In this project, we created a twitter bot using python that is meant to be deployed to an Amazon EC2 intance using docker to run the application automatic and continuous backstage. The twitter bot (@YahooTwitBot) can be used to find useful information regarding to companies' stock ticker value when using the right command. @YahooTwitBot will respond to mentions from Twitter users requesting stock ticker value using a certain company's symbol. The twitter bot can also say hello. If user requests help or enters an unsupported command, the bot will guide user to user instruction.

**Additional Notes for Professor**

This repository contains the necessary files to write a python application that can be run to execute the Twitter API, reading and writing information from the remote YahooFinance API. The main bot code are in the bots file, everything else are meant to be necessary files that can help deploy the bot to the Amazon EC2 instance. The screenshots folder contain images that show effort and partial work in the depolyment method. Only one step was left in such process, but was unable to be successfully deployed because of the laptop chip version.  

# User Instruction
**1. Get stock ticker value** (Benchmark #1 & #3)
 - When sending a tweet to bot @YahooTwitBot with a certain company's symbol (i.e. @YahooTwitBot AMZN), the twitter bot will reply with that company's stock ticker, company's full name, and time at which the price is set. 
 - A complete and searchable list of all companies supported by this bot and the symbol-name conversion can be found at this link (https://finance.yahoo.com/lookup).
 - @YahooTwitBot will also guide users to this page if user uses a unrecognized or mistaken company symbol.  

**2. Hello**
 - When sending a tweet to bot @YahooTwitBot that contains "hello!", the twitter will respond "Hello back to you!" 

**3. Help!** (Benchmark #2)
 - When sending a tweet to bot @YahooTwitBot that contains "help!" or "info!", the twitter will respond with a link to this page which contains the user instruction.

**4. Miscellaneous**
 - Please always add "!" at the end of a "hello", "help", or "info" request for amusement reasons. 
 - The bot doesn't distinguish between capital and lowercase letters. Everything works! 
