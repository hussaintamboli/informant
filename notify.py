# -*- coding: utf-8 -*-
import pynotify
import errors

_app = "svn-notify"

def init_pynotify():
    try:
        pynotify.init(_app)
    except Exception as e:
        raise errors.PynotifyError("Error in initializing pynotify. %s" % e)

def desktop_notification(**kwargs):
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

def loop_desktop_notification(notifications):
    for notification in notifications:
        desktop_notification(title=notification.get('title'), message=notification.get('message'))

if __name__ == '__main__':
    title, message, icon, urgency = "Title", '''message''', "/home/hussain/Pictures/interstellar.jpg", "low"
    for i in range(1, 5):
        desktop_notification(title=str(i), message=message, icon=icon, urgency=urgency)
    

