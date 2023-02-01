from rest_framework.decorators import api_view
from Accounts.api.serializers import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from Accounts.models import *
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST',])
def log_out_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data={}

        if serializer.is_valid():
            account = serializer.save()
            data['Success'] = "Registration is sucessful you can login now"
            data['username']= account.username
            data['email'] = account.email
            data['token'] = get_tokens_for_user(account)
        else:
            data = (serializer.errors)
        return Response(data)
