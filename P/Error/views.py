from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import ERROR
from .models import Comment
from .serializers import ErrorSerializer
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated




@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def add_error(request : Request):

    if not request.user.is_authenticated and request.user.has_perm('Error.add_error'):
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED) #give the message and stop.
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



# update error or handling something.
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
  #
def update_error(request : Request, error_id): #
    up_error = ERROR.objects.get(id=error_id)

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
    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        errors = ERROR.objects.filter(error_desc__contains=search_phrase)
    else:
        errors = ERROR.objects.all()

    responseData = {
        "msg": "list of Errors",
        "Errors": ErrorSerializer(instance=errors, many=True).data
    }
    return Response(responseData,status=status.HTTP_404_NOT_FOUND)




@api_view(['GET','PUT','DELETE'])
def error_details(request,id):

    try:
       error = ERROR.objects.get(pk=id)
    except ERROR.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
       serializer = ErrorSerializer(error)
       return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ErrorSerializer(error, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            error.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


#here we start with COMMENTS
@api_view(['POST'])
def addComment(request):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data) #Validate your data with form.
        if serializer.is_valid():
            instance = serializer
            instance.save(Commit=False) #Will save your data if valid.
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
def delete_comment(request: Request, Comment_id):
    del_com = Comment.objects.get(id=Comment_id)
    del_com.delete()
    return Response({"msg" : "Deleted Successfully"})


@api_view(['GET'])
def list_comment(request: Request):
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


