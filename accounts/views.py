from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Group, Permission, User
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
        user = User.objects.get(pk=int(request.POST.getlist('user')[0]))
        for role_id in request.POST.getlist('roles'):
            user.groups.add(Group.objects.get(pk=int(role_id)))
            user.save()
        return HttpResponse('Roles assigned successfully')

    if request.method == "GET":
        return render(request, 'accounts/assignRole.html', {
            'roles': Group.objects.all(), 'users': User.objects.all()
        })


def assignPermission(request):
    if request.method == 'POST':
        user = User.objects.get(pk=int(request.POST.getlist('user')[0]))
        for permission in request.POST.getlist('permissions'):
            user.user_permissions.add(Permission.objects.get(pk=int(permission)))
            user.save()
        return HttpResponse('Permissions added for the user successfully')
    
    return render(request, 'accounts/assignPermission.html', {
            'users': User.objects.all(), 'permissions': Permission.objects.all()
        })
