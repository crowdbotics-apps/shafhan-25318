from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecordingViewSet,
    EventViewSet,
    SubscriptionViewSet,
    CourseViewSet,
    GroupViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    SubscriptionTypeViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("module", ModuleViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("group", GroupViewSet)
router.register("course", CourseViewSet)
router.register("lesson", LessonViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("event", EventViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("category", CategoryViewSet)
router.register("recording", RecordingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
