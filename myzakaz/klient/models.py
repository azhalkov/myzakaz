from django.db import models
from django.contrib.auth.models import AbstractUser


# https://docs-djangoproject-com.translate.goog/en/4.2/topics/auth/customizing/?_x_tr_sl=auto&_x_tr_tl=ru&_x_tr_hl=ru#auth-custom-user


class User(AbstractUser):
    phone = models.CharField(verbose_name=("телефон"), max_length=11,  unique=True, db_index=True, null=True)

    def __str__(self) -> str:
        return f"{self.phone}"
    
    class Meta(AbstractUser.Meta):
        # Comes from original Django Auth declaration
        swappable = "AUTH_USER_MODEL"
