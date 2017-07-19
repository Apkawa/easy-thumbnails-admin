from django.conf import settings
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = []


urlpatterns += [
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # import debug_toolbar
    #
    # urlpatterns += patterns('',
    #     url(r'^__debug__/', include(debug_toolbar.urls)),
    # )

from django.views.i18n import javascript_catalog

js_info_dict = {
    # 'packages': ('your.app.package',),
}
urlpatterns += [
    url(r'^jsi18n/$', javascript_catalog, js_info_dict, name='javascript-catalog'),
]
