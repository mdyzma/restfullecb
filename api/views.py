from rest_framework import generics
from .serializers import CurrencySerializer
from .models import Currency

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
