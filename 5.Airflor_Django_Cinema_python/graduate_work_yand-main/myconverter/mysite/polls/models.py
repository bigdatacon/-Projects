import uuid
# https://www.youtube.com/watch?v=fsVY66QBhwM
from django.db import models
import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _




class Fileupl(TimeStampedModel):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    file_path = models.FileField(_('File'), upload_to='files/')
    resolution = models.CharField(_('Resolution'), null=True, max_length=100)
    codec_name = models.CharField(_('Codec'), max_length=100, null=True, blank=True)
    display_aspect_ratio = models.CharField(_('Display Aspect Ratio'), max_length=100, null=True, blank=True)
    fps = models.IntegerField(_('FPS'), null=True, blank=True)
    film = models.ForeignKey('FilmWork',  related_name='files', null=True, verbose_name="Фильм", on_delete=models.CASCADE)
    #
    class Meta:
        verbose_name = _('Fileupl')
        verbose_name_plural = _('Fileupl')
        # managed = False
        # db_table = f'"content"."file"'
        ordering = ["file_path"]
    #
    def __str__(self):
        return f'{self.file_path}'

class FilmWork(TimeStampedModel):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('Name'), max_length=255, null=True,)
    certificate = models.TextField(_('Certificate'), blank=True)
    file_path = models.FileField(_('Original file'), upload_to='film_works/')
    # files = models.ManyToManyField('Fileupl', through='FileFilmWork', related_name='filmworks')

    class Meta:
        verbose_name = _('Film')
        verbose_name_plural = _('Films')
        # managed = False
        # db_table = f'"content"."film_work"'
        ordering = ["title"]

    def __str__(self):
        return f'{self.file_path}'


