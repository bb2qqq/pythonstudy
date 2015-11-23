#############           LOG         #####################

### show commit message and HEAD only
    git log --pretty=oneline

### git log one-liner
    git log --pretty=format:'%h  %ar %<(13) %an "%s"'

### git graph log one-liner
    git log --pretty=format:' %<(13) %an "%s"' --graph

### git search for key word contain in commit changes of the recently 2 days commits.
    git log -Skey_word --since='2 days 1 minute ago'

### git search all commits include changes of targeted file_name or path_name
    git log file_name/path_name

### git Find commits whose commit messages contains "period" and author name contains "song" and commiter name contains "yue"( Though I found without all-match it works the same way)
    git log --grep='period' --author='song' --commiter='yue' --all-match

### git Show the recently 5 commits only
    git log -5

### Show git commits before 2013-12-01 with no merges-in
    git log --before='2013-12-01' --no-merges

### Show the changed file during a commit
    git show --name-only commit-head

### Compare same file between 2 commits.
    git diff $start_commit..$end_commit -- path/to/file

###################         REMOTE          ###########################

### Set local branch to pull from target remote branch
    git branch --set-upstream-to=origin/remote_branch_name local_branch_name

### get remote url
    git config --get remote.origin.url

### git remote operations
    git remote show/add/rename/rm

### git fetch only fetch reomte branch data, git pull will fetch and merge automatically
    git fetch remote_name remote_branch_name
    git pull  remote_name remote_branch_name

###  fetch all remote data
    git fetch --all

### pull from the upstream branch, If your local branch is checking out from a remote branch, that remote branch is upstream branch of this local branch
    git pull

### To push local branch datas to remote and create a remote branch if there isn`t such a branch
    git push remote_name  local_branch_name

### Push local branch data to specified remote branch, if there isn`t such a remote branch, create one.
    git push remote_name local_branch_name:remote_branch_name

### Push local branch to remote tracking branch by force, whcih may cause remote commit loss, use it with caution.
    git push -f

##################          BRANCH          ###########################


### create a branch from current branch and checkout to it at the same time
    git checkout -b branch_name

### create a branch from base_branch and checkout to it at the same time
    git checkout -b branch_name base_branch_name

### create a local branch with the same name of remote branch and track to it
    git checkout --track remote_branch_name

### change the tracking remote branch, another synonym for '-u' is '--set-upstream-to'
    git branch -u remote_name/branch_name

### call visual tools to help doing the merge process
    git mergetool

### showing verbose infos for all branches
    git branch -v

### showing more info than -v, include upstream branch for each branch
    git branch -vv

### To view branches that are merged or not merged with current branch
    git branch --merged / --no-merged

### Delete merged branch, if it isn`t merged, using -D to force delete
    git branch -d branch_name

### Checkout to client, find the common ancestor of server and client, and the change patches from that commit to current client branch commit, store them and replay them on master commit. And switch branch client head to this final commit.
    git rebase --onto master server client

### Checkout to topicbranch, replay its changes on basebranch
    git rebase [basebranch] [topicbranch]
    * DO NOT REBASE COMMITS OUTSIDE YOUR REPOSITORY

### Equal to "git fetch" + "git rebase origin/tracked_branch"
    git pull --rebase


###################         TAG             ############################



### list all tags contains "key_word"
    git tag -l "*key_word*"

### delete specific tag, I found it by myself!
    git tag -d tag_name

### -a makes annotated tag and -m makes a tag message
    git tag -a v0.1 -m 'your tag message'

###  View content of particular tag/HEAD
    git show tag/HEAD

### `git tag` with no options make a lightweight tag, but it is suggested that you and a '-lw' or '_lw' subfix, so others will know that is light-weight
    git tag tag_name_lw

### Add a tag for specific HEAD of your git files, even when this HEAD is in the past
    git tag [options] tag_name HEAD

### push specific tag to remote server
    git push remote tag_name

### push all local tags to remote server
    git push remote --tags

### Show the SHA-1 ID of a tag
    git rev-parse tag_name


###################         OTHERS          ###########################


### Apply a change info in a particular commit to current branch:
    git cherry-pick d42c389f

### Apply a particular stash to current working directory, reapply the stage status, too.
    git stash apply stash@{3} --index

### git removing all deleted files
    git rm $(git ls-files --deleted)

### edit gitconfig
    vim ~/.gitconfig

### @{u} and @{upstream} are short for the upstream branch of current branch, so this command merge the current branch with its upstream branch
    git merge @{u}
