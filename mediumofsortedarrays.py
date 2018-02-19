


'''
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
'''

def findMedianSortedArrays(nums1, nums2):
    n = len(nums1) + len(nums2)
    i=0
    j=0
    k = 0
    ans = []
    check = n/2
    while k <= check:
        if (nums1[i] > nums2[j] ):
            ans.append( nums2[j])
            j += 1
        else:
            ans.append(nums1[i])
            i += 1
        k += 1
    if n % 2 == 0:
        return float(ans[check] + ans[check-1]) / 2
    else:
        return float(ans[check])
          
        



nums1 = [1, 2]
nums2 = [3, 4]
print findMedianSortedArrays( nums1, nums2)