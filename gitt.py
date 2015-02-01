#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import path
import git
import notify
import errors

class Git:

    '''Informant keeps you in the loop while collaborating
       1. Keep tabs on git changes being done on the repo. 
          It evidently lets you know if your working copy is not upto date
       2. It reminds you that your working copy has staged / uncommited changes
    '''

    def __init__(self, repo_path, icon=None):
        self.repo_path = repo_path
        self.icon = icon
 
    def list_status_working_copy(self):
        '''Track un commited files. Create payload based on their status
        e.g. modified, added, deleted, etc'''
        try:
            repo = git.Repo(self.repo_path)
            untracked_files = {
	        'untracked' : repo.untracked_files
	    }
	    notify.loop_desktop_notification(untracked_files, self.icon)
        except Exception as e:
            raise errors.GitError(e)

    def repo_status(self):
        pass


if __name__ == '__main__':
    g = Git('/home/hussain/Documents/MyRepos/informant',
            '/home/hussain/Pictures/me.jpg'
    )
    g.list_status_working_copy()
