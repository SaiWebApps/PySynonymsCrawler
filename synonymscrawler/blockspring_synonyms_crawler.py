import blockspring
import requests
from lxml import html

def _get_synonyms(word):
    '''
        Return a list of all of the synonyms of word from thesaurus.com.
        If there is an error during the retrieval process, then return None.
    '''
    ERROR_XPATH = '//li[@id="words-gallery-no-results"]'
    RESULTS_XPATH = '//div[@class="synonyms"]/div[@class="filters"]/div[@class="relevancy-block"]/div/ul/li/a/span[@class="text"]/text()'
    url = ''.join(['http://www.thesaurus.com/browse/', word])
    tree = html.fromstring(requests.get(url).text)
    return None if tree.xpath(ERROR_XPATH) else tree.xpath(RESULTS_XPATH)

def _crawl_helper(overall_results, word, current_level, max_level):
    '''
        word: initially, the level-0 or seed word that we are finding relations for;
            later on, is a word that is current_level degrees away from the original
        overall_results: dict, where the key is a word and the value is the degrees of
            separation between the key and the original word (level 0)
        current_level: keep track of the number of degrees of separation between current
            word and original word
        max_level: maximum # of degrees of separation; used as part of exit condition
    '''
    # EXIT CONDITION
    # If word is max_level degrees away from the seed word, then we're done.
    if current_level == max_level:
        return True

    # Attempt to get synonyms for the current word. If there was an error, make a
    # note in overall_results and stop recursing for this word.
    synonyms_list = _get_synonyms(word)
    if not synonyms_list:
        error_count = overall_results.get('errors', 0)
        overall_results['errors'] = error_count + 1
        return

    # Otherwise, add an entry in overall_results, where the key is word and
    # the value is the number of degrees (current_level) of separation b/w word
    # and the original seed word.
    overall_results[word] = current_level
    
    # Then, use the 1st 2 synonyms in synonyms_list to generate the next level of synonyms.
    MAX_SYNONYMS = 2
    for i, synonym in enumerate(synonyms_list):
        previous_level = overall_results.get(synonym, None)

        # Skip synonym if it is equivalent to word or if it was already encountered
        # previously, at a closer level than this one.
        if synonym == word or (previous_level is not None and previous_level <= current_level):
            continue
        # Generate synonyms for the first MAX_SYNONYMS words in the list.
        # If we encountered this synonym at a further level previously OR we are
        # done processing the first MAX_SYNONYMS words, then simply add an entry for
        # this word.
        if (previous_level is not None and previous_level > current_level) or i > MAX_SYNONYMS:
            overall_results[synonym] = current_level + 1
            continue
        _crawl_helper(overall_results, synonym, current_level + 1, max_level)


def _invert_index(orig_map):
    '''
        Essentially performs an inverted index operation on orig_map and returns
        the results. In other words, the resulting dict will use orig_map's values
        as the keys; result's values will be the list of keys in orig_map that
        correspond to each value.
    '''
    inverted_map = {}
    
    for key in orig_map:
        orig_value = orig_map[key] # Will become key of inverted_map
        inverted_values = inverted_map.get(orig_value, [])
        inverted_values.append(key) # Key becomes a value for "orig_value" in inverted_map.
        inverted_map[orig_value] = inverted_values
    
    return inverted_map

    
def crawl(word, max_num_levels):
    '''
        Return a dict where the key is an integer level (representing the
        number of degrees of separation from "word") and the value is the
        list of words that are key-degrees from word.
        Notes:
            - Here, "degrees of separation" is a measure of how closely related "word" 
            is to some other word.
            - Keys in the result dict will be integers between 0 and max_num_levels inclusive.
    '''
    if not max_num_levels:
        return {'0': word} if _get_synonyms(word) else None

    word_level_map = {}
    
    # Populate word_level_map with {key: related-word, value: level-num < max_num_levels}.
    _crawl_helper(word_level_map, word, 0, max_num_levels)
    if len(word_level_map) == 1 and "errors" in word_level_map: # No results, only errors
        return None
    # Otherwise, reorganize the map so that the keys -> level, values -> list of words at that level.
    return _invert_index(word_level_map)


def block(request, response):
    # Required parameters: word & max_degrees_of_separation
    word = request.params.get('word', None)
    max_degrees_of_separation = request.params.get('max_degrees_of_separation', -1)

    # If required parameters are not present, error out.
    if not word or max_degrees_of_separation < 0:
        response.addErrorOutput('Input Error', 'Please specify a valid word and a positive degrees of separation.')
        response.end()
        return

    # Otherwise, forward crawler results to the response.
    crawler_results = crawl(word, max_degrees_of_separation)
    if not crawler_results:
        response.addErrorOutput('Error', 'No results found for specified word.')
        response.end()
        return
    for level in crawler_results:
        response.addOutput(level, crawler_results[level])
    response.end()

blockspring.define(block)