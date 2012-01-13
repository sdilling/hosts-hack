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
for line in f:
    out.write(line)
if len(args) > 0:
    # get parameter host file
    g = open('data/'+args[0]+'-hosts')
    for line in g:
        out.write(line)
out.close()

shutil.copyfile(file, '/etc/hosts')
