from spack import *

class PyFinat(PythonPackage):
    """FInAT is not a tabulator """

    homepage = "https://github.com/FInAT/FInAT"
    url      = "https://github.com/FInAT/FInAT"
    git='https://github.com/FInAT/FInAT'
   
    version('master', branch='master')

    #depends_on('py-setuptools', type="build")
    #depends_on('py-wheel', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-sympy', type=("build","run"))
