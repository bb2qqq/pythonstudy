# Print server numbers in a column with your specified number range
seq 163 180 | awk '{print "g"$1}'
