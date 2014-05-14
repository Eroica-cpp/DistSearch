Search Engine
============

现在开了一个github的仓库，用来：  
1. 托管搭建搜索引擎的代码。  
2. 记录各种学习资料和学习笔记。  


## Reference
参考文献及学习笔记

#### 1. [Building a Search Engine with Nutch and Solr in 10 minutes](http://www.building-blocks.com/thinking/building-a-search-engine-with-nutch-and-solr-in-10-minutes/)

详细的教程，但是版本有一点老，很多链接失效了。  

下面有评论：  

“I'm using nutch 1.7 and solr 3.6.2. I fetch a problem by using your above code of solrconfig.xml there has an error. i think the name attribute of lst under request handler will not "defaults" its "default" for solr 3.6.2 with nutch 1.7. hope you will make correction or specify version specific note. i read the document. they told that "default" is a magic word for this configuration. hope it may helpful for someone...”  

我觉得只看[官网的教程](http://wiki.apache.org/nutch/NutchTutorial)就行了，足够好足够详细  

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
官方nutch教程，里面写的相当详细。  
注：这个是nutch 1.x 版本的教程， nutch有2.x的版本了，但是文档不是很多。建议还是用nutch 1.7或1.8

#### 6. [Python 爬虫如何入门学习？](http://www.zhihu.com/question/20899988/answer/24923424?utm_campaign=official_account&utm_source=weibo&utm_medium=zhihu&utm_content=answer)
知乎上关于爬虫的一个很好的讲解，里面涉及到集群爬虫，不过用的是python.

#### 7. [Git 教學(1) : Git 的基本使用](http://blog.gogojimmy.net/2012/01/17/how-to-use-git-1-git-basic/)
git 入门教程，写的很详细很好，第二篇[Git 教學(2)：Git Branch 的操作與基本工作流程](http://blog.gogojimmy.net/2012/01/21/how-to-use-git-2-basic-usage-and-worflow/)讲解git下多人协作的流程。




