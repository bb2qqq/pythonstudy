##################          GREP            #################################



grep -Fnrl lush ./      * Find recursively on current directory those files which contains keyword lush and list them out.
# -F = fixed string, -n = show line number(not used here), -r = recursively, -l = list files instead of show lines contains pattern

find  -name '*Garcia*' |xargs  grep -l 'Aureliano'          * Find all files contains name "Garcia" and list those files who has "Aureliano" in it.
# xargs is used to pass "standard input" or "pipe aruguments" to commands such like "grep" or "awk", or to break the long arguments of list into pieces so it is acceptable for some commands







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





#####################           SED         #############################



# find line of file contains keyword and del it
sed -i '/key_word/d' target_file









###################             OTHERS              ######################



# Print server numbers in a column with your specified number range
seq 163 180 | awk '{print "g"$1}'


# copy file structures with particular file size restriction
rsync -a --min-size 1k --max-size 1m original_path /new_destination/
