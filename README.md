Python Synonyms Crawler
=======================

A Python utility that fetches synonyms for a specified word.

------------------------------------------------------------------------

Installation
------------

``` sourceCode
$ pip install synonymscrawler
```

*synonymscrawler* has 3 dependencies:

-   lxml
-   requests
-   blockspring

**pip** installs the latter two along with this package.
To install the former on Windows:

-   Install the appropriate .whl file from lxml\_.
-   If you’re lucky, then there will be two files: a zip folder and a .whl file. In that case, copy the .whl file to the Scripts directory in your Python installation folder, and invoke pip on it.
-   If you’re not so lucky, then there will only be a zip folder. If you’re using a virtual environment (as you should be), then extract the zip folder, and copy the contents to \[virtual-environment-dir-name\]/Lib/site-packages.
-   Confirm successful installation via **pip list**.

------------------------------------------------------------------------

Modules
-------

### simple\_synonyms\_crawler

``` sourceCode
from synonymscrawler import simple_synonyms_crawler
simple_synonyms_crawler.crawl('adumbrate', 50)
```

Returns a list of up to N synonyms for a given word.
Here, we shall return up to 50 synonyms for “adumbrate.”

### synonyms\_crawler

``` sourceCode
from synonymscrawler import synonyms_crawler
synonyms_crawler.crawl('adumbrate', 2)
```

Returns a dictionary object, where the keys are levels, and the values are the list of synonyms at each level.
For example, the output of this code block would be:

``` sourceCode
{
    0: ['adumbrate'], 

    1: ['suggest', 'cloud', 'portend', 'intimate', 
        'bode', 'augur', 'outline', 'foretell', 
        'darken', 'obscure', 'sketch', 'indicate', 
        'mist'], 

    2: ['main features', 'skeleton', 'rough draft', 
        'characterize', 'depiction', 'survey', 
        'haze', 'tone down', 'conformation', 
        'thumbnail sketch', 'aperçu', 'skeletonize', 
        'plot', 'figure', 'line', 'cloudover', 
        'configuration', 'rough out', 'digest', 
        'compendium', 'bare facts', ...]
}
```

In other words:

{
level0: \[starting word\],
level1: \[immediate synonyms for starting word\],
level2: \[synonyms for words in level1\]
}

### blockspring\_synonyms\_crawler

SynonymsCrawler API\_

To run, download the BlockSpring CLI, and follow the instructions here\_ to test it locally.

The output should be similar to that of **synonyms\_crawler** above, except for the fact that level 0’s value will be the starting word alone, rather than a list with the starting word. In other words:

<pre>
{
       0: 'adumbrate',
       1: [adumbrate's synonyms],
       2: [synonyms of adumbrate's synonyms],
       .....
}
</pre>
–