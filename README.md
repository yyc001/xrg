# 计算机组成原理 课程设计

虽然这是我做课设的原始工程，画的图和写的代码可能比较丑，不过有很多东西复用起来会很方便。

`EXP1` 和 `EXP2` 是前两个比较简单的实验。

`EXP33` 是基于微指令实现的的16位 CPU。微指令部分详见 [微指令设计.md](微指令设计.md)

`soc` 是一个方便小可爱们做实验的 SoC 框架，里面有一个 16bit 的 ram、一个空实现的 CPU，并引出了若干调试引脚。你需要做的是 fill 这个 CPU。**相信我，用它做实验，你会感谢yyc学姐的。**

`u_compile.py` 是一个根据你设计的微指令**直接生成 `.mif` 文件**的脚本，它的配置文件是 `u_config.py`。如果你的 CPU 架构与 `EXP33` 不同，需要修改这两个文件的内容。

`i_compile.py` 是一个根据伪汇编代码**直接生成 `.mif` 文件**的脚本，它的配置文件是 `i_config.py`。如果你的指令集与 `EXP33` 不同，需要修改这两个文件的内容。
