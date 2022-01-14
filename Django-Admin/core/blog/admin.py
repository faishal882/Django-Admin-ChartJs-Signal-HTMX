from django.contrib import admin
from django.contrib import messages
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

# from django import forms
# import django.apps
# TEXT = 'Some text that we can include'


class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Database"
    login_template = 'blog/admin/login.html'


class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


class TestAdminPermission(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        # return obj is None or obj.title != "fdfdsds"
        if obj != None and request.POST.get('action') == 'delete_selected':
            messages.add_message(request, messages.ERROR, (
                "I really hope you are sure about this!"
            ))
        return True

    def has_view_permission(self, request, obj=None):
        return True


blog_site = BlogAdminArea(name='BlogAdmin')

blog_site.register(Post, TestAdminPermission)
admin.site.register(Post, SummerAdmin)
admin.site.register(Category)

# class PostForm(forms.ModelForm):
#  def __init__(self, *args, **kwargs):
#      super(PostForm, self).__init__(*args, **kwargs)
#      self.fields['title'].help_text = 'New Help Text'

#      class Meta:
#          model = Post
#          exclude = ('slug',)


# class PostFormAdmin(admin.ModelAdmin):
#      form = PostForm

# admin.site.register(Post, PostFormAdmin)


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#  fieldsets = [
#    ('Section1', {
#         'fields': ('title', 'author'),
#         'description': '%s' % TEXT,
#    }),
#    ('Section2', {
#         'fields': ('slug',),
#         'classes': ('collapse',),
#    })
#  ]

# models = django.apps.apps.get_models()
# print(models)

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

# admin.site.register(Category)
# admin.site.register(Post)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#  fields = ['title', 'author']


# class BlogAdminArea(admin.AdminSite):
#  site_header = "Blog Admin Area"

# blog_site = BlogAdminArea(name='BlogAdmin')

# blog_site.register(post)
