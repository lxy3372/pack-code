# pack-code

---

## 使用说明

简单打包增量发布的源代码，说明：

1. 项目地址：项目原开发文件夹目录
2. 打包目录：文件打包到对应目录
3. 打包列表：需要打包的文件列表，以**项目地址**为根目录的相对地址
4. 打包名称：打包后压缩包的对应名称以及包类型
5. 产生.zipignore 说明： 由于zipfile打包无法加密，暂使用一种比较投机的方式，zip u -p 添加密码,故添加了一个无用的`.zipignore`文件


![截图](./screenshot.png)

## 依赖

#### 包依赖

```bash
pip install wxpython

pip install pyinstaller
```

#### 环境依赖

windows需要安装7z打包工具，并将7z.exe 加入到环境变量中
Linux/Mac Os 需要安装zip

## 打包

```bash
pyinstall -F -w  -i ./bitmaps/zip.ico wxrun.py
```

