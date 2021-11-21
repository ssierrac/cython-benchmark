from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy

extensions = [
    Extension("heat_py", 
        ["heat.py"],
    ),
    Extension("heat_cy", 
        ["cyheat.pyx"],
    )
]

setup(
    name="heat_cyt",
    ext_modules=cythonize(
        extensions,
        compiler_directives={'language_level' : "3"},
        include_path=[numpy.get_include()],
        annotate=True
        ),
)
