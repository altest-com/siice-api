from django.contrib import admin

from . import models


@admin.register(models.Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Corporation)
class CorporationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Dependency)
class DependencyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Secondment)
class SecondmentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Medical)
class MedicalAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Polygraphic)
class PolygraphicAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Psychological)
class PsychologicalAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Socioeconomic)
class SocioeconomicAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Toxicological)
class ToxicologicalAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass