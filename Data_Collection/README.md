{\rtf1\ansi\ansicpg936\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;\f1\fnil\fcharset0 Menlo-Bold;}
{\colortbl;\red255\green255\blue255;\red83\green83\blue83;\red67\green67\blue67;\red38\green38\blue38;
}
{\*\expandedcolortbl;;\cssrgb\c40000\c40000\c40000;\cssrgb\c33333\c33333\c33333;\cssrgb\c20000\c20000\c20000;
}
\margl1440\margr1440\vieww25340\viewh15260\viewkind0
\deftab720
\pard\pardeftab720\sl380\partightenfactor0

\f0\fs32 \cf2 \expnd0\expndtw0\kerning0
# Data Collection Description\
\
## Analysis:\
	\
	After look through the target pages, I notice that there are three layers of web pages need to be crawled, i.e home page, discussion page, and reply page (could be that there are multiple reply pages for the same discussion).\
\
## Procedure:\
	\
	### Crawling: Build on Scrapy scripts to iteratively request discussion pages for each home page, and crawl required data on the discussion page. Moreover, I also repeatedly crawl discussion information if that discussion includes multi-page replies. All data as entries with JSON line format were written into a \'91.txt\'92 file. \
	\
	### Post-processing: Replies should be merged into the same entry, if the same post includes multi-page replies. Considering scalability of the code, I used pyspark to merge replies into its corresponding entry.\
\
## Data Structure:\
\'91\'92\'92\
\{\'a0\'a0\cf3 \
\'a0\'a0\'a0
\f1\b \cf4 "690782"
\f0\b0 \cf2 :\{\'a0\'a0\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "post"
\f0\b0 \cf2 :\{\'a0\'a0\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "post_timestamp"
\f0\b0 \cf2 :\cf3 "2019-01-09T15:47+00:00"\cf2 ,\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "writer"
\f0\b0 \cf2 :\cf3 "sarah45050"\cf2 ,\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "post_content"
\f0\b0 \cf2 :\cf3 "My\'a0stomach\'a0gets\'a0irritated\'a0with\'a0certain\'a0foods\'a0so\'a0I\'a0can\'a0eat\'a0\'a0very\'a0little."\
\'a0\'a0\'a0\'a0\'a0\'a0\cf2 \},\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "reply"
\f0\b0 \cf2 :\{\'a0\'a0\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "0"
\f0\b0 \cf2 :\{\'a0\'a0\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "response_text"
\f0\b0 \cf2 :\cf3 "The\'a0first\'a0thing\'a0to\'a0do\'a0is\'a0to\'a0see\'a0a\'a0doctor\'a0then\'a0we\'a0could\'a0take\'a0it\'a0from\'a0there."\cf2 ,\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "response_time"
\f0\b0 \cf2 :\cf3 "2019-01-09T16:12+00:00"\cf2 ,\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "responser"
\f0\b0 \cf2 :\cf3 "lester90053"\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf2 \},\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "1"
\f0\b0 \cf2 :\{\'a0\'a0\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "response_text"
\f0\b0 \cf2 :\cf3 "Hi\'a0Sarah,\'a0sorry\'a0to\'a0hear\'a0you're\'a0struggling."\cf2 ,\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "response_time"
\f0\b0 \cf2 :\cf3 "2019-01-09T18:17+00:00"\cf2 ,\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf4 "responser"
\f0\b0 \cf2 :\cf3 "jeff4242"\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf2 \}\cf3 \
\'a0\'a0\'a0\'a0\'a0\'a0\cf2 \}\cf3 \
\'a0\'a0\'a0\cf2 \}\cf3 \
\cf2 \}\
\'91\'92\'92}