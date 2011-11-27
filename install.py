#!/usr/bin/env pyhton2.7
import os

def _get_symlinks():
    """
    Get all files ending in .symlink from dirs
    Doesn't follow symbolic links
    @return:
    List of tuples (path, [files])
    eg.
    [(path, [ foo.symlink]), (...),...]
    """
    out = []
    walker = os.walk(".")
    #OPTIMIZE: exclude directories? 
    for path, directory, files in walker:
        symlinks = filter(lambda x: x.rfind(".symlink") >= 0, files)
        if (symlinks):
            out.append((path, symlinks))
    return out

def install(args = None):
    """
    Install dotfiles in computer
    """
    symlinks = _get_symlinks()
    for path, links in symlinks:
        for link in links:
            fname = "." + link.rstrip(".symlink")
            print("linking %s..." % fname)
            fpath_old = os.path.join(path, link)
            fpath = os.path.join(os.path.expanduser('~'), fname)
            if (os.path.exists(fpath)):
                resp = raw_input("%s exists. [S]kip, [O]verwrite: " % fname)
                if (resp.lower() == 's'):
                    print ("skipping")
                    continue
                elif (resp.lower() == 'o'):
                    print ("overwriting")
                    os.remove(fpath)
                else:
                    print("invalid input, skipping")
            # Create hard link to dot file
            os.link(fpath_old, fpath)
        print("done :)")



#Rename files to proper names
#symlinks = map(lambda x: '.' + x.rstrip('.symlink'), symlinks)
            

