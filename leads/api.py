from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset
# allows us to create a CRUD api w/o specifying explicit methods
# for the functionality, no routes, use default router easily
class LeadViewSet(viewsets.ModelViewSet):
	queryset = Lead.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = LeadSerializer