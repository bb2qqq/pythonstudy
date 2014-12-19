git log --pretty=format:'%h  %ar %<(13) %an "%s"'               # git log one-liner

git log --pretty=format:' %<(13) %an "%s"' --graph              # git graph log one-liner

git log -Skey_word --since='2 days 1 minute ago'                # git search for key word contain in commit changes of the recently 2 days commits.

git log file_name/path_name                                     # git search all commits include changes of targeted file_name or path_name

git log --grep='period' --author='song' --commiter='yue' --all-match             # git Find commits whose commit messages contains "period" and author name contains "song" and commiter name contains "yue"( Though I found without all-match it works the same way)

git log -5                                                      # git Show the recently 5 commits only

git log --before='2013-12-01' --no-merges                       # Show git commits before 2013-12-01 with no merges-in

# FOR MORE INFORMATIONS, DO  man grep log
