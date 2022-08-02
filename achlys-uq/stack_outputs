#!/usr/bin/env python3

''' This script stacks Achlys output files in the current directory. Since
earlier Achlys processes have longer file names, it stacks them according 
to the file name length, using the longest name first. Simulation times of
later output files are adjusted accordingly.
'''

__author__ = 'Mikkel Bue Lykkegaard'
__copyright__ = 'Copyright 2022, digiLab'
__credits__ = ['Mikkel Bue Lykkegaard', 'Tim Dodwell', 'Freddy Wordingham']
__license__ = 'MIT'
__version__ = '0.1'
__maintainer__ = 'Mikkel Bue Lykkegaard'
__email__ = 'mikkel@digilab.co.uk'
__status__ = "Development"

import argparse
import glob
import pandas as pd

parser = argparse.ArgumentParser(description='Stack Achlys output files')
parser.add_argument('-o', '--outfile', dest='outfile', type=str, default='ogorodnikova.csv',
                    help='An output file name (default: "ogorodnikova.csv")')
args = parser.parse_args()

files = glob.glob("*.csv"); files.sort(key=len, reverse=True)

dfs = []

for f in files:
    print('Processing {}...'.format(f))
    dfs.append(pd.read_csv(f))

for i in range(1, len(dfs)):
    dfs[i] = dfs[i].drop(0)
    dfs[i]['time'] += dfs[i-1]['time'].iloc[-1]

print('Writing {}...'.format(args.outfile))
pd.concat(dfs, ignore_index=True).to_csv(args.outfile, index=False)
