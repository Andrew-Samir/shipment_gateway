from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet
from django.utils import timezone


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super().update(date_deleted=timezone.now())

    def hard_delete(self):
        return super().delete()

    def alive(self):
        return self.filter(date_deleted=None)

    def dead(self):
        return self.exclude(date_deleted=None)


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(date_deleted=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModel(models.Model):
    date_deleted = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('User', on_delete=models.DO_NOTHING, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self, deleted_by = None):
        self.date_deleted = timezone.now()
        self.deleted_by = deleted_by
        self.save()

    def hard_delete(self):
        super().delete()


class BaseModel(SoftDeletionModel):
    
    class Meta:
        abstract = True
