from django.conf import settings
from django.shortcuts import render

def require_company(request):
    return render(request, 'myapp/register.html', backend=request.session['partial_pipeline']['backend'])
