from rest_framework import viewsets, permissions, filters

from .serializers import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
   
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'date_joined']
    ordering = ['date_joined']
  

    def get_queryset(self):
        queryset = User.objects.all()  # Start with the full queryset
        filters = {}

        # Get parameters from the request query
        username = self.request.query_params.get('username')
        email = self.request.query_params.get('email')

        # Dynamically apply filters based on query params
        if username:
            filters['username__icontains'] = username
        if email:
            filters['email__icontains'] = email

        if filters:
            queryset = queryset.filter(**filters) # if all condition is met it takes in the input and use as filters
        
        return queryset # and return the queryset
