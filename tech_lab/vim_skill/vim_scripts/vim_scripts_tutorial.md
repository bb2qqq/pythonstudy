### Show all current vim variables
    :let

### Create local variables
    :let s:local_var = 42

>    b:name      variable local to a buffer  
>    w:name      variable local to a window  
>    g:name      global variable (also in a function)  
>    v:name      variable predefined by Vim  

### Delete variables

    :unlet global_var
    :unlet s:local_var

### Check if a var name exists already

    if exists("var_name")
        echo "variable name already in use"
    endif

    if !exists("var_name")
        echo "Usable variable name"
    endif

> In vim, zero is false. Anything else is True  
> [Caution!], vim will convert any string without digit ahead to zero  
> Thus, `:if "true"` will be considered as `:if false`  
> meanwhile `:if "1true"` is true, and `:if "0true"` still false.  

### Special Escape Characters
    \e      <Esc>
    \<Esc>  <Esc>
    \<C-W>  CTRL-W

> The last two are just examples. The `"\<name>"` form can be used to include the special key "name".

### Vim expressions
    $NAME       environment variable
    &name       option
    @r          register

    Examples:
    :echo "The value of 'tabstop' is" &ts
    :echo "Your home directory is" $HOME
    :echo @a == 0

### Concatenate Strings
In vim script, you use `.` to join strings

    echo "I am" . " your daddy."


### Conditional Expression

Example: `a ? b : c`, If "a" evaluated to true, "b" is used, otherwise "c" is used.


### Value Comparison

As we have mentioned, strings starts without a number would be consider zero when comparing to a number. Thus:

    :echo "string_starts_with_alpha" == 0
    1
    :echo "!!!&?*Punctuations" == 0
    1
    :echo "End_with_number369" == 0
    1
    :echo "42startswith_number" == 0
    0
    :echo "42startswith_number" == 42
    1

When comparing strings, ignore option is used, you can specify `==#` to match case, and `==?` to ignore case.

    # VIEW VALUE OF IGNORECASE OPTION

    :echo &ignorecase
    0
    :echo &ic
    0


    # COMPARISON EXAMPLES

    :echo "PApa" ==? "paPa"
    1
    :echo "JORDAN" ==# "jorDAn"
    0


Besides of comparing equal, you can compare if a `string` match with a pattern,  
by using `s =~ p` and `s !~ p`, where `s` is a string, and `p` a pattern

    :echo "nimabi" =~ 'n*m*b'
    1
    echo "nimabi" =~ 'nmb'
    0
    echo "nimabi" !~ 'nmb'
    1

    if str !~ '\.$'
        echo "string doesn't end with period"
    endif
> Be aware that when pattern wrapped in `single quotes`, you only need `one slash` to escape special characters.  
> If you wrapped pattern in `two single quotes`, you'll need `two slash` to escape a special character.

### EXEC function in vim script

    :let str1 = "r"
    :let str2 = "!date"
    :execute str1 . str2

To exectue normal mode command, we use `normal` as the initial command

    # Be aware you can't copy this command in OSX directly
    # You need to type  by pressing CTRL-V, then <Esc>

    :normal Insert and clone  yyp

    # Another way to excute a normal mode command is using execute with strings,
    # in this way, the command is copiable
    :execute "normal iInsert and clone \<Esc> yyp"

### EVAL Function in vim script

    let p = eval('&path')
    echo p
    .,/usr/include,,


## Functions
### A few usages of functions in vim:

    :let line = getline(".")
    :let replaced_line = substitute(line, '\a', "*", "g")
    :call setline(".", replaced_line)

    # RESULT
    :*** **** = *******(".")

> `.` means the position of the cursor

### Define your own functions

Function name must begin with a capital letter, bare return returns 0.  
Variables inside a function is a local function.  
You can speicified a local variable with prepending `l:`, or it may clash with vim reserve variables.  
Such as when typing `count` in a function, you are refers to `v:count`.  
To define variables of other scopes, you prepend it with `g:`, `a:` or `s:`.  
`g:` is `global variable`, `a:` is `argument variable` and `s:` is `script variable`.  

To redefine an exists function you use add `!` to `:function`, which is `:function!`.

Function with range:

    function AddShellPrompt() range
        let lnum = a:firstline
        while lnum <= a:lastline
            let replaced_line = substitute(getline(lnum), '^\s\+', '&>>>', '')
            call setline(lnum, replaced_line)
            let lnum += 1
        endwhile
    endfunction

    # By using `:1,-1 call AddShellPrompt()
    # You can add >>> for all your code examples in a markdown file


Function without range:

    function PrintLine()
        echo getline(".")
    endfunction

    # By using `:1,20 call PrintLine()
    # You will get line1 to line20 printed on your screen.
    # Meanwhile cursor moved to line20




