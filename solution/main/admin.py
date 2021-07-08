from django.contrib import admin
from .models import (
    AboutViewSubjects1, AboutViewSubjects2, AboutViewSubjects3, AboutViewSubjects4, AboutViewSubjects5,
    HomeViewSubjects1,
    NewsViewSubjects1, NewsViewSubjects2, NewsViewSubjects3, 
    ServicesViewSubjects1, ServicesViewSubjects2, ServicesViewSubjects3,
    )
admin.site.register(AboutViewSubjects1)
admin.site.register(AboutViewSubjects2)
admin.site.register(AboutViewSubjects3)
admin.site.register(AboutViewSubjects4)
admin.site.register(AboutViewSubjects5)

admin.site.register(HomeViewSubjects1)

admin.site.register(NewsViewSubjects1)
admin.site.register(NewsViewSubjects2)
admin.site.register(NewsViewSubjects3)

admin.site.register(ServicesViewSubjects1)
admin.site.register(ServicesViewSubjects2)
admin.site.register(ServicesViewSubjects3)