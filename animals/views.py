from rest_framework import generics
from .serializer import AnimalSerializer
from .models import Animal
from .permissions import IsOwnerOrReadOnly

class AnimalList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer