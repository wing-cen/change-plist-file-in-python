# change-plist-file-in-python
使用python修改plist 文件的相关内容<br>
<img src="bg.jpg">

<p>plist 文件实质上是一个xml文件，通常在mac,iphone上看到后缀名为plist的都是这种文件，这种文件有两种形式，一种是明文的xml形式，还有一种是二进制形式的文件。所以我写了两种形式的转换。
<p>在Xcode的项目上有很多个target，每次打包程序都要修改一次这些plist文件的版本号，纯手动来,效率极其低下。所以写了个脚本批处理一下。

<h3>使用</h3>
由于MAC默认使用的是python2.7，而我使用的biplist库在2.7下不适用所以需要安装python3+<br>
<br>
MAC 命令行使用python3 +<br>
方法1、修改MAC 默认python版本。alias python="/usr/local/bin/python3.6"<br>

方法2、~/.bash_profile文件<br>
在python文件夹中从framework框架中拷贝python的文件夹过来<br>
命令行python3即可<br>


修改版本运行：python3 plist2XML.py (.py文件和版本文件在同一个目录中)<br>

//生成的plist文件可以是明文的XML形式 或者 二进制的形式<br>


<h5>1、plist2Binary.py</h5> <br>
以二进制形式进行保存<br>

<h5>2、plist2XML.py</h5> <br>
以XML明文形式保存
