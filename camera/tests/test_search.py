import pytest


@pytest.mark.django_db(transaction=True)
class TestCameraSearcher:
    def filter_by_name(self):
        pass