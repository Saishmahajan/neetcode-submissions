class Solution:
    def findMedianSortedArrays(self,nums1, nums2):

    # Always take the smaller array as A
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A, B = nums1, nums2
        m, n = len(A), len(B)

        left, right = 0, m

        while left <= right:

            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            maxLeftA = float('-inf') if partitionA == 0 else A[partitionA - 1]
            minRightA = float('inf') if partitionA == m else A[partitionA]

            maxLeftB = float('-inf') if partitionB == 0 else B[partitionB - 1]
            minRightB = float('inf') if partitionB == n else B[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:

                # Even total length
                if (m + n) % 2 == 0:
                    return (
                        max(maxLeftA, maxLeftB)
                        + min(minRightA, minRightB)
                    ) / 2

                # Odd total length
                return max(maxLeftA, maxLeftB)

            elif maxLeftA > minRightB:
                right = partitionA - 1

            else:
                left = partitionA + 1