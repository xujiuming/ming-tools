from typing import List

'''
设定 下标 index 
从第二个元素开始循环 
当元素的值 跟 index位置的值不相等 则证明是新的值  
设置 index+1位置的值为 当前i的值 
# 截断数组 保留 0-index+1
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index + 1
