from rest_framework.serializers import ModelSerializer

from my_smartstore_backend.models import User, Category, Slide, Product, ProductOption, ProductImage, PageItem


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email','phone','fullname']




class CategorySerializre(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'position', 'image']

class SlideSerializre(ModelSerializer):
    class Meta:
        model = Slide
        fields = ['position', 'image']

class ProductSerializre(ModelSerializer):
    class Meta:
        model = Product
        fields = ['__all__']

class ProductOptionSerializre(ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['__all__']
#
class ProductImageSerializre(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['__all__']
#

class PageItemSerializre(ModelSerializer):
    class Meta:
        model = PageItem
        fields = ['__all__']