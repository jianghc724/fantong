from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.bbs_list, name='index'),
    url(r'^personal/(\w+)/(\w*)$', views.get_user, name='personal'),
    url(r'^accounts/profile/$', views.update_time),
    url(r'^accounts/profile/$', views.update_time),
    url(r'changepassword/(.+)/$', views.change_password),
    url(r'^bbs_post_detail/(\d+)/(\w*)$', views.bbs_post_detail, name='postDetail'),
    url(r'changeimage/(.+)/$', views.change_image),
    url(r'^follow_user_deal/$', views.follow_user_deal),
    url(r'^ajax_deal/$', views.ajax_deal),
    url(r'^ajax_change_nickname/(\w+)/$', views.ajax_change_nickname),
    url(r'^ajax_append_image/$', views.ajax_append_image),
    url(r'^ajax_append_files/$', views.ajax_append_files),
    url(r'^search/post/(\w+)/$', views.search_postbycontent),
    url(r'^search/user/(\w+)/$', views.search_userbyusername),
    url(r'^follow_post_deal/$', views.follow_post_deal),
    url(r'^like_post_deal/$', views.like_post_deal),
    url(r'^delete_post_deal/$', views.delete_post_deal),
    url(r'^ajax_get_tag/$', views.ajax_get_tag),
    url(r'^search_by_tag/(.+)/$', views.search_by_tag),
    url(r'^forbid_user_deal/$', views.forbid_user_deal),
    url(r'^delete_user_deal/(\w+)/$', views.delete_user_deal),
    url(r'^rank/(\w+)/$', views.rank),
    url(r'^top_post_deal/$', views.top_post_deal),
]
