import os
import sys

def clean(hard=False):
    for filename in os.listdir('planes'):
        os.remove(filename)
    for filename in os.listdir('meshes'):
        os.remove(filename)
    if hard:
        for filename in os.listdir('results'):
            os.remove(filename)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'hard':
            clean(hard=True)
    else:
        clean()