from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import ERRORModel
from .models import Comment
from .serializers import ErrorSerializer
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated




@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])#
def add_error(request : Request):
    '''
    this method will check if the user is authenticate or user has permission
    and all users have permission to  add_errors with the solutiono and refrece of the answer.
    '''

    if not request.user.is_authenticated or not request.user.has_perm('Error.add_errormodel'): #must be lowercase.
        return Response({"msg" : "Not Allowed check on your authentication and Permission"}, status=status.HTTP_401_UNAUTHORIZED) #give the message and stop.
    # if not request.user.has_perm('Error.add_error'):
    #     return Response({"msg": "doesn't have permission"})
    new_error = ErrorSerializer(data=request.data)
    if new_error.is_valid():
        new_error.save()
        dataResponse={
            "msg" : "Created Successfully",
            "Error" : new_error.data
        }

        return Response(dataResponse)
    else:
        print(new_error.errors)
        dataResponse = {"msg" : "couldn't create a Error"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT'])
 @authentication_classes([JWTAuthentication])
 @permission_classes([IsAuthenticated])
  #
def update_error(request : Request, error_id): #

    '''
        this method will check if the user is authenticate
        then so can update on the error already exsit.

    '''

    up_error = ERRORModel.objects.get(id=error_id)

    updated_error = ErrorSerializer(instance=up_error, data=request.data)
    if updated_error.is_valid():
        updated_error.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_error.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)





# list of error


@api_view(['GET'])
def list_error(request: Request):
    '''
            this method will show all the list of the errors created by users
            and you can search by any phrase exsit in the error_description.


        '''
    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        errors = ERRORModel.objects.filter(error_desc__contains=search_phrase)
    else:
        errors = ERRORModel.objects.all()

    responseData = {
        "msg": "list of Errors",
        "Errors": ErrorSerializer(instance=errors, many=True).data
    }
    return Response(responseData,status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_Error(request: Request, ERRORModel_id):
    '''
               this method will delete any error you want
               by the error id must be authenticate.


    '''

    del_error = ERRORModel.objects.get(id=ERRORModel_id)
    del_error.delete()
    return Response({"msg" : "Deleted Successfully"})



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])


def addComment(request):
    '''
        this method will check on the user if authonticate then
        you will be can add the comments.

    '''
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data) #Validate your data with form.
        if serializer.is_valid():
            instance = serializer
            instance.save() #Will save your data if valid.
            # data = {'success':True,'msg':"Store comment's data successfully"}
            # return Response(data)
            dataResponse = {
                "msg": "Created Successfully",
                "Comment": serializer.data
            }
            return Response(dataResponse)


    else:

        print(serializer.errors)
        dataResponse = {"msg": "couldn't create a comment"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])

def delete_comment(request: Request, Comment_id):
    '''
    this function will be delete the comment
    just Expert can delete the comment.
    '''
    if not request.user.is_authenticated or not request.user.has_perm('Error.delete_comment'): #must be lowercase.
        return Response({"msg" : "Not Allowed check on your authentication and Permission"}, status=status.HTTP_401_UNAUTHORIZED)
    del_com = Comment.objects.get(id=Comment_id)
    del_com.delete()
    return Response({"msg" : "Deleted Successfully"})


    new_error = ErrorSerializer(data=request.data)
    if new_error.is_valid():
        new_error.save()
        dataResponse={
            "msg" : "Created Successfully",
            "Error" : new_error.data
        }

        return Response(dataResponse)
    else:
        print(new_error.errors)
        dataResponse = {"msg" : "couldn't create a Error"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)







@api_view(['GET'])
def list_comment(request: Request):

    '''
    this method will show  list of the comment .
    and search for any phrase exsit in the comment_phrase.

    '''
    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        commm = Comment.objects.filter(comment__contains=search_phrase)
    else:
        commm = Comment.objects.order_by('-created_at').all()

    responseData = {
        "msg": "list of Comment",
        "Comments": CommentSerializer(instance=commm, many=True).data
    }
    return Response(responseData)
