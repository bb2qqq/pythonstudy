### GREP ###


* Find recursively on current directory those files which contains keyword _luck_ and list them out.

	  grep -Fnrl luck ./

>	-F = fixed string, -n = show line number(not used here), -r = recursively, -l = list files instead of show lines contains pattern


* Find all files contains name "Garcia" and list those files who has "Aureliano" in it.

		find  -name '*Garcia*' |xargs  grep -l 'Aureliano'

>	xargs is used to pass "standard input" or "pipe aruguments" to commands such like "grep" or "awk", or to break the long arguments of list into pieces so it is acceptable for some commands


* Grep for string "\t" + "apple" + "\t", -P means Perl-style regex, this can search for pattern contain tab

	  grep -P "\tapple\t"


* Search except files with some kind of string, here find pattern in file_names except those contains 'master' in file name

	  grep --exclude='*master*'  pattern  file_names


* Find file that does not contern the pattern

      grep -L "pattern" files



### FIND ###


* Search file modified between 12-05 08:00:00 to 12-06 00:00:00, with the file size greater than 10MB and samller than 20MB, containing word "quirk" in the file name

	  find -newermt '2014-12-05 8' ! -newermt '2014-12-06' -size +10M -size -20M -name "*quirk*"

* Find files with word "dwarf" in file name and list them out by last modify time

	  find -name "*dwarf*"-exec ls -lhrt {} \;


* Find file files with particular size print out their total disk usage

	  find -type f -size +5M -exec du {} \; | awk '{total += $1} END {print total}'


* Find file files with particular size and delete them

	  find -type f -size +5M -delete


* Find file cotains "*pinche*" only on the first level

	  find -name "*pinche*" -maxdepth 1


* Find something does not match the option, at here name not contains master, but could be other options

  	  find -! -name "*master*"


* Find directory with name containling config in all directories of system

	  find / -type d -name '*config*'


* Find files in target directories and mv them to a new directory

	  find *dir_pattern* -type f -name "*" -exec mv {} /path/to/new_dir \;
	  find . -type d -name "*dir_pattern*" -exec bash -c 'mv "{}"/* /path/to/new_dir' \;

>	bash -c treat the string afterwards as a command, here {} is the result of the find command



### SED ###



* find line of file contains keyword and del it

	  sed -i '/key_word/d' target_file


* print specified line in linux, here print the line 100

	  sed -n '100p'


### PROCESS ###

* find the process_id of a particular program

      pgrep cron



### FILE & DIRECTORIES ###

* Two ways of set sticky bit for a file

      chmod +t target_file
      chmod 1777 target_file

* Make anyone runs the file like they are they owner or member of the owner group.

      chmod u+s file
      chmod g+s file

* Read the file as input to cat

      cat < file

* List file with suffix to show their file-type

      ls -F

> `/` for directory, `*` for executable, `@` for symbolic link, `=` for socket, `%` for whiteout, `|` for FIFO
> whiteout files's purpose is to mask files which can't actually be deleted so they disappear from directories
> FIFO stands for `First In, First Out`, and has another name `named pipe`, it enables different processes to commnunicate.


* List files by revert Size order

      ls -lShr

* Synchronize file from remote to local

	  rsync -chavzP --stats user@remote.host:/path/to/copy /path/to/local/storage

>	-c for checksum, -v for verbose, -P for progress, -h for human readable format, -z for compress, -a for archive mode

* Synchronize file from local to remote

	  rsync -chavzP --stats /path/to/copy user@host.remoted.from:/path/to/local/storage


* Sync from all content from one directory from to another directory with different name

	  rsync -r /origin/*  /target/


* Unzip file with size greater than 4G

	  jar xf huge_file.zip

* copy file structures with particular file size restriction

	  rsync -a --min-size 1k --max-size 1m original_path /new_destination/

* request confirmation before delete a file, and -i option override any previous -f option, but and override -f after -i

	  rm -i pattern/file

* change a directory readable and writable for everyone

      sudo chmod -R ugo+rw /target/directory

>   ugo means user, group and others, -R means for the directory and its child-objects within

* view the contenting file list of a zip file

      unzip -l target.zip

* Print files without extract them ( will print out some unzip heads, too )

      unzip -c target.zip file1 fil2 file_pattern

* Change owner and owner group of a file

      chown target_user:target_group target_file

* Make a file writable

      chmod +w target_file

* Print column 1 and 5 separated by :

      cut -d: -f1,5 target_file

> cut will always print out multiple fields with delimiters, while awk can omit it, awk is a more sophisticated tool, and cut a leaner one.

* Print column 1 to 8 separated by !

      cut -d! -f1-8 target_file

* print character 2 and 5 of every line in the target\_file/output

      cut -c 2,5 target_file

* print character 3 to 9 of every line in target\_file/output

      cut -c 3-9 target_file

* print lines in a file in reverse order

      tail -r target_file

* execute executable file

      /path/to/executable_file

> Usually, we are execute in the directory where the file is in, thus we use relative path `./executable_file` at that situation.

* fastly delete all the content of a file

      >target_file

* Write lines with special characters to a file

      echo ' !#/usr/bin/awk -f ' >> target_file

> using `"` to wrap the sentence will make bash search its history, and `'` avoid this issue

* Rename multiple files

      # First, install mmv on your machine
      mmv '*.mp3' '#1.wma'


### USERS ###

* view groups briefly

      groups

* view all groups

      cut -d: -f1 /etc/group

> -d is short for -delimiter, here : is the specified delimiter rather than default \t, -f refers to the field separated by delimiter, here -f1 means print the first field separated by ':'

* view all users

      cut -d: -f1 /etc/passwd


### COMMAND FOR COMMAND ###

* These two commands are identical, they both read and execute the commands write in a file in the current shell envioronment

	  source file_name
	  . file_name	

* Execute the output of the previous command

      sed -n 'line_num p' | bash                              # excute specified line
      tail -n 5 your_file | bash                              # excute the last five line of a file

##### cron  #####
In cron, you have two important meta command to memorize:

      crontab -l        # List out all current cron task
      crontab -e        # Edit cron job for current user

You should add all those cron tasks by typing `crontab -e`

* Add a line to crontab without `crontab -e` _(edit mode to add task to cron)_

	  crontab -l > temp_cron_file
	  echo "* * * * * sh my_sync.sh" >> temp_cron_file
	  crontab temp_cron_file
	  rm temp_cron_file

* run the command every 2 hours, every 20 mintues a time in the running hour

      */20 */2 * * *  command

* run the command between hours 17-20, and in these hours, every minute a time between 5-8

      5-8 17-20 * * *  command

* run the command in minute 18 and 36 and 54 of hour 18 and hour 20

      18,36,54   18,20 * * * command

* run the command everytime you reboot

      @reboot command


### PROCESS AND PROGRAM ###

* Locate a program`s path in the system

	  which program_name
	  whereis program_name

* kill all screen sessions

	  killall -15 screen


### OTHERS ###

* execute a executable program

    exec program

* show login informations

      last

* show recently kernel infos

      sudo dmesg

* change default shell

      chsh -s /bin/your_shell

* Show most detailed info when connecting by ssh

      ssh -vvv usr@host

* Print server numbers in a column with your specified number range

	seq 163 180 | awk '{print "g"$1}'


* Prohibit using  >  to write to file, use >| to force write, this can avoid mis-operate between > and >>
set -o noclobber                                            # Disable  >
set +o noclobber                                            # Enable   >


* Passing all variables as a string to the command or script

	  some_command "$@"

>   if you have 'a.sh' which contains 'echo "$@"', then you can do `sh a.sh 'to print out any kind of sentences'`, you`ll got the sentence **to print out any kind of sentences** on your screen now.


* date without padding 0 area on month _( 2015101 instead of 20150101 )_

	  date +"%Y%-m%d"

* redirect stderror content to where stdout content goes

	command somefile > target_doc 2>&1

> 2 denotes standard error, while 1 denote standard out, & act as special descriptor


* generate ssh key

        ssh-keygen -t rsa

* Read input and assign it as value to the variable

        read MY_VAR

##### CALCULATION #####

* add

      expr 1 + 1

* multiply

      expr 6 \* 4

* divide

      expr 8 / 5            # will only keep the int part

* modulus

      expr 3 % 8


### ON MAC ###

* copy what pwd print to clipboard

	  pwd | pbcopy

* paste whatever in clipboard

 	  pbpaste
