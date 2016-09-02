from setuptools import setup, find_packages
from os import path

import pypandoc

# Constants
README_FILE = 'README.md'
THIS_DIR_ABS_PATH = path.abspath(path.dirname(__file__))
README_ABS_PATH = path.join(THIS_DIR_ABS_PATH, README_FILE)
VERSION = '0.91'

# Load README file's contents into "readmeContents."
try:
  readmeContents = pypandoc.convert(README_ABS_PATH, 'rst')
except:
  # If pandoc hasn't been installed on the system, then install it
  # first and then try to convert REAMDE.md to rst format.
  pypandoc.pandoc_download.download_pandoc()
  readmeContents = pypandoc.convert(README_ABS_PATH, 'rst')

# Package Config
setup(
  name = 'synonymscrawler',
  packages = ['synonymscrawler'],
  version = VERSION,
  description = 'Python Synonyms Crawler Implementation',

  # So that PyPI page will display README contents.
  # Prereq: Contents must in RST format.
  long_description = readmeContents,

  # Author details
  author = 'Sairam Krishnan',
  author_email = 'sairambkrishnan@gmail.com',
  
  # MIT License (LICENSE file)
  license = 'MIT',
  
  # Dependencies
  install_requires = [
  	'blockspring',
  	'requests'
  ],
  
  # GitHub Repo URLs
  url = 'https://github.com/SaiWebApps/PySynonymsCrawler',
  download_url = 'https://github.com/SaiWebApps/PySynonymsCrawler/tarball/' + VERSION,
 
  keywords = ['Python', 'synonyms-crawler', 'web-scraping', 'text-parsing']
)