from django.core.management.base import BaseCommand

from TestUser.models import User
from followers.models import Follower
from posts.models import Posts



class Command(BaseCommand):

    def handle(self, *args, **options):
        self.create_user()
        self.create_follower()
        self.create_post()
        self.stdout.write('Success')


    def create_user(self):
        for i in range(10):
            user = User.objects.create(
                username = f"username {i+2}",
                # email = f'email{i}@gmail.com',
                is_active = True,
                gender = 'male'
            )
            user.set_password(f'j0j0j{i}')
            user.save()


    def create_follower(self):
        user_list = User.objects.order_by()[2:]
        for user in user_list:
            Follower.objects.create(
                user = user,
                subscriber_id = 1,
            )


    def create_post(self):
        user_list = User.objects.all()
        for user in user_list:
            for i in range(10):
                Posts.objects.create(
                    text = f'TEST POST user{user.id} post {i}',
                    user = user,
                )