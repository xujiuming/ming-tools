from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 线性循环
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    break
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicate1(self, nums: List[int]) -> bool:
        '''
        排序 然后比较连续两个是否相等
        '''
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:
            print(nums[i - 1], nums[i])
