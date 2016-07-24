from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', vhfdx_start_page, name='vhfdx_start_page'),
    # url(r'^load_file/', load_file, name='load_file'),
    # url(r'^dict_status_set/', dict_status_set, name='dict_status_set'),

]
