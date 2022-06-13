from django.urls import  path
from . import  views

app_name = 'Error'



urlpatterns = [
    # Here Start With Errors Model
    path('add',views.add_error, name = 'add_error'),
    path('list',views.list_error, name='list_error'),
    path('update/<error_id>', views.update_error, name='list_error'),
    path('error/<int:id>',views.error_details, name= 'error_datails'),  #update and delete and show_error by your request.

    # Here Start With Comment Model

    # Hint: remember write before write Endpoints like==>  error/addcomment

    path('addcomment',views.addComment, name = 'add_comment'),
    path('deletecomment/<Comment_id>',views.delete_comment, name = 'delete_comment'),
    path('showcom',views.list_comment, name = 'list_comment'),
]