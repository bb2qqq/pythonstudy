### Show all current vim variables
    :let
    :put L2 | put L1

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

Function with undefinite numbers of variables:

In vim, you can specify that a function need particular numbers of concret variables,  
and undefinite numbers of possible variables(max optional var num is 20).  
Let's see an example:

    function EchoVars(v1, v2, ...)
        echo a:v1
        echo a:v2
        echo a:0
        echo a:1
        echo a:2
        echo a:000
    endfunction

    "# CALL IT
    call EchoVars('a','b','c','d','e', 'f', 'g')

    "# RESULT
    a
    b
    5
    c
    d
    ['c', 'd', 'e', 'f', 'g']

From the example above, we can see `a:0` refers to the total num of optional vars,  
`a:000` is the list of all optional vars, meanwhile `a:1` is the first optioanl var, and so on.

<br/>
There is a way to assign a reference to a function by using `function()`. Here is an example:

    :function Titan()
    :    echo "Shivering under the power of reference, insects!"
    :endfunction
    :let Ref1 = function('Titan')
    :call Ref1()

    Shivering under the power of reference, insects!

You use `function` to view all user-defined functions, type `function FunctionName` to view code of a particular function.  
And `:delfunction FunctionName` can help you delete a function.


## CLASSES
Vim script doesn't have class structure. But you can "Leverage" a dict to make it a rudimental class.  
And you use `copy()` function to make instances of it.

    :let ClassZ = {'author': "Juchen.Zeng"}
    :function ClassZ.Print_author_name()
    :    echo self.author
    :endfunction

    :function ClassZ.Change_author_name(arg1)
    :    let self.author = a:arg1
    :endfunction

    :call ClassZ.Print_author_name()

    Juchen.Zeng

    :call ClassZ.Change_author_name('MarioLuisGarcia')
    :call ClassZ.Print_author_name()

    MarioLuisGarcia

    :put = string(ClassZ)

    {'Change_author_name': function('2'), 'author': 'MarioLuisGarcia', 'Print_author_name': function('1')}

    "# You can use `function {function_numer} to view a numbered function, e.g.
    :function {2}

       function 2(arg1) dict
    1      let self.author = a:arg1
       endfunction



There is another way to define dict methods, by using extra `dict` argument when defining a function.

    :function Tell_joke() dict
    :    echo "This is funny!"
    :endfunction

    :call Tell_joke()
    E725: Calling dict function without Dictionary: Tell_joke

    :let ClassZ['Talk'] = function('Tell_joke')
    :call ClassZ.Talk()

    This is funny!

# DATA TYPES

## LIST
### Append elements to list
    :let vl = []
    :call add(vl, 'i1')
    :call add(vl, 'i2')
    :echo vl

    ['i1', 'i2']

### Extend a list
    :let L1 = [1, 2]
    :let L2 = [3, 4]
    :echo L1 + L2

    [1, 2, 3, 4]

    :echo L1

    [1, 2]

    :let L1 += L2
    :let L2 = L2 + L1
    :put = string(L2)

    [3, 4, 1, 2, 3, 4]

    :call extend(L2, L2)

    [3, 4, 1, 2, 3, 4, 3, 4, 1, 2, 3, 4]

    :call add(L1, L1)
    :put = string(L1)

    [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [1, 2, 3, 4, [{E724}]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

    :let L3 = [5, 6]
    :call add(L2, L3)

    [3, 4, 1, 2, 3, 4, 3, 4, 1, 2, 3, 4, [5, 6]]


### Iterate over a list
    "# Example 1
    :let L = [1,2,3,4,5]
    :let n = 0
    :for i in L
    :   let n += i
    :endfor
    :echo n

    15

    "# Example 2
    :for line in getline(10, 60)
    :    if line =~ "me"
    :       put = matchstr(line, '[a-z]*me[a-z]*')
    :    endif
    :endfor

    "# RESULT(deleted some "name" result)
    name
    meanwhile
    name
    environment
    name



# Syntax

### Excpetion Catch
Catch particular exception

    :try
    :   read ~/files_not_exists
    :catch /E484:/
    :   echo "Sorry, the dir was using to store cookies now"
    :endtry

Bare exception

    :try
    :    call messi_jugar_baloncesto
    :catch
    :    echo "Esto es increible"
    :endtry

Finally syntax

    :try
    :   call murninho_is_brazilian()
    :catch /What?/
    :finally
    :   echo "He win the Prime League at least"
    :endtry

> No matter what happens between `try` and `finally`, the command in `finally` part will always been executed.


### Line continuation

    :!vim temp.vim
    function Line_continuation_demonstration()
        echo "Let's test the line
              \ continuation in
              \ vim."
    endfunction

    :source temp.vim
    :call Line_continuation_demonstration()

    Let's test the line continuation in vim.
