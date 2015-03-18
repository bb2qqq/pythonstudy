#!/usr/bin/perl
@list=(1,2,3,4,5);
%dict=(1,2,3,4,5);

print "$list[0]\n";         # using [ ] to wrap index
print "$dict{1}\n";         # using { } to wrap key

print "@list[2]\n";
#print "%dict{2}\n";


