Tutorial details    
Bash / ksh and other modern shell on Linux has three file descriptors:  
  stdin (0)
  stdout (1)
  stderr (2)

Syntax To redirect all output to file  

The syntax is as follows to redirect output (stdout) as follows:

 
command-name >  output.txt
command-name >  stdout.txt
 
Syntax To redirect all error to file

The syntax is as follows to redirect errors (stderr) as follows:

 
command-name 2> errors.txt
command-name 2> stderr.txt
 
Syntax to redirect both output (stdout) and errors (stderr) to different files

The syntax:

 
command1 > out.txt 2> err.txt
command2 -f -z -y > out.txt 2> err.txt
 
Syntax to redirect both output (stdout) and errors (stderr) to same file

The syntax is:

 
command1 > everything.txt 2>&1
command1 -arg > everything.txt 2>&1
 
Syntax to redirect errors (stderr) to null or zero devices

Data written to a null or zero special file is discarded by your system. This is useful to silence out errors (also know as 'error spam'):

 
command1 2> /dev/null
command1 2> /dev/zero
command2 -arg 2> /dev/null
command2 -arg 2> /dev/zero
 
Tip: Use tee command to redirect to both a file and the screen same time

The syntax is:

 
command1 |& tee log.txt
## or ##
command1 -arg |& tee log.txt
## or ##
command1 2>&1 | tee log.txt
 
Another usage:

#!/bin/bash
# My script to do blah ...
foo(){
 :
} 2>&1 | tee foo.log
 
OR

#!/bin/bash
# My script to do blah ...
{
   command1
   command2
} 2>&1 | tee script.log
