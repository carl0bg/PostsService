# from django.conf import settings
from django.db import models
from TestUser.models import User


class OutstandingToken(models.Model):
    '''выданные токены'''
    id = models.BigAutoField(primary_key=True, serialize=False)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    jti = models.CharField(unique=True, max_length=255)
    token = models.TextField()

    created_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()

    class Meta:
        # abstract = ( #TODO 
        #     "rest_framework_simplejwt.token_blacklist" not in settings.INSTALLED_APPS
        # )
        ordering = ("user",)
        db_table = 'OutstRefresh'

    def __str__(self) -> str:
        return "Token for {} ({})".format(
            self.user,
            self.jti,
        )


class BlacklistedToken(models.Model):
    '''уже токены в блэклисте'''
    id = models.BigAutoField(primary_key=True, serialize=False)
    token = models.OneToOneField(OutstandingToken, on_delete=models.CASCADE)

    blacklisted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Blacklist'


    def __str__(self) -> str:
        return f"Blacklisted token for {self.token.user}"
