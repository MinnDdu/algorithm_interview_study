# 937 Reorder Log Files

# My answer
class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        result = []
        i = 0
        for l in range(len(logs)):
            if logs[i].split()[1].isalpha():
                result.append(logs.pop(i))
            else:
                i += 1
        if len(result) == 0:
            return logs
        else:
            for i in range(0, len(result) - 1):
                minimum_index = i
                for j in range(i+1, len(result)):
                    # when letter identifier & contents are different
                    if result[j][result[j].find(' ')+1:] < result[minimum_index][result[minimum_index].find(' ')+1:]:
                        minimum_index = j
                    # when letter identifier & contents are the saem
                    elif result[j][result[j].find(' ')+1:] == result[minimum_index][result[minimum_index].find(' ')+1:] and \
                        result[j][:result[j].find(' ')] < result[minimum_index][:result[minimum_index].find(' ')]:
                        minimum_index = j
                if minimum_index != i:
                    result[i], result[minimum_index] = result[minimum_index], result[i]
        print(result)
        print(logs)
        print(result + logs)
        return result + logs
    
sol = Solution()
print(sol.reorderLogFiles(["zoey i love you","lucas i love you","rong i love you"]))