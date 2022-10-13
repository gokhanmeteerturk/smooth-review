from django import forms
from smoothapp.models import ReviewSubmission

class UploadReviewSubmissionForm(forms.ModelForm):

    class Meta:
        model = ReviewSubmission
        fields = ['description', 'image']

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'mt-3 border-0'})
        }