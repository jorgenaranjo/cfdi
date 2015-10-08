import setuptools


setuptools.setup(setup_requires=['pbr'],
                 pbr=True,
                 test_suite="invoice.test",
                 package_data={'': ['*.yaml']})
