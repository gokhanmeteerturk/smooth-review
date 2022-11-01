from django import forms
from smoothapp.models import ReviewSubmission, WaitListRecord
from smoothapp.cssClassNames import FormCss


class UploadReviewSubmissionForm(forms.ModelForm):
    class Meta:
        model = ReviewSubmission
        fields = ['description', 'screenshot_app', 'screenshot_review']

        widgets = {
            'description': forms.TextInput(attrs={'class': FormCss.text_input_class_name}),
            'screenshot_app': forms.FileInput(attrs={'class': FormCss.file_input_class_name}),
            'screenshot_review': forms.FileInput(attrs={'class': FormCss.file_input_class_name})
        }
        labels = {
            'description': 'Message to the developer',
            'screenshot_app': 'Screenshot of the app',
            'screenshot_review': 'Screenshot of your review'
        }
        warn_fake_ss = ' Irrelevant/misleading screenshots will cause permanent account removal.'
        help_texts = {
            'description': 'Optional. You can leave a short message to the developer.',
            'screenshot_app': 'Take a screenshot proving you opened the app before leaving a review.' + warn_fake_ss,
            'screenshot_review': 'Take a screenshot of the App Store or Play Store showing your review.' + warn_fake_ss
        }


class WaitListForm(forms.ModelForm):
    class Meta:
        model = WaitListRecord
        fields = ['email']
        widgets = {
            'email': forms.EmailInput()
        }
