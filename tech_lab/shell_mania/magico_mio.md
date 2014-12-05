# Print server numbers in a column with your specified number range
seq 163 180 | awk '{print "g"$1}'

# Search file between 12-05 08:00:00 to 12-06 00:00:00, with the file size greater than 10MB and samller than 20MB, containing word <equip> in the file name
find -newermt '2014-12-05 8' ! -newermt '2014-12-06' -size +10M -size -20M -name "*equi*"
