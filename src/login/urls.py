from django.urls import path
from . import views # This Views I Created It
#
#
# # AUTHENTICATION:-------------------------------------------------------------------------------------------------------
urlpatterns = [
        # Display Login Web Page
        path('login_pag/' , views.login_page_DEF   ,  name='login_page-URL' ),
        path("login/"     , views.Login            , name="login"),
] 