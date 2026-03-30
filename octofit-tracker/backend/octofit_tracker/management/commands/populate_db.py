from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Define models for teams, activities, leaderboard, and workouts
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create teams
        marvel = app_models.Team.objects.create(name='Team Marvel')
        dc = app_models.Team.objects.create(name='Team DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create activities
        app_models.Activity.objects.create(user=ironman, type='run', duration=30)
        app_models.Activity.objects.create(user=captain, type='cycle', duration=45)
        app_models.Activity.objects.create(user=batman, type='swim', duration=60)
        app_models.Activity.objects.create(user=superman, type='run', duration=50)

        # Create workouts
        app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
        app_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes')

        # Create leaderboard
        app_models.Leaderboard.objects.create(user=ironman, points=100)
        app_models.Leaderboard.objects.create(user=batman, points=120)
        app_models.Leaderboard.objects.create(user=superman, points=110)
        app_models.Leaderboard.objects.create(user=captain, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
