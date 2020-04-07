from rest_framework.test import APITransactionTestCase

from .factory import (
    ModelFactory,
    DateFieldFactory,
    TimeFieldFactory,
    DateTimeFieldFactory
)
from .mixins import (
    MixinViewCreateTest,
    MixinViewListTest,
    MixinViewRetrieveTest,
    MixinViewUpdateTest,
    MixinViewDeleteTest
)


class _ViewTest(APITransactionTestCase):

    url_list = ''
    url_detail = ''
    model_factory: ModelFactory = None
    list_count = 1
    valid_data = {}
    list_instances = []
    destroy_instances = []

    def setUp(self):
        self.invalid_data = {}

        self.valid_data = {
            'Full data': self.model_factory.api_post_data(),
            'Minimal data': self.model_factory.api_post_data(full=False)
        }

        self.instances = [
            self.model_factory.create_instance()
            for _ in range(self.list_count)
        ]


class _FieldViewTest(
    _ViewTest,
    MixinViewCreateTest,
    MixinViewListTest,
    MixinViewRetrieveTest,
    MixinViewUpdateTest,
    MixinViewDeleteTest
):
    pass


class DateFieldViewTest(_FieldViewTest):

    url_list = 'api:date-fields-list'
    url_detail = 'api:date-fields-detail'
    model_factory = DateFieldFactory()


class TimeFieldViewTest(_FieldViewTest):

    url_list = 'api:time-fields-list'
    url_detail = 'api:time-fields-detail'
    model_factory = TimeFieldFactory()


class DateTimeFieldViewTest(_FieldViewTest):

    url_list = 'api:datetime-fields-list'
    url_detail = 'api:datetime-fields-detail'
    model_factory = DateTimeFieldFactory()


del _FieldViewTest

