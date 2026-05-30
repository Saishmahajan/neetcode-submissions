class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join([x for x in s if x.isalnum()]).lower()
        print(s2)
        s3 = s2[::-1]
        if s2 == s3:
                return True
        else:
                return False