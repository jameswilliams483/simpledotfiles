import os
import unittest

from simpleutils import utils as sutils
from simpledotfiles.utils import *

from os.path import join

TEMP_DIR = "tmp"
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
TEST_FILES = ["foo.symlink", "bar.symlink", "foobar"]

class TestMain(unittest.TestCase):
    def setUp(self):
        os.mkdir(TEMP_DIR)
        sutils.touch(join(TEMP_DIR, "foo.symlink"))
        sutils.touch(join(TEMP_DIR, "bar.symlink"))
        sutils.touch(join(TEMP_DIR, "foobar"))

    def test_basic(self):
        print("testing basics...")
        res = _collect_files("symlink")
        self.assertEquals(res, [('./tmp', ['bar.symlink', 'foo.symlink'])])
        print(res)

    def tearDown(self):
        os.remove(join(TEMP_DIR, "foo.symlink"))
        os.remove(join(TEMP_DIR, "bar.symlink"))
        os.remove(join(TEMP_DIR, "foobar"))
        os.rmdir(TEMP_DIR)

if __name__ == '__main__':
    unittest.main()
