Presentation
==============

1. 基本介绍
--------------

2. 特性
--------------
	1. 全文检索
	2. 搜索推荐
	3. 每周精选（邮件推送）
	4. 关键消息实时提醒

3. 大致流程
--------------

4. 深入讲解中间用的的算法和优化技术
--------------
	- Full text search
	- Recommender
		- Content-Based Method： deal with cold setup problem
			1. Text Feature Extraction
				- VSM (Vector Space Model)
				- LDA (Latent Dirichlet Allocation)
				- GMM (Gaussian Mixture Model)
			2. K-means
				- faced problem: sparse matrix
				- multi-level index
		- Memory-Based Method (Collaborative Filter)
			when we have certain amount of users and their behavior records
			1. item-based
			2. user-based 
		
