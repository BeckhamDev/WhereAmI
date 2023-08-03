from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address


class AddressView(CreateView):
    
    model = Address
    fields = ['address', 'lat', 'long']
    template_name = 'home.html'
    success_url = '/'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['access_token'] = 'pk.eyJ1IjoiYmVja2hhbS1kZXYiLCJhIjoiY2xrdjl2aTY1MHFzbzNmcnVvMjc3ajd3YiJ9.vqsAU7gD3HR45vxmbtzK5w'
        context['addresses'] = Address.objects.all()
        return context 