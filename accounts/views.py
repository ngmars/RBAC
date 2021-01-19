from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def createRole(request):
    if request.method == "POST":
        try:
            group = Group.objects.create(name=request.POST.get("group_name"))
        except:
            return HttpResponse("Group name already exists")

        for i in request.POST.getlist("permissions"):
            group.permissions.add(Permission.objects.get(pk=int(i)))
            group.save()
        return HttpResponse("Group Created")

    if request.method == "GET":
        context = {"permissions": Permission.objects.all()}
        return render(request, "accounts/createRole.html", context)


def assignRole(request):
    if request.method == "POST":
        pass
    if request.method == "GET":
        pass
