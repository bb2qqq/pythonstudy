### CHARACTER CLASS

`[]` is called a `character class`, it means if a single character is in the `character class`, it's matched.  
There is a metacharacter `-` inside the `character class`, it means a range.  
[0-9] means from `0` to `9`, which is [0123456789]  
[A-Z] means from `A` to `Z`  
[a-z] means from `a` to `z`  

In `grep -e`, the rank of these ranges are, `0-9 > A-Z > a-z`, so you can use `[0-z]` to represent all alphanum char, and `[A-z]` for any alphabetic char.  
And of course you can use mixture pattern like `[0-5b-kD-Z]`  
