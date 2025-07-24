def group_anagrams(words):
	anagram_dict = {}
	for word in words:
		sorted_word = ''.join(sorted(word))
            
		if sorted_word in anagram_dict:
			anagram_dict[sorted_word].append(word)
            
		else:
			anagram_dict[sorted_word] = [word]
                  
	return list(anagram_dict.values())


words = ['lump', 'eat', 'me', 'tea', 'em', 'plum']
print(group_anagrams(words))

'''Time Complexity: O(n * klogk), where n is the number of words in the list and k is the length of the longest word.

Auxiliary Space: O(n*k), as we are using a dictionary to store the anagrams.'''

            

def groupAnagrams(strs):
    res = {}
    for s in strs:
        count = [0] * 26 # a .... z
        for c in s:
            count[ord(c) - ord("a")] += 1
            print(count)
        key = tuple(count)
        
        if key in res:
            res[key].append(s)
            print("yes",res)
            
        else:
            res[key] = [s]
            print("no",res)
            
    
    return list(res.values())

strs = ["eat","tea","tan","ate","nat","bat"]
#print(groupAnagrams(strs))
