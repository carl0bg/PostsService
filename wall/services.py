from posts.models import Posts



class Feed:
    '''Service feeds'''
    def get_post_list(self, user):
        return Posts.objects.filter(user__owner__subscriber = user)\
            .order_by('-created_date')\
            .select_related('user')\
            .prefetch_related('comments')

    def get_single_post(self, pk: int):
        return Posts.objects.select_related('user').prefetch_related('comments').get(id = pk)

    # def get_post_list(self, user):
    #     return Posts.objects.filter(user__owner__subscriber=user).order_by('-created_date')\
    #         .select_related('user').prefetch_related('comments')

    
feed_service = Feed()