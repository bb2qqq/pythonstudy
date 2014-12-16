P1   ****************************************************************************************



working area, stage area, and git area are 3 separated file systems.

For example:
You got a file1, its content is "Hello world"
You used "git add file1" to stage it, no you have git status "change for commit: modified: file1 "

Now you add a line "Bye, world" in file1.
Doing "git status", you will got:
"change for commit: modified: file1 "
"change not prepared for commit: modified: file1 "

So there are two files in two different area now.

But of course, when you use "vim file1" to edit, if there are modified content not added, you will see
them first, the working area file is on the top layer.
You can use "git checkout file1" to remove all the current changes in working area. The modified content in the stage area will not be affected by this command.


Assuming you have a file1 in a branch named 'branch1', its content is "Jambalaya",
now you checkout from master to this branch1 with the staged file1, you will meet an Aborting error.
Because this staged file1 will have conflict with the commited file1 in branch1.
So what if I make another branch from master at this moment?
After 'git branch branch2' You will find 'Hello world' in it. Then you check back to master, reset file1 and checkout it later. You will find an empty file1 in master, then you back to branch1, you will find file1 is empty there, too. Which means "When you made a new branch, what do you do is to copy all the commited file from the source branch. Yes, staged files and modified files are shared between branches, as if there is not a commit file with same name in the targeted checkout branch."





P2   ****************************************************************************************
