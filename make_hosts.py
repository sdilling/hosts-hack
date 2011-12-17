#!/usr/bin/python

import sys
import shutil
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-f', '--file', dest='filename', help='change name of output file', metavar='FILE')
(options, args) = parser.parse_args()
f = open('data/plain-hosts')
if options.filename:
    file = options.filename
else:
    file = 'data/new-hosts'
out = open(file, 'w')
if args.count > 0:
    # get parameter host file
    print args
for line in f:
    out.write(line)
out.close()
#shutil.copyfile(file, '/etc/hosts')
