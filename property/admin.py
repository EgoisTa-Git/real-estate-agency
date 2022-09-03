from django.contrib import admin

from .models import Flat, Complain, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner', )


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'address']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    ]
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by', )
    inlines = [
        OwnerInline,
    ]


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')
    list_display = [
        'user',
        'flat',
        'text',
    ]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ['name', 'pure_phone']
    list_display = [
        'name',
        'pure_phone',
    ]
