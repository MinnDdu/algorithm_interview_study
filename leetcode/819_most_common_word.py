# 819 Most Common Word

# My answer
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = re.sub(r'[^a-zA-Z]', '@' , paragraph.lower())
        arr = paragraph.split('@')
        arr[:] = (w for w in arr if w != '')
    
        candidates = {}
        for w in arr:
            w = w.strip()
            if w in banned:
                continue
            elif w not in banned and w not in candidates: 
                candidates[w] = 1
            elif w not in banned and w in candidates:
                candidates[w] += 1
        result = [key for key, value in candidates.items() if max(candidates.values()) == value]
        print(arr)
        return result[0]
    
sol = Solution()
# print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))
# print(sol.mostCommonWord("a, a, a, a, b,b,b,c, c", ['a']))

# Study book - 1. defaultdict & regex
import collections

def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    paragraph = re.sub(r"[^\w]", ' ', paragraph.lower())

    words = [word for word in paragraph.split() if word not in banned]
    print(words)
    
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1
    
    return max(counts, key=counts.get)


# Study book - 2. Counter & most_common()
def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r"[^\w]", ' ', paragraph).lower().split() if word not in banned]
    counter = collections.Counter(words)

    return counter.most_common(1)[0][0]