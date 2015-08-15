" TOY FUNCTIONS AREA

function EchoVars(v1, v2, ...)
    echohl Visual
    echo a:v1
    echohl None
    echo a:v2
    echo a:0
    echo a:1
    echo a:2
    echo a:000
endfunction

let ClassZ = {'author': "Juchen.Zeng"}
function ClassZ.Print_author_name()
    echo self.author
endfunction

function ClassZ.Change_author_name(arg1)
    let self.author = a:arg1
endfunction

function Echo_to_file(expr_str)
    redir => zen_temp | exe a:expr_str | redir END | put=zen_temp
endfunction
