#!/bin/python3
# author ming

import asyncio


async def beforeTask(s):
    """
    前置任务
    """
    # 模拟task 执行延迟
    print("模拟延迟启动消息{}s".format(s))
    await asyncio.sleep(s)
    print("模拟延迟执行完成消息{}s".format(s))
    return s


async def asyncGetScreenfetch():
    # 尝试执行 screenfetch
    try:
        res = await asyncio.create_subprocess_shell("screenfetch", stdout=asyncio.subprocess.PIPE,
                                                    stderr=asyncio.subprocess.PIPE)
        sout, serr = await res.communicate()
        # res.returncode, sout, serr, res.pid
        if res.returncode == 0:
            print(sout.decode('utf-8'))
            return "fasdf"
    except OSError:
        return '安装screenfetch可以获得screenfetch图！'


if __name__ == '__main__':
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    screenfetch_future = asyncio.ensure_future(asyncGetScreenfetch(), loop=loop)
    loop.run_until_complete(screenfetch_future)
    print(screenfetch_future)
    loop.close()
    # asyncio.run(asyncio.wait(ts))
    # 执行其他task
    print('after task ..........')
