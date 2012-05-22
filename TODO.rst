Now:
------

0.1
------
- move everything to /src and set up directroy status !1
- wipe everything in git and start over with correct protections !1



############################################
Experimental
============
Options:
---------------
append
    Adds the following line to end of existing dot file
    ## {% simplelogfiles_start %}
    ## simpledotfiles_start
    ## DON'T delete anything below this line
    ...
    ## {% simplelogfiles_end %}

 delete
    Delete dotfiles
    -a
        Delete all dotfiles

extend
  Keep old configuration but in a seperate file.
  eg.
  mv .bashrc .bashrc_local
  ln .bashrc ~/.bashrc
  ...
  source ~/.bashrc_local

overwrite
    removes old file

skip-all

overwrite-all

append-all

backup-all
    Saves backups as ~/.dotfiles/<file>

#######################

Meta File
----------
The .meta file is used to specify linkage conventions for .symlink_custom and .priv files.
Data is stored in key value pairs in the form of <file_name> = <linkage path>

  eg.
    gitconfig.symlink_custom = "/opt/local/etc/.gitconfig"

Note that the full path name needs to be given

