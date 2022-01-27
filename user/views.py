from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
#사용자가 데이터베이스 안에 있는지 검사하는 함수




def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')  # 회원가입 화면 보여주기
    elif request.method == 'POST':
        username = request.POST.get('username', '')  # post로 데이터가져옴. 그중에 username, 없다면 None
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')
        # me = UserModel.objects.get(username=username)
        # if username == me.username:
        #     return render(request,'user/signup.html')

        if password != password2:
            #패스워드가 같지 않다고 알람
            return render(request, 'user/signup.html',{'error':'패스워드를 확인 해 주세요!'})
        else:
            if username =='' or password =='':
                return render(request, 'user/signup.html',{'error':'사용자 이름과 비밀번호를 작성해주세요'})
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:#exist_uer가 있다면
                return render(request,'user/signup.html',{'error':'사용자가 이미 존재합니다'})
            else:
                UserModel.objects.create_user(username=username,password=password,bio=bio)
                return redirect('/sign-in')  # 회원가입 완료되면 로그인페이지로


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        # 암호화된 비번과 입력된 비번이 일치하는지, 사용자와 맞는지 확인해서 me 라는 변수에 사용자를 넣어줌

        if me is not None:
            auth.login(request, me)
            return redirect('/')#tweet/urls
        else:
            return render(request, 'user/signin.html',{'error':'아이디 혹은 패스워드를 확인 해 주세요'})
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        return render(request, 'user/signin.html')
@login_required() #로그인이 되어있어야만 접근할 수 있음
def logout(request):
    auth.logout(request)
    return redirect('/')



# user/views.py

@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'user/user_list.html', {'user_list': user_list})


@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect('/user')