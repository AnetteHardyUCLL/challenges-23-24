# Symmetric and Asymmetric Encryption

## 1. Introduction

Caesar Cipher is a fun way to encrypt a message between friends but it is hardly secure enough for real world systems.

Take a look at the [following movie](https://www.youtube.com/watch?v=jhXCTbFnK8o) to get a good overview on multiple encryption techniques.

One of the main takeaways is that there are two classes of encryption techniques used in software nowadays:
* Symmetric encryption (such as DES), meaning that the same key is used for encrypting and decrypting
* Asymmetric encryption (such as RSA), which relies on two different keys and fancy mathematics for encrypting and decrypting

Asymmetric encryption relies on key-pairs consisting of a public and a private key. One key is used for decrypting and one key is used for encrypting. Note that this means that you can use RSA for two very different use-cases:
* Encrypt with the public key and decrypt with the private key: this is a very secure way to send someone an encrypted message. Suppose that Alice wants to receive a message from Bob. Alice creates a key-pair and gives the public key to Bob. He encrypts the message with the public key. Since only Alice has the private key, she is the only one that can decrypt the message. It is not bad if someone else gets his hands on the public key, that only means that that person can create encrypted messages that Alice could decipher.
* Encrypt with the private key and decrypt with the public key: there is no security since everyone can get hold of the public key. However, since only one person holds the private key that corresponds to that public key this is a very strong technique to confirm your identity. We will use this idea in the [challenge on SSH-keys](./../../../git-challenges/04-ssh/description.md).

## 2. Challenge

You can use [this site](https://www.devglan.com/online-tools/rsa-encryption-decryption) to play around with RSA encryption and decryption.

As an example, I have created an RSA keypair consisting of a private and a public key. I have encrypted a message with my private key.

The encrypted message is as follows:

```
lui6+keJcMbAdzM2gYF27xEFI1dNhOEc0DQfg0W3eLbqlYIEym2oU7ht+0tf6eN6SmQ7d19QJqnms+eX9cmsHN/vLH52Jc1MXBrPsvVNkuTMRlw257ax8zIlu9QzL74QT77oSjJ8tzvkNSePUn3RfMr3fkV3Ef5Mdee6lLwgHC0=
```

(As an aside, note how the encrypted message is also encoded in [Base 64](../01-base64/description.md).)

The public key is as follows:

```
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCwmIlkO7KiZlESLc2g/Q6Oa8928DK/sizHG3ehUb3o1B99yCCPAKl/SWtxWhxtyd1kn3PUaqayiq6uFOHUWlhuxe4UoX4S7gt10bpulPEEl7suyjV0ajw2+r7sTbdtpfxaw2Lgtfpg0Dlfh42TiHEsAQ7N5k7wdOun0iVsVkrrHQIDAQAB
```

Using the site (use Cipher Type RSA in the dropdown), what was the encrypted message?

Create a textfile `solution.txt` in the directory of this file. Your textfile should contain 1 line. Push your solution to your GitHub repository.

## 3. General rules

In order to get a "SUCCESS" from the verify script, you will need to make sure that:

-   You have followed the instructions exactly as described in the text. Do not put extra text in files or create extra folders unless asked to do so.
-   Assume that the verify script is case-sensitive. Pay attention to the exact naming of files and folders.
-   Never make changes to the verify script (yes, we will verify all verify scripts afterwards). Changes to the verify script will result in a "FAIL" for the entire challenge.
-   You will only receive a "SUCCESS" if you complete all the steps successfully. If you only complete part of the challenge steps, you will receive a "FAIL" for the entire challenge.