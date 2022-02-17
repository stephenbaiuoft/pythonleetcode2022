from black import main

from pyleetcode.string.kmp import KMP


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len1 = len(haystack)
        len2 = len(needle)
        if len1 < len2:
            return -1
        # this is "a" and "a" same size, we'd still need 0
        for i in range(len1 - len2 + 1):
            # for python even i > len(haystack) in array index no issue
            # it's just empty
            if haystack[i : i + len2] == needle:
                return i
        return -1


if __name__ == "__main__":

    k = KMP()
    k.match("mississippi", "issip")
    # s.strStr("mississippi", "issip")
