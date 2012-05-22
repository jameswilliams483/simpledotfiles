import os
from simpledotfiles.settings import *

__all__ = ("_collect_files",)

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
