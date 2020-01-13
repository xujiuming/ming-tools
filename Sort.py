#!/usr/bin/env python3
# author： ming
# 演示排序方法的脚本
# 参考博客: https://www.cnblogs.com/haiyan123/p/8395926.html
# 未排序之前的数组   每个函数排序的时候 请深拷贝 避免对原数组进行操作
import copy
import time

int_l = [1, 32, 423, 67, 100, 111, 222, 333, 123, 534, 1310, 12300, 1102, 1111, 111, 222321]


def count_time(info="排序"):
    def _count_time(func):
        def _wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            print("{}耗时:{}s".format(info, str(round((end_time - start_time), 2))))
            return result

        return _wrapper

    return _count_time


@count_time("冒泡排序")
def bubble_sort(l: list):
    """
    冒泡排序
        顺序比较大小  当前面的大 那么互换未知    一直到整个数组从小到大顺序排列 看起来跟冒泡一样 所以叫做冒泡排序
    百度百科: https://baike.baidu.com/item/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F/4602306?fr=aladdin

    1：比较和互换位置 最后一个元素不进行比较
    2:循环n-1次

    :param l: 未排序数组
    """
    # 避免影响原数组 进行深拷贝
    t_l = copy.deepcopy(l)
    # 循环n-1次
    for num in range(len(t_l) - 1):
        # 最后一个元素不判断
        for i in range(len(t_l) - 1):
            # 判断当前元素是否大于后一个元素
            if t_l[i] > t_l[i + 1]:
                # 当前元素和后一个元素互换值
                t_l[i], t_l[i + 1] = t_l[i + 1], t_l[i]
    return t_l


if __name__ == '__main__':
    print(bubble_sort(int_l))
    print("--------------------------------------------")
