from django.contrib import admin
from .models import Employee
from .models import Facility
from .models import Employeerole
from .models import Occupation
from .models import Postalcode
from .models import Received
from .models import Schedules
from .models import Workat
from .models import Infected
from .models import Vaccine
from .models import Emails


admin.site.register(Employee)
admin.site.register(Facility)
admin.site.register(Employeerole)
admin.site.register(Occupation)
admin.site.register(Postalcode)
admin.site.register(Received)
admin.site.register(Schedules)
admin.site.register(Workat)
admin.site.register(Infected)
admin.site.register(Vaccine)
admin.site.register(Emails)

# Register your models here.
