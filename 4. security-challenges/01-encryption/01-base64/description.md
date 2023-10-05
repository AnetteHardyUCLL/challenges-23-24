# Base 64

## 1. Prerequisites

None.

## 2. Introduction

Internally a computer represents everything in _bits_. A _bit_ is the basic unit in which to represent information in digital systems. A bit contains the value 1 or 0. By giving meaning to sequences of bits we can use bits to represent more complex information.

*Base64* is such a way to give meaning to certain sequences of bits, a couple of examples:
* 000000 represents the letter **A** in Base64
* 111101 represents the number **9** in Base64
* 101010 represents the letter **q** in Base64
* You can find the full set of characters that can be expressed in Base64 [Here](https://en.wikipedia.org/wiki/Base64#Design)

Suppose we find the following bit-sequence on a hard-drive: 000111 011110 011010 100101 100101 101000. If we know that these bits represent Base64 characters then it is possible to translate these bits to text. Feel free to try this with the character table mentioned above, you will see that this bit-sequence represents "Hello".

Base64 works with sequences of 6 bits. With sequences of 6 bits you can form at most 64 different combinations (2^6). On the Wikipedia page you can see that the letters A-Z, the letters a-z and the numbers 0-9 all have a bit sequence in Base64.

Such a scheme that allows us to translate characters to bits and vice versa is called an **encoding scheme**. Many different encoding schemes exist, each with their own sequence length. To give some examples, Base64, ASCII and UTF-8 are commonly used schemes.

### Why is it used?

The power of Base64 lies in the fact that (almost) only the characters A-Za-z0-9 can be represented. These characters are very plain and are seldomly assigned special meaning in a system.

More complex text often has characters that can only be represented by encoding schemes that work with 8 bits or more. Using such a scheme it is possible to also use special characters such as "%" or "{". Many systems give special meaning to such characters. The character *?* in URLs is associated with a search parameter for example. Here is an example URL from Google: https://www.google.com/search?q=google.

Base64 allows us to represent bits as text that does not contain any of these special characters. This is an interesting format to send text across the internet or to store it without problems because most programs and systems will not give special meaning to any of the characters used in Base64 text.

### Enconding & Decoding

Base64 is an interesting format, but how can we translate text from and to Base64?

* Translation to Base64 from readable text is called *Base64-encoding* 
* Translation from Base64 to readable text is called *Base64-decoding*

In short, we need to know the encoding scheme of the text that we want to translate. Using the character set of this scheme we replace each character with its bit sequence. Then we regroup the bits in groups of 6 (the length of a Base64 sequence) and replace these sequences with letters using the Base64 character set. Watch [this movie](https://www.youtube.com/watch?v=7gSSMy_M4HU) for a more detailed explanation and an example.

Let's give an example:

The text `Hello, this is an explanation about Base64 encoding and decoding` becomes `SGVsbG8sIHRoaXMgaXMgYW4gZXhwbGFuYXRpb24gYWJvdXQgQmFzZTY0IGVuY29kaW5nIGFuZCBkZWNvZGluZw==` in Base64.

This translation happens by converting the text to bits according to its encoding-scheme. The bits are then regrouped in groups of 6 and these groups are then transformed to characters according to the Base64 encoding-scheme.

You will often encounter Base64 when surfing on the internet or looking in a database. Now that you can translate Base64 you can always take a peek under the hood!

### Important Notice

Encoding text to Base64 is not a means of encyrption. By converting text to Base64 it is no longer human readable. But everyone can translate Base64 back to human readable text. **It is not a safe way to encrypt sensitive information.**

## 3. Challenge

Answer the following questions for yourself to make sure that you understand Base64:

1. What is an encoding scheme?
1. How does the Base64 encoding scheme work and why is it used?
1. How do you encode and decode text to Base64?

Create a textfile `solution.txt` in the directory of this file. Answer the following questions and push your solution to your GitHub repository:

1. Encode this string to Base64: `Base64 is very convenient to send text without special characters like "&é"'(§è!çà)-"`  (you do not have to translate this by hand like in the movie, search for a Base64 encoder on internet)
1. Decode this string from Base64: `VGhpcyBpcyBub3QgYSBzZWNyZXQsIG9ubHkgQmFzZTY0IGVuY29kZWQgdGV4dA==` (you do not have to translate this by hand like in the movie, search for a Base64 decoder on internet)

Your textfile should contain 2 lines.

## 4. General rules

In order to get a "SUCCESS" from the verify script, you will need to make sure that:

-   You have followed the instructions exactly as described in the text. Do not put extra text in files or create extra folders unless asked to do so.
-   Assume that the verify script is case-sensitive. Pay attention to the exact naming of files and folders.
-   Never make changes to the verify script (yes, we will verify all verify scripts afterwards). Changes to the verify script will result in a "FAIL" for the entire challenge.
-   You will only receive a "SUCCESS" if you complete all the steps successfully. If you only complete part of the challenge steps, you will receive a "FAIL" for the entire challenge.
