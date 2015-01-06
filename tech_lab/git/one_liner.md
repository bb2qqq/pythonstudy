#############           LOG         #####################
git log --pretty=oneline                                        # show commit message and HEAD only

git log --pretty=format:'%h  %ar %<(13) %an "%s"'               # git log one-liner

git log --pretty=format:' %<(13) %an "%s"' --graph              # git graph log one-liner

git log -Skey_word --since='2 days 1 minute ago'                # git search for key word contain in commit changes of the recently 2 days commits.

git log file_name/path_name                                     # git search all commits include changes of targeted file_name or path_name 
git log --grep='period' --author='song' --commiter='yue' --all-match             # git Find commits whose commit messages contains "period" and author name contains "song" and commiter name contains "yue"( Though I found without all-match it works the same way)

git log -5                                                      # git Show the recently 5 commits only

git log --before='2013-12-01' --no-merges                       # Show git commits before 2013-12-01 with no merges-in

# FOR MORE INFORMATIONS, DO  man grep log




###################         REMOTE          ###########################

git remote show/add/rename/rm                                   # git remote operations

git fetch remote_name remote_branch_name                        # git remote data transfer
git pull  remote_name remote_branch_name





###################         TAG             ############################

git tag -l "*key_word*"                                         # list all tags contains "key_word"

git tag -d tag_name                                             # delete specific tag, I found it by myself!

git tag -a v0.1 -m 'your tag message'                           # -a makes annotated tag and -m makes a tag message

git show tag/HEAD                                               #  View content of particular tag/HEAD

git tag tag_name_lw                                             # `git tag` with no options make a lightweight tag, but it is suggested that you and a '-lw' or '_lw' subfix, so others will know that is light-weight

git tag [options] tag_name HEAD                                 # Add a tag for specific HEAD of your git files, even when this HEAD is in the past

git push remote tag_name                                        # push specific tag to remote server

git push remote --tags                                          # push all local tags to remote server

git rev-parse tag_name                                          # Show the SHA-1 ID of a tag

###################         OTHERS          ###########################

git rm $(git ls-files --deleted)                                # git removing all deleted files

global git config is under ~/.gitconfig

git checkout -b branch_name                                     # create a branch and checkout to it at the same time
