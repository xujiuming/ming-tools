#!/bin/python3
import datetime
import time

from scapy.all import traceroute
from scapy.as_resolvers import AS_resolver_radb

domains = '10.10.10.42'
target = domains.split(' ')
dport = [5432, 22]
if len(target) >= 1 and target[0] != '':
    # 启动路由跟踪
    res, unans = traceroute(domains, dport=dport, retry=-2)
    # traceroute生成的信息绘制成svg
    res.graph(target="> traceroute_graph{}.svg".format(datetime.datetime.now().__format__('%Y%m%d%H%M%S')),
              ASres=AS_resolver_radb(),
              type="svg")  # ASres=AS_resolver_radb()改变为可用的whois提供商,而非原来的ASres=None后默认的被qiang了的提供商
    time.sleep(1)
# svg 转格式为 png
# subprocess.Popen("/usr/local/bin/convert test.svg test.png", shell=True)
else:
    print("IP/domain number of errors, exit")
