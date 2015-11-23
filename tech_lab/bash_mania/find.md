我们经常会需要在文件夹里寻找符合某些条件的文件。  
如修改于某一个时间段，具有特定名称，特定大小，等。  
下列命令提供了一些寻找这些文件的方法。

## Find file among special time range
      find -newermt '2015-01-23'    #  find files newer than the 2015-01-23, include 2015-01-23
      find ! -newermt '2015-01-23'  #  Here the "!" means "NOT", so, this will find files earlier than 2015-01-23, and not include '2015-01-23', since its the reverse supplement of the previous command.
      find  -newermt '2015-01-23' ! -newermt '2015-01-24'   # This command will find the file modified just in '2015-01-23'

> if a file is created on "2015-03-01 00:00:00", find -newermt '2015-03-01' won't get it(On Unix find, Linux find untested).


## Find files using both time, size, name conditions
Search file modified between 12-05 08:00:00 to 12-06 00:00:00, with the file size greater than 10MB and samller than 20MB, containing word "quirk" in the file name

      find -newermt '2014-12-05 8' ! -newermt '2014-12-06' -size +10M -size -20M -name "*quirk*"

## Find files and list them by modified time order
Find files with word "dwarf" in file name and list them out by last modify time

      find -name "*dwarf*" -exec stat -c "%y %n" {} \; | sort


## Find file files with particular size print out their total disk usage

      find -type f -size +5M -exec du {} \; | awk '{total += $1} END {print total}'


## Find file files with particular size and delete them

      find -type f -size +5M -delete
      find -type f -size 0k -delete     # delete all empty files


## Find files in a specified directory depth
Find file cotains "*pinche*" only on the first level

      find -name "*pinche*" -maxdepth 1


## Find things doesn't satisfied condition
Find something does not match the option, at here files whose name doesnn't contain master, but you can use `!` on other options, such as time, size.

      find -! -name "*master*"


## Find specified file type
Find directory with name containling config in all directories of system

      find / -type d -name '*config*'


## Find files in target directories and mv them to a new directory

      find "dir_pattern" -type f -name "file_pattern" -exec mv {} /path/to/new_dir \;
      find . -type d -name "dir_pattern" -exec bash -c 'mv "{}" /path/to/new_dir' \;

>   bash -c treat the string afterwards as a command, here {} is the result of the find command

