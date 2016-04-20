#!/bin/python3
import sys
import zlib
from wrpg.wmap import pack


def usage(argv):
    print("Usage : {} file out_filename".format(argv[0]))


def main(argv):
    data = pack.pack(argv[1])
    with open(argv[2], 'wb+') as f:
        f.write(data)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage(sys.argv)
        exit()
    main(sys.argv)
