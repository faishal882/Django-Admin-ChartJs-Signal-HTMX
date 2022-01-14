from django.contrib import admin
from .models import Profile


class EmailFilter(admin.SimpleListFilter):
    title = "Email Filter"
    parameter_name = "user_email"

    def lookups(self, request, model_admin):
        return (
            ('has_email', 'has_email'),
            ('no_email', 'no_email')
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'has_email':
            return queryset.exclude(user__email="")
        if self.value().lower() == 'no_email':
            return queryset.filter(user__email='')


class Filter(admin.ModelAdmin):
    list_display = ("id", "email", "created_at", "role", "is_active")
    list_filter = ("is_active", "role", "created_at", EmailFilter)


admin.site.register(Profile, Filter)


class BookstoreAdminArea(admin.AdminSite):
    site_header = "Bookstore Admin Area"


bookstore_site = BookstoreAdminArea(name='BookstoreAdmin')

# blog_site.register(post)
