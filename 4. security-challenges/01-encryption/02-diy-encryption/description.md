# DIY Encryption

## 1. Introduction

In the previous challenge we saw that Base64 is not a good means of encryption. But what is?

Encrypting information - making it unreadable for humans - is the domain of cryptography.

Many encryption techniques exist, let's start with a simple (and familiar?) one.

One of the oldest encryption systems is attributed to Julius Caesar and is called the [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

The idea is very simple, we encrypt a message by replacing each letter with a different letter that comes later in the alphabet:

```text
Plain	    A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
Encrypted	X	Y	Z	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W
```

The distance between the original and the encrypted letter is the _key_ necessary for decrypting the message. In the example above the key is 23.

Encrypting a message with the Caesar Cipher is as easy as replacing every letter in the message. `I am a secret` becomes `F xj x pbzobq` with key 23.

Decrypting a message is easy if you know the key. Unfortunately it is also not that difficult without knowing the key. Since there are only 26 keys, trying them all will surely give you the answer. Another help for decrypting is frequency analysis. Some letters occur more in text than others. By counting letters in encrypted text it is possible to guess which encrypted letter corresponds to an `e` for example, making it easier to guess the key used for encrypting.

## 2. Challenge

Create a textfile `solution.txt` in the directory of this file. Answer the following question and push your solution to your GitHub repository:

1. Encode this string using a Caesar Cipher with key 5: `Caesar Cipher is a very easy encryption technique`. Upper case characters are encrypted to upper case characters and lower case characters to lower case characters.

Your textfile should contain 1 line.

## 3. General rules

In order to get a "SUCCESS" from the verify script, you will need to make sure that:

-   You have followed the instructions exactly as described in the text. Do not put extra text in files or create extra folders unless asked to do so.
-   Assume that the verify script is case-sensitive. Pay attention to the exact naming of files and folders.
-   Never make changes to the verify script (yes, we will verify all verify scripts afterwards). Changes to the verify script will result in a "FAIL" for the entire challenge.
-   You will only receive a "SUCCESS" if you complete all the steps successfully. If you only complete part of the challenge steps, you will receive a "FAIL" for the entire challenge.