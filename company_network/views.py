from rest_framework import generics
from company_network.models import Contributor
from company_network.permissions import IsActive
from company_network.serializers import ContributorSerializer

class ContributorListAPIView(generics.ListAPIView):
    """
    A view to retrieve a list of contributors.
    """
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()
    permission_classes = [IsActive]

class ContributorCreateAPIView(generics.CreateAPIView):
    """
    A view to create a new contributor.
    """
    serializer_class = ContributorSerializer
    permission_classes = [IsActive]

class ContributorRetrieveAPIView(generics.RetrieveAPIView):
    """
    A view to retrieve a contributor instance.
    """
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()
    permission_classes = [IsActive]

class ContributorUpdateAPIView(generics.UpdateAPIView):
    """
    A view to update a contributor instance.
    """
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()

    def perform_update(self, serializer):
        serializer.save(debt=self.get_object().debt)

class ContributorDestroyAPIView(generics.DestroyAPIView):
    """
    A view to delete a contributor instance.
    """
    queryset = Contributor.objects.all()
    permission_classes = [IsActive]
