from drf_yasg import openapi

USER_NOT_AUTHORIZED_RESPONSE = openapi.Response('user not authorised',
                                                examples={'application/json': {
                                                    'error': 'user not authorised'
                                                }})

AUTH_PARAMETER = openapi.Parameter('Authorization',
                                   openapi.IN_HEADER,
                                   description='Token dsadfasdfsadfsd',
                                   type=openapi.TYPE_STRING)

user_create_doc = {
    'request_body': openapi.Schema(type=openapi.TYPE_OBJECT,
                                   required=['email', 'password'],
                                   properties={
                                       'email': openapi.Schema(type=openapi.TYPE_STRING),
                                       'password': openapi.Schema(type=openapi.TYPE_STRING)
                                   }),
    'responses': {
        '201': openapi.Response('user created',
                                examples={'application/json': {
                                    'email': 'UserExample@gmail.com',
                                    'token': 'dkkk3jaoaovfav'
                                }}),
        '409': openapi.Response('email is already taken',
                                examples={'application/json': {
                                    'error': 'email is already taken'
                                }}),
        '400': openapi.Response('bad request')
    }
}

user_login_doc = {
    'request_body': openapi.Schema(type=openapi.TYPE_OBJECT,
                                   required=['email', 'password'],
                                   properties={
                                       'email': openapi.Schema(type=openapi.TYPE_STRING),
                                       'password': openapi.Schema(type=openapi.TYPE_STRING)
                                   }),
    'responses': {
        '200': openapi.Response('ok',
                                examples={'application/json': {
                                    'email': 'user@gmail.com',
                                    'token': 'ldjaldjfllasdflas'
                                }}),
        '400': openapi.Response('Bad request',
                                examples={'application/json': {
                                    'error': ["user with this name and password was not found"]
                                }})
    }

}

is_authenticated_doc = {
    'manual_parameters': [
        AUTH_PARAMETER,
    ],
    'responses': {
        '200': openapi.Response('ok',
                                examples={'application/json': {
                                    'is_authenticated': True
                                }}),
        '403': USER_NOT_AUTHORIZED_RESPONSE
    }
}

is_email_taken_doc = {
    'manual_parameters': [
        openapi.Parameter('email',
                          openapi.IN_PATH,
                          description='check email',
                          type=openapi.TYPE_STRING)
    ],
    'responses': {
        '200': openapi.Response('ok',
                                examples={'application/json': {
                                    'is_email_taken': False
                                }}),
        '403': USER_NOT_AUTHORIZED_RESPONSE
    }
}
