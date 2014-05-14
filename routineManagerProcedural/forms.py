from django import forms

from models import Request
from models import Sequence
from models import Album
from models import Plan


from django.forms import ModelForm




class RequestForm(ModelForm):
    class Meta:
        model = Request
        
 
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = "form-control"
        self.fields['laboratory'].widget.attrs['class'] = "form-control"        
        self.fields['telnumber'].widget.attrs['class'] = "form-control"
        self.fields['email'].widget.attrs['class'] = "form-control"     
        self.fields['laboratory'].widget.attrs['readonly'] = True        
        self.fields['telnumber'].widget.attrs['readonly'] = True 
        self.fields['email'].widget.attrs['readonly'] = True 
#         self.fields['request_is_ALERT'].widget.attrs['class'] = "form-control"
        self.fields['target_type'].widget.attrs['class'] = "form-control"
        self.fields['sequences_number'].widget.attrs['class'] = "form-control"
#         self.fields['sequences_number'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['class'] = "form-control"
        self.fields['status'].widget.attrs['readonly'] = True
         
 
class SequenceForm(ModelForm):
    class Meta:
        model = Sequence
        
 
    def __init__(self, *args, **kwargs):
        super(SequenceForm, self).__init__(*args, **kwargs)
        self.fields['request'].widget.attrs['class'] = "form-control"
        self.fields['request'].widget.attrs['readonly'] = True
        self.fields['coord_system_id'].widget.attrs['class'] = "form-control"
        self.fields['target_ra'].widget.attrs['class'] = "form-control"
        self.fields['target_dec'].widget.attrs['class'] = "form-control"        
        self.fields['jd1'].widget.attrs['class'] = "form-control"
        self.fields['jd2'].widget.attrs['class'] = "form-control"
        self.fields['event_type'].widget.attrs['class'] = "form-control"
        self.fields['burst_id'].widget.attrs['class'] = "form-control"
        self.fields['priority'].widget.attrs['class'] = "form-control"
        self.fields['duration'].widget.attrs['class'] = "form-control"
        self.fields['status'].widget.attrs['class'] = "form-control"
        self.fields['status'].widget.attrs['readonly'] = True
        

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        
 
    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['sequence'].widget.attrs['class'] = "form-control"
        self.fields['sequence'].widget.attrs['readonly'] = True
        self.fields['type'].widget.attrs['class'] = "form-control"
        self.fields['plans_number'].widget.attrs['class'] = "form-control"
        self.fields['status'].widget.attrs['class'] = "form-control"
        self.fields['status'].widget.attrs['readonly'] = True
                 
 
class PlanForm(ModelForm):
    class Meta:
        model = Plan
        
         
    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        self.fields['album'].widget.attrs['class'] = "form-control"
        self.fields['album'].widget.attrs['readonly'] = True
        self.fields['iteration_number'].widget.attrs['class'] = "form-control"
        self.fields['integration_time'].widget.attrs['class'] = "form-control"
        self.fields['filter'].widget.attrs['class'] = "form-control"
        self.fields['status'].widget.attrs['class'] = "form-control"
        self.fields['status'].widget.attrs['readonly'] = True
       
    
      