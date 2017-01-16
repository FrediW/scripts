#!/usr/bin/env python

import sys

x = {}

# order: full block, double slab, slab, slab inverted, stairs 0-7
x['jungle'] = ['5:3', '125:3', '126:3', '126:11', '136:0', '136:1', '136:2', '136:3', '136:4', '136:5', '136:6', '136:7']
x['cobble'] = [  '4',  '43:3',  '44:3',  '44:11',  '67:0',  '67:1',  '67:2',  '67:3',  '67:4',  '67:5',  '67:6',  '67:7']
x['oak'] =    [  '5',   '125',   '126',  '126:8',  '53:0',  '53:1',  '53:2',  '53:3',  '53:4',  '53:5',  '53:6',  '53:7']

x['sprucelog'] = ['17:1', '17:5', '17:9', '17:13']
x['oaklog'] = ['17:0', '17:4', '17:8', '17:12']

source = x[sys.argv[1]]
target = x[sys.argv[2]]

if len(target) != len(source):
  print "Incompatible transformation"
  exit -1
  
macro = []

for i in range(0, len(source)):
  macro.append('//replace ' + source[i] + " " + target[i])

print '|'.join(macro)


