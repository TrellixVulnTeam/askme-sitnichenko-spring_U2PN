from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question, Tag, User, Answer
from django.db.models import Count

# Create your views here.


def pagination(list_obj, list_num, request):
    paginator = Paginator(list_obj, list_num)
    page = request.GET.get('page')
    content = paginator.get_page(page)

    return content


def index(request):
    content = pagination(Question.objects.all().annotate(num_answers=Count("answer", distinct=True)), 5, request)
    tags = Tag.objects.all()
    users = User.objects.all()
    user = request.user
    return render(request, "index.html", {'questions': content, 'tags': tags[:10], 'user': user, 'users': users[:10]})


def question(request, id):
    question = Question.objects.get_question_by_id(id)
    answers = pagination(Answer.objects.get_answers_by_id(id), 3, request)
    tags = Tag.objects.all()
    users = User.objects.all()
    user = request.user
    return render(request, "question_page.html", {'answers': answers, 'question': question, 'tags': tags[:10], 'user': user, 'users': users[:10]})


def hot(request):
    content = pagination(Question.objects.all(), 5, request)
    tags = Tag.objects.all()
    users = User.objects.all()
    user = request.user
    return render(request, "hot.html", {'questions': content, 'tags': tags[:10], 'user': user, 'users': users[:10]})


def login(request):
    tags = Tag.objects.all()
    users = User.objects.all()
    user = request.user
    return render(request, "login.html", {'tags': tags[:10], 'user': user, 'users': users[:10]})


def settings(request):
    tags = Tag.objects.all()
    users = User.objects.all()
    user = request.user
    return render(request, "settings.html", {'tags': tags[:10], 'user': user, 'users': users[:10]})


def register(request):
    tags = Tag.objects.all()
    users = User.objects.all()
    user = request.user
    return render(request, "register.html", {'tags': tags[:10], 'user': user, 'users': users[:10]})


def tag_listing(request, tagname):
    content = pagination(Question.objects.get_questions_by_tag(tagname), 5, request)
    tags = Tag.objects.all()
    users = User.objects.all()
    user = request.user
    return render(request, "tag_listing.html", {"questions": content, "tag": tagname, 'tags': tags[:10], 'user': user, 'users': users[:10]})


def question_form(request):
    tags = Tag.objects.all()
    users = User.objects.all()
    user = request.user
    return render(request, "question_form.html", {'tags': tags[:10], 'user': user, 'users': users[:10]})

