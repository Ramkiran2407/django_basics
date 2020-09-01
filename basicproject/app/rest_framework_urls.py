from rest_framework import routers 
from app.classviews import RegisterEmployees, EmployeeRegister


router = routers.DefaultRouter() 

router.register(r'user_reg', RegisterEmployees) 
router.register(r'emp_reg', EmployeeRegister) 

urlpatterns = router.urls