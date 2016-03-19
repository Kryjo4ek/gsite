from django.shortcuts import render_to_response, Http404, redirect
from vote.models import Votes, Answer, Comments
from django.core.exceptions import ObjectDoesNotExist
from vote.forms import CommentForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect


def all(request):

    args = {'votes': Votes.objects.all()}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    return render_to_response('vote.html', args)

def onevote(request, votes_id=1, number_page=1):
    paginator_objects = Answer.objects.filter(answer_id_vote=votes_id)
    paginator_page = Paginator(paginator_objects, 2)
    args = {}
    args.update(csrf(request))
    args['vote'] = Votes.objects.get(id=votes_id)
    args['answers'] = paginator_page.page(number_page)
    args['form'] = CommentForm
    args['username'] = auth.get_user(request).username

    return render_to_response('onevote.html', args)


def addlike(request, votes_id):

    try:
        if votes_id in request.COOKIES:
            redirect('/')
        else:
            vote = Votes.objects.get(id=votes_id)
            vote.vote_like += 1
            vote.save()
            response = redirect('/')
            response.set_cookie(votes_id, "test")
            return response

    except ObjectDoesNotExist:
        raise Http404

    return redirect('/')

def addcomment(request, votes_id):

    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.answer_id_vote = Votes.objects.get(id=votes_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/votes/get/%s/' %votes_id)


def answerall(request):

    if request.POST:
        answers = request.POST
        votes = Votes.objects.all()
        for vote in votes:
            answer = Answer.objects.get(id=answers[str(vote.id)])
            print(answer)
            answer.vote_number += 1
            answer.save()

    args = {}
    args.update(csrf(request))
    args['votes'] = Votes.objects.all()

    return render_to_response('answerall.html', args)