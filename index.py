# -*- coding: utf-8 -*-

import os
import sys


def convert_human_readable_size_to_byte(hs):
    return int(hs)


def create_sample_file(s, p):
    if os.path.exists(p):
        raise ValueError("File %s has exist" % p)

    with open(p, 'w+b') as f:
        for i in range(0, s):
            f.write('x')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "invalid arguments, sample: python index.py sample.data 1M"
    else:
        p = sys.argv[1]
        size = convert_human_readable_size_to_byte(sys.argv[2])
        try:
            create_sample_file(size, p)
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print sys.exc_info()[2]
