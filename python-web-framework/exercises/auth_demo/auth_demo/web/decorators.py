from django.http import HttpResponse


# def allowed_groups(allowed_roles=[]):
#     print(231)
#     def decorator(view_func):
#         print(
#         )
#         def wrapper(request, *args, **kwargs):
#             group = None
#             if request.user.groups.exists():
#                 print('1')
#                 group = request.user.groups.all()[0].name
#             if group in allowed_roles:
#                 print('2')
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse()
#         return wrapper
#     return decorator

def allowed_groups(groups=None):
    if groups is None:
        groups = []

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponse(f'Not authenticated')

            if request.user.is_superuser or not groups:
                return view_func(request, *args, **kwargs)

            user_groups = request.user.groups.filter(name__in=groups)

            if not user_groups:
                return HttpResponse('Not in the any of the allowed groups')
            return view_func(request, *args, **kwargs)

        return wrapper

    print(groups)
    if callable(groups):
        view_func = groups
        groups = []
        return decorator(view_func)

    return decorator
