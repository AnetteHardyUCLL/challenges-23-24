# Git basics

## 1. Prerequisites

[git introduction](./../00-introduction/description.md) read and movies watched.

## 2. Introduction

You have already been given the general explanation of Git and its installation in the introduction challenge. In this challenge, you will be introduced to the basic operations of version control with Git: add, commit and push.

Initially, when you make changes to files in your working directory, Git considers them to be in "untracked" state. By using the `git add` command, you can selectively choose which files to include in the next commit (move them to the "staged" state).

The command `git commit` is used to save all the staged changes in the Git history. Every commit represents a snapshot of the changes made to the git repository. We can visualize the history of commits as a sequence of snapshots of the files in the repository. The following figure shows an example of a commit history:

<a href="./commit-history.png" target="_blank">
    <img src="./commit-history.png">
</a>

Every circle in the figure above represents a commit, every commit is a new version (snapshot) of the file "Solution.txt".

Finally, with `git push` you upload your local commits to a remote git repository. In this course, your remote repository is hosted on GitHub.

## 3. Challenge

To complete this challenge successfully, you should start a Git bash session in the folder where you have cloned the git-challenges repository. So not in the subdirectory "git-challenges/01-basics", but in the parent directory.

### 3.1. Add, commit and push a file

1.  Create a new empty file in the same folder as these instructions (git-challenges/01-basics) with the name "solution.txt".
1.  In Git bash (started in the root challenges folder), run the following command:


    ```console
    $ git status
    ```

1.  You will see that git is not yet tracking the file. The output should look like:


    ```text
    On branch master
    Your branch is up to date with 'origin/master'.

    Untracked files:
        (use "git add <file>..." to include in what will be committed)
            ...

    no changes added to commit (use "git add" and/or "git commit -a")
    ```

1.  In the "..." in the output above, you will see a line for each untracked file. Copy the line containing your solution file and paste it on the first line of solution.txt. Make sure you don't copy any leading or trailing spaces, just the text itself. Otherwise, the verification script will fail.
1.  Stage the file and commit it to your local repository:


    ```console
    $ git add git-challenges/01-basics/solution.txt
    $ git commit -m "Solution file"
    ```
    Via `git add` you tell git to track the file, `git commit` is going to effectively add the file to the local repository. With the "-m" option, you add a message to the commit.

1.  Now go to your github repository via a browser and navigate to the "git-challenges/01-basics" folder. As you can see, your solution.txt file is not there yet. This is because we need to "push" the changes you just made on your local repository to the remote version:


    ```console
    $ git push
    ```
    Refresh your browser and you will see that the file (with the commit message) is now present.

1.  You can run the status command again. Normally, the output should be as follows:


    ```text
    Your branch is up to date with 'origin/master'.

    nothing to commit, working tree clean
    ```

### 3.2. Add, commit and push a folder

Create a subfolder named 'challenge-1' in the '01-basics' folder. Create a new file "solution.txt" with the text `challenge 1 completed` on the first line. Make sure that this folder is pushed to your remote repository.

## 4. General rules

In order to get a "SUCCESS" from the verify script, you will need to make sure that:

-   You have followed the instructions exactly as described in the text. Do not put extra text in files or create extra folders unless asked to do so.
-   Assume that the verify script is case-sensitive. Pay attention to the exact naming of files and folders.
-   Never make changes to the verify script (yes, we will verify all verify scripts afterwards). Changes to the verify script will result in a "FAIL" for the entire challenge.
-   You will only receive a "SUCCESS" if you complete all the steps successfully. If you only complete part of the challenge steps, you will receive a "FAIL" for the entire challenge.
