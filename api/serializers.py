from rest_framework import serializers
from django.contrib.auth.models import User
from items.models import Item ,FavoriteItem



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class ItemSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "itemapi_id"
        )
    added_by = serializers.SerializerMethodField()
    favourited  = serializers.SerializerMethodField()
    added_by = UserSerializer()
    class Meta:
        model = Item
        fields = ['id','image','name','detail','added_by','favourited']

    def get_favourited(self,obj):
        favorite = FavoriteItem.objects.filter(user=obj.added_by)
        count = 0
        for i in favorite:
            count += 1
        return count



class ItemDetailSerializer(serializers.ModelSerializer):

    favourited_by=serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['id','image','name','description','favourited_by']

    def get_favourited_by(self,obj):
        favorite = FavoriteItem.objects.filter(user=obj.added_by)
        count =[]
        for i in favorite:
            count.append(i)
        return count





class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data
