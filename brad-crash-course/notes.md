project - entire website
app - can be many in single project

# Django Crash Course Commands

```bash
# Install pipenv
pip install pipenv
```

```bash
# Create Venv
pipenv shell
```

```bash
# Install Django
pipenv install django
```

```bash
# Create project
django-admin startproject pollster
cd pollster
```

```bash
# Run server on http: 127.0.0.1:8000 (ctrl+c to stop)
python manage.py runserver
```

```bash
# Run initial migrations
python manage.py migrate
```

```bash
# Create polls app
python manage.py startapp polls
```

```bash
# Create polls migrations
python manage.py makemigrations polls
```

```bash
# Run migrations
python manage.py migrate
```

```bash
# Using the shell
python manage.py shell

>>>  from polls.models import Question, Choice
>>>  from django.utils import timezone
>>>  Question.objects.all()
>>>  q = Question(question_text="What is your favorite Python Framework?", pub_date=timezone.now())
>>>  q.save()
>>>  q.id
>>>  q.question_text
>>>  Question.objects.all()
>>>  Question.objects.filter(id=1)
>>>  Question.objects.get(pk=1)
>>>  q = Question.objects.get(pk=1)
>>>  q.choice_set.all()
>>>  q.choice_set.create(choice_text='Django', votes=0)
>>>  q.choice_set.create(choice_text='Flask', votes=0)
>>>  q.choice_set.create(choice_text='Flask', votes=0)
>>>  q.choice_set.all()
>>>  quit()
```

```bash
# Create admin user
python manage.py createsuperuser
```

```bash
# Create pages app
python manage.py startapp pages
```
