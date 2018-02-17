def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        k = 0
        while i < (m + n) -1:
            
            if nums2[ k ] > nums1[ j ]:
                j += 1
            else:
                nums1.insert(i,nums2[ k ])
                k += 1
                nums1 = nums1[0:len(nums1)-1]
            i += 1


nums1 =[4,5,6,0,0,0]
n = 3
nums2 = [1,2,3]
m = 3
print(merge( nums1, m, nums2, n))
