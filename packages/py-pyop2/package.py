from spack import *

class PyPyop2(PythonPackage):
    """ """

    homepage = "https://github.com/OP2/PyOP2"
    url      = "https://github.com/OP2/PyOP2"
    git='https://github.com/OP2/PyOP2'
    
    version('master', branch='master')
    version('testing', branch='connorjward/fix-get-petsc-dir')

    phases = ['build_ext', 'install']
    
    depends_on('py-setuptools', type="build")
    depends_on('py-pytest', type="build")
    depends_on('py-flake8', type="build")
    depends_on('py-decorator')
    depends_on('py-cython')
    depends_on('py-numpy')
    depends_on('py-mpi4py')
    
    depends_on('firedrake.petsc@main')
    depends_on('firedrake.py-petsc4py@main')

    depends_on('firedrake.py-coffee')

    depends_on('firedrake.py-loopy@firedrake')

    
    # @run_before('build_ext')
    # def fixme(self):
    #     filter_file(r'packages=\[\'pyop2\'\]', 'packages=[\'pyop2\',\'pyop2.codegen\']', 'setup.py')
        #with open('setup.py', 'r') as ff :
        #    print( ff.read() )
