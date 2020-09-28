from django.contrib import admin
from Vote.models import *

# Register your models here.
admin.site.register(Constituency)
admin.site.register(Candidate)
admin.site.register(VoterDetails)