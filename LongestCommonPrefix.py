#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
#Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

def longestCommonPrefix(strs):
    res = ""
    common = ""
    minLen = shortestStr(strs)

    if 1 <= len(strs) <= 200 and minLen <= 200:
        for i in range(minLen):
            common = strs[0][i]
            flag = 1
            for s in range(1, len(strs)):
                if strs[s][i] != common:
                    flag = 0
            if flag == 1:
                res = res + common
    return res

def shortestStr(strs):
    l = 201
    for i in strs:
        if 0 <= len(i) <= 200 and len(i) < l:
            l = len(i)
    return l

resStr1 = longestCommonPrefix(["flower","flow","flight"])
print(resStr1)
resStr2 = longestCommonPrefix(["dog","racecar","car"])
print(resStr2)