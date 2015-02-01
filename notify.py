# -*- coding: utf-8 -*-

import pynotify
import errors

_app = "svn-notify"

# init pynotify. can be a decorator
def init_pynotify():
    try:
        pynotify.init(_app)
    except Exception as e:
        raise errors.PynotifyError("Error in initializing pynotify. %s" % e)

def desktop_notification(**kwargs):
    '''Use python's pynotify lib to show desktop notification
    :kwargs - dynamic keyword arguments
    ::title - title on the notification (default bold)
    ::message - message that appears below the title
    ::icon - icon that appears on the left side
    ::urgency - severity of the notification'''

    title, message, icon, timeout, urgency = (kwargs.get(k) \
        for k in ['title', 'message', 'icon', 'timeout', 'urgency']
    )
    urgency_map = {
        'low' : pynotify.URGENCY_LOW,
	'normal' : pynotify.URGENCY_NORMAL,
	'critical' : pynotify.URGENCY_CRITICAL
    }
    urgency = urgency_map.get(urgency) or pynotify.URGENCY_NORMAL
    init_pynotify()
    try:
        n = pynotify.Notification(title, message, icon)
        n.set_timeout(timeout or 1)
	n.set_urgency(urgency)
        n.show()
        # You can close the notification before it has timed out
        # n.close()
    except Exception as e:
        raise errors.PynotifyError("Error in showing notification. %s" % e)

def loop_desktop_notification(payload, icon=None):
    '''Show multiple desktop notifications.
    :payload - a dict. title=key, message=form a message from the payload value
    :icon - image to be shown on the desktop notification'''
    for title, file_list in payload.iteritems():
        if file_list:
            message = ['%s. %s\n' % (i+1, v) for i, v in enumerate(file_list)]
            message = ''.join(message).rstrip()
            # create desktop notification
            desktop_notification(title=title, message=message, icon=icon)

if __name__ == '__main__':
    title, message, icon, urgency = "Title", '''message''', "/home/hussain/Pictures/interstellar.jpg", "low"
    desktop_notification(title=title, message=message, icon=icon, urgency=urgency)
    

