from django.contrib import admin

from .models import Flat, Complain, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'address']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'owners_phonenumber',
        'owner_pure_phone',
    ]
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by', )


class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'complain_address')
    list_display = [
        'user',
        'complain_address',
        'complain_text',
    ]


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    readonly_fields = ['owner_pure_phone']
    list_display = [
        'owner',
        'owner_pure_phone',
    ]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain, ComplainAdmin)
admin.site.register(Owner, OwnerAdmin)
