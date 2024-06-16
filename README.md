# MHGU TABLE CHS

怪物猎人GU解包Table数据简体中文内容

## 内容说明

`chS/table`目录是解包文件`nativeNX\chS\table`的内容，`target`目录是使用`gmd.py`转码后的内容。在转码期间有些内容使用`UTF-8`会出现转码错误，错误的内容使用`<Decode Error>`占位。换行符使用`<BR/>`占位

文本的内容是直接平铺的，网上能收到的资料比较少，我也不清楚怎么判断不同的表格具体有多少列，所以只能自行判断了。

比如：

- `target\table\armorSeriesData_chS.txt`应该是5个为一组，奇数行为装备名称，偶数行为装备说明。
- `target\table\itemData_chS.txt`是2个为一组，每组第一个是物品名称，第二个是物品说明

## 参考内容

### 解包方法

- [如何解包switch游戏（动森为例）](https://zhuanlan.zhihu.com/p/349681765)
- [如何解包mhrise](https://www.bilibili.com/read/cv11670696/)

### 解包工具

- [SciresM/hactool](https://github.com/SciresM/hactool)

### GMD解码

- [mhvuze/gmdDump](https://github.com/mhvuze/gmdDump)
