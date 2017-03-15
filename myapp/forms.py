from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin import widgets
import datetime
from .models import Poll,Add_act

STATE_TYPES = (
	(0, 'Monday'),
	(1, 'Tuesday'),
	(2, 'Wednesday'),
	(3, 'Thursday'),
	(4, 'Friday'),
	(5, 'Saturday'),
	(6, 'Sunday'),
)

class PollForm(ModelForm):

	state = forms.ChoiceField(choices=STATE_TYPES, widget=forms.RadioSelect())

	class Meta:
		model =  Poll
		exclude=['Poll']

		fields = ('state',)
		widgets = {
			'state': forms.RadioSelect(),
		}

	def __init__(self, *args, **kwargs):
		super(PollForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

class AddForm(ModelForm):
	class Meta:
		model =  Add_act
		exclude=['Add_act']

	def __init__(self, *args, **kwargs):
		super(AddForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))