from django.shortcuts import render


def index(request):
  post = [1,2,3,4,5,6]
  context = {}
  context['post'] = post
  return render(request, 'app/index.html', context)


def post(request, id):
  context = {}
  return render(request, 'app/post.html', context)


def manage(request):
  context = {}
  return render(request, 'app/manage.html', context)


def history(request):
  context = {}
  return render(request, 'app/history.html', context)