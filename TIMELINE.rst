













Old junk
############################################################
Bucket
=========


0.*
============

0.2

0.1
- initial build

#################################################
#######################
MileStone 1
===========================
Features:
---------------
Update commnad
    If we added new config files to simpledotfiles, only add new files not already
 hard linked.

Log Command:

Local Files:
    Ability to rename old file as <foo>.local and source that file in newly symlinked .rc file. Might not work for all dotfiles.

Configuration:
---------------
LOCAL_PRECEDENCE = False
    If True, sourced .local files will take precedence over dotfile files

Details:
---------------
~/.simpledotfiles
- backups
- logs


Thrash:
---------------
Upgrade support:
-> mark simpledotfiles files as such and overwrite previous files if current dotfile is newer (this won't ever happen though because files are hardlinked)
