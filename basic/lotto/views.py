from django.shortcuts import render
import random
# Create your views here.
def lotto(reqeust) :

    Number = random.sample(range(1,46),6)
    Lotto_no = Number

    return render(reqeust,'lotto.html',{'Lotto_no' : Lotto_no})