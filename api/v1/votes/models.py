from django.db import models
from django.conf import settings
from api.v1.menus.models import MenuItem


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, related_name='votes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'menu_item')

    def __str__(self):
        return f"Vote by {self.user} for {self.menu_item}"
