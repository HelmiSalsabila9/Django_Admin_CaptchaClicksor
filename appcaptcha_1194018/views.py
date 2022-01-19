from django.shortcuts import render
from appcaptcha_1194018.forms import UserForm
from appcaptcha_1194018.models import Captcha_Clicksor

# Create your views here.
def index(request):
 return render(request, 'appcaptcha_1194018/index.html')

def user(request):
    user_list = Captcha_Clicksor.objects.order_by('name')
    user_dict = {"userform":user_list}
    return render(request,'appcaptcha_1194018/user.html',context=user_dict)

def form_view(request):
    form=UserForm()
    
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'appcaptcha_1194018/form_page.html',{'form':form})
