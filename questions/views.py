from django.db.models.query_utils import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import *
from questions.forms import AnswerForm, QuestionForm
from django.http import HttpResponseRedirect
from questions.models import Answer, Question

# Create your views here.

def landing_page(request):
    return render(request, "landing.html")

def LikeView(request, pk):
    question = get_object_or_404(Question, id=request.POST.get('question_id'))
    if question.likes.filter(id=request.user.id).exists():
        question.likes.remove(request.user)
        question.is_liked = False
        question.save()
    else:
        question.likes.add(request.user)
        question.is_liked = True
        question.save()
    return HttpResponseRedirect(reverse('questions:index'))

def LikeAnswer(request, pk):
    answer = get_object_or_404(Answer, id=request.POST.get('answer_id'))
    if answer.likes.filter(id=request.user.id).exists():
        answer.likes.remove(request.user)
        answer.is_liked = False
        answer.save()
    else:
        answer.likes.add(request.user)
        answer.is_liked = True
        answer.save()
    return HttpResponseRedirect(reverse("questions:index"))

def question_delete(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return redirect('questions:index')

class QuestionCreateView(CreateView):
    model = Question
    template_name = "question_create.html"
    form_class = QuestionForm

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("questions:index")

class QuestionListView(ListView):
    model = Question
    template_name = 'index.html'
    paginate_by = 8
    ordering = ['-timestamp']

class QuestionDetailView(DetailView):
    model = Question
    template_name = "question_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AnswerForm()
        return context

class CommentView(CreateView):
    model = Answer
    form_class = AnswerForm

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        pk = self.kwargs.get('pk')
        question = Question.objects.get(id=pk)
        return reverse("questions:details", kwargs={'pk': question.pk})

class SearchResultsView(ListView):
    model = Question
    template_name = 'index.html'
    paginate_by = 20
    ordering = ['-timestamp']

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        if query:
            q_list = Question.objects.filter(
                Q(question__icontains=query) | Q(id__icontains=query) | Q(author__username__icontains=query)
            ).order_by('-timestamp')
            return q_list
        return Question.objects.all().order_by('-timestamp')

class QuestionUpdateView(UpdateView):
    model = Question
    template_name = 'question_update.html'
    form_class = QuestionForm

    def get_success_url(self):
        return reverse("questions:index")
