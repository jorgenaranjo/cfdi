import setuptools


setuptools.setup(setup_requires=['pbr'],
                 pbr=True,
                 test_suite="cfdi.test",
                 package_data={'': ['*.yaml']})
