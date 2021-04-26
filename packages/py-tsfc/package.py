from spack import *

class PyTsfc(PythonPackage):
    """ """

    homepage = "https://github.com/firedrakeproject/tsfc"
    url      = "https://github.com/firedrakeproject/tsfc"
    git='https://github.com/firedrakeproject/tsfc'
    
    version('master', branch='master')

    #depends_on('py-setuptools', type="build")
    depends_on('py-numpy')

    depends_on('firedrake.py-coffee')                        
    depends_on('firedrake.py-fiat')
    depends_on('firedrake.py-finat')
    depends_on('firedrake.py-ufl')

