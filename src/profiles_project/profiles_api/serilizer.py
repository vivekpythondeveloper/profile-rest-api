from rest_framework import serializers
from . import models

class FirstSerilizer(serializers.Serializer):
    # serializs the name and every data in this class
    name  = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    # for updating of user profile

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = models.UserProfile(email=validated_data['email'],
                name = validated_data['name']
                )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    # profile feed serializer

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','create_on')
        extra_kwargs = {'user_profile':{'read_only':True}}
