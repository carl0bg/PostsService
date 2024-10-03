from django.db import models
from TestUser.models import User


class BlacklistedToken(models.Model):

    id = models.BigAutoField(primary_key=True, serialize=False)
    user = models.CharField(max_length=255)

    jti = models.CharField(unique=True, max_length=255)

    class Meta:
        ordering = ("user",)
        db_table = 'blacklist'

    def __str__(self) -> str:
        return f"Token for {self.user} - jti: {self.jti}"



# class BlacklistedToken(models.Model):
#     '''уже токены в блэклисте'''
#     id = models.BigAutoField(primary_key=True, serialize=False)
#     token = models.OneToOneField(OutstandingToken, on_delete=models.CASCADE)

#     blacklisted_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'Blacklist'


#     def __str__(self) -> str:
#         return f"Blacklisted token for {self.token.user}"
