from django.db import models
from django.utils import timezone


class CategoryQuerySet(models.QuerySet):

    def published(self):
        return self.filter(is_published=True)


class PostQuerySet(models.QuerySet):

    def published(self):
        return self.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        ).distinct()

    def for_index_page(self):
        return self.published()
