import bs4 as bs
import urllib.request
import csv
#number of scrapped pages
pages = 1

#Scrap quotes with specific tag. replace the 'love' with your wanted tag.
tag = "/tag/love" #leave empty for popular quotes

#scrapping loop for every pages
for page in range(1,pages+1):
    source = urllib.request.urlopen(f"https://www.goodreads.com/quotes{tag}?page={page}").read()
    soup = bs.BeautifulSoup(source, 'lxml')
    quotes = soup.find_all('div',class_='quoteText')
    quotes = list(quotes)
    
    #delete script tags & and take only the texts from tags
    texts = []
    for item in quotes:
        while item.script is not None:
            item.script.decompose()
        texts.append(item.get_text())
    
    #split quotes and authors
    authors = []
    words = []    
    for element in texts:
        elements = element.split('\n')
        words.append(elements[1].strip())
        elements[4] = elements[4].replace(',','')
        authors.append(elements[4].strip())
    
    #save to directory
    with open('quotes_with_author.tsv','a', encoding='utf8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(words,authors))
    print("page ",page,"has been harvested!")