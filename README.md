## 项目初始化
- git clone path //下载项目到本地
- git branch  //查看分支  代码开发需要在feat分支下进行，功能完成后及时提交代码，避免代码覆盖
- git checkout branch_name  // 切换分支
- 0.git pull    //拉取远端代码
- 1.git status  //  查看文件状态
- 2.git add .  //将文件加入缓存区
- 3.git commit -m "feat: 说明信息"  //提交文件至本地代码库
- 4.git push  //提交代码至远端
- (注：每次提交必须要经历上诉两个步骤)
### 依赖包安装
- （注:由于pycharm建立项目时会自动生成venv文件（虚拟环境文件），会将工程环境与本地环境隔离，可以在File->settings->project->project interpreter 下进行设置python运行环境）
- 该项目需要pyqt5依赖包

- 本地下载 
```
pip install pyqt5
```

- venv下载 
```
在File->settings->project->project interpreter 下进行设置python运行环境
添加镜像文件，下载对应依赖包
参考网址：https://blog.csdn.net/selfimpro_001/article/details/88670584
```

- 文件说明
```
---CogPara.ui  //QT ui文件
---CogPara.py  //QT py文件
---CogParaWindow.py //主程序入口
---readdemo.py  //数据处理模块
```

- 学习网址
```
参考网址：https://blog.csdn.net/u011740601/article/details/103952172
```

····