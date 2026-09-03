class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for word in s:
            count[word] = count.get(word, 0) + 1
        for word in t:
            count[word] = count.get(word, 0) - 1

        for value in count.values():
            if value != 0:
                return False

        return True