class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s2 = "".join([x for x in s if x.isalnum()]).lower()
        # print(s2)
        # s3 = s2[::-1]
        # if s2 == s3:
        #         return True
        # else:
        #         return False

        s2 = "".join([x for x in s if x.isalnum()]).lower()

        l, r = 0, len(s2)-1
        while l < r:
                if s2[l]!= s2[r]:
                        return False
                l += 1
                r -= 1
        return True
                

# s2 = ''
# print(s[::-1])
# for str in s:
#     if str.isalnum():
#         s2.join('')
# print(s2)