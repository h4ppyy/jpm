from django.http.response import JsonResponse


def create_post(request):
  return JsonResponse({"result": 200})


def read_post(request):
  return JsonResponse({"result": 200})


def update_post(request):
  return JsonResponse({"result": 200})


def delete_post(request):
  return JsonResponse({"result": 200})


def read_history(request):
  return JsonResponse({"result": 200})