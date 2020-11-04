

import os
import numpy as np

# 数据储存
A01 = []
A02 = []
A03 = []
B01 = []
testers = {'A01': A01, 'A02': A02, 'A03': A03, 'B01': B01}

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root) # 当前目录路径
        # print(dirs) # 当前路径下所有子目录
        # print(files) # 当前路径下所有非目录子文件
        return dirs

# 获取目录下所有文件路径
def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)
day_dir=file_name('data')

def main():
    for day in day_dir:
        # 获取day文件下文件
        data_list = []
        listdir( 'data\\' + day, data_list )

        # 处理文件夹下
        for path in data_list:
            # 根据path提供的文件路径，可以获得有效信息：天数，测试者，时间
            # Q:将对应测试者的数据放到对应数组中
            print( path )
            with open( path, "r", encoding='UTF-8' ) as f:
                b = []
                for line in f.readlines():
                    try:
                        line = int( line.strip( '\n' ) )  # 去掉列表中每一个元素的换行符
                        if (line > 200 and line <= 1000):
                            b.append( line )
                    except:
                        # 忽略文字信息
                        continue
                # 输出预处理值
                print( b )

                testers[path[11: 14]].append(b)

                # 计算数据求均值，方差
                b = np.array( b )
                print( "均值:", b.mean() )
                print( '标准差:', b.std() )


if __name__ == '__main__':
    main()
    print(testers)