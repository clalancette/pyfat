import pytest
import subprocess
import os
import sys

prefix = '.'
for i in range(0,3):
    if os.path.exists(os.path.join(prefix, 'pyfat.py')):
        sys.path.insert(0, prefix)
        break
    else:
        prefix = '../' + prefix

import pyfat

from common import *

def do_a_test(tmpdir, outfile, check_func):
    testout = tmpdir.join("writetest.img")

    # Now open up the ISO with pyiso and check some things out.
    fat = pyfat.PyFat()
    with open(str(outfile), 'rb') as fp:
        fat.open(fp, os.fstat(fp.fileno()).st_size / 1024)
        check_func(fat, os.fstat(fp.fileno()).st_size)

        with open(str(testout), 'wb') as outfp:
            fat.write(outfp)
        fat.close()

    # Now round-trip through write.
    fat2 = pyfat.PyFat()
    with open(str(testout), 'rb') as fp:
        fat2.open(fp, os.fstat(fp.fileno()).st_size / 1024)
        check_func(fat2, os.fstat(fp.fileno()).st_size)
        fat2.close()

def test_parse_nofiles(tmpdir):
    indir = tmpdir.mkdir("nofiles")
    outfile = str(indir) + ".img"
    subprocess.call(["mkfs.msdos", "-C", str(outfile), "1440"])

    do_a_test(tmpdir, outfile, check_nofiles)