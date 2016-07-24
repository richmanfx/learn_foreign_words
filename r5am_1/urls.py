from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^learn_foreign_words/', include('learn_foreign_words.urls')),
    url(r'^vhfdx_fd_locators/', include('vhfdx_fd_locators.urls')),
]
