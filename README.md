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
