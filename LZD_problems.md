LZD遇到的问题
===================
这里记录我遇到的BUG和问题.

### 1. Solr不支持中文搜索. 因为我无论用什么关键词搜中文,返回的结果都是一样的.
解决方案可能来自于下载中文分词插件.(百度"solr 支持中文")
### 2. Nutch不爬公文通
因为http://www.szu.edu.cn/robots.txt 写了不给爬。 尝试了使用`bin/nutch freegen`手动生成了segment,
也尝试了向seed.txt里面注入公文通的网址，
再学习了使用`bin/nutch readdb, readlinkdb, readseg`查看nutch的数据库。
结果发现数据库记录着nutch还是因为robots.txt不愿意爬公文通。

