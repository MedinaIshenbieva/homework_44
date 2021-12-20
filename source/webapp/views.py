from django.shortcuts import render

# Create your views here.

def result(request):
    if request.method == 'GET':
        return render(request, 'numbers.html')   
    elif request.method == 'POST':
        context = {
        "result": ''

        }
        number = (request.POST.get('numbers').split())
        secret_nums = [1, 2, 3, 4]
        bulls = 0
        cows = 0
        if len(number) != 4:
            context['result'] = 'Enter four numbers'
        for n in number:
            if n >= 10:
                context['result'] = 'Enter less than 10'
        if len(number) != len(set(number)):
            context['result'] = 'Enter unique numbers'
        for i in range(len(number)):
            if secret_nums [i] == number[i]:
                bulls += 1
            elif number[i] in secret_nums:
                cows += 1
        if secret_nums == number:
            return "<h1>You got it right!</h1>"

    return render(request, 'numbers.html', context)