from django.shortcuts import render
from rest_framework import generics
from .models import Entry
from .serializers import EntrySerializer
from rest_framework.response import Response

# Create your views here.
from rest_framework import generics
from .models import Entry
from .serializers import EntrySerializer

from rest_framework import status
from rest_framework.response import Response

class EntryListCreateView(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    
    
class EntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    
class AllEntrysListView(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    
class EntryUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    partial = True
    
    
class EntryDeleteView(generics.DestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Entry"))