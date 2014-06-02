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

##### !IMPORTANT! I am skeptical about this. I think the action described above --- "I stopped the crawler, cleaned the out-of-szu.edu.cn data of the crawlers by:  "
might have causes other changes, perhaps filtering out some SZU urls, thus causing the crawler cannot find any outlinks.  
So I started another brand-new crawlling: $NUTCH/SZU_Crawl_2, using the corrected configuration described above, 
because a new crawlling is more "pure" than the previous one and is unaffected by the potential side-effect of "mergedb", "mergelinkdb".

