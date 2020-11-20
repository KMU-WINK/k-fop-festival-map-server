from rest_framework import viewsets
from booth.models import Region
from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication , BasicAuthentication
from booth.serializers import RegionSerializer


# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method == "GET": # GET을 제외한 모든 메서드는 대상이 소유자를 구분함
#             return True
#         else:
#             return obj.host == request.user


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all() # 대상 데이터들
    serializer_class = RegionSerializer # 직렬화 도구
    permission_classes = [IsAdminUser] # 권한 설정
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication] # 인증 수단

    def get_queryset(self): # get 요청 시 가져올 데이터 범위 . 학생회 이외의 리전을 가져오면 안댐
        try:
            return Region.objects.filter(host=self.request.user)
        except TypeError:
            return None

    def perform_create(self, serializer): # 생성 시 누가 소유할 것인가 지정
        serializer.save(host=self.request.user)