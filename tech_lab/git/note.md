!!! in this file, () stands for optional choice, <> stands for user_typed content.

To fetch from github using ssh, you use:
    git rm $(git ls-files --deleted)

To change http remote to ssh, you use:
    git remote set-url origin git@github.com:<Username>/<Project>.git



# Extra labor I've been done:
If you want to see the changes introduced between the current version of a file and the file a month ago, Git can look up the file a month ago and do a local difference calculation, instead of having to either ask a remote server to do it or pull an older version of the file from the remote server to do it locally.



# The benefit of git:
    Git Has Integrity
Everything in Git is check-summed before it is stored and is then referred to by that checksum. This means it’s impossible to change the contents of any file or directory without Git knowing about it. This functionality is built into Git at the lowest levels and is integral to its philosophy. You can’t lose information in transit or get file corruption without Git being able to detect it.



# Git store mechanism:
    The mechanism that Git uses for this checksumming is called a SHA-1 hash. This is a 40-character string composed of hexadecimal characters (0–9 and a–f) and calculated based on the contents of a file or directory structure in Git. A SHA-1 hash looks something like this:

24b9da6552252987aa493b52f8696cd6d3b00373
You will see these hash values all over the place in Git because it uses them so much. In fact, Git stores everything in its database not by file name but by the hash value of its contents.



# Something about git-config:
    Git comes with a tool called git config that lets you get and set configuration variables that control all aspects of how Git looks and operates. These variables can be stored in three different places:

/etc/gitconfig file: Contains values for every user on the system and all their repositories. If you pass the option --system to git config, it reads and writes from this file specifically.

~/.gitconfig or ~/.config/git/config file: Specific to your user. You can make Git read and write to this file specifically by passing the --global option.

config file in the Git directory (that is, .git/config) of whatever repository you’re currently using: Specific to that single repository.

Each level overrides values in the previous level, so values in .git/config trump those in /etc/gitconfig



# To view all possible gitconfigs from all git files:
    Git comes with a tool called git config that lets you get and set configuration variables that control all aspects of how Git looks and operates. These variables can be stored in three different places:

/etc/gitconfig file: Contains values for every user on the system and all their repositories. If you pass the option --system to git config, it reads and writes from this file specifically.

~/.gitconfig or ~/.config/git/config file: Specific to your user. You can make Git read and write to this file specifically by passing the --global option.

config file in the Git directory (that is, .git/config) of whatever repository you’re currently using: Specific to that single repository.

Each level overrides values in the previous level, so values in .git/config trump those in /etc/gitconfig

You can also check what Git thinks a specific key’s value is by typing git config <key>:

$ git config user.name
Zeng Juchen



# Searching for advancing git help:
Getting Help
If you ever need help while using Git, there are three ways to get the manual page (manpage) help for any of the Git commands:

$ git help <verb>
$ git <verb> --help
$ man git-<verb>
For example, you can get the manpage help for the config command by running

$ git help config
These commands are nice because you can access them anywhere, even offline. If the manpages and this book aren’t enough and you need in-person help, you can try the #git or #github channel on the Freenode IRC server (irc.freenode.net). These channels are regularly filled with hundreds of people who are all very knowledgeable about Git and are often willing to help.



# Creat a git directory using clone:
    command: git clone <remote_branch> (<target_directory>)
    That creates a directory named “libgit2”, initializes a .git directory inside it, pulls down all the data for that repository, and checks out a working copy of the latest version. If you go into the new libgit2 directory, you’ll see the project files in there, ready to be worked on or used. If you want to clone the repository into a directory named something other than “libgit2”, you can specify that as the next command-line option:

$ git clone https://github.com/libgit2/libgit2 mylibgit



# View file change:
    command: git diff
    To see what you’ve changed but not yet staged, type `git diff` with no other arguments.
That command compares what is in your working directory with what is in your staging area. The result tells you the changes you’ve made that you haven’t yet staged.

    command: git diff --staged
If you want to see what you’ve staged that will go into your next commit, you can use git diff --staged. This command compares your staged changes to your last commit:



# Using difftool to view differences:
    command: git difftool (--staged)
    If you run git difftool instead of git diff, you can view any of these diffs in software like Araxis, emerge, vimdiff and more. Run git difftool --tool-help to see what is available on your system.



# Adding and commit at the same time:
    command: git commit -a -m 'add and commit at the same time';
Adding the -a option to the git commit command makes Git automatically stage every file that is already tracked before doing the commit, letting you skip the git add part:



# Remove staged file from git track:
    command: git rm --cached (or --staged) target_file



# Remove massive file from git:
    command git rm (target_dir/)\*key_word
Note the backslash (\) in front of the *. This is necessary because Git does its own filename expansion in addition to your shell’s filename expansion. This command removes all files that have the .log extension in the log/ directory. Or, you can do something like this:



# Move file in git:
    command git mv file_from file_to
This is like a combination of three commands:
mv file_from file_to
git rm file_from
git add file_to



# View git commit history:
    command: git log
    command: git log -p                * To view detailed change
    command: git log -p -2             * To view detailed change of last `2` commit
    command: git log --stat            * To view how many lines each file has changed
    command: git log --pretty=oneline  * To view the Head and commit message only, in 1 line
    command: git log --pretty=short    * view commit message, Head, author, in 3 line, (full, fuller) instead of short for more info

    command: git log --pretty=format:'%h  %ar %<(13) %an "%s"' --graph * A nice magic one liner
    * --graph option shows a primitive git graphical flow

    * format option under pretty flag allows you to print out customized log information:
    sample command: git log --pretty=format:"%h - %an, %ar: %s"

        Useful options for git log --pretty=format
        Option  Description of Output

        %H
        Commit hash

        %h
        Abbreviated commit hash

        %T
        Tree hash

        %t
        Abbreviated tree hash

        %P
        Parent hashes

        %p
        Abbreviated parent hashes

        %an
        Author name

        %ae
        Author e-mail

        %ad
        Author date (format respects the –date= option)

        %ar
        Author date, relative

        %cn
        Committer name

        %ce
        Committer email

        %cd
        Committer date

        %cr
        Committer date, relative

        %s
        Subject

    * Tips: when viewing logs, under Unix, git will use vim to do the operation, so you can use  10j, 30k to move up and down.
    * Tips: Author is the one who wrote the code, commiter is the one who commit this code on a branch,
            They can be the same guy or not, in a huge project, someone will play a professioner reviewer and commiter role.
