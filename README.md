informant
---------
Informant keeps you in the loop while colaborating using *svn* and *git*
- Keep tabs on svn changes being done on the repo. It evidently lets you know if your working copy is not upto date (TBD)
- It reminds you that your working copy has staged / uncommited / untracked changes (done)

Samples
-------
![sample output for files with status M](https://github.com/hussaintamboli/informant/raw/master/screenshots/sample_output_modified.png "sample output for files with status M")

![sample output for files with status ?](https://github.com/hussaintamboli/informant/raw/master/screenshots/sample_output_unversioned.png "sample output for files with status ?")


Tools used
----------
- pynotify
- pysvn
- GitPython
- arrow (TBD)

Milestones
----------
- `pysvn` and `GitPython` don't have good documentation. I am exploring it manually.
- `pynotify` doesn't work properly. e.g. timeout and urgency don't work

TODO
----
- informant for remote changes in both `svn` and `git`

Contribute
----------
- Fork the repository
- Add yourself to AUTHORS
- Test. Write unittests. 
- Restructure
- Report bugs / Fix bugs

..
Hussain (@hussain_tamboli)
