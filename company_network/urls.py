from django.urls import path

from company_network.views import ContributorCreateAPIView, ContributorListAPIView, ContributorRetrieveAPIView, \
    ContributorUpdateAPIView, ContributorDestroyAPIView

urlpatterns = [
    path('', ContributorListAPIView.as_view(), name='contributor_list'),
    path('create/', ContributorCreateAPIView.as_view(), name='contributor_create'),
    path('<int:pk>/', ContributorRetrieveAPIView.as_view(), name='contributor_retrieve'),
    path('update/<int:pk>/', ContributorUpdateAPIView.as_view(), name='contributor_update'),
    path('delete/<int:pk>/', ContributorDestroyAPIView.as_view(), name='contributor_delete'),
]