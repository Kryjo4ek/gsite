from django.forms import ModelForm
from vote.models import Answer


class CommentForm(ModelForm):

    class Meta:

        model = Answer
        fields = ['vote_answer']


#class AnswerForm(ModelForm):

#    class Meta:

 #       model = Answer
  #      fields = ['vote_answer']