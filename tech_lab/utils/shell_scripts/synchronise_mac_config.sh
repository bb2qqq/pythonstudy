# I'd better use rsync instead of cp one day
cp ~/.bash_profile  ~/zen/pythonstudy/tech_lab/config/OSX/bash_profile

# filter
grep -v "ssh" ~/.bashrc | grep -v "admin" > ~/tmp
cp ~/tmp ~/zen/pythonstudy/tech_lab/config/OSX/bashrc
cp ~/.vimrc ~/zen/pythonstudy/tech_lab/config/CrossPlatform/vimrc
cp ~/.vimrc ~/zen/pythonstudy/tech_lab/config/OSX/vimrc
cp ~/.vim/plugin/* /Users/zen1/zen/pythonstudy/tech_lab/vim_skill/my_plugin

# Universal code
cp /Users/zen1/zen/automation/General/new_system/general_gadget/* /Users/zen1/zen/pythonstudy/tech_lab/my_work/zen_system/
