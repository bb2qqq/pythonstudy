# chmod

`ls -lhrt`

    drwxr-xr-x  3 zen1  staff   102B Jan 21 21:30 scripts
    -rw-r--r--@ 1 zen1  staff   5.7K Feb  3 17:39 bash_magic.md
    -rw-r--r--  1 zen1  staff     0B Feb  3 20:40 self_tutorial.md

The first column indicates the permission for the file.

The second column shows the hard link number of the file or directory

The third column is the owner

The fourth column is the group where the owner belongs

The fifth column is the size of the file

The sixth column is the last modified time of the file

The seventh column is the name of the file


The first letter of file permission column, d or -, indicate the file is a directory or a normal file.

The next three letters behind the first letter, indicate the permisson for that file as owner of file.  
r for read  
w for write(or delete)  
x for execute  

> if you got x for a directory, that means you can search that directory.

There are three 'rwx' block in total.  
The second 'rwx' block shows the permission for the members of the group which the file owner is in.
The last 'rwx' block shows the permission of any others who are not the owner nor in the group of which the owner is in, in short, other users.

*Root user can do anything to any file*

_command of chmod_

         chmod who=permissions filename/directory
         chmod who+permissions filename/directory
         chmod who-permissions filename/directory
         chmod who=target_user filename/directory   \# this will make 'who' has the same permissions as target_user/group
         chmod who-target_user filename/directory   \# this will delete the those permission of target_user from 'who'
         chmod who+target_user filename/directory   \# this will add the permissions of target_user to 'who'

> You use + to add permission for some user, - to delete permission for some user, and = to made the permission of user exactly as what you type.

If you got two files, "raw_data" and "analy_data.sh", in the first one stores all your cofidential datas. And the second script will give out some result based on some low-security-level data of "raw_data" file. Which can be run by many colleagues.  
But the problem is, if someone directly used the 'analy_data.sh' which he has permission to exec. He will not be allowed to open the 'raw_data', so he can not get the result.  
To solve this, you can use the command `chmod u+s analy_data.sh`, this will made anyone who execute the script do have the same capacity as the file owner in the scope of the script.  
You can also use `chmod g+s file` to make the user who execute the file has the same permission as the group of the file.

You can also convert these permissions to binary numbers and then further convert them to arabic numbers

--- for  000  = 0
--x for  001  = 1
-w- for  010  = 2
-wr for  011  = 3
r-- for  100  = 4
r-x for  101  = 5
rw- for  110  = 6
rwx for  111  = 7
