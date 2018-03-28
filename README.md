
# Xcode Snippets

## 使用前请阅读——[由代码块驱动的代码规范](./Guidline.html)

## Install

```
# 1.打开Terminal，切换到当前目录
cd **
# 2.执行部署脚本
python setup.py
# 3.看到“执行完成”字样即成功了。
# 4.重启Xcode
```


## 向服务器提交代码块的注意事项：

* 文件名以功能简称为准
* 文件复制到本地Git库中根据功能分层的目录中
* 请明确作用范围(Completion scope)


### 作用范围(Completion scope)

| 名称 | 实际范围 |
| --- | --- |
| All | 包含所有情况 |
| Class Implementation |  类的实现代码 |
| Class Interface Variables |Interface中声明的私有变量。(即大括号内的部分，如大括号内声明的_label。) |
| Class Interface Methods |  Interface中方法声明部分。（大括号外的部分。）|
| Top Level | Class 之外 |
| Code Expression |  |
| Function or Method | |
| Preprocessor directive | |
| String or Commont | |

需要额外注意的就是 *Class Interface Variables* 和 *Class Interface Methods* 的分别。


## Q&A

#### 有没有备份？

答案：有的。并且，每次执行更新都会生成一份备份文件，地址如下：
```
~/Library/Developer/Xcode/UserData/CodeSnippets.时间戳
```

#### 如何找到修改或创建的代码块文件？

~/Library/Developer/Xcode/UserData/CodeSnippets 目录下，非引用链接文件的即是。





