from django.forms import ModelForm
from checkbook.models import Information
from checkbook.models import Accounts


class AccountInfo(ModelForm):
    class Meta:
        model = Information
        fields = '__all__'


class ChooseAccount(ModelForm):
    class Meta:
        model = Accounts
        fields = '__all__'

