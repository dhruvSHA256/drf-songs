from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import User
from .serializer import UserSerializer


# TODO: match hashed password and return JWT
def authUser(data):
    print(data)
    try:
        user = User.objects.get(email=data["email"])
        if user.password == data["password"]:
            jwt = "success"
            response = {"token": jwt}
        else:
            response = {"error": "unauthorized"}
        return response
    except:
        return {"error": "No User Found"}


class UserApi(APIView):
    @staticmethod
    def getUsers():
        # User.objects.all().delete()
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return serialized_users.data

    @staticmethod
    def createUser(data):
        if User.objects.filter(email=data["email"]).exists():
            return {"error": "Email already registered"}
        if User.objects.filter(username=data["username"]).exists():
            return {"error": "Usernam already taken"}
        serialized_user = UserSerializer(data=data)
        if serialized_user.is_valid():
            serialized_user.save()
            return serialized_user.data
        return serialized_user.errors

    @staticmethod
    def deleteUser(data):
        try:
            user = User.objects.get(email=data["email"])
            user.delete()
            response = {"success": "deleted user"}
            return response
        except:
            return {"error": "No User Found"}

    @staticmethod
    def updateUser(data):
        try:
            user = User.objects.get(id=data["id"])
            # data['password'] = hashed password
            serialized_user = UserSerializer(user, data=data, partial=True)
            if serialized_user.is_valid():
                serialized_user.save()
                return serialized_user.data
            return serialized_user.errors
        except:
            return {"error": "No User Found"}

    def get(self, request):
        return Response(UserApi.getUsers())

    def post(self, request):
        return Response(UserApi.createUser(request.data))

    def patch(self, request):
        return Response(UserApi.updateUser(request.data))

    def delete(self, request):
        return Response(UserApi.deleteUser(request.data))
