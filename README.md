# JiaGuoMeng
家国梦建筑摆放计算

## 使用方法

- 搭建python环境
	1. 访问[python官网](https://www.python.org/downloads/windows/)
	2. 在导航栏中依次点击Downloads----Windows
	3. 在Stable Releases条目下选择最新版的windows安装程序（后缀executable installer）下载（32位64位自行选择）
	4. 安装首页勾选 Add Python to Path 点击Install Now（推荐）或自定义路径
	5. 打开cmd，输入python -V，出现版本号为安装成功
	6. 在cmd中输入`python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose`并回车，安装数学依赖模块
- 使用
	1. 将github代码下载到本地并解压
	2. 右键点击config.py选择Edit with IDLE根据提示进行个人配置
	3. 在cmd中输入：cd 文件夹地址 （如：cd C:\Users\Lawrence\Desktop\JiaGuoMeng）
	4. 输入：python jiaguomeng_v_2_0.py 并回车
- 问题
　　出现其他类似:`ModuleNotFoundError: No module named 'numpy'`的提示，参照环境搭建第六条输入`python -m pip install --user 模块名`并回车

公式参考： https://bbs.nga.cn/read.php?tid=18675554
nga：https://bbs.nga.cn/read.php?tid=18677204

## 更新记录：

10.2更新：
- 调整算法逻辑，使用当前建筑等级进行计算，更加贴近游戏实际
- 修复了一系列bug
- 调整输出，计算输出当前秒伤

9.28更新：
- 修复了一系列数值bug
- 优化了政策计算
- 修复升级优先级的bug

9.30更新：
- 进一步优化代码和交互逻辑
- 增加在线版本
