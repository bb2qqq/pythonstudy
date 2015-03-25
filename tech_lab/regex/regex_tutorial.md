### CHARACTER CLASS

`[]` is called a `character class`, it means if a single character is in the `character class`, it's matched.  
There is a metacharacter `-` inside the `character class`, it means a range.  
[0-9] means from `0` to `9`, which is [0123456789]  
[A-Z] means from `A` to `Z`  
[a-z] means from `a` to `z`  

In `grep -e`, the rank of these ranges are,   
`0-9 > A-Z > a-z`, so you can use `[0-z]` to represent all alphanum char, and `[A-z]` for any alphabetic char.  
And of course you can use mixture pattern like `[0-5b-kD-Z]`  

**Reverse match**

Inside a `character class`, `^` means to reverse match,  
like `egrep '[^0-z]$' target_file` will find out any line in that ends up not with alphanumeric nums.  


### Alternation

`|` means for `or` in regex  
`()` can be used to wrap expressions in many cases, like in python do.  
`egrep -n ' (I|me) .* (yes|no) ' file` will find any line that has word "I" or "me" in it, and in the same line, after arbitary words, "yes" or "no" appears.

> The expressions wrapped by `()` can be a single complete regex!  
> You can treat them like regex nested in regex


### Ignoring case

Ignoring case isn't a part of regex, but many tools offers this feature,
in `egrep`, using `-i` can enable the ignoring case feature.


### Word Boundaries

`\<` and `\>` are `metasequences`, it was used to match the start position and end position of a word.  
A start position of a word means the letter before it isn't any `alphanumeric chars` or `_`.  
An end positon of a word means the letter after it isn't `alphanumeric char` or `_`.  

This is an advancing feature only support by some kind of softwares.  

### Optional Items

`[char]?` means char can be show here or not, its presence is optional.

Thus we can also say `?` means previous pattern is present `0 time or once`.

### Other Quantifiers: Repetition

`+` means pattern occurs `once or any more times`
`.` means pattern occurs `any times`

** interval quantifier **
As an advance function, `pattern{min, max}` means pattern should occurs at least `min` times and at most `max` times.

> `?`, `+`, `*` works on the character before them

### Parenthesis and Backreferences

`\1`, `\2`, `\3` will match the first, second, third parenthesis expressions.

This `egrep -nr '\<([A-z]+) +\1\>' will much two continous identical words. Let's analyze it.  
`([A-z]+)` means chars from 1 to any number composed with letters,  
a preceding `\<` and a following ` +`  ensured we match a single world here.  
Then `\1` means the previous pattern wrapped in `()`, a preceding ` +` and a following `\>` also ensures this is a single word.  
Thus we can match two continuous identical word.


### The Great Escape

For special `meta-chars`, you can use `\` to convert it into a normal character.  
But be aware, in a `character class`, it won't work.  

