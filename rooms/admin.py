from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    pass


# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "Spaces",
            {
                "fields": (
                    "guests",
                    "beds",
                    "bedrooms",
                    "baths",
                )
            },
        ),
        (
            "More About the Spaces",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "city",
        "country",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "description",
        "count_amenities",
    )

    ordering = (
        "name",
        "price",
        "bedrooms",
    )

    list_filter = (
        "host__superhost",
        "host__gender",
        "instant_book",
        "city",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "country",
    )

    search_fields = ("city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj):
        print(obj.amenities.all())
        return obj.amenities.all()[0]

    count_amenities.short_description = "amentiy"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ """

    pass
