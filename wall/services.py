from posts.models import Posts
from followers.models import Follower



def feed(user):
    # 1
    news = []
    subs = Follower.objects.filter(subscriber = user)
    for sub in subs:
        news.append(Posts.objects.filter(user = sub.user, created_date__hour = 1).order_by('-created_date'))

    
