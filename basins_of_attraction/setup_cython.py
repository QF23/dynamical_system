'''
program:       setup_cython.py
author:        tc
last-modified: 2015-04-16
description:   compiles a cython module
notes:         to be executes through
               $ python setup_cython.py build_ext --inplace
'''

from distutils.extension import Extension
from Cython.Distutils import build_ext
from distutils.core import setup
import glob

if __name__ == '__main__':
    for lib in glob.glob('*.pyx'):
        print 'compiling %s' % lib
        basename = lib[:-4]
        ext_modules = [Extension(basename, [basename + '.pyx'],
                                 libraries=['gsl', 'gslcblas'])]
        # compiler directive which allows you to use pydoc
        for  e  in  ext_modules:
            e.pyrex_directives  =  {'embedsignature': True}
        # compiling
        setup(cmdclass={'build_ext': build_ext},
              ext_modules = ext_modules)
        print 'done'
