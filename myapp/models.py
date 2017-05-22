#!/usr/bin/python
#-*-coding: utf-8 -*
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

STATE_TYPES = (
	(1, 'Monday'),
	(2, 'Tuesday'),
	(3, 'Wednesday'),
	(4, 'Thursday'),
	(5, 'Friday'),
)
FACULTY_TYPES = (
    ('1', u'คณะวิทยาศาสตร์และเทคโนโลยี'),
    ('2', u'คณะวิศวกรรมศาสตร์'),
    ('3', u'คณะสถาปัตยกรรมศาสตร์และการผังเมือง'),
    ('4', u'คณะแพทยศาสตร์'),
    ('5', u'คณะสาธารณสุขศาสตร์'),
    ('6', u'คณะทันตแพทยศาสตร์'),
    ('7', u'คณะสหเวชศาสตร์'),
    ('8', u'คณะพยาบาลศาสตร์'),
    ('9', u'คณะสังคมวิทยาและมานุษยวิทยา'),
    ('10', u'คณะศิลปศาสตร์'),
    ('11', u'คณะนิติศาสตร์'),
    ('12', u'คณะรัฐศาสตร์'),
    ('13', u'คณะสังคมสงเคราะห์ศาสตร์'),
    ('14', u'คณะพาณิชยศาสตร์และการบัญชี'),
    ('15', u'คณะเศรษฐศาสตร์'),
    ('16', u'คณะวารสารศาสตร์และสื่อสารมวลชน'),
    ('17', u'คณะศิลปกรรมศาสตร์'),
    ('18', u'สถาบันเทคโนโลยีนานาชาติสิรินธร'),
    ('19', u'วิทยาลัยโลกคดีศึกษา'),
    ('20', u'วิทยาลัยแพทยศาสตร์นานาชาติจุฬาภรณ์'),
    ('21', u'วิทยาลัยนวัตกรรม'),
    ('22', u'วิทยาลัยนวัตกรรมอุดมศึกษา'),
    ('23', u'วิทยาลัยสหวิทยาการ'),
    ('24', u'วิทยาลัยนานาชาติปรีดี พนมยงค์'),
    ('25', u'คณะเภสัชศาสตร์'),
    ('26', u'คณะวิทยาการเรียนรู้และศึกษาศาสตร์'),
)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=20,blank=True, null=True) # datefield YYYY-MM-DD
    faculty = models.CharField(choices=FACULTY_TYPES,max_length=50)
    gender=models.CharField(
        choices=(
            ('1', u'Male'),
            ('2', u'Female'),
            ),
        max_length=6, blank=True, null=True
    )
    student_id = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10,blank=True, null=True)
    photo = models.ImageField(upload_to="image_profile", blank=True)
    def __unicode__(self):
        return u"%s"%(self.first_name)

class Add_act(models.Model):
    type_of_act = models.CharField(
        choices=(
            ('2', u'Activity'),
            ('1', u'Event'),
            ),
        max_length=10, default='2'
    )
    category=models.CharField(
        choices=(
            ('1', u'Sport'),
            ('2', u'Music'),
            # ('3', u'ศิลป์'),
            ('4', u'Club'),
            ('5', u'Workshop'),
            # ('6', u'Education'),
            ('7', u'Camp'),
            ('8', u'Other'),
            ),
        max_length=20, default='8'
    )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000,blank=True, null=True)
    speaker_name = models.CharField(max_length=200,blank=True, null=True)
    # present_by = models.CharField(max_length=50)
    date_time = models.CharField(max_length=200) # YYYY-MM-DD
    place = models.CharField(max_length=1000)
    college_years = models.CharField(
        choices=(
            ('1', u'รับระดับชั้นปี 1 ขึ้นไปหรือเทียบเท่า'),
            ('2', u'รับระดับชั้นปี 2 ขึ้นไปหรือเทียบเท่า'),
            ('3', u'รับระดับชั้นปี 3 ขึ้นไปหรือเทียบเท่า'),
            ('4', u'รับระดับชั้นปี 4 ขึ้นไปหรือเทียบเท่า'),
            ('5', u'รับทุกระดับชั้นปี'),
            ),
        max_length=20, default='5'
    )
    quantity = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="image_activity")
    register_link = models.CharField(max_length=200,blank=True, null=True)
    create_by_user_id = models.CharField(max_length=100)
    score = models.CharField(max_length=100,blank=True, null=True)
    def __unicode__(self):
        return u"%s %s"%(self.type_of_act,self.name)

class Poll(models.Model):
    activity = models.ForeignKey(Add_act, blank=True,null=True)
    vote = models.IntegerField(choices=STATE_TYPES, default=0, null=True)
    days = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    def __unicode__(self):
        return u"%s"%(self.vote)

