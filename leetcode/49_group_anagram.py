# 49 Group Anagram

import collections

# My answer
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []

        for word in strs:
            sort = sorted(word)
            if len(result) == 0:
                result.append([word])
            else:
                add = True
                for i in range(len(result)):
                    if sort == sorted(result[i][0]):
                        result[i].append(word)
                        add = False
                        
                if add:
                    result.append([word])
        return result

sol = Solution()
# print(sol.groupAnagrams(['a']))
# -> algorithm is right but time limit exceeded

# Study book - 1. defaultDict
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    print(anagrams)
    return list(anagrams.values())
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# What about using builtin dictionary? -> key error occurs when I want to add a key that dictonary didn't added it before
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    print(anagrams)
    return list(anagrams.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
