Liu Zhuode's activity Log
===============
This file is used for recording my activity with respect to the project.

Notations:  
$NUTCH: the directory where nutch lies.  
$SOLR : the directory where solr lies.  


### 2014-06-01 23:00
Finished the configuration of nutch, which is basically working on the files in $NUCTH/conf/.   
Then I started my first crawl, it is placed in SZU_Crawl_1. Output of nutch >> SZU_Crawl_1_20140601.out .

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

### 2014-06-04 9:00
(contents below are copied directly from github issue)  
{content}  
>我已经设置了conf/regex-urlfilter.txt注释掉这一条规则：  
>\# skip URLs containing certain characters as probable queries, etc.  
>-[?*!@=]   
>让它不过滤公文通的网页。  
>同时也把seed.txt的内容删掉， 只填写一条http://www.szu.edu.cn/board/ ，  
>让它爬公文通， 它还是不爬。 不知道怎么回事了。  
>{end content}   

Now I figured out what happened. The webpage is filtered out by robots.txt. Even though robots.txt is located in http://www.szu.edu.cn/robots.txt , NOT in http://www.szu.edu.cn/board/robots.txt, nutch still tries to find robots.txt in http://www.szu.edu.cn/board/ 's parent domain http://www.szu.edu.cn/ and obviously nutch successfully finds it.

That's how I figure out this:
Nutch has a useful feature: dumping its crawl database.
1. bin/nutch readdb -dump SZU_Crawl_3/crawldb/ DUMPCRAWLDB3  
``
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

``  

##### The last line clearly indicates : ROBOTS_DENIED(18)  

Now let's see what's in the other two databases using command readseg and readlinkdb  
2. bin/nutch readlinkdb SZU_Crawl_2/linkdb/ -dump DUMPLINKDB2  
``
http://aec.szu.edu.cn/  Inlinks:  
 fromUrl: http://www.szu.edu.cn/2014/news/index_82.html anchor: 社会培训  
 fromUrl: http://www.szu.edu.cn/2014/news/702.html anchor: 社会培训  
 fromUrl: http://www.szu.edu.cn/2014/news/2533.html anchor: 自学考试招生  
 fromUrl: http://www.szu.edu.cn/2014/news/1862.html anchor: 自学考试招生  
 fromUrl: http://www.szu.edu.cn/2014/news/180.html anchor: 成人高等教育  
..............  
``  

3.  bin/nutch readseg SZU_Crawl_3/segments/20140604170003/ TESTDUMP  
``
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
``
