from django.contrib import admin
from accounts.models import CustomUser,Eventregisterationuser,Eventregister1 #AddOnServices,pharamcytab,Emptytext,Labour,Empty,Eventregister1, ModuleMaster,

admin.site.register(CustomUser)

class Eventregisteradmin(admin.ModelAdmin):
    list_display = ['user', 'header_eventimage', 'ticker_content','active']
    list_filter = ['user', 'header_eventimage', 'ticker_content','active']
    search_fields = ['user']

admin.site.register(Eventregisterationuser,Eventregisteradmin)


@admin.register(Eventregister1)
class Eventregister1Admin(admin.ModelAdmin):
    list_display = (
    'id', 'eventtitle', 'targetaudiance', 'eventtype', 'created_on', 'Chairpersons', 'name', 'mobilenumber', 'email',
    'Moderatorname', 'mmobile', 'memail', 'ContactPersonanme', 'Cmobile', 'Cemail', 'organizedby', 'sponserby',
    'Registerationrequired', 'paymentrequired', 'partnerrequired')

    def trip_link(self, obj):
        if obj.eventtitle:
            return "<a href='dynamic.html'>Link</a>" % obj.eventtitle
        else:
            return ''

# Register your models here.
# @admin.register(AddOnServices)
# class AddOnServicesAdmin(admin.ModelAdmin):
#    list_display=('id','add_onservices','add_on_servicescode','amount','cgst','sgst','gst')
# # Register your models here.
# @admin.register(ModuleMaster)
# class ModuleMasterAdmin(admin.ModelAdmin):
#     fields = ('module_name','module_code','no_of_patients','web_space','amount','cgst','sgst','gst','total_amount','updated_on','created_on')
#
#
# @admin.register(pharamcytab)
# class pharamcytabAdmin(admin.ModelAdmin):
#    list_display=('id','companyname','addresslineone','addresslinetwo','streetname','city','country','state','pincode','nationalhead','contactnumber','emailaddress','phonenumber','regionalhead','regionalcontactnumber','regionalemailaddress','regionalphonenumber','scientifichead','scientificcontactnumber','scientificemailaddress','scientificphonenumber','updated_on','created_on')
#
#
#
# @admin.register(Emptytext)
# class EmptytextAdmin(admin.ModelAdmin):
#     list_display=('id','froms','to','gender','umo1','umo2','conversationfactor','refrencerange','high')
#
# @admin.register(Labour)
# class LabourAdmin(admin.ModelAdmin):
#     list_display=('id','investigationname','synonyms','importantnotes','selectdropdownlist','select')
#     radio_fields={'selectdropdownlist':admin.VERTICAL}
#
# @admin.register(Empty)
# class EmptyAdmin(admin.ModelAdmin):
#     list_display=('id','froms','to','gender','umo1','umo2','conversationfactor','refrencerange','high')

