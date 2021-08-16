Spack repository containing packages for installing [Firedrake](https://firedrakeproject.org)
and applications depending on Firedrake such as [Irksome](https://github.com/firedrakeproject/Irksome/)
and [icepack](https://github.com/icepack/icepack/).

## Installation instructions

To install Firedrake you should run:

```bash
$ spack repo add <this directory>
$ spack env create -d <env directory>
$ spack env activate <env directory>
$ spack add py-firedrake@develop
$ spack install
```
