### Attach 特定的session
    tmux attach -t session_number


### 改变tmux命令激活键
tmux默认的激活键是ctrl-b，这会和移动光标向后的快捷键相冲突。
所以我把它改成ctrl-m, 一个不曾被使用的快捷键
    vim ~/.tmux.conf
    # Write
    unbind C-b
    set -g prefix C-m


### 不重启tmux session读取tmux配置
1. 按下激活键(默认为ctrl+B)
2. 输入`:source-file ~/.tmux.conf`，按回车，done!


### tmux 数据结构等级
Session 是最高级的object
`tmux new -s <name-of-my-session>`用来在terminal里开启新session
在tmux内，按激活键，输入`:new -s <name-of-my-session>`来开启新session
按激活键 + s, 可以显示当前所有tmux session, 输入序号进入相对应的session
Session的推荐用法是用项目命名，一个session用于一个项目的开发。

Window是次一级的object
在Session里，可以有多个window
你使用激活键 + c 来创建新window
window也可以有名字，方便辨识。
在windows间切换，你使用激活键 + window的数字编号（显示在屏幕下方status bar里）

Pane是最低级的object
一个window由若干个pane组成
激活键 + % 可以分一个竖直pane出来，激活键 + " 分一个水平的pane出来
按激活键 + 方向键可以让光标移动到相应方向的pane里
