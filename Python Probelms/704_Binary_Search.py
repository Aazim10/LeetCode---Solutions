class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        while lo<=hi:
            mid = (lo+hi)//2
            mid_val = nums[mid]
            if mid_val==target:
                if (mid-1)>0 and nums[mid-1]==target:
                    hi = mid-1
                else:
                    return mid
            elif mid_val<target:
                lo = mid + 1
            else :
                hi = mid - 1
        return -1
