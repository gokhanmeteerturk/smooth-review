from django.shortcuts import render

# Create your views here.
from smoothapp.forms import UploadReviewSubmissionForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from smoothapp.models import ReviewSubmission
from django.views import View


def index(request):
    return HttpResponse("Hello, world. You're at the smoothapp index.")


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context_data = {
            'title': 'Smooth Reviews',
            'test_parameter': 'Test Value'
        }
        return render(request, self.template_name, context_data)


class ReviewSubmissionView(FormView):
    template_name = 'submit.html'
    form_class = UploadReviewSubmissionForm

    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
