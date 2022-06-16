from django.urls import  path
from . import  views

app_name = 'Error'



urlpatterns = [
   
    path('add',views.add_error, name = 'add_error'),
    path('list',views.list_error, name='list_error'),
    path('update/<error_id>', views.update_error, name='list_error'),
    path('delerror/<ERRORModel_id>',views.delete_Error, name = 'delete_error'),
    
    path('addcomment',views.addComment, name = 'add_comment'),
    path('deletecomment/<Comment_id>',views.delete_comment, name = 'delete_comment'),
    path('showcom',views.list_comment, name = 'list_comment')
]
