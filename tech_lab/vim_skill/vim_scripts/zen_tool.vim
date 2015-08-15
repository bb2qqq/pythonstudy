" Vim script for facilitate Zen's Daily works
" Last Change Aug 15 2015
" Maintainer:   Mario Luis Garcia <bb2qqq@gmail.com>
" License: All rights reserved.

" Enable line continuation by set cpoptions option to default value
let s:save_cpo = &cpo
set cpo&vim


" Avoid crush with another plugin and reload error
if exists("g:loaded_zen_tool")
    finish
endif
let g:loaded_zen_tool = 1


" TOY FUNCTIONS AREA
" Massively add python prompt symbol in a markdown file
function AddShellPrompt() range
    let lnum = a:firstline
    let match_pattern = '^\s\+.*[-\+_*/%=]\|.*import\|.*print\|.*def\|.*class\|.*while\|.*for\|.*if\|.*elif\|.*else\|.*pass\|.*continue\|.*break\|.*return'
    while lnum <= a:lastline
        let current_line = getline(lnum)
        if match(current_line, match_pattern) == 0
            let replaced_line = substitute(current_line, '^\s\+', '&>>>', '')
            call setline(lnum, replaced_line)
        endif
        let lnum += 1
    endwhile
endfunction


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

function Line_continuation_demonstration()
    echo "Let\'s test the line
          \ continuation in
          \ vim."
endfunction



" Restore cptions value to user set value after plugin executed
let &cpo = s:save_cpo
unlet s:save_cpo
