#!/usr/bin/env python2.7
import argparse
import sys
import os
#TODO: deal with special cases in a specials directory
# eg. vim files, try to save current vim config in a local file
#TODO: save logs somewhere
#TODO: add ability to preview file during command prompt

__version__ = '0.0.1'

# Files in here won't be symlinked. Assumes unique directory names
IGNORE = ['.git']
OVERWRITE_ALL = False
SKIP_ALL = False
#TODO: change this to automatic
CUSTOM = ['vim']

p = argparse.ArgumentParser(description="dotfiles installer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument('-c', '--confirm', default = False, action = 'store_true',
            help="ask for confirmation before linking")



def _collect_files(pattern):
    """
    Collect all files by searching recursively via current directory.
    Will ignore files in IGNORE
    @params:
    pattern to search for
    @return:
    List of tuples (path, [files])
    eg.
    [(path, [ foo.symlink]), (...),...]
    """
    #TODO(high): not sure if this works
    global IGNORE
    out = []
    walker = os.walk(".")
    for path, directory, files in walker:
        for inum, dname in enumerate(directory):
            if (dname in IGNORE): del directory[inum]
        symlinks = filter(lambda x: x.endswith(pattern), files)
        if (symlinks):
            out.append((path, symlinks))
    return out


#OPTIMIZE: cache these results
def _get_symlinks():
    """
    Get all files ending in .symlink
    @return:
    List of tuples (path, [files])
    eg.
    [(path, [ foo.symlink]), (...),...]
    """
    print ("gathering symlinks...")
    res = _collect_files("symlink")
    return res

def install(args = None):
    """
    Install dotfiles in computer
    """
    global SKIP_ALL
    global OVERWRITE_ALL
    CONFIRM = args.confirm
    import pdb
    pdb.set_trace()

    symlinks = _get_symlinks()

    for path, links in symlinks:
        for link in links:
            fname = "." + link.rstrip(".symlink")
            fpath_old = os.path.join(path, link)
            fpath = os.path.join(os.path.expanduser('~'), fname)

            flag_create = True
            #SC: Handle file collision
            if (os.path.exists(fpath)):
                if (SKIP_ALL):
                    flag_create = False
                else:
                    resp = raw_input("%s exists. [s]kip, [S]kip All, [O]verwrite: "
                            % fname)
                    if (resp == 's'):
                        flag_create = False
                    if (resp == 'S'):
                        SKIP_ALL = True
                        flag_create = False
                    elif (resp.lower() == 'o'):
                        print ("overwriting...")
                        os.remove(fpath)
                    else:
                        print("invalid input, skipping")
                        flag_create = False

            # Confirmation before creating
            if (CONFIRM):
                resp = None
                while (resp not in ["y", "n"]):
                    resp = raw_input("do you want to create %s? [y]es, [n]o" % fname)
                if (resp == 'y'):
                    flag_create = False

            # Create hard link to dot file
            if (flag_create):
                print("linking %s..." % fname)
                try:
                    os.link(fpath_old, fpath)
                except OSError:
                    # Broken symlink
                    if (os.path.lexists(fpath)):
                        os.remove(fpath)
                    # Try linking again
                    os.link(fpath_old, fpath)
            else:
                print("skipping %s" % fname)
    print("done :)")

def main():
    args = p.parse_args(sys.argv[1:])
    install(args)


#Rename files to proper names
#symlinks = map(lambda x: '.' + x.rstrip('.symlink'), symlinks)
if __name__ == "__main__":
    main()

