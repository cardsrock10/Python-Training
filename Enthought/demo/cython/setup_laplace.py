from setuptools import setup, Extension
from Cython.Distutils import build_ext

import numpy

ext = Extension("pyx_lap", ["pyx_lap.pyx"],
                include_dirs = [numpy.get_include()])
setup(
  name = "CythonGuide",
  ext_modules=[ext],
  cmdclass = {'build_ext': build_ext}
)
