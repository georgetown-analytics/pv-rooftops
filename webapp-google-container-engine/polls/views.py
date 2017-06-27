# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


##new code below:

from django.shortcuts import render
from .models import Question
from .models import TestDbDjango

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    #old context
    #context = {'latest_question_list': latest_question_list}
    
    #rdsdb = 42
    rdsdb = TestDbDjango.objects.using('rds-postgres').order_by('year')
    context = {'latest_question_list': latest_question_list, 'rdsdb':rdsdb}
    
    return render(request, 'polls/mat-index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
