from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Captain America', email='cap@marvel.com', team=marvel),
            User(name='Batman', email='batman@dc.com', team=dc),
            User(name='Superman', email='superman@dc.com', team=dc),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create workouts
        workouts = [
            Workout(name='Cardio', description='Cardio workout', suggested_for='All'),
            Workout(name='Strength', description='Strength workout', suggested_for='Marvel'),
            Workout(name='Agility', description='Agility workout', suggested_for='DC'),
        ]
        for workout in workouts:
            workout.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date='2025-12-10')
        Activity.objects.create(user=users[3], type='Cycling', duration=45, calories=400, date='2025-12-10')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=250)
        Leaderboard.objects.create(team=dc, points=200)

        # Ensure unique index on email
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('Database populated with test data and unique index on email created.'))
