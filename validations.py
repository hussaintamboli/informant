# -*- coding: utf-8 -*-
from os import path
import pysvn
import errors

def validate_path(wc_path):
    if not wc_path:
        raise errors.InvalidPathError('path is empty')
    if not path.exists(wc_path):
        raise errors.InvalidPathError('%s is invalid' % wc_path)

def validate_svn_url(svn_url):
    if not svn_url:
        raise errors.InvalidUrlError('Svn Url is empty')
    client = pysvn.Client()
    if not client.is_url(svn_url):
        raise errors.SvnError('%s is not a svn url' % svn_url)


