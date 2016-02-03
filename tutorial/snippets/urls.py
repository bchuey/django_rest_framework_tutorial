from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

# app_name = 'snippets'

"""
Bind ViewSet classes into set of concrete views
"""

snippet_list = SnippetViewSet.as_view({
	'get': 'list',
	'psot': 'create',
})

snippet_detail = SnippetViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy',
})

snippet_highlight = SnippetViewSet.as_view({
	'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
	'get': 'list'
})

user_detail = UserViewSet.as_view({
	'get': 'retrieve'	
})


urlpatterns = [
	url(r'^$', api_root),
	url(r'^users/$', user_list, name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
	url(r'^snippets/$', snippet_list, name='snippet-list'),
	url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
	url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
]


urlpatterns = format_suffix_patterns(urlpatterns)