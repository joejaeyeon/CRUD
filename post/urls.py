from django.urls import path
from . import views

urlpatterns = [
    path('', views.posthome, name='posthome'),
    path('new', views.postnew, name='postnew'),
    path('create', views.postcreate, name='postcreate'),
    path('show/<int:post_id>', views.postshow, name='postshow'),
    path('edit/<int:post_id>', views.postedit, name='postedit'),
    path('update/<int:post_id>', views.postupdate, name='postupdate'),
    path('delete/<int:post_id>', views.postdelete, name='postdelete'),
    path('comentcreate/<int:post_id>', views.postcomentcreate, name='postcomentcreate'),
    path('comentdelete/<int:post_id>/<int:c_id>',views.postcomentdelete, name='postcomentdelete'),
]
