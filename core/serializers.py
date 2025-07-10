from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Suggestion
from django.contrib.auth.models import User



# Signup view 
class SignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])  # 🔐 hash password
        user.save()
        return user




# Suggestion view
class SuggestionSerializer(serializers.ModelSerializer):
    submitted_by = serializers.SerializerMethodField()

    class Meta:
        model = Suggestion
        fields = '__all__'
        read_only_fields = ['submitted_by']

    def get_submitted_by(self, obj):
        if obj.is_anonymous:
            return None
        return obj.submitted_by.username if obj.submitted_by else None

    def create(self, validated_data):
        request = self.context['request']
        if not validated_data.get('is_anonymous', False):
            validated_data['submitted_by'] = request.user
        return super().create(validated_data)

