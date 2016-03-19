from django.db import models

# Create your models here.


class Votes(models.Model):

    class Meta():

        db_table = 'votes'

    vote_question = models.CharField(max_length=200)

    vote_time = models.DateTimeField()

    vote_like = models.IntegerField(default=0)


class Answer(models.Model):

    class Meta():

        db_table = 'answer'

    vote_answer = models.CharField(max_length=200)
    answer_id_vote = models.ForeignKey(Votes)
    vote_number = models.IntegerField(default=0)

class Comments(models.Model):

    class Meta():

        db_table = 'comment'

    comment_text = models.TextField(verbose_name='vvedi comment')
    comment_like = models.IntegerField(default=0)
    comment_id_vote = models.ForeignKey(Votes)


