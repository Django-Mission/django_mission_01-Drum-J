from django.shortcuts import render
import random
# Create your views here.

def lotto2 (request) :

    num1 = request.GET.get('num1')
    
    return render(request,'lotto2.html')

def lottor (request) :

    Lotto_no = list()
    for number in range(0,num1) :
        number = random.sample(range(1,46),6)
        Lotto_no.sort()
        Lotto_no.append(number)
        
        
    return render(request,'lottoresult.html',{'Lotto_no' : Lotto_no},{'game' : num1})