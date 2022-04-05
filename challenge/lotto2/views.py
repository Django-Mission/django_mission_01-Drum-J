from django.shortcuts import render
import random
# Create your views here.

def lotto2 (request) :
    num1 = request.GET.get('num1')

    return render(request,'lotto2.html',{'game' : num1})

def lottor (request) :
    num1 = request.GET.get('num1')
    Lotto_no = list()
    for number in range(0,int(num1)) :
        number = random.sample(range(1,46),6)
        number.sort()
        Lotto_no.append(number)
        
        
    return render(request,'lottoresult.html',{'Lotto_no' : Lotto_no, 'game' : num1})
    # 값을 2개 보낼때는 {}안에 ,로 구분해서 넣어야 하는 듯!
    # {'Lotto_no' : Lotto_no} ,{'game' : num1} 이렇게 넣었을때 자꾸 오류남
    # 이것때문에 계속 안되서 속상....