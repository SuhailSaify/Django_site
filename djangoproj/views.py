from django.shortcuts import render


def home_page(request):
    content = "hello there..."
    return render(request, "dummy.html", {"content": content})
