from distutils.core import setup

VERSION = 0.8

setup(
  name = 'synonymscrawler',
  packages = ['synonymscrawler'],
  version = VERSION,
  description = 'Python Synonyms Crawler Implementation',
  author = 'Sairam Krishnan',
  author_email = 'sairambkrishnan@gmail.com',
  license = 'MIT',
  install_requires = [
  	'blockspring',
  	'requests'
  ],
  url = 'https://github.com/SaiWebApps/PySynonymsCrawler',
  download_url = 'https://github.com/SaiWebApps/PySynonymsCrawler/tarball/' + VERSION,
  keywords = ['Python', 'synonyms-crawler', 'web-scraping', 'text-parsing']
)