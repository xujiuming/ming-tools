from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)
        nums = sorted(nums)
        i = 0
        while i <= nums_len:
            # 当是最后一个的时候 为不同值
            if i == nums_len - 1:
                return nums[i]
            # 判断当前值跟下一个值是否相等 相等则跳过下一个  不想等则当前值为只出现一次的数字
            if nums[i] == nums[i + 1]:
                i += 1
            else:
                return nums[i]
            i += 1


if __name__ == '__main__':
    # 排序法
    nums = [4, 1, 2, 1, 2, 4, 5, 6, 6, 5, 3]
    nums_len = len(nums)
    nums = sorted(nums)
    i = 0
    while i <= nums_len:
        # 当是最后一个的时候 为不同值
        if i == nums_len - 1:
            print(nums[i])
            break
        # 判断当前值跟下一个值是否相等 相等则跳过下一个  不想等则当前值为只出现一次的数字
        if nums[i] == nums[i + 1]:
            i += 1
        else:
            print(nums[i])
            break
        i += 1

    # 位运算方法
    # 任何数和0异或运算 结果是原来的数字  a^0 = a
    # 任何数和自身做异或运算 结果是0  a^a = 0
    # 异或运算满足交换律和结合律 a^b^a=b^a^a=b^(a^a)=b^0=b
    result = 0
    nums = [4, 1, 2, 1, 2, 4, 5, 6, 6, 5, 3]
    for i in range(len(nums)):
        # 进行异或运算
        result = result ^ nums[i]
    print(result)
