from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='geomarea',
  version='0.0.1',
  description='A calculator of an area of a figure',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  url='',  
  author='v.laso',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='area, circle, triangle', 
  packages=find_packages(),
  install_requires=[''] 
)