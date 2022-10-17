from django.shortcuts import render

# Create your views here.
from smoothapp.forms import UploadReviewSubmissionForm, WaitListForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from smoothapp.models import ReviewSubmission, WaitListRecord
from django.views import View


class IndexView(FormView):
    template_name = 'index/index.html'
    success_url = '/waitlist-successful/'
    form_class = WaitListForm

    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data['title'] = 'Smooth Reviews'

        return context_data


class ReviewSubmissionView(FormView):
    template_name = 'submit.html'
    form_class = UploadReviewSubmissionForm

    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class WaitListFormSuccessView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "registration/waitlist_successful.html")
