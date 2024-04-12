from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from profiles.models import UserProfile

class Command(BaseCommand):
    help = 'Creates UserProfile instances for all existing users'

    def handle(self, *args, **options):
        # Query all existing users
        users = User.objects.all()

        for user in users:
            # Check if a UserProfile instance already exists for the user
            if not hasattr(user, 'userprofile'):
                # Create a UserProfile instance based on user information
                UserProfile.objects.create(user=user, email=user.email, password=user.password)

        self.stdout.write(self.style.SUCCESS('Successfully created UserProfile instances for all existing users'))