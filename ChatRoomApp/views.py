import uuid
import pyaes, pbkdf2, binascii, os, secrets

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from ChatRoomApp.models import Message
from ChatRoomApp.serializer import ChatApiSerializer
from rest_framework.response import Response


def ChatLogin(request):
    return render(request, 'login/index.html')


def SignInRoom(request):
    if request.method == "POST":
        username = request.POST.get('username')
        print(username)

    else:
        return HttpResponse('Method Not Allowed')
    return HttpResponse('Method Not Alloweddddd')


@cache_page(60 * 1)
def Chats(request):
    models = Message.objects.all().order_by('-timestamp')

    unique_id = uuid.uuid4().hex[:10].upper()
    context = {
        'models': models,
        'usernameDefault': unique_id
    }


    return render(request, 'chat/index.html', context)


# @cache_page(60 * 1)
@api_view(['GET'])
@permission_classes([AllowAny])
def chatApi(request):
    models = Message.objects.all()
    # copymodels = []
    # password = "s3cr3t*c0d3"
    # passwordSalt = os.urandom(16)
    # key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
    # iv = secrets.randbits(256)
    # aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    # for i in models:
    #     decrypted = aes.decrypt(bytes.decode(i.content))
    #     print('Decrypted:', decrypted)
    #     copymodels.append({
    #         'id': i.id,
    #         'sender': i.sender,
    #         'content': decrypted,
    #         'timestamp': i.timestamp
    #     })
    serializer = ChatApiSerializer(models, many=True)
    return Response(serializer.data)
