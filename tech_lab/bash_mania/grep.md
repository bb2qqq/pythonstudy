## GREP ##

### Non greedy search
    grep -P 'a*?b+?c??'
> By default, grep doesn't support non greedy search, and -P means enable the Perl style regex, which support non greedy search.

### Print pattern only in result
    grep -o pattern files

### Don't print file name in result
    grep -h pattern *

### Print serveral lines around pattern
* Print 3 lines above pattern
    grep -A 3 pattern files
* Print 3 lines below pattern
    grep -B 3 pattern files
* Print 3 lines both above and below pattern
    grep -C 3 pattern files


* grep for utf-8 character in a file
    grep --color='auto' -P -n '[^\x00-\x7F]' your_file

* list file names only for files contain patterns

    grep -l pattern *


`egrep` = `grep -E` means using the Extended Regular Expression

`fgrep` = `grep -F` means treat pattern as fixed string, separted by newline
    content of my_pattern file:
        Jack
        Tom
        Mary


    grep -F -f my_pattern target_file      # This will grep any line contains Jack, Tom or Mary in target_file

* Find recursively on current directory those files which contains keyword _luck_ and list them out.

      grep -Fnrl luck ./

>   -F = fixed string, -n = show line number(not used here), -r = recursively, -l = list files instead of show lines contains pattern


* Find all files contains name "Garcia" and list those files who has "Aureliano" in it.

        find  -name '*Garcia*' |xargs  grep -l 'Aureliano'

>   xargs is used to pass "standard input" or "pipe aruguments" to commands such like "grep" or "awk", or to break the long arguments of list into pieces so it is acceptable for some commands


* Grep for string "\t" + "apple" + "\t", -P means Perl-style regex, this can search for pattern contain tab

      grep -P "\tapple\t"


* Search except files with some kind of string, here find pattern in file_names except those contains 'master' in file name

      grep --exclude='*master*'  pattern  file_names


* Find file that does not contain the pattern

      grep -L "pattern" files

