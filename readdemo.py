with open("demo1.txt", "r") as f:
    b=[]
    for line in f.readlines():
        line = int(line.strip('\n'))  #去掉列表中每一个元素的换行符
        print(line)
        if( line>200 and line<=1000):
            b.append(line)
    print(b)