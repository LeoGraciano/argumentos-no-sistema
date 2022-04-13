#!/user/bin/env python3
import sys
import os

args = sys.argv
qt_args = len(args)

if qt_args <= 1:
    print('Faltando argumentos:')
    print('-l', 'Para Lista todos os aquivos nessa pasta', sep='\t')
    print('-d', 'Para Lista todos os diretorios nessa pasta', sep='\t')

only_files = False
if '-l' in args:
    only_files = True

only_directories = False
if '-d' in args:
    only_directories = True


for file in os.listdir('.'):
    if only_files and os.path.isfile(file):
        print('--FILE', file, sep='\n')

    if only_directories and os.path.isdir(file):
        print('--DIR', file, sep='\n')
