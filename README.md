Spack repository containing packages for installing [Firedrake](https://firedrakeproject.org)
and some applications that depend on Firedrake:
 - [Gusto](https://firedrakeproject.org/gusto/)
 - [icepack](https://icepack.github.io/)
 - [Irksome](https://firedrakeproject.github.io/Irksome/)
 - [Thetis](https://thetisproject.org/)


## Installation instructions
While the spack based installation is under evaluation please refer to
the detailed install instructions [here](https://hackmd.io/@TzVnFeL0TMCb3FaAi9qYBA/ByaRskMQ5).

If you have already read those instructions, here is a quick reference:
To install Firedrake you should run:

```bash
$ spack repo add <this directory>
$ spack env create -d firedrake
$ spack env activate firedrake
$ spack add py-firedrake@develop %gcc ^mpich ^openblas
$ spack install
```

You can specify a different compiler, MPI distribution and BLAS provider.


## Install script
There is an experimental minimal install script that can add all the
development packages. Usage:
```bash
./spack_install_script.sh directory_name spec_to_install
```

To perform the installation above:
```bash
./spack_install_script.sh firedrake py-firedrake@develop %gcc ^mpich ^openblas
```

### Other tested configurations
Note that in each case the compiler must be installed and registered
correctly with Spack before attempting to run the command.

Standard GCC 11.2 with Openblas, MPICH 4.0.2 and Python 3.10.4:
```bash
./spack_install_script.sh standard_firedrake py-firedrake@develop %gcc@11.2.0 ^python@3.10.4 ^openblas ^mpich@4.0.2
```

Using the AMD toolchain:
```bash
./spack_install_script.sh amd_firedrake py-firedrake@develop %aocc@3.2.0  ^python@3.10.4 ^amdblis ^amdlibflame ^amdscalapack ^mpich
```

Using the Intel toolchain:
```bash
./spack_install_script.sh intel_firedrake py-firedrake@develop %intel@2021.5.0 ^python@3.10.4 ^intel-oneapi-mkl ^intel-oneapi-mpi
```

Using the LLVM clang compiler:
```bash
./spack_install_script.sh clang_firedrake py-firedrake@develop %clang@13.0.0 ^openblas ^mpich
```

NVidia toolchain (`nvhpc`) is WIP.
