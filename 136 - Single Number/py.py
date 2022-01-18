# Python - 136. Single Number
# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for x in nums:
        #     x_pos = nums.index(x)
        #     for y in nums[x_pos+1]:
        #         if x == y:
        #             nums.remove(x)
        #             nums.remove(y)
        #             break
        for x in nums:
            x_pos = nums.index(x)
            nums[x_pos] = "a"
            print(x)
            # nums.remove(x)
            print("after remove ", nums)
            if x not in nums:
                print(x)
                return x
            nums.remove(x)