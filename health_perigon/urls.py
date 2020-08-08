from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings #register_form
from accounts.views import home,registerlink,partner_visibility,eventregister,eventtable,editevent,destroyevent, login_view, logout_view, contact, password_reset, contact_master, change_password, send_otp, verify_otp #existing_module_master, create_module_master, edit_module_master, destroy_module_master,addservice,addonservice,pharmacy,pharmacytable,lob,destroypharamcy,labotable,destroylaboratory,destroyemptytext,edit_laboratorytable,edit_service,edit_pharmacy,edit_labotable,laboratory
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),

    # path('register_form/',register_form, name="register_form"),
    path('contact/',contact, name="contact"),
    path('contact_master/',contact_master, name="contact_master"),

    path('password_reset/',password_reset, name="password_reset"),
    path('change_password/',change_password, name="change_password"),
    path('accounts/login/',login_view, name="login_view"),
    path('accounts/logout/',logout_view, name="logout_view"),
    path('send_otp/',send_otp, name="send_otp"),
    path('verify_otp/',verify_otp, name="verify_otp"),

    path('editevent/<int:module_id>',editevent, name="editevent"),
    path('destroyevent/<int:module_id>',destroyevent,name="destroyevent"),
    path('partner_visibility/',partner_visibility,name='partner_visibility'),
    path('eventregister/',eventregister,name="eventregister"),
    path('eventtable/',eventtable,name="eventtable"),
    path('registerlink/<int:module_id>',registerlink,name="registerlink"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

