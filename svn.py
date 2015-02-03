#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import path
import pysvn
import notify
import errors
import validations

class Svn:

    '''Informant keeps you in the loop while collaborating
       1. Keep tabs on svn changes being done on the repo. 
          It evidently lets you know if your working copy is not upto date
       2. It reminds you that your working copy has staged / uncommited changes
    '''

    def __init__(self, svn_wc_path=None, svn_repo_url=None, notification_icon=None):
        self.client = pysvn.Client()
        self.svn_wc_path = svn_wc_path 
        validations.validate_path(self.svn_wc_path)
        self.svn_repo_url = svn_repo_url 
        validations.validate_svn_url(self.svn_repo_url)
        self.icon = notification_icon 
        validations.validate_path(self.icon)
	self._init_svn_statuses()
        self.headrev = self.client.info(self.svn_wc_path).revision
        self.headrev_number = self.headrev.number
        self.svn_wc_statuses = {
            pysvn.wc_status_kind.modified : 'modified',
            pysvn.wc_status_kind.added : 'added',
            pysvn.wc_status_kind.deleted : 'deleted', 
            pysvn.wc_status_kind.conflicted : 'conflicted',
            pysvn.wc_status_kind.unversioned : 'unversioned',
            #pysvn.wc_status_kind.ignored : 'ignored'
        } # include more later after some research. 

    def _init_svn_statuses(self):
        self.svn_statuses = {
	    'modified' : [],
	    'added' : [],
	    'deleted' : [],
	    'conflicted' : [],
	    'unversioned' : [],
            #'ignored' : []
	}

    def list_not_upto_date(self):
        '''Track files that are not upto date'''
        try:
            revlog = self.client.log(self.svn_wc_path, \
                     revision_start=self.headrev, revision_end=self.headrev, \
                     discover_changed_paths=False)  
            print revlog
        except Exception as e:
            raise errors.SvnError(e)

    def list_status_working_copy(self):
        '''Track un commited files. Create payload based on their status
        e.g. modified, added, deleted, etc'''
        try:
            list_status = self.client.status(self.svn_wc_path, recurse=True)
            for item in list_status:
	         text_status = item.data.get('text_status')
                 file_path = item.data.get('path')
                 file_path_rel_svn_url = path.relpath(file_path, self.svn_wc_path)
                 if text_status in self.svn_wc_statuses:
                     # get actual string status from text_status later
		     wc_text_status = self.svn_wc_statuses.get(text_status)
                     #pdb.set_trace()
		     self.svn_statuses[wc_text_status].append(file_path_rel_svn_url)
            notify.loop_desktop_notification(self.svn_statuses, self.icon)	    
        except Exception as e:
            raise errors.SvnError(e)


if __name__ == '__main__':
    hist = Svn('/test path',
               '/test path',
               '/test path')
    # working
    hist.list_status_working_copy()
    # in progress
    # hist.list_not_upto_date()
