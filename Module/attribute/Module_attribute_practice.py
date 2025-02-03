from pipelines import feeds

if hasattr(feeds, "feed_1"):
    print("1.Yes")
    lol = getattr(feeds, "feed_1")
    feed = lol.config
    if hasattr(feed, "feed_config"):
        print("2.yes")
        feed_config = getattr(feed, "feed_config")
        print("3", feed_config["feed_name"])
        if hasattr(feed_config, "feed_name"):
            print("3.yes")
        else:
            setattr(feed, "engine", "pandas")
            print(feed.engine)

# if hasattr(feeds, "feed_1"):
#     print("Yes")
# from Module.attribute.pipelines.feeds.finance.feed_1 import config

# print(config)

# print(pwd)
