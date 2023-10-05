# Reconnaissance

Read/Watch about the reconnaissance phase of the cyber kill chain (in the resources mentioned in the previous challenge). Can you tell the difference between active and passive reconnaissance?

#### Challenge
Create a file `solution.txt` in this directory. Your solution will eventually consist of 7 lines, filled in with answers from the following sections.

#### 1 Active versus Passive Reconnaissance

Below are three actions performed by a hacker, what type of reconnaissance is the hacker doing (answer only with “A” for active and “P” for Passive)? 
- The hacker visits the website of the UCLL school, hoping to get some of their employee names. What kind of reconnaissance activity is this? 
- The hacker pings the IP address of the UCLL school webserver to check if ICMP traffic is blocked. What kind of reconnaissance activity is this? 
- The hacker meets the IT administrator of the UCLL and tries to use social engineering to get more information about their systems and network infrastructure. What kind of reconnaissance activity is this? 

The flag corresponds to the three letters (A or P) that correspond to the answers. For example, if you would answer P three times: __PPP__.

Enter these three letters as the first line of your solution file.

#### 2 Google Dorking

Info: https://www.freecodecamp.org/news/google-dorking-for-pentesters-a-practical-tutorial/

Google Dork the internet to find a PDF file from the UCLL college in which there is a list of student numbers listed in classes for a certain bachelor programme ("indeling") in the year 2019. All you know is that it's for the year 2019. In case you would find two similar files, take the one where some student numbers are highlighted.

The flag corresponds to the highlighted number (xxxxxxx) in the third column. Example: __0864795__

Enter these numbers as the second line of your solution file.

#### 3 Whois

Using the whois command is often the first thing to check for a website. It is available in any Linux environment or WSL in your Windows environment (or also in the Microsoft SysInternals Suite, highly underestimated tools which are very useful for security purposes, documentation: https://learn.microsoft.com/en-us/sysinternals/). Using whois, answer the following questions.

The flag is composed of several lines, one line per answer:
- Line 1: The name of the registrar for the UCLL website (in capitals)
- Line 2: The name (EN abbreviation, in capitals) of the law preventing to show too much information when performing the whois command
- Line 3: The full name of the registrar for the Microsoft website (as mentioned in whois)
- Line 4: The IANA ID number of the registrar for the Microsoft website 
- Line 5: The full e-mail address of the Tech Email (all lowercases)

Fill these answers in on lines 3-7 in your solution file.