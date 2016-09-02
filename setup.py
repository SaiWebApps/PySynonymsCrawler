from distutils.core import setup

setup(
  name = 'synonymscrawler',
  packages = ['synonymscrawler'],
  version = '0.4',
  description = 'Python Synonyms Crawler Implementation',
  author = 'Sairam Krishnan',
  author_email = 'sairambkrishnan@gmail.com',
  license = 'MIT',
  install_requires = [
  	'blockspring',
  	'requests'
  ],
  url = 'https://github.com/SaiWebApps/SynonymsCrawler',
  download_url = 'https://github.com/SaiWebApps/SynonymsCrawler/tarball/0.4',
  keywords = ['Python', 'synonyms-crawler', 'web-scraping', 'text-parsing']
)