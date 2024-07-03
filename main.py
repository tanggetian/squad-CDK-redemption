# 导入Flask框架和其他必要的库
from flask import Flask, render_template, request,send_from_directory
import time
import frozen_dir
import os
# by 本程序由唐格天制作

# 创建Flask应用实例
app = Flask(__name__, template_folder=frozen_dir.app_path() + r'\templates',
            static_folder=frozen_dir.app_path() + r'\static')
# template_folder='../xxxx' 指 前端文件的目录
# static_folder="../xxxx"  指 静态文件的目录

# 网页图标
@app.route('/favicon.ico')#设置icon
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),#对于当前文件所在路径,比如这里是static下的favicon.ico
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
    
    
# 定义CDK文件路径
cdk_file = frozen_dir.app_path() + r'\cdk.txt'  # 月cdk
cdk_file1 = frozen_dir.app_path() + r'\cdk1.txt'  # 季cdk
cdk_file2 = frozen_dir.app_path() + r'\cdk2.txt'  # 年cdk
cdk_file3 = frozen_dir.app_path() + r'\cdk3.txt'  # 天cdk
cdk_file4 = frozen_dir.app_path() + r'\cdk4.txt'  # 永久cdk


# 定义根路径的路由和对应的函数
@app.route('/')
def index():
    # 渲染index.html模板文件并返回
    return render_template('index.html')


# 定义提交路径的路由和对应的函数，该函数处理POST请求
@app.route('/submit', methods=['POST'])
def submit():
    # 从表单中获取Steam ID和CDK
    steam_id = request.form['steam_id']
    cdk = request.form['cdk']

    # 输入的Steam ID
    steamid = steam_id

    # 获取Steam ID的长度
    length = len(steamid)
    a = 0

    # 检查CDK是否存在于cdk_file中
    with open(cdk_file, 'r') as file:
        # 一个月
        cdk_list = file.read().splitlines()
        if cdk in cdk_list:
            a = 1

    with open(cdk_file1, 'r') as file:
        # 一个季度
        cdk_list = file.read().splitlines()
        if cdk in cdk_list:
            a = 2

    with open(cdk_file2, 'r') as file:
        # 一年
        cdk_list = file.read().splitlines()
        if cdk in cdk_list:
            a = 3

    with open(cdk_file3, 'r') as file:
        # 一天
        cdk_list = file.read().splitlines()
        if cdk in cdk_list:
            a = 4

    with open(cdk_file4, 'r') as file:
        # 永久
        cdk_list = file.read().splitlines()
        if cdk in cdk_list:
            a = 5

        # 检查Steam ID格式是否正确
    if length == 17:
        # 打开Admins.cfg文件以追加模式
        admins = open(frozen_dir.app_path() + r'\Admins.cfg', "a", encoding="utf-8")
        current_timestamp = time.time()
        current_time = time.localtime(current_timestamp)  # 转换为本地时间
        if a == 1:  # 一个月
            # 获取当前时间
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_timestamp))
            cdk_file_del = cdk_file
        elif a == 2:  # 一个季度
            current_month = current_time.tm_mon + 2  # 获取当前月份加二的值
            current_year = current_time.tm_year  # 获取当前年份的值
            current_day = current_time.tm_mday  # 获取当前日期
            new_timestamp = time.mktime((current_year, current_month, current_day, 0, 0, 0, current_time.tm_mon,
                                         current_time.tm_wday, current_time.tm_yday))  # 计算新的时间戳
            new_time = time.localtime(new_timestamp)  # 将新的时间戳转换为本地时间
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', new_time)  # 将新的时间格式化为字符串
            cdk_file_del = cdk_file1
        elif a == 3:  # 一年
            current_month = current_time.tm_mon + 11  # 获取当前月份加十一的值
            current_year = current_time.tm_year  # 获取当前年份的值
            current_day = current_time.tm_mday  # 获取当前日期
            new_timestamp = time.mktime((current_year, current_month, current_day, 0, 0, 0, current_time.tm_mon,
                                         current_time.tm_wday, current_time.tm_yday))  # 计算新的时间戳
            new_time = time.localtime(new_timestamp)  # 将新的时间戳转换为本地时间
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', new_time)  # 将新的时间格式化为字符串
            cdk_file_del = cdk_file2
        elif a == 4:  # 一天
            current_month = current_time.tm_mon - 1  # 获取当前月份减一的值
            current_year = current_time.tm_year  # 获取当前年份的值
            current_day = current_time.tm_mday + 1  # 获取当前天加一
            new_timestamp = time.mktime((current_year, current_month, current_day, 0, 0, 0, current_time.tm_mon,
                                         current_time.tm_wday, current_time.tm_yday))  # 计算新的时间戳
            new_time = time.localtime(new_timestamp)  # 将新的时间戳转换为本地时间
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', new_time)  # 将新的时间格式化为字符串
            cdk_file_del = cdk_file3
        elif a == 5:  # 永久
            time_str = time.strftime('2099-01-01 12:00:00')  # 将新的时间格式化为字符串
            cdk_file_del = cdk_file4
        else:
            # 如果CDK不在文件中，返回错误页面
            return render_template('cdkerror.html')
            
        if a != 0:  # 如果cdk有值
            # 将Steam ID和时间写入文件
            admins.write("Admin=")
            admins.write(steamid)
            admins.write(":预留 //")
            admins.write(time_str + '\n')

            # 关闭文件
            admins.close()

            # 输出CDK到控制台
            print(cdk)

            # 从CDK.txt文件中删除已使用的CDK
            # 读取cdk_file文件的所有内容

            with open(cdk_file_del, "r") as file:
                lines = file.readlines()
            # 创建一个空列表，用于存储更新后的行
            updated_lines = []
            # 遍历文件中的每一行
            for line in lines:
                # 如果当前行不包含CDK，则添加到更新后的行列表中
                if cdk not in line:
                    updated_lines.append(line)
            # 写回更新后的行列表到cdk_file文件中
            with open(cdk_file_del, "w") as file:
                file.writelines(updated_lines)

            if a == 1:
                # 返回'兑换完成一个月'页面给用户
                return render_template('ok_mon.html')
            elif a == 2:
                # 返回'兑换完成季度'页面给用户
                return render_template('ok_quarter.html')
            elif a == 3:
                # 返回'兑换完成年'页面给用户
                return render_template('ok_year.html')
            elif a == 4:
                # 返回'兑换完成天'页面给用户
                return render_template('ok_day.html')
            elif a == 5:
                # 返回'兑换完成永久'页面给用户
                return render_template('ok_vvip.html')
    else:
        # 如果Steam ID长度不是17，返回错误页面
        return render_template('steam64error.html')    

# 当脚本直接运行时，启动Flask应用
if __name__ == '__main__':
    app.run()
