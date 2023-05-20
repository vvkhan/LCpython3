#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
#Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

def longestCommonPrefix(strs):
    minLen = 201
    for i in strs:
        if 0 <= len(i) <= 200 and len(i) < minLen:
            minLen = len(i)

    res = ""
    if 1 <= len(strs) <= 200 and minLen <= 200:
        for i in range(minLen):
            common = strs[0][i]
            flag = True
            for s in range(1, len(strs)):
                if strs[s][i] != common:
                    flag = False
                    return res
            res = res + common
    return res

resStr1 = longestCommonPrefix(["flower","flow","flight"])
print(resStr1)
resStr2 = longestCommonPrefix(["dog","racecar","car"])
print(resStr2)
resStr3 = longestCommonPrefix(["carpet", "car", "cannon"])
print(resStr3)
resStr4 = longestCommonPrefix(["cir", "car"])
print(resStr4)