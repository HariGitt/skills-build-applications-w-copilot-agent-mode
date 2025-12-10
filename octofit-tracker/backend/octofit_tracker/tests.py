from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')
        self.user1 = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        self.user2 = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        self.workout = Workout.objects.create(name='Cardio', description='Cardio workout', suggested_for='All')
        self.activity = Activity.objects.create(user=self.user1, type='Running', duration=30, calories=300, date='2025-12-10')
        self.leaderboard = Leaderboard.objects.create(team=marvel, points=100)

    def test_user_team(self):
        self.assertEqual(self.user1.team.name, 'Marvel')
        self.assertEqual(self.user2.team.name, 'DC')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Running')
        self.assertEqual(self.activity.calories, 300)

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Cardio')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)
