from setuptools import setup, find_packages

setup(name='SHICTHRSWMICManager',
      version='1.0.0',
      description='SHICTHRS WMIC Manager',
      url='https://github.com/JNTMTMTM/SHICTHRS_WMICManager',
      author='SHICTHRS',
      author_email='contact@shicthrs.com',
      license='GPL-3.0',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['colorama==0.4.6'],
      zip_safe=False)
