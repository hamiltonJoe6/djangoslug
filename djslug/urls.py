from django.urls import path, re_path
from . import views

app_name = "SimpleBlog"

urlpatterns = [
	path('index/', views.index, name="index"),
	path('index1/', views.index1, name="index1"),
	path('bd/<slug:slug>/<str:id>/', views.Blogdetail1, name="bd"),
	path('', views.BlogView, name="blogview"),
	path('detailview/<slug:slug>/<str:id>/', views.Blogdetail.as_view(), name='detail'),

	path('detailview1/<slug:slug>/<str:id>/', views.BlogDetailView.as_view(), name='detail1'),

	path('message/', views.msg, name="message"),

	path('comment/<slug:slug>/<str:id>/',views.postComment, name='postComment'),

]
