from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .views import QueuesView, GetQueueInfoView, AddMemberToQueueView, EditQueueMember, DeleteMemberFromQueueView, ClearMemberships, ClearQueues, ClearTokens, ClearUsers
from token_auth import views

urlpatterns = [
    path('auth', csrf_exempt(views.LoginView.as_view())),
    path('users', csrf_exempt(views.SignUpView.as_view())),

    path('queues', csrf_exempt(QueuesView.as_view())),
    path('queues/<int:queue_id>', csrf_exempt(GetQueueInfoView.as_view())),
    path('queue/<int:queue_id>/member/<int:member_id>', csrf_exempt(EditQueueMember.as_view())),
    path('queues/<int:queue_id>/members', csrf_exempt(AddMemberToQueueView.as_view())),
    path('queues/<int:queue_id>/members/<int:member_id>', csrf_exempt(DeleteMemberFromQueueView.as_view())),

    path('clear/memberships', csrf_exempt(ClearMemberships.as_view())),
    path('clear/users', csrf_exempt(ClearUsers.as_view())),
    path('clear/queues', csrf_exempt(ClearQueues.as_view())),
    path('clear/tokens', csrf_exempt(ClearTokens.as_view())),
]