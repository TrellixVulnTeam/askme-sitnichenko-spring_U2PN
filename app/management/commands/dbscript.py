from django.core.management.base import BaseCommand, CommandError

from app.models import (
    User,
    Tag,
    Question,
    Answer,
)

import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_tag()
        self.create_user()
        self.create_question()
        self.create_answers()

    def create_user(self):
        for i in range(10000):
            user = User()
            user.username = f'Username{i}'
            user.email = f'{i}@live.com'
            user.password = "qwerty"

            user.save()

    def create_tag(self):
        for i in range(10000):
            tag = Tag()
            tag.title = f'tag{i}'

            tag.save()

    def create_question(self):
        for i in range(100000):
            author = random.choice(User.objects.all())
            q = Question()
            q.title = f'Question {i}'
            q.text = f'How to do the {i} task?'
            q.author = author
            q.save()
            q.tags.add(random.choice(Tag.objects.all()))


    def create_answers(self):
        author = random.choice(User.objects.all())
        for i in range(1000000):
            answer = Answer()
            answer.text = f'answer {i}'
            answer.author = author
            answer.question = random.choice(Question.objects.all())
            answer.save()

