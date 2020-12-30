import os
import re

# 版本号  setup.py  ming.py 引用  每次发布 版本+1
ming_global_version = 1.80


def getVersion():
    return ming_global_version


class ToolsDependency:
    """
    工具依赖
    """
    cmd: str
    desc: str
    installDemoCmd: str

    def __init__(self, cmd, desc=None, installDemoCmd=None):
        self.cmd = cmd
        self.desc = desc
        self.installDemoCmd = installDemoCmd


# 工具依赖信息数组
tools_dependency_info_arr = [
    ToolsDependency('cat'),
    ToolsDependency('ssh'),
    ToolsDependency('sftp'),
    ToolsDependency('vi'),
    ToolsDependency('dd'),
    ToolsDependency('git'),
    ToolsDependency('free'),
    ToolsDependency('ip'),
    ToolsDependency('dot', "绘制svg图案,graphviz", 'yay -Syyu graphviz'),
    ToolsDependency('screenfetch', "显示当前操作系统信息", 'yay -Syyu screenfetch'),
    # ToolsDependency('showError', '测试错误情况', 'test'),
]

# 配置目录存放在 用户根目录
root_config_dir = '{}/.jiuming-tools'.format(os.path.expanduser('~'))
if not os.path.exists(root_config_dir):
    os.makedirs(root_config_dir)

# 功能配置目录
config_default_file = '{}/.jiuming-tools/config'.format(os.path.expanduser('~'))
if not os.path.exists(config_default_file):
    os.makedirs(config_default_file)

# 脚本默认文件夹
script_default_file = '{}/.jiuming-tools/config/script'.format(os.path.expanduser('~'))
if not os.path.exists(script_default_file):
    os.makedirs(script_default_file)

# ssh 私钥默认文件夹
private_key_default_file = '{}/.jiuming-tools/config/privateKey'.format(os.path.expanduser('~'))
if not os.path.exists(private_key_default_file):
    os.makedirs(private_key_default_file)

# 正则
compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
compile_host_mame = re.compile('^[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?$')
