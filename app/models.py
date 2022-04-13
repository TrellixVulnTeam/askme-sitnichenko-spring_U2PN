from django.db import models
from django.db.models import Count

# Create your models here.


class UserManager(models.Manager):
    def all_users(self):
        return self.all()

    def get_user_by_id(self, id):
        return self.get(id=id)


class QuestionManager(models.Manager):
    def get_question_by_id(self, id):
        return self.get(id=id)

    def get_questions_by_tag(self, tagname):
        tag = Tag.objects.get(title=tagname)
        result = self.filter(tags=tag)
        print(result)
        return result

    def get_question_by_popular(self):
        return (
            self.all()
                .annotate(
                num_likes=Count("questionlikes", distinct=True),
                num_answers=Count("answer", distinct=True),
            )
                .order_by("-num_likes")[:10]
        )

    def get_question_by_date(self):
        return (
            self.all()
                .annotate(
                num_likes=Count("questionlikes", distinct=True),
                num_answers=Count("answer", distinct=True),
            )
                .order_by("-create_date")
        )

    # def create_question(self, author, title, text, tags):
    #     question = self.model(
    #         author=author,
    #         title=title,
    #         text=text,
    #     )
    #
    #     question.save()


class User(models.Model):
    username = models.CharField(max_length=256)
    email = models.EmailField()
    password = models.CharField(max_length=256)


class TagManager(models.Manager):
    def all_tags(self):
        return self.all()

    def get_tag_by_name(self, name):
        return self.get(title=name)

    # def create_tag(self, title):
    #     tag = self.model(title=title)
    #
    #     tag.save()


class Tag(models.Model):
    objects = TagManager()
    title = models.CharField(max_length=50, verbose_name="Tag")

    def __str__(self):
        return self.title


class Question(models.Model):
    objects = QuestionManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    # create_date = models.DateField(auto_now=True, auto_now_add=True)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=1000)


class AnswerManager(models.Manager):
    def all_answers(self):
        return self.all()

    def get_answers_by_id(self, id):
        return self.filter(question__id=id)

    # def create_answer(self, author, question, text):
    #     answer = self.model(
    #         author=author,
    #         question=question,
    #         text=text,
    #     )
    #
    #     answer.save()
    #
    #     return answer


class Answer(models.Model):
    objects = AnswerManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    text = models.TextField(verbose_name="Answer text")
    is_correct = models.BooleanField(default=False, verbose_name="Answer corrective")

    def __str__(self):
        return self.text

