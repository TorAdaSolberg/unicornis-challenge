from django.contrib import admin
from .models import Meeting, Issue, Attendance, Document
# Register your models here.

admin.site.register(Meeting)
admin.site.register(Issue)
admin.site.register(Document)
admin.site.register(Attendance)
