from typing import List

'''
输入一个非负数 k  
数组向右移动k个位置 

要求空间为 O(1)
https://leetcode-cn.com/problems/rotate-array/solution/xuan-zhuan-shu-zu-by-leetcode/
'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverseNums(nums: List[int], start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        nums_len = len(nums)
        kn = k % nums_len
        # 反转全部元素
        reverseNums(nums, 0, nums_len - 1)
        # 反转[0,k%n]数组
        reverseNums(nums, 0, kn - 1)
        # 反转[k%n,n]
        reverseNums(nums, kn, nums_len - 1)


def reverseNums(nums: List[int], start: int, end: int):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    #### 暴力循环方式
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    nums_len = len(nums)
    tmp = None
    for i in range(k):
        # 获取最新数组最后一个元素
        previous = nums[nums_len - 1]
        for l in range(nums_len):
            # 依次替换 一次替换一个
            # 当前元素赋值临时变量
            tmp = nums[l]
            # 当前元素填充下一个元素
            nums[l] = previous
            # 当前元素变成下一次循环的下一个元素
            previous = tmp
    print(nums)

    #### 使用反转
    # 这个方法基于这个事实：当我们旋转数组 k 次， k%n 个尾部元素会被移动到头部，剩下的元素会被向后移动。
    # 在这个方法中，我们首先将所有元素反转。然后反转前 k%n 个元素，再反转后面 n-(k%n)个元素，就能得到想要的结果。
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    nums_len = len(nums)
    kn = k % nums_len
    # 反转全部元素
    reverseNums(nums, 0, nums_len - 1)
    # 反转[0,k%n]数组
    reverseNums(nums, 0, kn - 1)
    # 反转[k%n,n]
    reverseNums(nums, kn, nums_len - 1)
    print(nums)

    ####环状替换
    # 从第1个元素开始  算出适合的位置n  1替换n  tmp=n    当n=start的时候 证明已经轮换一圈  然后从start+1元素继续
    # 如果 n%k==0 ，其中 k=k%n （因为如果 kk 大于 nn ，移动 kk 次实际上相当于移动 k%n 次）。这种情况下，我们会发现在没有遍历所有数字的情况下回到出发数字。此时，我们应该从下一个数字开始再重复相同的过程。
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    nums_len = len(nums)
    kl = k % nums_len
    # 总共要替换count次才能成功
    count = 0
    # 从0元素开始
    start = 0
    while count < nums_len:
        # 当前元素为start
        current = start
        # 下一个元素的值
        prev = nums[start]
        while True:
            # 获取当前元素应该在的位置
            next = (current + kl) % nums_len
            # 把替换位置的元素存储到临时变量
            temp = nums[next]
            # 将元素放到正确的位置
            nums[next] = prev
            # 下一个元素为刚刚替换掉的元素
            prev = temp
            # 刚刚替换掉的元素为当前处理元素
            current = next
            # 置换次数+1
            count += 1
            # 当当前元素位置跟开始位置相同 证明已经替换一轮  本元素不再处理  处理 start+1元素
            if current == start:
                start += 1
                break
    print(nums)
