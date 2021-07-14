**IMPORTANT**

I have not yet managed to get this working quite yet. See `TODO.md` for outstanding tasks.

---

To add this repository to spack run (from the repository root)

```bash
$ spack repo add .
```

## Using the Firedrake fork of PETSc

To get PETSc to clone from the Firedrake fork we apply a patch to the upstream `package.py` file from Spack.
To regenerate the `package.py` in this repository run the `rebase-petsc` script.

## Current workflow

```bash
$ spack repo add <this directory>
$ spack env create -d <env directory>
$ spack env activate <env directory>
$ spack add py-firedrake@develop
$ spack develop py-firedrake@develop (this will not work)
$ spack install --fail-fast
```
