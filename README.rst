Overview:
=========
This is to help manage your dotfiles across multiple configurations

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
.priv
  These files are ignored by git. Sensitive config options should be put here

Files
---------
etc
  screenrc.symlink
  tmux.conf.symlink

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


