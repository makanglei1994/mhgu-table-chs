# MHGU TABLE CHS

怪物猎人GU解包Table数据简体中文内容

## 内容说明

`chS/table`目录是解包文件`nativeNX\chS\table`的内容，`target`目录是使用`gmd.py`解码后的内容。在解码期间有些内容使用`UTF-8`编码进行解码时会出现转码错误，错误的内容使用`<Decode Error>`占位。文本中的换行符使用`<BR/>`占位

解码后的`*.txt`文本内容是直接平铺的，不确定在原文件中是否有记录具体格式（例如多少列），但是网上能找到的资料比较少，目前只能人工自行判断。

比如：

- `target\table\armorSeriesData_chS.txt`应该是5个为一组，奇数行为装备名称，偶数行为装备说明。
- `target\table\itemData_chS.txt`应该是2个为一组，每组第一个是物品名称，第二个是物品说明

## 参考内容

### 解包方法

- [如何解包switch游戏（动森为例）](https://zhuanlan.zhihu.com/p/349681765)
- [如何解包mhrise](https://www.bilibili.com/read/cv11670696/)

### 解包工具

- [SciresM/hactool](https://github.com/SciresM/hactool)

### GMD解码

- [mhvuze/gmdDump](https://github.com/mhvuze/gmdDump)
