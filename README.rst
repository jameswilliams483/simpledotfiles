Overview:
=========
This is to help manage your dotfiles across multiple configurations.


Files
=========

Suffixes:
---------------
.custom
  These files need special instructions _experimental_

.symlink
  These files are hardlinked to the user's home directory.

#######################
.symlink_custom
  These files are hardlinked but directory needs to be specified.
  Details located in .meta file.

.priv
  These files are ignored by git. Sensitive config options should be put here

Folders:
---------
protected
    Everything in here is ignored by git

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

