#!/bin/python3
# author ming
# gevent 实现 发布订阅  订阅者累计n个消息执行操作

import gevent


def beforeTask(s):
    """
    前置任务
    """
    # 模拟task 执行延迟
    print("模拟延迟启动消息{}s".format(s))
    gevent.sleep(s)
    print("模拟延迟执行完成消息{}s".format(s))


if __name__ == '__main__':
    n = 10
    futures = []
    for i in range(0, n):
        futures.append(gevent.spawn(beforeTask, i))
    # 阻塞future 结果 获取所有future结果 认为前面n个task执行完毕
    for f in futures:
        f.get()
    # 执行其他task
    print('after task ..........')
