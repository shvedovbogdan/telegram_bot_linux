import feedparser


def feed_parser():
    # Первое сообщение
    NewsFeed = {'Custudio_Реестр': 'https://custudio.pp.ua/rss/',

                # Второе сообщение
                }
    message = dict()
    for key in NewsFeed.keys():
        current_news = feedparser.parse(NewsFeed[key]).entries[0]
        message[key] = current_news.title + '\n' + current_news.link
    return message
