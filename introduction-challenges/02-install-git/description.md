# Install git

## 1. Prerequisites

Visual Studio Code is installed.

## 2. Introduction

In this challenge we will install and configure git on your pc.

## 3. Challenge

### 3.1. Install git

1. Navigate to <a href="https://git-scm.com/download" target="_blank">this page</a>
1. Click on the icon of your operating system to download the latest version
    * Are you using Windows? Download the 64-bit version of the Standalone Installer.
    * Are you using macOS and are you familiar with homebrew? Install via homebrew. If you do not know homebrew then download the binary installer.
1. Execute the installer
   * Let git install to the default location
   * In the `Select Components` screen, leave all checkmarks as they are
       * Are you using Windows? Make sure that `Open Git Bash Here` is selected.
   * Are you using Windows? In the `Choosing the default editor used by Git` screen on Windows, select `Select Visual Studio Code as Git's default editor` (install Visual Studio Code first!).

Time to make sure that the installation was successful:

1. Open a shell by...
     * On Windows, opening start and typing `git bash` followed by enter
     * On macOS, opening a terminal (enter `terminal` in Spotlight Search)
1. Enter:
   ```bash
   git --version
   ```
   This should display `git version 2.xy.z`. You do not want to see `command not found`.
1. Enter:
   ```bash
   git config --global user.email "jan.janssens@student.ucll.be"
   ```
   with your own email address between the quotes
1. Enter:
   ```bash
   git config --global user.name "Jan Janssens"
   ```
   with your own name between the quotes

### 3.2. Make a GitHub account

1. Navigate to <a href="https://github.com/" target="_blank">GitHub</a>
1. Click on `Sign up` in the top-right corner and go through the sign-up process
    * Use your UCLL email address
    * Choose a recognisable and decent username, for example `FirstnameLastnameUCLL`