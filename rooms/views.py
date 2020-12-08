from math import ceil
from django.shortcuts import render
from . import models

# Create your views here.


def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    page_count = models.Room.objects.count() / ceil(page_size)
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(
        request,
        "rooms/home.html",
        context={
            "potato": all_rooms,
            "page": page,
            "page_count": int(page_count),
            "page_range": range(1, int(page_count) + 1),
        },
    )
