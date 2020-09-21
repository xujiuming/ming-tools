from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pass


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = []
    #hash 表
    # 构建hash表 nums i
    hashNums1 = {}
    for i in range(len(nums1)):
        if not hashNums1.has_key(nums1[i]):
            hashNums1.setdefault()
    # 计算结果
