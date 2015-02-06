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

git fetch remote_name remote_branch_name                        # git fetch only fetch reomte branch data, git pull will fetch and merge automatically
git pull  remote_name remote_branch_name

git fetch --all                                                 #  fetch all remote data

git pull                                                        # pull from the upstream branch, If your local branch is checking out from a remote branch, that remote branch is upstream branch of this local branch

git push remote_name  local_branch_name                         # To push local branch datas to remote and create a remote branch if there isn`t such a branch

git push remote_name local_branch_name:remote_branch_name       # Push local branch data to specified remote branch, if there isn`t such a remote branch, create one.

git push -f                                                     # Push local branch to remote tracking branch by force, whcih may cause remote commit loss, use it with caution.

##################          BRANCH          ###########################

git checkout -b branch_name                                     # create a branch from current branch and checkout to it at the same time

git checkout -b branch_name base_branch_name                    # create a branch from base_branch and checkout to it at the same time

git checkout --track remote_branch_name                         # create a local branch with the same name of remote branch and track to it

git branch -u remote_name/branch_name                           # change the tracking remote branch, another synonym for '-u' is '--set-upstream-to'

git mergetool                                                   # call visual tools to help doing the merge process

git branch -v                                                   # showing verbose infos for all branches

git branch -vv                                                  # showing more info than -v, include upstream branch for each branch

git branch --merged / --no-merged                               # To view branches that are merged or not merged with current branch

git branch -d branch_name                                       # Delete merged branch, if it isn`t merged, using -D to force delete

git rebase --onto master server client                          # Checkout to client, find the common ancestor of server and client, and the change patches from that commit to current client branch commit, store them and replay them on master commit. And switch branch client head to this final commit.

git rebase [basebranch] [topicbranch]                           # Checkout to topicbranch, replay its changes on basebranch
    * DO NOT REBASE COMMITS OUTSIDE YOUR REPOSITORY

git pull --rebase                                               # Equal to "git fetch" + "git rebase origin/tracked_branch"


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

vim ~/.gitconfig                                                # edit gitconfig

git merge @{u}                                                  # @{u} and @{upstream} are short for the upstream branch of current branch, so this command merge the current branch with its upstream branch
