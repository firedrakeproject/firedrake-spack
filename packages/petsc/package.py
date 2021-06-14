# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class Petsc(Package):
    git = 'https://github.com/firedrakeproject/petsc.git'

    version('develop', branch='firedrake', no_cache=True)

    depends_on('blas')
    depends_on('lapack')
    depends_on('mpi')
    depends_on('mumps')
    depends_on('python@3.4:', type='build')

    phases = ['configure', 'build', 'install']

    def configure_args(self):
        args = [
            '--with-cc={}'.format(self.spec['mpi'].mpicc),
            '--with-cxx={}'.format(self.spec['mpi'].mpicxx),
            '--with-fc={}'.format(self.spec['mpi'].mpifc),
            'CFLAGS={}'.format(' '.join(self.spec.compiler_flags['cflags'])),
            'FFLAGS={}'.format(' '.join(self.spec.compiler_flags['fflags'])),
            'CXXFLAGS={}'.format(' '.join(self.spec.compiler_flags['cxxflags'])),
            '--with-shared-libraries',
            '--with-blas-lib={}'.format(self.spec['blas'].libs),
            '--with-lapack-lib={}'.format(self.spec['lapack'].libs)
        ]
        return args

    def configure(self, spec, prefix):
        python('configure', '--prefix={}'.format(prefix), *self.configure_args())

    def build(self, spec, prefix):
        make('MAKE_NP={}'.format(make_jobs), parallel=False)

    def install(self, spec, prefix):
        make('install')

    def setup_build_environment(self, env):
        # configure fails if these env vars are set outside of Spack
        env.unset('PETSC_DIR')
        env.unset('PETSC_ARCH')

    def setup_run_environment(self, env):
        # Set PETSC_DIR in the module file
        env.set('PETSC_DIR', self.prefix)
        env.unset('PETSC_ARCH')

    def setup_dependent_build_environment(self, env, dependent_spec):
        # Set up PETSC_DIR for everyone using PETSc package
        env.set('PETSC_DIR', self.prefix)
        env.unset('PETSC_ARCH')
