from django.contrib import admin
from myapp.models import Poll,Add_act

# Register your models here.

class AddAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Add_act._meta.fields]

class PollAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Poll._meta.fields]


admin.site.register(Add_act,AddAdmin)
admin.site.register(Poll,PollAdmin)
