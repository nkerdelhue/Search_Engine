#Finish crawl web

def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):

    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
			
			
			
#Definition of the index, used to associate keyword to an url
#The data structure is a list of list [keyword1, [url1],[url2]....]...


#This function takes three arguments : the index, the keyword and an url associate
def add_to_index(index, keyword, url):
	for entry in index:
		if entry[0] == keyword :
			entry[1].append(url)
			return
	index.append([keyword, [url]])


def lookup(index, keyword):
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	
	return []

def add_page_to_index(index, url, content):
	words = content.split()
	for word in words:
		add_to_index(index, word, url)
		
		
def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index, page, content)
			union(tocrawl, get_all_links(content))
			crawled.append(page)
	
	return index
	
	
