from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'birthday']

    def create(self, validated_data):
        # Вы можете добавить дополнительную логику для создания пользователя, если необходимо
        return User.objects.create_user(**validated_data)
    