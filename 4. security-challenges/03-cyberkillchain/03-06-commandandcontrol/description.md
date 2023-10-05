# Command and Control

Command and Control (C2) infrastructure is a critical component of various cyberattacks, often associated with malicious activities such as creating botnets, executing remote commands on compromised systems, and distributing malicious payloads. Let's break down the key concepts in this context:

    - Zombies: In the context of C2, zombies are computers or devices that have been compromised by a malicious actor. These compromised systems are under the control of the attacker and can be used to carry out various tasks without the knowledge or consent of the device owner.

    - Botnet: A botnet is a network of compromised devices (zombies) that are controlled by a central entity, usually the attacker. Botnets are used for various malicious purposes, such as launching distributed denial-of-service (DDoS) attacks, distributing spam, or carrying out coordinated cyberattacks.

    - Shell: A shell refers to a command-line interface that allows a user to interact with a computer's operating system. In the context of C2, gaining a shell on a compromised system provides the attacker with direct access to execute commands on that system.

    - Agent: An agent is a piece of malicious software (malware) that is installed on a compromised system and acts as a conduit for the attacker. The agent communicates with the C2 server, receiving commands and sending back information about the compromised system.

    - Payload: A payload is the malicious code or action that an attacker delivers to a compromised system. This could include executing a malicious program, stealing sensitive data, or initiating further actions, all of which are dictated by the attacker through the C2 server.

    - Beacon: A beacon is a signal or message sent by a compromised system to the C2 server to indicate that the system is still active and ready to receive commands. Beacons are often designed to be stealthy, making detection more difficult.

    - C2 Server: The C2 server is the central control point for the attacker. It receives communication from the compromised agents (zombies), issues commands to these agents, and gathers information from the compromised systems. The C2 server plays a pivotal role in managing the botnet and orchestrating the attack.

C2 Frameworks (Products) and Capabilities:

Several C2 frameworks (also known as C2 tools or platforms) are used by both malicious actors and security professionals for testing and defense. Here are a few notable ones:

    - Metasploit: Metasploit is a widely used penetration testing framework that includes a robust C2 infrastructure. It allows security professionals to simulate real-world attacks, assess vulnerabilities, and test defenses.

    - Cobalt Strike: Cobalt Strike is a commercial penetration testing tool that includes advanced C2 capabilities. It's often used by security teams for red teaming exercises to test an organization's security posture.

    - Empire: Empire is an open-source post-exploitation framework that provides a versatile C2 platform. It's designed for offensive security operations, enabling operators to interact with compromised systems.

    - PowerShell Empire: A post-exploitation framework built on top of PowerShell, enabling attackers to control compromised systems through PowerShell scripts. It's particularly effective in environments where PowerShell is commonly used.

These C2 frameworks provide various capabilities, including the ability to execute commands on compromised systems, pivot through networks, maintain persistence, exfiltrate data, and simulate different types of attacks. It's important to note that while these tools can be used by security professionals for legitimate purposes, they can also be misused by malicious actors, highlighting the importance of cybersecurity awareness and defense. 

The knowledge and understanding of C2 infrastructure are essential for both offensive (ethical hacking, penetration testing) and defensive (cybersecurity) purposes.

On this page (https://thedfirreport.com/2023/02/06/collect-exfiltrate-sleep-repeat/), you can find a detailed report of a cyber security incident, which has been occurring since August 2022. Read the report and try to understand the concepts we have seen. 

## Challenge

Create a solution.txt file in this directory. It will eventually consist of 12 lines.

Answer the following questions:

- Line 1: What APT was behind the incident? We need the MITRE ID of this APT Group: 
- Line 2: What was most likely the delivery method of the malicous Word file? We need the Mitre Technique ID:  
- Line 3: When parsing the Macro, what was the first suspicious behavior dectected? We need the exact wording as mentioned in the output: 
- Line 4: Sysmon is a tool available in the Microsoft ... (enter the useful toolset we already mentioned in this challenge that contains Sysmon as well): 
- Line 5: What sysmon event ID notified us about the creation of Script.ps1 file? 
- Line 6: What's the name of the first scheduled task created to obtain persistence? (one word made up of two words, mentioned in the report)
- Line 7: what's the name of the second scheduled task created? (one word made up of several words, mentioned in the report)
- Line 8: For discovering the current state of the victim's antivirus product, what command is executed (hint: powershell command)? 
- (do not include this in your solution.txt file) Run this command on your own laptop/pc to see if your antivirus is working correctly and up-to-date.
- Line 9: How did the attackers grab the data (we need the generic name for this type of maware): 
- Line 10: What's the full Mitre Technique ID for this activity? 
- Line 11: Data was sent (exfiltrated) to the C2 server at this IP address: 
- Line 12: What's the full Mitre Technique ID for this activity?