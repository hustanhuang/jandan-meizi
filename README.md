# jandan-mz

爬[煎蛋妹子图](http://jandan.net/ooxx)的恶俗工具😃

## 依赖

```
python3

pip:
  beautifulsoup4
  lxml
```

## 用法

### 抓取图片地址

```bash
python main.py [start_page] [end_page]
```

### 下载

抓取完成后会生成文件夹`[start_page]-[end_page]`，里面有一个`urls`文件。

然后下就行了

```bash
wget -i urls --tries=1
```

## 这样的恶俗工具随手一抓就是一大把

https://github.com/kulovecc/jandan_spider

https://github.com/tonyxyl/jandan

https://github.com/haipz/Jandan-Picture-Downloader

https://github.com/bjianhang/jandan

https://github.com/haipz/JandanPicture

（反正就是个根本没有技术含量的玩意
