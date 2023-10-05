# GitHub and SSH

## 1. Prerequisites

Encryption line from the security challenges completed.

## 2. Introduction

When using git and GitHub, you need to authenticate yourself with GitHub (remember [this challenge](./../../introduction-challenges/03-getting-the-challenges/description.md) where we authenticated with a token or via a credentials manager).

Remember from the [encryption challenges](./../../security-challenges/01-encryption/03-symmetric-and-asymmetric-encryption/description.md) that using asymmetric keys is also a very strong method of proving your identity and thus authenticating.

In this challenge, we will configure **SSH** keys to authenticate with GitHub, eliminating the need for a token or a credentials manager. SSH is a tool that allows you to connect securely with servers, it uses asymmetric encryption for authentication behind the screens. 

You can find some background information on SSH [here](https://levelup.gitconnected.com/what-is-ssh-103f89e3e4b8). You'll see that it also uses symmetric encryption after the connection is made!

## 3. Challenge

Configure SSH for connecting to GitHub when using git command-line.

1. Follow these guides
    * Always read the section for your own Operating System!
    * [Creating a key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
    * [Adding a key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
    * [Testing your connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)
    * [Key passphrase](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases)
1. Create a textfile `solution.txt` in the directory of this file. Paste your **public key** in this textfile. Push your solution to your GitHub repository.