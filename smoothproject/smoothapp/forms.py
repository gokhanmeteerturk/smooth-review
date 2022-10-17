from django import forms
from smoothapp.models import ReviewSubmission, WaitListRecord


class UploadReviewSubmissionForm(forms.ModelForm):
    class Meta:
        model = ReviewSubmission
        fields = ['description', 'screenshot_app', 'screenshot_review']

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'screenshot_app': forms.FileInput(attrs={'class': 'mt-3 border-0'}),
            'screenshot_review': forms.FileInput(attrs={'class': 'mt-3 border-0'})
        }


class WaitListForm(forms.ModelForm):
    class Meta:
        model = WaitListRecord
        fields = ['email']
        widgets = {
            'email': forms.EmailInput()
        }
