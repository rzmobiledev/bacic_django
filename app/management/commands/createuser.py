from django.db.utils import IntegrityError
from django.core.management import BaseCommand
from app.models import User

# log
from logger.log import Log


class Command(BaseCommand):
    """Calling database"""

    def create_user(
            self,
            name: str,
            username: str,
            email: str,
            password: str,
            admin: bool = False,
            staff: bool = False,
    ) -> User:
        staff = True if admin else staff
        try:
            user, created = User.objects.get_or_create(
                username=username,
                email=email,
                is_staff=staff,
                is_superuser=admin,
                is_active=True,
            )
            user.name = name
            user.set_password(password)
            user.save()

            self.stdout.write(self.style.SUCCESS(
                "User {} created".format(user.name)))
            return user

        except IntegrityError:
            Log.error("This email or user is already exists!")

    def handle(self, *args, **kwargs):
        user = (
            "rz",
            "rz",
            "admin@gmail.com",
            "password123",
            True,
            True,
        )
        self.create_user(*user)
