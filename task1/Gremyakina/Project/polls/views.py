from django.shortcuts import render
import Database


def index(request):
    data = ''
    for i in range(1, 251):
        info = Database.get(i)
        n = '\n'
        data += f'''<div>
                <img src="static/polls/pics/{i}.jpeg"><br>'''
        data += f'''
                    {info.replace(n, '<br>')}
                </div>'''
    return render(request, 'polls/index.html', {'data': data})
