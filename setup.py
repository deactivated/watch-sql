import os.path

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='watch_sql',
      version="0.1",
      author="Mike Spindel",
      author_email="mike@spindel.is",
      license="MIT",
      keywords="mysql pcap packet capture",
      url="http://github.com/deactivated/watch-sql",
      description='',
      install_requires=[
          'dpkt', 'pcap', 'sqlparse', 'pygments'],
      scripts=['bin/watch_sql'],
      packages=find_packages(),
      long_description=read('README.rst'),
      zip_safe=False,
      classifiers=[
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Programming Language :: Python"])
