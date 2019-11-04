from qa.views import test

urlpatterns = patterns('qa.views',
                        url('login/', test, name='login'),
                        url('signup/', test, name='signup'),
                        url('question/<int:id>/', test, name='question'),
                        url('ask/', test, name='ask'),
                        url('popular/', test, name='popular'),
                        url('new/', test, name='new'),
                        url('', test, name='home'),
                        )
