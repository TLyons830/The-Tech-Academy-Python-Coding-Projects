from django.contrib import admin

from checkbook.models import Accounts
from checkbook.models import Information


admin.site.register(Accounts)

admin.site.register(Information)

