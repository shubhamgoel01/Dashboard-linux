from django.contrib import admin
from Home.models import WebBeta1, WebBeta2, WebBeta3, WebBeta4, NewUpdateInfo, RRFImage
# Register your models here.
class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]



admin.site.register(RRFImage, imageAdmin)
admin.site.register(WebBeta1)
admin.site.register(WebBeta2)
admin.site.register(WebBeta3)
admin.site.register(WebBeta4)
admin.site.register(NewUpdateInfo)



