from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def calculate(request):
    result = {'answer': ''}
    try:
        num1 = int(request.GET.get('num1'))
        num2 = int(request.GET.get('num2'))
        operator = request.GET.get('op')

        
        if operator == "add":
            result['answer'] = num1 + num2
        elif operator == "sub":
            result['answer'] = num1 - num2
        elif operator == "mul":
            result['answer'] = num1 * num2
        else:
            result['answer'] = num1 / num2
    except Exception as e:
        result['answer'] = str(e)

        

    return render(request, 'index.html', result)

def myfunc():
    return render(request, 'index.html', {'name':'nasir'})

def myfunc():
    return render(request, 'index.html', {'name':'nasir'})