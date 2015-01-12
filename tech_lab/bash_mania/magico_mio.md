##################          GREP            #################################



	# -F = fixed string, -n = show line number(not used here), -r = recursively, -l = list files instead of show lines contains pattern
grep -Fnrl lush ./      * Find recursively on current directory those files which contains keyword lush and list them out.

        # Find all files contains name "Garcia" and list those files who has "Aureliano" in it.
find  -name '*Garcia*' |xargs  grep -l 'Aureliano'
      	* xargs is used to pass "standard input" or "pipe aruguments" to commands such like "grep" or "awk", or to break the long arguments of list into pieces so it is acceptable for some commands

        # -P means Perl-style regex, this can search for pattern contain tab
grep -P "\tapple\t"




#################          FIND             #################################



	# Search file between 12-05 08:00:00 to 12-06 00:00:00, with the file size greater than 10MB and samller than 20MB, containing word "quirk" in the file name
find -newermt '2014-12-05 8' ! -newermt '2014-12-06' -size +10M -size -20M -name "*quirk*"


	# Find files with word "dwarf" in file name and list them out by last modify time
find -name "*dwarf*"-exec ls -lhrt {} \;


	# Find file files with particular size print out their total disk usage
find -type f -size +5M -exec du {} \; | awk '{total += $1} END {print total}'


	# Find file files with particular size and delete them
find -type f -size +5M -delete


	# Find file cotains "*pinche*" only on the first level
find -name "*pinche*" -maxdepth 1

	# Find something does not match the option, at here name not contains master, but could be other options
find -! -name "*master*"


	# Find directory with name containling config in all directories of system
find / -type d -name '*config*'



#####################           SED         #############################



	# find line of file contains keyword and del it
sed -i '/key_word/d' target_file

        # print specified line in linux, here print the line 100
sed -n '100p'


###################             OTHERS              ######################



	# Print server numbers in a column with your specified number range
seq 163 180 | awk '{print "g"$1}'


	# copy file structures with particular file size restriction
rsync -a --min-size 1k --max-size 1m original_path /new_destination/


	# kill all screen sessions
killall -15 screen

	# These tow commands are identical, they both read and execute the commands write in a file in the current shell envioronment
source file_name / . file_name


* -c for checksum, -v for verbose, -P for progress, -h for human readable format, -z for compress, -a for archive mode
	# Synchronize file from remote to local
rsync -chavzP --stats user@remote.host:/path/to/copy /path/to/local/storage

	# Synchronize file from local to remote
rsync -chavzP --stats /path/to/copy user@host.remoted.from:/path/to/local/storage


        # Sync from all content from one directory from to another directory with different name
rsync -r /origin/*  /target/


	# Unzip file with size greater than 4G
jar xf huge_file.zip

        # Locate a program`s path in the system
which program_name


####################            ON MAC              #######################

pwd | pbcopy                                        	# copy what pwd print to clipboard

pbpaste                                             	# paste whatever in clipboard
