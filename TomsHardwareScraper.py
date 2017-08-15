import datetime
import newspaper
from newspaper import ArticleException

business_insider_paper = newspaper.build("http://www.tomshardware.com/articles/news/?sort=publish_date&sortdir=desc", memoize_articles = False)

for article in business_insider_paper.articles:

    print(article.url)

    article.download()
    try:
        article.parse()
    except ArticleException:
        pass


    this_file = open(str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.') + '.txt', mode = 'w')
    this_file.write(article.title)
    this_file.write("\n")
    this_file.write(article.text)
    this_file.write("\n")
    this_file.write(str(article.publish_date))
    this_file.close()

    print(article.publish_date)
    print(article.title)
    print(article.text)