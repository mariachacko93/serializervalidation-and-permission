from .models import comment
from rest_framework import serializers
from .models import comment



def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

class commentserializer(serializers.ModelSerializer):
    num = serializers.IntegerField(label='Number',validators=[multiple_of_ten])

    email2=serializers.EmailField(label="confirm email")
    class Meta:
        model=comment
        fields="__all__"
        # [
        #     "email",
        #     "email2",
        #     "content",
        
        # ]

    def validate_email2(self,value):
        data=self.get_initial()
        email1=data.get("email")
        email2=value
        if(email1!=email2):
            raise serializers.ValidationError("Email doesnt match")
        return value

    def validate(self,data):
        email=data["email"]
        qs=comment.objects.filter(email=email)
        if qs.exists():
            raise serializers.ValidationError("User already exists")
        return data

    # def create(self,validated_data):
    #     email=validated_data["email"]
    #     content=validated_data["content"]
    #     ob=comment(email=email,content=content)
    #     ob.save()
    #     return validated_data

    # def update(self,instance,validated_data):
    #     instance.email=validated_data.get('email',instance.email)
    #     instance.content=validated_data.get('content',instance.content)
    #     instance.save()
    #     return instance