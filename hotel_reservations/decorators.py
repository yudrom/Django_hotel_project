from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def login_required_with_message(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, message='Войдите в систему для успешного бронирования.')
            return redirect('/accounts/login/')
        return view_func(request, *args, **kwargs)

    return _wrapped_view
