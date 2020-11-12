

import os
import numpy as np

# 测试者总数
people_total=3

# 数据储存（测试者所有的测试）
A01 = []
A02 = []
A03 = []
B01 = []
testers = {'A01': A01, 'A02': A02, 'A03': A03, 'B01': B01}


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):#os.walk遍历给定文件夹
        # print(root) # 当前目录路径
        # print(dirs) # 当前路径下所有子目录
        # print(files) # 当前路径下所有非目录子文件
        return dirs#只要子目录，也就是只返回类似于"day01"这样的天数文件夹

# 获取目录下所有文件路径
def listdir(path, list_name):#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)

#获取data里面的day0x文件夹     
day_dir=file_name('data')

# 数据储存（测试者每阶段的测试），右 n = len(day_dir)的天数，自然需要n组，每组包含四个受试者，即A01...
testers_day = [{'A01': [], 'A02': [], 'A03': [], 'B01': []} for i  in range(len( day_dir ))]
# 数据储存（测试者每阶段的结果） 
testers_day_result = [{'A01': [], 'A02': [], 'A03': [], 'B01': []} for i  in range(len( day_dir ))]
testers_day_total_result = [ [] for i  in range(len( day_dir ))]

def main():
    for day in day_dir:#按天来
        # 获取day文件下文件
        data_list = []
        listdir( 'data\\' + day, data_list )#获取第n天文件夹dayn下的所有文件

        # 处理文件夹下
        for path in data_list:#此时的path已经是具体受试者信息的文件了
            # 根据path提供的文件路径，可以获得有效信息：天数，测试者，时间
            # Q:将对应测试者的数据放到对应数组中

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
                #此时的b，包含dayn下面，受试者x的全部有效信息
                # 输出预处理值
                # print( b )

                testers[path[11: 14]].append(b)
                #path[11: 14] = A01,即受试者，testers[X]可以查看受试者X的信息
                # print("path = "+path[11: 14])

                

                testers_day[int(path[8:10])-1][path[11: 14]].append(b)
                # print("path = "+path[8:10])
                #path = 01，即天数
                # test_day[x][y]可以查看第x天，受试者y的信息


                # 计算数据求均值，方差
                # b = np.array( b )
                # print( "均值:", b.mean() )
                # print( '标准差:', b.std() )


def day_calc(list_day):
    # enumerate函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
    for index,i in enumerate(list_day):
        # print('第',index+1,'阶段')
        day_mean = []
        day_std = []
        for key in i.keys():
            # 计算数据求均值，方差
            if (i[key]):
                b = np.array( i[key] )
                # print( '测试者:', key )
                # print( "均值:", b.mean() )
                # print( '标准差:', b.std() )
                # print( '协方差:', b.cov() )
                day_mean.append(b.mean())
                day_std.append(b.std())
                testers_day_result[index][key]=[b.mean(), b.std()]
        day_mean = np.array( day_mean )
        day_std = np.array( day_std )
        testers_day_total_result[index]=[day_mean.mean(),day_std.mean()]
    # 数据格式
    # [{'A01': [563.2, 163.68066471028274], 'A02': [564.5, 180.50138503623734], 'A03': [558.0, 60.0], 'B01': []}, {'A01': [], 'A02': [], 'A03': [], 'B01': [558.0, 60.0]}]

#数据形式如下
(
    {
        'A01': [[618, 498, 800, 300, 600], [618, 498, 800, 300, 600]], 
        'A02': [[618, 498, 800, 300, 600, 800, 300, 600]], 
        'A03': [[618, 498]], 
        'B01': [[618, 498]]
    }, 

    [
        {
            'A01': [[618, 498, 800, 300, 600], [618, 498, 800, 300, 600]],
            'A02': [[618, 498, 800, 300, 600, 800, 300, 600]],
            'A03': [[618, 498]], 
            'B01': []
        }, 

        {
            'A01': [],
            'A02': [], 
            'A03': [], 
            'B01': [[618, 498]]
        }
    ]
)

# 提供外部接口
def get_data():
    main()
    return testers,testers_day

def get_total_day():
    main()
    day_calc( testers_day )
    return testers_day_total_result

if __name__ == '__main__':
    main()
    day_calc(testers_day)
    print(get_total_day())


