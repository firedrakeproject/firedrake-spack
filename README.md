To add this repository to spack run (from the repository root)

```bash
$ spack repo add .
```

## Using the Firedrake fork of PETSc

To get PETSc to clone from the Firedrake fork we apply a patch to the upstream `package.py` file from Spack.
To regenerate the `package.py` in this repository run the `rebase-petsc` script.
