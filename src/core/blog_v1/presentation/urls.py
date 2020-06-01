from django.urls import path, include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .blog import views


app_name = 'v1'

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="A blog api",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="xcixor@outlook.com"),
        license=openapi.License(name="BSD License"),
        validators=['ssv']
        ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter(trailing_slash=False)
router.register(
    r'posts/?', views.BlogPostDetail,
    )

urlpatterns = [
    path(
        'swagger/<format:.json>',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(
        'swagger/<format:.yaml>',
        schema_view.without_ui(cache_timeout=0), name='schema-yml'),
    path(
        '',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'
    ),
    path('v1/', include(router.urls))
]
