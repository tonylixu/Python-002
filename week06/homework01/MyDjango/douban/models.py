from django.db import models


# Create your models here.
class Movie(models.Model):
    comments_id = models.BigAutoField(primary_key=True)
    movie_comments = models.CharField(max_length=400)
    movies_stars = models.IntegerField()
    movie_comment_date = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'douban_movie'