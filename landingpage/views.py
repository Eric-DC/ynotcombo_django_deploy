
# Create your views here.
from django.views.generic.base import View
from django.http import HttpResponse
import textwrap 

class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Y Combinator? Y Not combinator</title>
            </head>
            <body>
                <h1>Y-NOT-COMBINATOR</h1>
                <p>kekekekeke</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)
