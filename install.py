import os
#TODO: deal with special cases in a specials directory
# eg. vim files, try to save current vim config in a local file
#TODO: save logs somewhere
#TODO: add ability to preview file during command prompt

# Files in here won't be symlinked. Assumes unique directory names
IGNORE = ['']
OVERWRITE_ALL = False
SKIP_ALL = False

#TODO: change this to automatic
CUSTOM = ['vim']

#OPTIMIZE: cache these results
def _get_symlinks():
    """
    Get all files ending in .symlink from dirs
    Doesn't follow symbolic links
    @return:
    List of tuples (path, [files])
    eg.
    [(path, [ foo.symlink]), (...),...]
    """
    global IGNORE

    print ("gathering symlinks...")
    out = []
    walker = os.walk(".")
    for path, directory, files in walker:
        for inum, dname in enumerate(directory):
            if (dname in IGNORE):
                del directory[inum]
        symlinks = filter(lambda x: x.rfind(".symlink") >= 0, files)
        if (symlinks):
            out.append((path, symlinks))
    return out

#TODO(high): think about this some more
def _get_dirs():
    """
    Get files like .vim and all subdirectories
    """
    global IGNORE

    print ("gathering directories...")
    out = []
    walker = os.walk(".")
    return

def install(args = None):
    """
    Install dotfiles in computer
    """
    global SKIP_ALL
    global OVERWRITE_ALL
    symlinks = _get_symlinks()

    for path, links in symlinks:
        for link in links:
            fname = "." + link.rstrip(".symlink")
            fpath_old = os.path.join(path, link)
            fpath = os.path.join(os.path.expanduser('~'), fname)

            #SC: Handle file collision
            if (os.path.exists(fpath)):
                if not (SKIP_ALL):
                    resp = raw_input("%s exists. [s]kip, [S]kip All, [O]verwrite: "
                            % fname)
                else:
                    if (SKIP_ALL):
                        print ("skipping %s..." % fname)
                        continue
                if (resp == 's'):
                    print ("skipping %s..." % fname)
                    continue
                if (resp == 'S'):
                    SKIP_ALL = True
                    print ("skipping %s..." % fname)
                    continue
                elif (resp.lower() == 'o'):
                    print ("overwriting")
                    os.remove(fpath)
                else:
                    print("invalid input, skipping")

            # Create hard link to dot file
            print("linking %s..." % fname)
            os.link(fpath_old, fpath)
    print("done :)")



#Rename files to proper names
#symlinks = map(lambda x: '.' + x.rstrip('.symlink'), symlinks)
if __name__ == "__main__":
    install()

