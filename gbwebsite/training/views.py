from django.shortcuts import render


def intro(request):
    return render(request, 'intro.html')


def part1(request):
    return render(request, 'part1.html')


def part2a(request):
    return render(request, 'part2a.html')


def part2b(request):
    return render(request, 'part2b.html')


def part3(request):
    return render(request, 'part3.html')


def part4(request):
    return render(request, 'part4.html')


def part5(request):
    user = request.user
    user.is_training_competed = True
    return render(request, 'part5.html')


def conclusion(request):
    return render(request, 'conclusion.html')
