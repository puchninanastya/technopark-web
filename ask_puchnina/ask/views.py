# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

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

def paginate(objects_list, num_objects_on_list, current_page):
	paginator = Paginator(objects_list, num_objects_on_list)
	page_range = paginator.page_range

	try:
		result_current_page = int(current_page)
	except ValueError:
		result_current_page = 1

	if (result_current_page > paginator.num_pages):
		result_current_page = paginator.num_pages

	return paginator.page(result_current_page), page_range

def newQuestions(request, page=1):
	questionsValues = QUESTIONS.values()
	questions, pr = paginate(questionsValues, 2, page)
	context = {
		'questions': questions,
		'page_range': pr,
		'page_url_name': 'new-questions-page',
	}
	return render(request, 'questions_list.html', context)

def hotQuestions(request, page=1):
	questionsValues = QUESTIONS.values()
	questions, pr = paginate(questionsValues, 2, page)
	context = {
		'questions': questions,
		'page_range': pr,
		'page_url_name': 'hot-questions-page',
	}
	return render(request, 'questions_list.html', context)

def tagQuestions(request, tagname, page=1):
	questions = QUESTIONS.values()
	return render(request, 'tag_questions.html', {"questions": questions})

def question(request, qid, page=1):
	question = QUESTIONS.get(qid, {})
	answersValues = ANSWERS.values()
	answers,pr = paginate(answersValues, 2, page)
	context = {
		'question': question,
		'answers': answers,
		'page_range': pr,
		'page_url_name': 'question-page',
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
