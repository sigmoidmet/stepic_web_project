def application(environ, start_response):
    status = '200 OK'
    headers = [
        ("Content-Type", "text/plain; charset=utf-8")  
        ]
    body = '\n'.join(environ['QUERY_STRING'].split('&')).encode()
    start_response(status, headers)
    return [body]
  
