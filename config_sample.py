# 这是一份实例配置文件
# 将其修改为你需要的配置，并将文件名修改为config.py

from nonebot.default_config import *

SUPERUSERS = [10000]    # 填写超级用户的QQ号，可填多个用半角逗号","隔开
COMMAND_START = {''}    # 命令前缀（空字符串匹配任何消息）
HOST = '127.0.0.1'      # 填写hoshino监听的ip，Windows本地搭建用此条配置
# HOST = '172.17.0.1'   # docker用此条配置
# HOST = '172.18.0.1'   # 阿里云中使用docker用此条配置
PORT = 8080             # 填写hoshino监听的端口

# 是否使用Pro版酷Q功能
IS_CQPRO = False

# 资源库文件夹  Nonebot访问本机资源
RESOURCE_DIR = '~/.hoshino/res/'

# 资源库 URL  用于docker中的酷Q读取宿主机资源，注意以'/'结尾
# 若留空则图片均采用base64发送，开销较大但部署方便
RESOURCE_URL = ''

# 启用的模块
MODULES_ON = {
    'botmanage',
    'groupmaster',
    'priconne',
    # 'kancolle',
    # 'subscribe',
    # 'setu',
    # 'translate',
    # 'dice',
}
