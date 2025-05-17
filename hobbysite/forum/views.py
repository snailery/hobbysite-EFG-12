from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models
from . import forms

def index(request):
    return HttpResponse("Forum home")

class ThreadListView(ListView):
    model = models.Thread
    template_name = "forum/thread_list.html" #former threads.html

    def get_queryset(self):
        # Load all threads with related categories and authors
        return models.Thread.objects.select_related("category", "author").all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_threads = self.get_queryset()

        if self.request.user.is_authenticated:
            profile = get_object_or_404(models.Profile, user=self.request.user)
            user_threads = all_threads.filter(author=profile).order_by("-created_on")
            other_threads = all_threads.exclude(author=profile).order_by("-created_on")
        else:
            user_threads = None
            other_threads = all_threads.order_by("-created_on")

        # Group other users' threads by category
        threads_by_category = {}
        for thread in other_threads:
            category_name = thread.category.name if thread.category else "Uncategorized"
            threads_by_category.setdefault(category_name, []).append(thread)

        context["user_threads"] = user_threads
        context["threads_by_category"] = threads_by_category
        context["create_url"] = reverse_lazy("forum:thread_create")
        
        return context


def thread_detail(request, pk):
    thread = get_object_or_404(models.Thread, pk=pk)
    related_threads = models.Thread.objects.filter(category=thread.category).exclude(pk=pk)[:2]
    comments = thread.comments.order_by("created_on")

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

            if request.method == "POST":

        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thread = thread
            comment.author = request.user.profile
            comment.created_on = timezone.now()
            comment.updated_on = timezone.now()
            comment.save()
            return redirect("forum:thread_detail", pk=thread.pk)
    else:
        form = forms.CommentForm()

    context = {
        "thread": thread,
        "related_threads": related_threads,
        "comments": comments,
        "comment_form": form,
        "can_edit": request.user.is_authenticated and thread.author.user == request.user
    }

    return render(request, "forum/thread_view.html", context)


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = models.Thread
    fields = ["title", "entry", "image", "category"]
    template_name = "thread_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class ThreadUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Thread
    fields = ["title", "entry", "image", "category"]
    template_name = "forum/thread_form.html"

    def get_success_url(self):
        return self.object.get_absolute_url()


    def test_func(self):
        thread = self.get_object()
        return thread.author.user == self.request.user
