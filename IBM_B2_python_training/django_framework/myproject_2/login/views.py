from django.shortcuts import render, HttpResponse

# Create your views here.
def myloginpage(request):
    return render(request, 'login.html', {})

def myregisteruserpage(request):
    return render(request, 'registeruser.html',{})

def myaddnewuserpage(request):
    """
    1. Get data from front end
    2. save it in db table
    :param request:
    :return:
    """
    # 1. Get data from front end
    # -------------------
    # all data will be captured in a dictionary request.POST
    entered_username = request.POST.get('uname')
    entered_password_1 = request.POST.get('pw1')
    entered_password_2 = request.POST.get('pw2')
    entered_email = request.POST.get('email')
    # -------------------

    # 2. save it in db table
    # -------------------
    from .models import MyModel
    new_user_model = MyModel()
    new_user_model.name = entered_username
    new_user_model.password = entered_password_1
    new_user_model.email = entered_email
    new_user_model.save()

    return HttpResponse('User created successfully')
    # -------------------

def myvalidatepage(request):
    """

    :param request:
    :return:
    """
    entered_username = request.POST.get('uname')
    entered_password = request.POST.get('pw')

    from .models import MyModel
    # ------------------------------
    print("All Entries: ", MyModel.objects.all(), sep="\n")
    print("-"*20)
    # ------------------------------
    # ------------------------------
    print("Values: ", MyModel.objects.all().values(), sep="\n")
    print("-"*20)
    # ------------------------------

    # # ------------------------------
    # print("Username value: ", MyModel.objects.get(name=entered_username), sep="\n")
    # print("-" * 20)
    # # ------------------------------

    try:
        MyModel.objects.get(name=entered_username)
        # If we get something then no error and we can assume user present
        return HttpResponse('Login Success')
    except:
        return HttpResponse("Login Failed")