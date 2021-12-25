from psaw import PushshiftAPI
import datetime as dt

api = PushshiftAPI()

TechNews_Subreddits = ["technews","hardware","Technology"]
CyberSecNews = ["netsec","privacy","nordvpn","hackernews", "infoSecNews"]
Economics = ["Economics", "economy"]
start_epoch = int(dt.datetime(2021, 12, 23).timestamp())

subm = list(api.search_submissions(after=start_epoch,
                                   subreddit='netsec',
                                   filter=['url', 'author',
                                           'title', 'subreddit'],
                                   ))
for sub in subm:
    print(sub.title)
    print(sub.url)

