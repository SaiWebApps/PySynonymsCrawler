import requests
from lxml import html

def _get_synonyms(word):
	'''
		Fetch and return a list of word's synonyms from Thesaurus.com.
		If info retrieval fails, then return an empty list.
	'''
	XPATH = '//div[@class="synonyms"]/div[@class="filters"]/div[@class="relevancy-block"]/div/ul/li/a/span[@class="text"]/text()'
	url = ''.join(['http://www.thesaurus.com/browse/', word])
	tree = html.fromstring(requests.get(url).text)
	return tree.xpath(XPATH)


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
	# EXIT CONDITION - If word is max_level degrees away from the seed word, then we're done.
	if current_level == max_level:
		return

	# Otherwise, add an entry in overall_results, where the key is word and
	# the value is the number of degrees (current_level) of separation b/w word
	# and the original seed word.
	overall_results[word] = current_level

	# Repeat this process for each of word's synonyms.
	MAX_SYNONYMS = 2
	for i, synonym in enumerate(_get_synonyms(word)):
		# Skip synonym if it is equivalent to word or if it was already encountered
		# previously (at an earlier level).
		if synonym == word or synonym in overall_results:
			continue
		if i > MAX_SYNONYMS:
			overall_results[synonym] = current_level + 1
			continue
		_crawl_helper(overall_results, synonym, current_level + 1, max_level)


def crawl(word, max_num_levels):
	'''
		Return a dict where the key is an integer level (representing the
		number of degrees of separation from "word") and the value is the
		list of words that are key-degrees from word.
		Notes: 
			- Here, "degrees of separation" is a measure of how closely related 
			"word" is to a synonym. 
			- Keys in the output dict will be integers in [0, max_num_levels].
	'''
	word_level_map = {}
	level_word_list_map = {}

	# Populate word_level_map with {key: related-word, value: level-num < max_num_levels}.
	_crawl_helper(word_level_map, word, 0, max_num_levels)
	# Now, in level_word_list_map, the key will be a level between 0 and max_num_levels inclusive,
	# and the value will be all of the words in word_level_map that belong to this level.
	# Essentially, perform an inverted-index operation.
	for word in word_level_map:
		level = word_level_map[word]
		word_list = level_word_list_map.get(level, [])
		word_list.append(word)
		level_word_list_map[level] = word_list

	return level_word_list_map