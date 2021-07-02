from django.http import HttpResponse
from .models import *
from django.utils import timezone


# Create your views here.
def index(request, id):
    member = Member.objects.filter(card_id=id).first()
    if not member:
        return HttpResponse("not existed ")
    else:
        last_record = TimeTable.objects.filter(member=member).last()
        if not last_record:
            TimeTable.objects.create(member=member, recorded_at=timezone.now(), status=True)
            return HttpResponse("obj created")
        else:
            TimeTable.objects.create(member=member, recorded_at=timezone.now(), status=(not last_record.status))

    return HttpResponse("id ")
