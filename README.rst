Overview:
=========
This is to help manage your dotfiles across multiple configurations.

Folders:
---------
protected
    Everything in here is ignored by git

Files suffixes:
---------------
.custom
  These files need special instructions _experimental_

.symlink
  These files are hardlinked to the user's home directory.

.symlink_custom
  These files are hardlinked but directory needs to be specified.
  Details located in .meta file.

.priv
  These files are ignored by git. Sensitive config options should be put here

Files
---------
etc
  screenrc.symlink
  tmux.conf.symlink

git
  gitconfig.priv
  gitconfig.symlink_custom

python
  pdbrc.symlink
  pylint.custom

vim
  gvimrc.symlink
  vimrc.symlink



#######################

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

