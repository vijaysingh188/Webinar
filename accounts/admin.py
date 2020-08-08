from django.contrib import admin
from accounts.models import CustomUser,Eventregisterationuser,Webregister #AddOnServices,pharamcytab,Emptytext,Labour,Empty,Eventregister1, ModuleMaster,

admin.site.register(CustomUser)

class Eventregisteradmin(admin.ModelAdmin):
    list_display = ['id','ticker_content']
    list_filter = ['ticker_content']


admin.site.register(Eventregisterationuser,Eventregisteradmin)


@admin.register(Webregister)
class WebregisterrAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'eventtitle', 'targetaudiance', 'eventtype', 'created_on', 'Chairpersons', 'name', 'mobilenumber', 'email',
    'Moderatorname', 'mmobile', 'memail', 'ContactPersonanme', 'Cmobile', 'Cemail', 'organizedby', 'sponserby',
    'Registerationrequired', 'paymentrequired', 'partnerrequired')

    def trip_link(self, obj):
        if obj.eventtitle:
            return "<a href='dynamic.html'>Link</a>" % obj.eventtitle
        else:
            return ''
