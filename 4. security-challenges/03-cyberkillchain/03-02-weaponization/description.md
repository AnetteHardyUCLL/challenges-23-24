# Weaponization
Read about the weaponization phase of the cyber kill chain. What kind of weapons could an attacker create? The most common weapon is some kind of malware. A list of different malware types can be found at: https://www.malwarefox.com/malware-types/

Now, take a look at the attached document "WinPrices.docm" in the folder "attachments" and answer the following questions.

Did you enable the macro in Word on your computer? This could have been dangerous! Always use a sandbox if you are unsure! Any.run (https://app.any.run/) is a free online sandbox you can use to run on any suspicious file. Also, virustotal (https://www.virustotal.com) is a great resource as well. Any.Run will execute the file and you can watch the activity. Virustotal will mainly check the checksum of the file and match with signature databases from antivirus products.

Check both tools for this file.

## Challenge

Create a file called solution.txt in this directory. It will eventually have five lines, as detailed below:

The flag is composed of several lines, one line per answer:
- Line 1: MD5 hash of the file (all lowercase letters)
- Line 2: What MITRE Technique is being used (we need the identifier, starting with T)? 
- Line 3: What was the main goal of using this technique?
- Line 4: How do hackers mostly do this? Hint: Look at https://www.picussecurity.com/resource/blog/picus-10-critical-mitre-attck-techniques-t1064-scripting (the word we're looking for is mentioned several times, write the noun form of the word - ending in "on")
- Line 5: What's the hidden flag in this document? Hint: the flag starts with "flag{"