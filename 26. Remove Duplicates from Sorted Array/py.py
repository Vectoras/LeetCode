# Python - 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for idx, val in enumerate(nums):
            # print(idx, val)
            if val is not None:
                for idx2 in range(idx+1, len(nums)):
                    if val == nums[idx2]:
                        nums[idx2] = None
                            
        for idx, val in enumerate(nums):
            print(idx, val)
            # if val is None:
            #     for idx2 in range(idx+1, len(nums)):
            #         if nums[idx2] is not None:
            #             nums[idx] = nums[idx2]
            #             nums[idx2] = None
        
        # print(nums)]
        
        #INCOMPLETE