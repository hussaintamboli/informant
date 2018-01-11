informant
---------
Informant keeps you in the loop while colaborating using *svn* and *git*
- Keep tabs on svn changes being done on the repo. It evidently lets you know if your working copy is not upto date (TBD)
- Notifications are sent on the desktop using `notify`

Tools used
----------
- pynotify
- pysvn
- arrow
- GitPython

Challenges
----------
- As of now, I am only focusing on `svn`. `pysvn` doesn't have a good documentation. Rather it doesn't have a documentation at all. So I am exploring it manually.
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
- Tests
- Report bugs / Fix bugs

..
Hussain (@hussain_tamboli)
