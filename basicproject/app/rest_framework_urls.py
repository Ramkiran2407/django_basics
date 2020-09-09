from rest_framework import routers 
from app.classviews import RegisterEmployees, EmployeeRegister, UserViewSet


router = routers.DefaultRouter() 

router.register(r'user_reg', RegisterEmployees) 
router.register(r'emp_reg', EmployeeRegister)
router.register(r'userview', UserViewSet, basename='user') 


urlpatterns = router.urls