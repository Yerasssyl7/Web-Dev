from django.http import JsonResponse

from .models import Product, Category


from rest_framework import viewsets, status
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.exceptions import ValidationError

from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        products = Product.objects.filter(category_id = pk)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_active == True and instance.count > 5:
            return Response(
                {'error': 'Delete forbidden: product is active and count > 5'},
                status=status.HTTP_403_FORBIDDEN
            )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)