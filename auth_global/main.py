
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DEFAULT_PAGINATION_CLASS':(
    #     #  'auth_global.pagnation.Coustompagnation'
    #      ),

    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 6

    # 'DEFAULT_FILTER_BACKENDS': (
    #      'django_filters.rest_framework.DjangoFilterBackend'
    #      ),

    #   'DEFAULT_RENDERER_CLASSES': [
    #        'rest_framework.renderers.JSONRenderer',
    #    ],
    #    'DEFAULT_PARSER_CLASSES': [
    #        'rest_framework.parsers.JSONParser',
    #    ]
    

}