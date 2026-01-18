from djoser.serializers import UserCreateSerializer
from account.models import User

def UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')