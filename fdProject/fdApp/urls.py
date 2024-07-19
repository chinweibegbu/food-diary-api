from django.urls import path
from .views import EntryListCreateView, EntryDetailView,AllEntrysListView,EntryDeleteView,EntryUpdateView

urlpatterns = [
    path('entries/', EntryListCreateView.as_view(), name='create-entry'),
    path('entries/<int:pk>/', EntryDetailView.as_view(), name='get-entry'),
    path('entries/all/', AllEntrysListView.as_view(), name='get-all-entries'),  
    path('entries/delete/<int:pk>/', EntryDeleteView.as_view(), name='delete-entry'), 
    path('entries/update/<int:pk>/', EntryUpdateView.as_view(), name='update-entry'), 
]