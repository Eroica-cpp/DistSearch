Search Engine
============

现在开了一个github的仓库，用来：  
1. 托管搭建搜索引擎的代码。  
2. 记录各种学习资料和学习笔记。  


## Reference
参考文献及学习笔记

#### 1. [Building a Search Engine with Nutch and Solr in 10 minutes](http://www.building-blocks.com/thinking/building-a-search-engine-with-nutch-and-solr-in-10-minutes/)

#### 2. [Nutch Tutorial on Ubuntu (10 easy steps)](https://sites.google.com/site/profileswapnilkulkarni/tech-talk/nutchtutorialonubuntu10easysteps)

#### 3. [Install Nutch 1.7 and Hadoop 1.2.0](http://nutchhadoop.blogspot.com/)

#### 4. [Install & Configure Solr on Ubuntu, the quickest way](https://github.com/sunspot/sunspot/wiki/Configure-Solr-on-Ubuntu,-the-quickest-way)

这篇文章主要讲两个方面：  
	1. 安装  
	2. 配置  

###### 安装
安装需要有java JDK6以上，没有的话：
```
$ sudo apt-get install openjdk-6-jdk
```

然后直接用apt-get安装solr和tomcat，40MB左右：
```
$ sudo apt-get install solr-tomcat
```

安装完了之后打开服务：
```
$ sudo service tomcat6 start
```

之后在浏览器中查看[http://localhost:8080/solr](http://localhost:8080/solr)即可

###### 配置
配置主要是讲如何设置用户和权限，以及针对具体的应用的设置，暂时没有试了。  
设置用户和权限以后肯定是要做的。

#### 5. [NutchTutorial](http://wiki.apache.org/nutch/NutchTutorial)
官方nutch教程




