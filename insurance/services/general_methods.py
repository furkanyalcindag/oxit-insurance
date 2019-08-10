from django.contrib.auth.models import User

from insurance.models import MenuAcente, MenuAnaAcente


def getMenu(request):
    menus =""
    if request.user.is_authenticated is True:
        user = User.objects.get(pk=request.user.id)
        if user.groups.all()[0].name == "Acente":
            menus = MenuAcente.objects.all()
        else:
            menus = MenuAnaAcente.objects.all()

    return {'menus': menus}
