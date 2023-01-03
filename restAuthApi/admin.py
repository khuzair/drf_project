from django.contrib import admin
from restAuthApi.models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# create custom user model admin
class UserModelAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'name', 'tc', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credintials', {'fields': ('email', 'password')}),  
        ('Personal info', {'fields': ('name','tc',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'tc', 'password1', 'password2'),  # these field show on the admin user careation page
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserModelAdmin)
