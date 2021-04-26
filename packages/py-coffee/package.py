from spack import *

class PyCoffee(PythonPackage):
    """ """

    homepage = "https://github.com/coneoproject/COFFEE"
    url      = "https://github.com/coneoproject/COFFEE"
    git='https://github.com/coneoproject/COFFEE'
    
    version('master', branch='master')
    
    depends_on('py-setuptools', type="build")
    depends_on('py-pulp')
    depends_on('py-numpy')
    depends_on('py-networkx')
    depends_on('py-six')