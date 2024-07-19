from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/all/',
        '/create/',
        '/update/',
        '/delete/',
        '/register/',
        '/token/',
        '/token/refresh',
    ]
    return Response(routes)
@api_view(['POST'])
def getAllPosts(request):
    userId = request.data.get("user_id")
    posts = Posts.objects.filter(user_id=userId)
    serializer = PostsSerialzer(posts,many=True)
    return Response(serializer.data)
     
@api_view(['POST'])
def createPost(request):
    serializer = PostsSerialzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatePost(request,pk):
    post = Posts.objects.get(id=pk)
    serializer = PostsSerialzer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletePost(request,ck):
    post = Posts.objects.get(id=ck)
    post.delete()
    msg = "successfully deleted a new Postr"
    return Response(msg)


@api_view(['POST'])
def registeration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user = serializer.save(validated_data=serializer.validated_data)
            data['response'] = "successfully registred a new user"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
