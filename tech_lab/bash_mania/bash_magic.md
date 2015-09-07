### Find tomorrow date
    tomorrow=$(date +"%Y-%m-%d" --date='-1 days ago')
    tomorrow=$(date +"%Y-%m-%d" --date='next day')


## SSH

### SSH PROXY
    ssh -D agent_port usr@remote_host
> After using this command, go to your network setting, enable socks proxy, and filled you `local ip(usually 127.0.0.1)` and `agent_port` in. Apply it.
> Be sure that on your remote host, in `/etc/ssh/sshd_config`, the `AllowTcpForwarding` option was set to `yes`.
> Then you can use your browser to surf online freely now!

### SSH Forwarding
SSH Forwarding enable an agent machine to visit a target machine where your public key resides in its `authorized_hosts`.
    ssh -A -i /path/to/my_ssh_private_key usr@remote_host_ip:port
> -A enables agent mode, -i specified identity files


### Exam Running Time of a program
    time your_command


### Execute command after ssh connection
    ssh user@target_ip  ls; pwd; echo "I'm king of the world"


### View checksum value of a file (check integrity)
    md5sum target_file


### List files with prepending numerical orders
    ls -v


### Use default value if specified value doesn't exists
    command ${1:-"default_value"}
    command ${1:-$2$3}


## OUTPUT REDIRECT

### Get input from a file
    command < input_source
> For example: `sort < b > a` will sort the content of b and redirect the output to a.

### Redirect error to file
    command 2> err_log

### Redirect output to one file, and error to another
    command 2> err_log 1> output

### redirect stderror and stdout together to a file

    command > err_and_output 2>&1  # Method 1
    command &> err_and_output         # Method 2, for recent version bash

### Print output, errors, and redirect them to file at the same time
    command |& tee err_and_output
    command 2>&1 | tee err_and_output

> 2 denotes standard error, while 1 denote standard out, & act as special descriptor

### Get unique(nearly) identifier for Linux machine
    hostid

### unzip f.tar.gz type file
    tar -zxvf f.tar.gz
> z: unzip, x: extract, v: verbose, f: forcefully done


### Forbid prompt message when openning new terminal window 
    touch ~/.hushlogin


### Source file without output on screen
    source ~/.bashrc > /dev/null 2>&1


### Change System default shell
    sudo chsh -s /path/to/shell username


## DATE & TIME

### fastly get current time in readable format
    time.strftime('%F %T')

### synchronize local date with remote server
    ntpdate cn.pool.ntp.org




### SYSTEM ###

Find release version of your Linux system:
    cat /etc/*release

Send email to address:

    echo 'I love you' | mail -s 'LOVE' address@domain.com

View server uptime from last power on

    uptime

View exit status of the most recent command

    echo $?

View network status

    iftop


### SED ###


* find line of file contains keyword and del it

	  sed -i '/key_word/d' target_file


* print specific line in linux, here print the line 100

	  sed -n '100p'


### PROCESS ###

* find the process_id of a particular program

      pgrep cron



### FILE & DIRECTORIES ###

* compress files one by one into new file and delte, and delete original file once it have been compressed.

    tar -zcvf my_log.tar.gz *.log --remove-files

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

> To copy recursively, add -r flag  
>	-c for checksum, -v for verbose, -P for progress, -h for human readable format, -z for compress, -a for archive mode  
>  Be careful!  -c option can check file diffs more exact, but the cost is this could slow the transfer significantly when transferring huge files.  

* Synchronize file from local to remote

	  rsync -chavzP --stats /path/to/copy user@host.remoted.from:/path/to/local/storage


* Sync from all content from one directory from to another directory with different name

	  rsync -r /origin/*  /target/


* Unzip file with size greater than 4G

	  jar xf huge_file.zip

* copy file structures with particular file size restriction

	  rsync -a --min-size 1 --max-size 1m original_path /new_destination/

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


### TEXT ###

* join files together horizontally

      paste target_files

* read a large file

      less large_file

> less won't need to read the whole file before starting,  so with large files it's much faster than vi.  
> but you can navigate in it with all kinds of vi commands!  
> By pressing `F`, you can view newly appended content to the file. It's similar to `tail -f`  
> But be aware, when pressing `F`, less won't doing quite right with `cat a > b`, beacause it's not append,  
> You'll need press `R` to refresh the screen to get new content of the file  
> Pressing `<CTRL> + G`, you can get detailed info about current page, include `file name`, `line-number`, and `percentage statistics`.  
> By pressing `v`, you'll use configured editor to edit the current file  
> Press `h` to get help


* print lines that are common to file1 and file2

      comm -12 <(sort file1) <(sort file2)

> `comm` command should deal with sorted file or output  
>  it will print out 3 columns, the first for lines are unique to file1, the second for lines are unique to file2, the 3rd for lines appears in both.  
> -1 will suppress the print of 1st column, -2 suppress the 2nd column, -3 suppress the 3rd column

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

* enable interpretation of backslash escapes in echo

      echo -e '\nback\tslash\n'

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



* generate ssh key

        ssh-keygen -t rsa

* Read input and assign it as value to the variable

        read MY_VAR

* Run two scripts at the same time, until both of them complete doing next step

        (sh script1.sh & sh script2.sh ) & wait
         # Next step

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

* copy large file on iterm

      `cat file` and then copy it in command line

* invoke javascript shell

      node

> start nodejs
