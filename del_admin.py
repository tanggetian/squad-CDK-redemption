from datetime import datetime, timedelta  # 从datetime模块导入datetime和timedelta类
import frozen_dir
#by 本程序由唐格天制作

# 定义一个函数is_outdated，用于判断给定的日期字符串是否早于当前时间一个月
def is_outdated(date_str):
    # 使用strptime方法将日期字符串转换为datetime对象
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")  # 假设日期字符串的格式为"年-月-日 时:分:秒"
    current_date = datetime.now()  # 获取当前的日期和时间
    # 判断给定的日期是否早于当前时间一个月
    if date < current_date - timedelta(days=30):  # 如果日期早于当前时间一个月，返回True
        return True
    else:  # 否则，返回False
        return False

# 初始化一个空列表lines_to_keep，用于存储需要保留的行内容
lines_to_keep = []

# 使用with语句打开文件"Admins.cfg"，读取文件内容并存储在列表lines中
with open(frozen_dir.app_path()+r'\Admins.cfg', "r") as file:
    lines = file.readlines()  # 读取文件内容到列表lines中

# 遍历列表lines中的每一行内容
for line in lines:
    # 提取每行中的时间字符串，并检查是否超过当前时间一个月
    if not is_outdated(line.split("//")[1].strip()):  # 使用split方法将行内容按"//"分割成两部分，并取第二部分作为日期戳，再使用strip方法去除空白字符
        lines_to_keep.append(line)  # 如果当前行不是过期行，则将其添加到lines_to_keep列表中

# 使用with语句再次打开文件"Admins.cfg"，但这次是写入模式（w模式），将保留的行内容写回文件中
with open(frozen_dir.app_path()+r'\Admins.cfg', "w") as file:
    for line in lines_to_keep:  # 遍历lines_to_keep列表中的内容，即保留的行内容
        file.write(line)  # 将保留的行内容逐行写回文件中
