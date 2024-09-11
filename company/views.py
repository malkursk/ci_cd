"""Module description"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    """Function description"""
    return render(request, "index.html")


@login_required
def profile(request):
    """Function description"""
    user = request.user
    return render(request, "profile.html", {"user": user})
