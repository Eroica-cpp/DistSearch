Liu Zhuode's activity Log
===============
This file is used for recording my activity with respect to the project.

Notations:  
$NUTCH: the directory where nutch lies.  
$SOLR : the directory where solr lies.  

### 2014-06-13 12:00:00
## <font color="red"> Impress.js </font>
is good, with a super good example [hashdog](http://www.hashdog.com/brochure/#/how), and I decided to use it as the templete for our presentation.  

## HTTrack
is super good! It is just a advanced, easy-to-use, GUI version of Nutch. It has a lot of customization parameters, really really flexible.


### 2014-06-07 9:00:00
##### !IMPORTANT! This log is instructions on how to run Nutch in Eclipse and change Nutch's source codes
In the log of **2014-06-04 9:00** I mentioned the nutch's inability to crawl webpages disallowed by robots.txt. Now I found a blog article on how to make Nutch ignore robots.txt via changing its source codes:  
http://lc87624.iteye.com/blog/1625677  
The prerequisites for this is that I have to run Nutch in Eclipse. 
Here is the tutorial: http://wiki.apache.org/nutch/NutchTutorial (in Sec.1 Set up from the source distribution). But this
tutorial is WRONG, and could not get nutch imported in Eclipse. The tutorial suggests to read [Running Nutch in Eclipse](http://wiki.apache.org/nutch/RunNutchInEclipse), I installed all the plugins mentioned in that webpage. But when I came to

      Run this command:
        ant eclipse
     
I got an error: 

      .....
      BUILD FAILED
      ....
      org.apache.thrift#thrift;0.2.0: not found
      ....
   
So I turned to another tutorial and successfully get nutch imported in Eclipse: [nutch 1.7 导入 eclipse 其他版本亦可参考。](http://blog.csdn.net/leave00608/article/details/21468871)   
Then I could modify the source codes for nutch. 

##### Next comes a special step:
* After I completed modifying the codes of org.apache.nutch.fetcher.Fetcher, I have Eclipse build the project.
* Eclipse will release the compiled .class files in $PROJECT_DIR/bin/org/apache/nutch/fetcher
* !IMPORTANT! I copied all the .class files, and use them to replace my original binary nutch installation's corresponding files --- $NUTCH/lib/**apache-nutch-1.8.jar**/org/apache/nutch/fetcher
* Note that
   1. I have to open .jar file with an archieve viewer.
   2. I have to replace ALL .class files in fetcher/, not just Fetcher.class --- coz I tried to do so and got an JAVA Exception from fetcher when crawling. 


### 2014-06-04 9:00
(contents below are copied directly from github issue)  
>我已经设置了conf/regex-urlfilter.txt注释掉这一条规则：  
>\# skip URLs containing certain characters as probable queries, etc.  
>-[?*!@=]   
>让它不过滤公文通的网页。  
>同时也把seed.txt的内容删掉， 只填写一条http://www.szu.edu.cn/board/ ，  
>让它爬公文通， 它还是不爬。 不知道怎么回事了。  
   


Now I figured out what happened. The webpage is filtered out by robots.txt. Even though robots.txt is located in http://www.szu.edu.cn/robots.txt , NOT in http://www.szu.edu.cn/board/robots.txt, nutch still tries to find robots.txt in http://www.szu.edu.cn/board/ 's parent domain http://www.szu.edu.cn/ and obviously nutch successfully finds it.

That's how I figure out this:  
Nutch has a useful feature---dumping its crawl database.  
1.bin/nutch readdb -dump SZU_Crawl_3/crawldb/ DUMPCRAWLDB3  

      http://www.szu.edu.cn/board/    Version: 7
      Status: 3 (db_gone)
      Fetch time: Sat Jul 19 17:00:05 CST 2014
      Modified time: Thu Jan 01 08:00:00 CST 1970
      Retries since fetch: 0
      Retry interval: 3888000 seconds (45 days)
      Score: 1.0
      Signature: null
      Metadata:
             _pst_=robots_denied(18), lastModified=0  

The last line clearly indicates : ROBOTS_DENIED(18)  
Now let's see what's in the other two databases using command readseg and readlinkdb  

2.bin/nutch readlinkdb SZU_Crawl_2/linkdb/ -dump DUMPLINKDB2  

      http://aec.szu.edu.cn/  Inlinks:  
      fromUrl: http://www.szu.edu.cn/2014/news/index_82.html anchor: 社会培训  
      fromUrl: http://www.szu.edu.cn/2014/news/702.html anchor: 社会培训  
      fromUrl: http://www.szu.edu.cn/2014/news/2533.html anchor: 自学考试招生  
      fromUrl: http://www.szu.edu.cn/2014/news/1862.html anchor: 自学考试招生  
      fromUrl: http://www.szu.edu.cn/2014/news/180.html anchor: 成人高等教育  
      ..............   
      
3.bin/nutch readseg SZU_Crawl_3/segments/20140604170003/ TESTDUMP  

      Recno:: 0  
      URL:: http://www.szu.edu.cn/board/  
      ..........  
      CrawlDatum::    
      Version: 7    
      Status: 37 (fetch_gone)    
      Fetch time: Wed Jun 04 17:00:05 CST 2014  
      Modified time: Thu Jan 01 08:00:00 CST 1970  
      Retries since fetch: 0  
      Retry interval: 2592000 seconds (30 days)  
      Score: 1.0  
      Signature: null  
      Metadata:  
             _ngt_=1401872401245  
             _pst_=robots_denied(18), lastModified=0  

尝试使用`bin/nutch freegen`手动生成含有一个公文通消息的网址的segment, 结果跟上面一样，仍然含有如下信息：  

            _pst_=robots_denied(18), lastModified=0


### 2014-06-02 9:00
!IMPORTANT! I found the crawler is ill-configured because it is trying to crawl outside the domain of szu.edu.cn.  
I stopped the crawler, cleaned the out-of-szu.edu.cn data of the crawlers by:  
1. corrected conf/regex-urlfilter.txt --- where the ill configuration lies.
2. run bin/nutch mergedb NEW_DB_PATH OLD_DB_PATH -filter
3. run bin/nutch mergelinkdb NEW_DB_PATH OLD_DB_PATH -filter
4. substitute the new DB for the old DB. 
5. I know this from http://www.blogjava.net/kxx129/archive/2009/09/05/294000.html , where there are info about "mergedb".

!IMPORTANT! Then I recrawled and  by examining the output,
I found that nutch crawlled a lot at the first few iterations.  
But after that it only crawlled few webpages in every iteration. This is an indicator that SZU have been fully crawlled.
Every page in SZU has been crawlled.

##### !IMPORTANT! I am skeptical about this. I think the action described above --- "I stopped the crawler, cleaned the out-of-szu.edu.cn data of the crawlers" might have caused other changes, perhaps filtering out some SZU urls, thus causing the crawler cannot find any outlinks.  
So I started another brand-new crawlling: $NUTCH/SZU_Crawl_2, using the corrected configuration described above, 
because a new crawlling is more "pure" than the previous one and is unaffected by the potential side-effect of "mergedb", "mergelinkdb".

cmdline used: bin/mycrawl urls/SZUseed.txt SZU_Crawl_2 http://localhost:8983/solr 100 | tee SZU_Crawl_2_20140602.out


### 2014-06-01 23:00
Finished the configuration of nutch, which is basically working on the files in $NUCTH/conf/.   
Then I started my first crawl, it is placed in SZU_Crawl_1. Output of nutch >> SZU_Crawl_1_20140601.out .
