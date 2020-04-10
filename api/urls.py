from rest_framework.routers import SimpleRouter

from . import views

app_name = 'api'

router = SimpleRouter()
router.register(r'candidates', views.CandidateView, 'candidates')
router.register(r'corporations', views.CorporationView, 'corporations')
router.register(r'dependencies', views.DependencyView, 'dependencies')
router.register(r'secondments', views.SecondmentView, 'secondments')
router.register(r'positions', views.PositionView, 'positions')
router.register(r'applications', views.ApplicationView, 'applications')
router.register(r'evaluations', views.EvaluationView, 'evaluations')
router.register(r'medicals', views.MedicalView, 'medicals')
router.register(r'polygraphics', views.PolygraphicView, 'polygraphics')
router.register(r'psychologicals', views.PsychologicalView, 'psychologicals')
router.register(r'socioeconomics', views.SocioeconomicView, 'socioeconomics')
router.register(r'toxicologicals', views.ToxicologicalView, 'toxicologicals')
router.register(r'images', views.ImageView, 'images')
router.register(r'files', views.FileView, 'files')
router.register(r'alerts', views.AlertView, 'alerts')

urlpatterns = router.urls
