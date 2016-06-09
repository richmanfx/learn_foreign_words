from django.conf.urls import url
from views import *

'''
urlpatterns = patterns('',
    url(r'^$', start_page, name='start_page'),
#    url(r'^popular/', question_popular, name='question_popular'),
#    url(r'^question/(?P<q_id>\d+)/', question, name='question'),
#    url(r'^ask/', ask_add, name='ask'),
#    url(r'^answer/', answer_add, name='answer'),
#    url(r'^signup/', signup, name='signup'),    
#    url(r'^login/', my_login, name='my_login'),
)
'''

urlpatterns = [
    url(r'^$', start_page, name='start_page'),
    url(r'^load_file/', load_file, name='load_file'),
    url(r'^dict_status_set/', dict_status_set, name='dict_status_set'),

]

