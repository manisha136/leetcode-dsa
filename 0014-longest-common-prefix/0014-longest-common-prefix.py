class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in range(len(min(strs))):
            for j in range(len(strs)):
                current=strs[j][i]
                if current!=strs[0][i]:
                    return strs[0][:i]
        return min(strs,key=len)           

        