from django.contrib import admin
from testapp.models import AndheriJob,ThaneJob,DadarJob
# Register your models here.
class AndheriJobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phone']

class ThaneJobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phone']


class DadarJobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phone']



admin.site.register(AndheriJob,AndheriJobAdmin)
admin.site.register(ThaneJob,ThaneJobAdmin)
admin.site.register(DadarJob,DadarJobAdmin)
