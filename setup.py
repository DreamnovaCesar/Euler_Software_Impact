from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='CHUNKS',
  version='0.1',
  description='Multiprocessing Euler',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Cesar Eduardo Munoz Chavez',
  author_email='cesareduardomucha@hotmail.com',
  license='LICENSE.TXT', 
  classifiers=classifiers,
  keywords='Euler', 
  packages=find_packages(),
  install_requires=[''],
  where='src'
)