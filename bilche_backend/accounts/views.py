from django_rest_passwordreset.views import ResetPasswordRequestToken, ResetPasswordConfirm
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ErrorDetail, ValidationError

from rest_framework.generics import CreateAPIView

from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserSerializer, MyAuthTokenSerializer


class MyObtainAuthToken(APIView):

    serializer_class = MyAuthTokenSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.serializer_class
        return serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {'token': token.key,
                 'user': {'fullname': user.fullname, 'email': user.email, 'level': user.level,
                          'phone_number': str(user.phone_number)}}, status=status.HTTP_200_OK)
        messages = list(serializer.errors.values())[0]
        error = {'error': messages[0]}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        request.data['username'] = request.data['email']
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token, create = Token.objects.get_or_create(user=user)
                data_response = dict()
                data_response['user'] = serializer.data
                data_response['token'] = token.key
                return Response(data_response, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        if 'username' in errors:
            errors.pop('username')
        if 'email' in errors:
            errors['email'] = [ErrorDetail(string='ایمیل نامعتبر است', code='invalid')]
        messages = list(errors.values())[0]
        error = {'error': messages[0]}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(ResetPasswordRequestToken):
    def post(self, request, *args, **kwargs):
        try:
            return super(ResetPasswordAPIView, self).post(request, *args, **kwargs)
        except ValidationError as e:
            error = e.detail['email'][0]
            translator = {'We couldn\'t find an account associated with that email. Please try a different e-mail address.': 'حسابی با این آدرس ایمیل یافت نشد.',
                          'Enter a valid email address.': 'ایمیل نامعتبر است.'}
            return Response({'error': translator[error]}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordConfirmAPIView(ResetPasswordConfirm):
    def post(self, request, *args, **kwargs):
        try:
            return super(ResetPasswordConfirmAPIView, self).post(request, *args, **kwargs)
        except ValidationError as e:
            if 'password' in e.detail:
                msg = 'این رمز به اندازه کافی امن نیست.' \
                      'رمز نمی تواند کوتاه تر از 8 کاراکتر یا فقط شامل اعداد باشد.'
            else:
                msg = 'شناسه معتبر نیست.'
            return Response({'error': msg}, status=status.HTTP_400_BAD_REQUEST)

