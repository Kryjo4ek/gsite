
from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    #url(r'^1/', 'vote.views.one'),

    url(r'^vote/answer/', 'vote.views.answerall'),
    url(r'^vote/addcomment/(?P<votes_id>\d+)/$', 'vote.views.addcomment'),
    url(r'^like/add/(?P<votes_id>\d+)/$', 'vote.views.addlike'),
    url(r'^page/(\d+)/(\d+)/$', 'vote.views.onevote'),
    url(r'^votes/get/(?P<votes_id>\d+)/$', 'vote.views.onevote'),

    url(r'^', 'vote.views.all'),



]
