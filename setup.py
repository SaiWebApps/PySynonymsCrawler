from setuptools import setup, find_packages
from codecs import open
from os import path

# Constants
README_FILE = 'README.rst'
VERSION = '0.9'
README_PATH = path.join(path.abspath(path.dirname(__file__)), README_FILE)

# Load README file's contents into "readmeContents."
with open(README_PATH, encoding = 'utf-8') as rf:
  readmeContents = rf.read()


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