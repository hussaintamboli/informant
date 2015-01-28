informant
---------
Informant keeps you in the loop while colaborating using *svn*
# Keep tabs on svn changes being done on the repo. 
It evidently lets you know if your working copy is not upto date
# It reminds you that your working copy has staged / uncommited changes

Samples
-------
![sample output for files with status=M](https://github.com/hussaintamboli/informant/tree/master/screenshots/sample_output_modified.png)

![sample output for files with status=?](https://github.com/hussaintamboli/informant/tree/master/screenshots/sample_output_unversioned.png)


Tools used
----------
- pynotify
- pysvn
- arrow (TBD)

Milestones
----------
- As of now, I am only focusing on `svn`. `pysvn` doesn't have a good documentation. Rather it doesn't have a documentation at all. So I am exploring it manually.
- `pynotify` doesn't work properly. e.g. timeout and urgency don't work
- Haven't been able to find a good python library that could interact with git

TODO
----
- informant for git

Contribute
----------
- Fork the repository
- Add yourself to AUTHORS
- Tests
- Report bugs / Fix bugs

..
Hussain (@hussain_tamboli)