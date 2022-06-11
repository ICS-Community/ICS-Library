> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.cnblogs.com](https://www.cnblogs.com/shiwanghualuo/p/12271274.html)

最近重新装了一下系统，之前安装好的 Sublime Text 倒是还能用，但是右键没有用 Sublime Text 打开的选项了，于是查了一下解决方案

### **_1_**|**_0_** **环境**

*   Win10 和 Win7 都可以
*   Sublime Text 3/4 都可以的
*   以下为 Win10 系统下截图

### **_2_**|**_0_** **添加右键打开文件**

1.  Win + R，输入 regedit, 打开注册表
    
2.  找到 **HKEY_CLASSESS_ROOT\*\Shell**, 右击新建**项**，命名为 **Sublime Text 3**（这里的名字决定在文件上右击，显示的内容），效果如下：  
    [![](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200206220604528-1824636244.png)](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200206220604528-1824636244.png)
    
3.  在新建的项 **Sublime Text 3** 下，新建**字符串值**，命名为 **Icon**, 值为 "**F:\Program Files\Sublime Text Build 3200 x64\sublime_text.exe,0**"，逗号前面为 Sublime Text 的安装路径，后面为 0。（这一步用于右击显示 Sublime Text 的图标），如下图：  
    [![](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200206220931251-295400665.png)](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200206220931251-295400665.png)
    
4.  在项 **Sublime Text 3** 下新建**项 --command**,**command** 项下的默认值修改为 "**F:\Program Files\Sublime Text Build 3200 x64\sublime_text.exe %1**"，**%1** 前面部分为 **Sublime Text 3** 中 exe 的路径，后加一个**空格**和 **%1** 。最终结果如下：  
    [![](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200206221341479-849902763.png)](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200206221341479-849902763.png)
    
5.  退出就可以了
    
6.  找一个文件，右击，可以得到如下效果：  
    [![](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200207104850356-2113796315.png)](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200207104850356-2113796315.png)
    

### **_3_**|**_0_** **添加右键打开文件夹**

1.  Win + R, 输入 **regedit**
2.  找到 **HKEY_CLASSES_ROOT\Directory\shell**
3.  在 **shell** 下新建一个项，命名为**用 Sublime Text 3 打开**（这个值显示在文件夹右键菜单上的值）
4.  这里同**上一部分中第 3 步**添加 **Icon** 的部分，在**用 Sublime Text 3 打开**下，新建字符串 **Icon**, 其他和上一部分相同，该步骤效果如下：  
    [![](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200206222124583-257727054.png)](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200206222124583-257727054.png)
5.  同**上一部分的第 4 步**，最终效果如下：  
    [![](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200206222304066-1739964560.png)](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200206222304066-1739964560.png)
6.  退出即可
7.  找一个文件夹，右击，可以得到如下效果：  
    [![](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200207104939375-1836369219.png)](https://img2018.cnblogs.com/blog/1044885/202002/1044885-20200207104939375-1836369219.png)

### **_4_**|**_0_** **参考**

*   [将 Sublime Text 3 添加到右键中的简单方法](https://www.jb51.net/article/130391.htm)
*   [【Web 小技巧】右键使用 Sublime Text 打开文件夹](https://www.cnblogs.com/sogoe/p/4293067.html) 7

__EOF__

![](https://files-cdn.cnblogs.com/files/shiwanghualuo/20190928163853.bmp)本文作者：**[Danno](https://www.cnblogs.com/shiwanghualuo/p/12271274.html)**  
本文链接：[https://www.cnblogs.com/shiwanghualuo/p/12271274.html](https://www.cnblogs.com/shiwanghualuo/p/12271274.html)  
关于博主：评论和私信会在第一时间回复。或者[直接私信](https://msg.cnblogs.com/msg/send/shiwanghualuo)我。  
版权声明：本博客所有文章除特别声明外，均采用 [BY-NC-SA](https://creativecommons.org/licenses/by-nc-nd/4.0/ "BY-NC-SA") 许可协议。转载请注明出处！  
声援博主：如果您觉得文章对您有帮助，可以点击文章右下角**【[推荐](javascript:void(0);)】**一下。您的鼓励是博主的最大动力！