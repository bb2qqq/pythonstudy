* Stash
  * <a href='#stash_save'> save </a>


### Stash
<a id ='stash_save' >
uisng `git stash` or `git stash save` to save current working directory status into stash  
You can add a message after `git stash save`  as a reminder, such as:  
`git stash save "git guidebook half-way, till the stash part"`
</a>

`git stash list` can list out all your stashes

`git stash apply` will apply the most recent stash,  
meanwhile `git stash apply stash@{n}` can apply the stash at the position `{n}` listed by `git stash list`.

But the apply command mentioned above can't reapply the staged changes,  
you need add an `--index` flag after `git stash apply` to do this

The `apply` option only tries to apply the stashed work,  
 you continued to have it on your stack.  
To remove it, you can run `git stash drop` with the name of the stash to remove, like:  
`git stash drop stash@{2}`

Or you can use `git stash pop stash@{2}` to apply a stash and drop it immediately after that.

** Advancing usage **

using `--keep-index` option to `stash save` command so that git won't stash anything in the staged area.  

By default, git stash will only store files that are already in the index.  
If you specify `--include-untracked` or `-u`, git will also stash any untracked files you have created.  

If you don't want to stash everything, you can use `--patch` flag, then you can select interactively which files you want to stash in a prompt.  

At last, if the branch you stashed from made some commits and is conflict with your stash.  
You can use `git stash branch <your_branch_name>` to make a branch from the commit where you stashed your work,  
and then apply your stash on it, drop the stash if successfully applied.

If you want to clean the directory, you can use `git stash --all` to add all files include ignored file into git stash.  

To empty the entire stash stacks, you use `git stash clear`

### Clean

Yet git will offer you another command to clean your directory: `clean`

To remove all the untracked files in your working directory, you can run `git clean -f -d`,  
which removes all untracked files and directories,  
`-f` means force  

If you want to ensure not to accidentally remove important file,  
you can use `git clean -d -n` to do a dry run,  
the `-n` option will show what will be deleted without delete them.  

By default, the git clean command will only remove untracked files that are not ignored.  
To remove all the ignored file, add an `-x` to the clean command.  

You can also add an `-i` flag to prompt out an interactive interface,  
through which you can confirm the deletion of file one by one, to avoid mistake.  

> To remove a committed file from all commit history, read this:
> https://help.github.com/articles/remove-sensitive-data/
