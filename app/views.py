from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view,renderer_classes,permission_classes
from app.serializers import UserSerializer, GroupSerializer, ProductSerializer,SupplierSerializer, OrderSerializer, AddressSerializer
from app.models import Product, Supplier, Order, Address
from django_filters.rest_framework import DjangoFilterBackend
from twilio.twiml.messaging_response import MessagingResponse
from rest_framework.renderers import JSONRenderer
from app.tasks import add
from functools import wraps
import jwt
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from django.core.exceptions import PermissionDenied

@api_view(['POST'])
@renderer_classes([JSONRenderer])
def whatsAppmsg(request):
    incoming_msg = request.data['Body'].lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if incoming_msg:
        if 'hi' in incoming_msg:
            quote = 'Hello'
            msg.body(quote)
            responded = True
        if 'order' in incoming_msg:
            quote = 'order details'
            msg.body(quote)
            # return a cat pic
            # msg.media('https://cataas.com/cat')
            responded = True
    if not responded:
        msg.body('Sorry!')
    return HttpResponse(str(resp))

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def testsqs(self):
    add.delay(3,5)
    status="true"
    return Response(status)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['productName', 'sku']

class SupplierList(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    if not auth:
        raise PermissionDenied("authorization_header_missing")
    parts = auth.split()
    if parts[0].lower() != "bearer":
        raise PermissionDenied("invalid_header")
    elif len(parts) == 1:
        raise PermissionDenied("Token not found")
    elif len(parts) > 2:
        raise PermissionDenied("Authorization header must be Bearer header")
    token = parts[1]

    return token

def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope

@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})

@api_view(['GET'])
def private(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})

@api_view(['GET'])
@requires_scope('read:messages')
def private_scoped(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})