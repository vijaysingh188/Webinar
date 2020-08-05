from django.contrib import admin
from django.urls import path
from accounts.views import home,partner_visbility, login_view, logout_view, contact, password_reset, contact_master, change_password, send_otp, verify_otp #existing_module_master, create_module_master, edit_module_master, destroy_module_master,addservice,addonservice,pharmacy,pharmacytable,lob,destroypharamcy,labotable,destroylaboratory,destroyemptytext,edit_laboratorytable,edit_service,edit_pharmacy,edit_labotable,laboratory,eventtable,eventregister,editevent,destroyevent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('partner_visbility/',partner_visbility,name='partner_visbility'),
    path('contact/',contact, name="contact"),
    path('contact_master/',contact_master, name="contact_master"),

    path('password_reset/',password_reset, name="password_reset"),
    path('change_password/',change_password, name="change_password"),
    path('accounts/login/',login_view, name="login_view"),
    path('accounts/logout/',logout_view, name="logout_view"),
    path('send_otp/',send_otp, name="send_otp"),
    path('verify_otp/',verify_otp, name="verify_otp"),

    # path('addservice/',addservice,name="addservice"),
    # path('addonservice/',addonservice,name="addonservice"),
    # path('pharmacy/',pharmacy,name="pharmacy"),
    # path('pharmacytable/',pharmacytable,name="pharmacytable"),
    # path('existing_module_master/',existing_module_master, name="existing_module_master"),
    # path('create_module_master/',create_module_master, name="create_module_master"),
    # path('edit_module_master/<int:module_id>',edit_module_master, name="edit_module_master"),
    # path('destroy_module_master/<int:module_id>',destroy_module_master, name="destroy_module_master"),
   
    # path('laboratorytable/',lob,name="laboratorytable"),
    # path('destroypharamcy/<int:module_id>',destroypharamcy,name="destroypharamcy"),
    # path('labotable/',labotable,name="labotable"),
    # path('destroylaboratory/<int:module_id>',destroylaboratory,name="destroylaboratory"),
    # path('destroyemptytext/<int:module_id>',destroyemptytext,name="destroyemptytext"),
    # path('edit_laboratorytable/<int:Labour>',edit_laboratorytable, name="edit_laboratorytable"),
    # path('edit_pharmacy/<int:module_id>',edit_pharmacy, name="edit_pharmacy"),
    # path('edit_service/<int:module_id>',edit_service, name="edit_service"),
    # path('laboratory/',laboratory ,name="laboratory"),
    # path('eventregister/',eventregister,name="eventregister"),
    # path('eventtable/', eventtable,name="eventtable"),
    # path('editevent/<int:module_id>',editevent, name="editevent"),
    # path('destroyevent/<int:module_id>',destroyevent,name="destroyevent"),
]
   


