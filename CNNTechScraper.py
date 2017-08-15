import datetime
import newspaper

cnn_tech_paper = newspaper.build("http://money.cnn.com/technology/?iid=Tech_Nav", memoize_articles = False)

for article in cnn_tech_paper.articles:

    print(article.url)

    article.download()

    article.parse()

    this_file = open(str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.') + '.txt', mode = 'w')
    this_file.write(article.title)
    this_file.write("\n")
    this_file.write(article.text)
    this_file.write("\n")
    this_file.write(article.publish_date)
    this_file.close()

    print(article.publish_date)
    print(article.title)
    print(article.text)
