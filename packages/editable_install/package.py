import inspect
from spack import *
from spack.package_base import PackageBase


class EditablePythonPackage(PythonPackage):
    def install(self, spec, prefix):
        '''Perform an editable install if `spack develop package` has been run.
        '''
        with working_dir(self.build_directory):
            if 'dev_path' in self.spec.variants:
                args = PythonPackage._std_args(self)
                args += ['--prefix=' + prefix]
                args += ['-e', self.spec.variants['dev_path'].value]
                pip = inspect.getmodule(self).pip
                pip(*args)
            else:
                super().install(spec, prefix)

    def setup_run_environment(self, env):
        if 'dev_path' in self.spec.variants:
            env.append_path('PYTHONPATH', self.spec.variants['dev_path'].value)

    def setup_dependent_run_environment(self, env, dependent_spec):
        if 'dev_path' in self.spec.variants:
            env.append_path('PYTHONPATH', self.spec.variants['dev_path'].value)


class EditableInstall(PackageBase):
    '''Dummy package, we don't actually want to install this!
    '''
    pass
