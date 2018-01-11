informant
---------
Informant keeps you in the loop while colaborating using *svn* and *git*
- Keep tabs on svn changes being done on the repo. It evidently lets you know if your working copy is not upto date (TBD)
- It reminds you that your working copy has staged / uncommited / untracked changes (done)
- Notifications are sent on the desktop using `notify`

Cron Setting
------------
PATH=<your path>:/home/hussain/Documents/MyRepos/informant
PYTHONPATH=<your python path>:/home/hussain/Documents/MyRepos/informant

0 * * * * DISPLAY=:0.0 svn.py <working_copy_path> <remote_url_of_repo> <icon_path> 2> /home/hussain/tmp/svn.log

0 * * * * DISPLAY=:0.0 gitt.py 2> /home/hussain/tmp/git.log

Tools used
----------
- pynotify
- pysvn
- arrow
- GitPython

Challenges
----------
- `pysvn` and `GitPython` don't have good documentation. I am exploring it manually.
- `pynotify` doesn't work properly. e.g. timeout and urgency don't work

TODO
----
- Check Issues
- informant for remote changes in both `svn` and `git`
- I am thinking of using [dulwich](https://github.com/jelmer/dulwich) instead of GitPython

Contribute
----------
- Fork the repository
- Add yourself to AUTHORS
- Test. Write unittests. 
- Restructure
- Report bugs / Fix bugs

..
Hussain (@hussain_tamboli)
