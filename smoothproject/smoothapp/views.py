from django.shortcuts import render

# Create your views here.
from smoothapp.forms import UploadReviewSubmissionForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from smoothapp.models import ReviewSubmission


def index(request):
    return HttpResponse("Hello, world. You're at the smoothapp index.")


class ReviewSubmissionView(FormView):
    template_name = 'index.html'
    form_class = UploadReviewSubmissionForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)
