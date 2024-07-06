from django.contrib.auth.models import User


class CustomAuthUser:
    def __init__(self, roles=None):
        self.pk = 0
        self.is_authenticated = False
        self._roles = roles or []

    @property
    def roles(self):
        if self._roles:
            return self._roles
        else:
            user = User.objects.get(pk=self.pk)
            return [group.name for group in user.groups.all()]
