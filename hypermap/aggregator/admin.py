from django.contrib import admin

from djcelery.models import TaskMeta

from models import Service, Layer, Check, SpatialReferenceSystem


class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ('id', 'type', 'title', 'active', )
    list_display_links = ('id', )
    search_fields = ['title', 'url', ]
    list_filter = ('type', )


class SpatialReferenceSystemAdmin(admin.ModelAdmin):
    model = SpatialReferenceSystem
    list_display = ('code', )


class LayerAdmin(admin.ModelAdmin):
    model = Layer
    list_display = ('name', 'title', 'service', )
    search_fields = ['name', 'title', ]


class CheckAdmin(admin.ModelAdmin):
    model = Check
    list_display = ('resource', 'checked_datetime', 'success', 'response_time', )
    list_display_links = ('resource', )
    search_fields = ['resource__title', ]


admin.site.register(Service, ServiceAdmin)
admin.site.register(Check, CheckAdmin)
admin.site.register(SpatialReferenceSystem, SpatialReferenceSystemAdmin)
admin.site.register(Layer, LayerAdmin)


# we like to see celery results using the admin
class TaskMetaAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'date_done', 'status', )

admin.site.register(TaskMeta, TaskMetaAdmin)
