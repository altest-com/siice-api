from drf_schemas.models import ItemSchema, Item

from .models import (
    Evaluation,
    Socioeconomic,
    Medical,
    Polygraphic,
    Psychological,
    Toxicological
)

sections = [{
    'field': 'socioeconomic',
    'model': Socioeconomic,
    'data_pk': 1,
    'data_name': 'Socioeconómico'
}, {
    'field': 'medical',
    'model': Medical,
    'data_pk': 2,
    'data_name': 'Médico'
}, {
    'field': 'psychological',
    'model': Psychological,
    'data_pk': 3,
    'data_name': 'Psicológico'
}, {
    'field': 'polygraphic',
    'model': Polygraphic,
    'data_pk': 4,
    'data_name': 'Poligráfico'
}, {
    'field': 'toxicological',
    'model': Toxicological,
    'data_pk': 5,
    'data_name': 'Toxicológico'
}]


def create_schemas():
    for section in sections:
        try:
            ItemSchema.objects.get(pk=section['data_pk'])
        except ItemSchema.DoesNotExist:
            schema = ItemSchema(name=section['data_name'])
            schema.pk = section['data_pk']
            schema.save()


def fill_evaluation(evaluation: Evaluation):
    for section in sections:
        eval_section = getattr(evaluation, section['field'], None)
        if eval_section is None:
            try:
                schema = ItemSchema.objects.get(pk=section['data_pk'])
            except ItemSchema.DoesNotExist:
                create_schemas()
                schema = ItemSchema.objects.get(pk=section['data_pk'])

            eval_data = Item.objects.create(schema=schema)
            eval_section = section['model'].objects.create(eval_data=eval_data)
            setattr(evaluation, section['field'], eval_section)
