from django.contrib import admin
from vote.models import Votes, Comments,Answer
# Register your models here.


class VoteInLine(admin.StackedInline):
    model = Comments
    extra = 2
    fields = ['comment_text']


class VoteInLine2(admin.StackedInline):
    model = Answer
    extra = 2
    fields = ['vote_answer']

class VoteAdmin(admin.ModelAdmin):
    fields = ['vote_question', 'vote_time']
    inlines = [VoteInLine, VoteInLine2]
    list_filter = ['vote_time']
admin.site.register(Votes, VoteAdmin)