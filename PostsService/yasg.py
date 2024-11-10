# from django.urls import path
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


# schema_view_admin = get_schema_view(
#    openapi.Info(
#       title="Admin",
#       default_version='v1',
#       description="Docs",
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

# schema_view_clent = get_schema_view(
#    openapi.Info(
#       title="PostService",
#       default_version='v1',
#       description="Docs",
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )



# urlpatterns = [
#     path('swagger<format>/', schema_view_admin.without_ui(cache_timeout=0), name='schema-json'),
#     path('swagger<format>/', schema_view_clent.without_ui(cache_timeout=0), name='schema-json'),
   
#     path('swagger/admin/', schema_view_admin.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('swagger/client/', schema_view_clent.with_ui('swagger', cache_timeout=0), name='schema-client-swagger-ui'),

#    #  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]

# from django.urls import path
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi



# schema_view = get_schema_view(
#    openapi.Info(
#       title="PostService",
#       default_version='v1',
#       description="Docs",
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )


# urlpatterns = [
#     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]


from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="PostService",
      default_version='v1',
      description="Docs",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]