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

from django.db import models

import datetime
from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# Create your models here.

class TestDbDjango(models.Model):
    geoid = models.IntegerField(blank=True, primary_key=True)
    county = models.CharField(max_length=4200, blank=True, null=True)
    state = models.CharField(max_length=4200, blank=True, null=True)
    year = models.CharField(max_length=4200, blank=True, null=True)
    quarter = models.CharField(max_length=4200, blank=True, null=True)
    count = models.CharField(max_length=4200, blank=True, null=True)
    households = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hhincome_above_200k = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    average_rtl_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_per_watt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    year_since_1990 = models.FloatField(blank=True, null=True)
    grid_to_panel_cost_ratio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    net_metering = models.CharField(max_length=42000, blank=True, null=True)
    net_metering_grade = models.CharField(max_length=42, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'test-db-django'



