from spack import *

class PyPyop2(PythonPackage):
    """ """

    homepage = "https://github.com/OP2/PyOP2"
    url      = "https://github.com/OP2/PyOP2"
    git='https://github.com/OP2/PyOP2'
    
    version('develop', branch='connorjward/fix-get-petsc-dir')

    phases = ['install']
    
    depends_on('py-setuptools', type="build")
    depends_on('py-pytest', type="build")
    depends_on('py-flake8', type="build")
    depends_on('py-decorator')
    depends_on('py-cython')
    depends_on('py-numpy')
    depends_on('py-mpi4py')
    
    depends_on('firedrake.petsc')
    depends_on('firedrake.py-petsc4py')

    depends_on('firedrake.py-coffee')

    depends_on('firedrake.py-loopy')

    phases = ['install']

    def install(self, *_):
        # Do an editable install if `spack develop firedrake` has been run.
        if 'dev_path' in self.spec.variants:
            self.setup_py('develop')
        else:
            self.setup_py('install')
