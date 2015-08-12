VIM: built-in functions

    Ascii Value of a Character : <code>char2nr()</code> ---- opposite: <code>nr2char</code>
## Cursor related
    line("$")
    line("'t")
    line(".")

    col(...)

## Setting the cursor:

    cursor(line, column)
    See also getpos() (which returns a list)

## Asking the user
    echo confirm("is this ok?", "&Yes\n&No")
    Make "No" the default choice
    echo confirm("is this ok?", "&Yes\n&No\n&Don't know", 2)

## List / Directory Commands
    add()
    filter()
    empty()
    remove()
    copy()
    deepcopy()
    count()
    get()
    index()
    insert()
    items()   " dict only
    join()    " list only
    keys()    " dict only
    values()  " dict only
    len()
    map()
    max()
    min()
    range()   " list only
    remove()
    repeat()  " also for strings
    reverse()
    sort()
    split()   " returns a list

## Functions related to functions
    function()

## Functions related to buffers
    getbufvar()
    setbufvar()
    getline()
    setline()
    getbufline()

## Functions related to interaction
    getchar()     "checks also for mouse clicks
    gecharmod()
    input()
    inputsecret()
    inputdialog()
    inputlist()
    inputsave()
    inputrestore()

## Functions related to the commandline
    getcmdline(),
    getcmdpos(),
    getcmdtype()
    setcmdpos()

## Functions related to to registers
    getreg()
    setreg()
    getregtype()

## Functions related to server
    remote_expr()
    remote_foreground()
    remote_peek()
    remote_read()
    remote_send()
    server2client()
    serverlist()
