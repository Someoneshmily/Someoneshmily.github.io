from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^data/$', views.data),
    url(r'^formdata/$' ,views.formdata),
    url(r'^create/$', views.create),
    url(r'^delete/$', views.delete),
    url(r'^edit/$', views.edit),
    url(r'^findAll/$', views.findAll),
    url(r'^edit_content/(\d+)/$', views.edit_html),
    # url(r'^find_one/(\d+)/$', views.findOne),
    url(r'^leave_msg/$', views.leave_msg),
    url(r'^create_msg/$', views.create_msg),
    url(r'^msg_data/$', views.msg_data),

]