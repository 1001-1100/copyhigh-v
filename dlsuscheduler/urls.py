from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("addItem", hello.views.addItempage, name="addItempage"),
    path("editItem", hello.views.editItempage, name="editItempage"),
    path("add", hello.views.addpage, name="addpage"),
    path("view", hello.views.viewpage, name="viewpage"),
    path("login", hello.views.getlogin, name="getlogin"),
    path("logout", hello.views.logout, name="logout"),
    path("postlogin", hello.views.postlogin, name="postlogin"),

    path("addInvEntry", hello.views.addInvEntry, name='addInvEntry'),
    path("addInvItem", hello.views.addInvItem, name='addInvItem'),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
