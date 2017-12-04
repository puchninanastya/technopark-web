# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#TEST DATA
QUESTIONS = {
	'1': {'id': 1, 'title': 'I`m your dream', 'text': 'I`m your dream, make you real', 'rating': 23,},
	'2': {'id': 2, 'title': 'I`m your eyes', 'text': 'I`m your eyes when you must steal', 'rating': 12,},
	'3': {'id': 3, 'title': 'I`m your pain', 'text': 'I`m your pain when you can`t feel', 'rating': 16,},
}

ANSWERS = {
	'1': {'id': 1, 'text': 'Make you real', 'rating': 1, 'correct': 1,},
	'2': {'id': 2, 'text': 'You must steal', 'rating': 2, 'correct': 0,},
	'3': {'id': 3, 'text': 'You can`t feel', 'rating': 3, 'correct': 1,},
}

def hello(request):
	output_str = "New request\n"
	if request.method == 'GET':
		if request.GET:
			get_qd = request.GET
			output_str += "Get Params:\n" + str(get_qd.items()) + "\n"
	elif request.method == 'POST':
		if request.POST:
			post_qd = request.POST
			output_str += ("Post Params:\n" + str(post_qd.items())) + "\n"
	else:
		return output_str("No params!\n")
	return HttpResponse(output_str)

def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 2))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(qs, limit)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return page, paginator

def newQuestions(request):
	questionsValues = QUESTIONS.values()
	page, paginator = paginate(request, questionsValues)
	paginator.baseurl = reverse('new-questions')
	context = {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	}
	return render(request, 'questions_list.html', context)

def hotQuestions(request):
	questionsValues = QUESTIONS.values()
	page, paginator = paginate(request, questionsValues)
	paginator.baseurl =  reverse('hot-questions')
	context = {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	}
	return render(request, 'questions_list.html', context)

def tagQuestions(request, tagname):
	questionsValues = QUESTIONS.values()
	tag = {'title': tagname}
	page, paginator = paginate(request, questionsValues)
	paginator.baseurl =  reverse('tag-questions', kwargs={'tagname': tagname})
	context = {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
		'tag': tag
	}
	return render(request, 'tag_questions.html', context)

def question(request, qid):
	question = QUESTIONS.get(qid, {})
	answersValues = ANSWERS.values()
	page, paginator = paginate(request, answersValues)
	paginator.baseurl = reverse('question', kwargs={'qid': qid})
	context = {
		'question': question,
		'answers': page.object_list,
		'page': page,
		'paginator': paginator,
	}
	return render(request, 'question.html', context)

def ask(request):
	return render(request, 'ask.html')

def login(request):
	return render(request, 'login.html')

def signup(request):
	return render(request, 'signup.html')

def settings(request):
	return render(request, 'settings.html')

def about(request):
	return render(request, 'about.html')
