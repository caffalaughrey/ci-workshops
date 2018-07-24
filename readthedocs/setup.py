from setuptools import setup
setup(name='ReadthedocsExample',
      version='0.1.0',
      description='A workshop for readthedocs.io',
      url='https://github.com/caffalaughrey/ci-workshops',
      author='Aaron Caffrey',
      author_email='acaffrey@salesforce.com',
      license='MIT',
      packages=['ReadthedocsExample'],
      package_dir = {'ReadthedocsExample': 'src'},
      zip_safe=False,
      install_requires=[
          'pytest',
          'pytest-runner',
          'responses',
          'sphinx'],
      tests_require=['pytest']
      )
