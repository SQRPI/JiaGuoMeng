# JiaGuoMeng
家国梦建筑摆放计算

## 使用方法

- 搭建python环境
	1. 访问[python官网](https://www.python.org/downloads/windows/)
	2. 在导航栏中依次点击Downloads----Windows
	3. 在Stable Releases条目下选择最新版的windows安装程序（后缀executable installer）下载（32位64位自行选择）
	4. 安装首页勾选 Add Python to Path 点击Install Now（推荐）或自定义路径
	5. 打开cmd，输入python -V，出现版本号为安装成功
	6. 在cmd中输入`python -m pip install --user numpy scipy tqdm pandas`并回车，安装数学依赖模块
- 使用
	1. 将github代码下载到本地并解压
	2. **右键点击config.py选择Edit with IDLE根据提示进行个人配置**
	3. 在cmd中输入：cd 文件夹地址 （如：cd C:\Users\Lawrence\Desktop\JiaGuoMeng）
	4. **运行jiaguomeng_v_2_0.py(输入：python jiaguomeng_v_2_0.py 并回车)**
- 问题
　　出现其他类似:`ModuleNotFoundError: No module named 'numpy'`的提示，参照环境搭建第六条输入`python -m pip install --user 模块名`并回车

## 更新记录

10.2更新：
- 调整算法逻辑，使用当前建筑等级进行计算，更加贴近游戏实际
- 修复了一系列bug
- 调整输出，计算输出当前秒伤

9.30更新：
- 进一步优化代码和交互逻辑
- 增加在线版本

9.28更新：
- 修复了一系列数值bug
- 优化了政策计算
- 修复升级优先级的bug

## 作者

- 本项目由我SQRPI（nga: 根派）和校友（nga: 温火融冰）合作完成。

- 温火融冰的前端整合版在：[点击访问](https://github.com/SQRPI/JiaGuoMeng)，大家不要忘记去支持一下点个star哦！

- nga原帖链接：[写了个计算建筑摆放最优策略的脚本](https://bbs.nga.cn/read.php?tid=18677204)

- 公式参考：[单建筑收益公式及一些tips](https://bbs.nga.cn/read.php?tid=18675554)

- 数据来源：[[攻略] 建筑收益及升级消耗数据](https://nga.178.com/read.php?tid=18741305)
- 另外关于火车机制的测评可以参考温火融冰在nga发布的攻略贴[[攻略] 火车机制探索与数据测试](https://nga.178.com/read.php?tid=18729321)
- 感谢一起参与修bug、提供数据、发布综述以及给我们点star的朋友们，你们的支持就是我们最大的动力！

