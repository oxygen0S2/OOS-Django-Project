from django.http import HttpResponse
from datetime import datetime


def current_datetime(req):
    now = datetime.now()
    html = f'''
          <!DOCTYPE html>
          <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Document</title>
            </head>
            <body>It is now {now}.</body>
          </html>  
          '''
    return HttpResponse(html)
