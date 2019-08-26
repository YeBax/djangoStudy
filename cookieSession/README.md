1 response.set_cookie(key, value)
2 request.COOKIE.get(key)
3 request.session[key=value]
    注意django的实现的流程 操作
4 request.session[key]

5 request.session.flush()
    '''
    1 request.COOKIE.get("sessionid")
    2 django-session.objects.filter(session_key=....).delete()
    3 response.delete_cookie("cookie_key", path="/", domain=name)
    '''