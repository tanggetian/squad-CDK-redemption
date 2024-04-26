# 导入Flask框架和其他必要的库
from flask import Flask, render_template, request
import time

#by 本程序由唐格天制作

# 创建Flask应用实例
app = Flask(__name__)

# 定义CDK文件路径
cdk_file = 'cdk.txt'

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
    id = steam_id

    # 获取Steam ID的长度
    length = len(id)

    # 检查CDK是否存在于cdk_file中
    with open(cdk_file, 'r') as file:
        cdk_list = file.read().splitlines()
        if cdk in cdk_list:
            # 检查Steam ID格式是否正确
            if (length == 17):
                # 打开Admins.cfg文件以追加模式
                admins = open("Admins.cfg", "a", encoding="utf-8")

                # 获取当前时间
                current_timestamp = time.time()
                current_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_timestamp))

                # 将Steam ID和时间写入文件
                admins.write("Admin=")
                admins.write(id)
                admins.write(":预留 //")
                admins.write(current_time_str)

                # 关闭文件
                admins.close()

                # 输出CDK到控制台
                print(cdk)

                # 从CDK.txt文件中删除已使用的CDK
                # 读取cdk_file文件的所有内容
                with open(cdk_file, "r") as file:
                    lines = file.readlines()
                # 创建一个空列表，用于存储更新后的行
                updated_lines = []
                # 遍历文件中的每一行
                for line in lines:
                    # 如果当前行不包含CDK，则添加到更新后的行列表中
                    if cdk not in line:
                        updated_lines.append(line)
                # 写回更新后的行列表到cdk_file文件中
                with open(cdk_file, "w") as file:
                    file.writelines(updated_lines)

                # 返回'兑换完成'页面给用户
                return render_template('ok.html')
            else:
                # 如果Steam ID长度不是17，返回错误页面
                return render_template('steam64error.html')
        else:
            # 如果CDK不在文件中，返回错误页面
            return render_template('cdkerror.html')


# 当脚本直接运行时，启动Flask应用
if __name__ == '__main__':
    app.run()
