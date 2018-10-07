from django.shortcuts import render


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        pass
    else:
        # GET
        # нарисовать страницу где можно ввести данные
        return render(request, 'login.html')


def main_page_view(request):
    f_name = 'ilia'
    l_name = 'kruglov'
    print('Current user: ', request.user)
    print('Request type: ', request.method)
    # print('Request parameters: ', params)  # TODO: Why it doesn't work?

    if request.method == 'GET':  # popular construction (in REST api more variants available) (29092019, 01:43:00)
        params = request.GET
        if 'login' in params:
            login = params['login']
    else:
        params = request.POST
        login = params['login']

    return render(request, 'index.html', {'first_name': f_name,
                                          'last_name': l_name,
                                          'request_type': request.method,
                                          'params': params
                                          })  # Context dictionary
