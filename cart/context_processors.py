from .models import *
from .views import *

def count(request):
    item_count=0
    if 'admin' in request.path:
        return{}

    else:
        try:

            ct=cartlist.objects.filter(cart_id=c_id(request))
            ct=cartitems.objects.all().filter(cart=ct[:1])
            for c in ct:
                item_count+=c.quan
        except cartlist.DoesNotExist:
            item_count=0

        return dict(itc=item_count)
