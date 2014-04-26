ElasticSearch, Sphinx, Lucene, Solr, Xapian. Which fits for which usage?=========================
link:
[http://stackoverflow.com/questions/2271600/elasticsearch-sphinx-lucene-solr-xapian-which-fits-for-which-usage](http://stackoverflow.com/questions/2271600/elasticsearch-sphinx-lucene-solr-xapian-which-fits-for-which-usage)

Answer 
===============
As the creator of ElasticSearch, maybe I can give you some reasoning on why I went ahead and created it in the first place :).

Using pure Lucene is challenging. There are many things that you need to take care for if you want it to really perform well, and also, its a library, so no distributed support, its just an embedded Java library that you need to maintain.

In terms of Lucene usability, way back when (almost 6 years now), I created Compass. Its aim was to simplify using Lucene and make everyday Lucene simpler. What I came across time and time again is the requirement to be able to have Compass distributed. I started to work on it from within Compass, by integrating with data grid solutions like GigaSpaces, Coherence and Terracotta, but its not enough.

At its core, a distributed Lucene solution needs to be sharded. Also, with the advancement of HTTP and JSON as ubiquitous APIs, it means that a solution that many different systems with different languages can easily be used.

This is why I went ahead and created ElasticSearch. It has a very advanced distributed model, speaks JSON natively, and exposes many advanced search features, all seamlessly expressed through JSON DSL.

Solr is also a solution for exposing an indexing/search server over HTTP, but I would argue that ElasticSearch provides a much superior distributed model and ease of use (though currently lacking on some of the search features, but not for long, and in any case, the plan is to get all Compass features into ElasticSearch). Of course, I am biased, since I created ElasticSearch, so you might need to check for yourself.

As for Sphinx, I have not used it, so I can't comment. What I can refer you is to this thread at Sphinx forum which I think proves the superior distributed model of ElasticSearch.

Of course, ElasticSearch has many more features then just being distributed. It is actually built with cloud in mind. You can check the feature list on the site.
