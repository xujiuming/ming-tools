#!/usr/bin/env python3
# author： ming
# 演示排序方法的脚本
# 参考博客: https://www.cnblogs.com/haiyan123/p/8395926.html
# 未排序之前的数组   每个函数排序的时候 请深拷贝 避免对原数组进行操作
import copy
import random
import time


def count_time(info="排序"):
    """
    装饰函数   为函数装饰计算耗时
    :param info: 名称
    :return:
    """

    def _count_time(func):
        def _wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            print("{}耗时:{}μs,结果:{}".format(info, str(
                round((int(round((end_time - start_time) * 1000000))), 2)), str(result)))
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
    3：有序区   每一趟排序之后  最大的一定在最后顺序已经固定  所以 第一趟之后 不需要对最大的数字进行判断  第二趟之后不需要对最大的两个数字进行判断
    :param l: 未排序数组
    """
    # 避免影响原数组 进行深拷贝
    t_l = copy.deepcopy(l)
    # 循环n-1次
    for num in range(len(t_l) - 1):
        # 有序区的不进行排序操作
        for i in range(len(t_l) - num - 1):
            # 判断当前元素是否大于后一个元素
            if t_l[i] > t_l[i + 1]:
                # 当前元素和后一个元素互换值
                t_l[i], t_l[i + 1] = t_l[i + 1], t_l[i]
    return t_l


@count_time("选择排序-n")
def selection_sort_n(l: list):
    """
    选择排序
        每次从剩余元素中找出最大或者最小 添加到新的有序序列中
        百度百科: https://baike.baidu.com/item/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F/9762418?fr=aladdin

    1：每次获取剩余队列中最小的值  跟当前躺数位置的元素互换
    2:  循环躺数 = n   如果增加中间临时变量可以减少为n-1
    :param l:
    :return:
    """
    # 深拷贝
    t_l = copy.deepcopy(l)
    for num in range(len(t_l)):
        for i in range(len(t_l)):
            # 选择最小的
            if t_l[num] < t_l[i]:
                # 置换位置
                t_l[num], t_l[i] = t_l[i], t_l[num]
    return t_l


@count_time("选择排序-(n-1)")
def selection_sort_n_1(l: list):
    """
    选择排序
        每次从剩余元素中找出最大或者最小 添加到新的有序序列中
        百度百科: https://baike.baidu.com/item/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F/9762418?fr=aladdin

    1：每次获取剩余队列中最小的值  跟当前躺数位置的元素互换
    2:n-1躺  识别无序区  来减少最后一次的循环
    :param l:
    :return:
    """
    # 深拷贝
    t_l = copy.deepcopy(l)
    # 躺数  只循环n-1躺 倒数第二趟 已经排好序了
    for num in range(0, len(t_l) - 1):
        # 假设当前最小值的下标
        min_num = num
        # 由于每一趟确定一个数值 所以第num个元素包含之前的肯定是有序的 num+1 开始无序
        for i in range(num + 1, len(t_l)):
            # 获取当前躺数最小的值的坐标
            if t_l[min_num] > t_l[i]:
                min_num = i
        # 置换位置
        t_l[min_num], t_l[num] = t_l[num], t_l[min_num]
    return t_l


if __name__ == '__main__':
    """
    调用各种排序  使用装饰器来打印耗时和结果
    """

    int_l = []
    # 随机生成部分数据
    for i in range(1000):
        int_l.append(random.randint(1, 10000))
    print("未排序数组:{}", str(int_l))
    bubble_sort(int_l)
    selection_sort_n(int_l)
    selection_sort_n_1(int_l)
