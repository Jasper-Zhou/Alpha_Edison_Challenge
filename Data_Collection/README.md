# Data Collection Description

## Analysis
	
After look through the target pages, I notice that there are three layers of web pages need to be crawled, i.e home page, discussion page, and reply page (could be that there are multiple-reply pages for the same discussion).

## Procedure

Crawling: Build on Scrapy scripts to iteratively request discussion pages for each home page, and crawl required data on the discussion page. Moreover, I also repeatedly crawl discussion information if that discussion includes multi-page replies. All data as entries with JSON line format were written into a ‘.txt’ file. 
	
Post-processing: Replies should be merged into the same entry, if the same post includes multi-page replies. Considering scalability of the code, I used pyspark to merge replies into its corresponding entry.

## Data Structure

	{  
	   "690782":{  
	      "post":{  
		 "post_timestamp":"2019-01-09T15:47+00:00",
		 "writer":"sarah45050",
		 "post_content":"My stomach gets irritated with certain foods so I can eat  very little."
	      },
	      "reply":{  
		 "0":{  
		    "response_text":"The first thing to do is to see a doctor then we could take it from there.",
		    "response_time":"2019-01-09T16:12+00:00",
		    "responser":"lester90053"
		 },
		 "1":{  
		    "response_text":"Hi Sarah, sorry to hear you're struggling.",
		    "response_time":"2019-01-09T18:17+00:00",
		    "responser":"jeff4242"
		 }
	      }
	   }
	}

