from django.shortcuts import render, redirect
from .forms import Contact
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Count, Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from .models import Post, Category, Tag

# Create your views here.

def index(request):
  return render(request, 'myblog/index.html')

def contact(request):
  return render(request, 'myblog/contact.html')

def complete(request):
    return render(request, 'myblog/complete.html')

def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            myself = form.cleaned_data['myself']
            recipients = [settings.EMAIL_HOST_USER]
            if myself:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect('myblog:complete')
    else:
        form = Contact()
    return render(request, 'myblog/contact.html', {'form': form})


class  PostDetailView(DetailView):
  template_name = 'myblog/post_detail.html'
  model = Post

  def get_object(self, queryset=None):
    obj = super().get_object(queryset=queryset)
    if not obj.is_public and not self.request.user.is_authenticated:
      raise Http404
    return obj

class IndexView(ListView):
  model = Post
  template_name = 'myblog/index.html'

  paginate_by = 2

class CategoryListView(ListView):
  template_name = 'myblog/category_list.html'
  queryset = Category.objects.annotate(
    num_posts=Count('post', filter=Q(post__is_public=True)))
  
class TagListView(ListView):
  template_name = 'myblog/tag_list.html'
  queryset = Tag.objects.annotate(num_posts=Count(
    'post', filter=Q(post__is_public=True)))

class CategoryPostView(ListView):
    model = Post
    template_name = 'myblog/category_post.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class TagPostView(ListView):
    model = Post
    template_name = 'myblog/tag_post.html'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        qs = super().get_queryset().filter(tags=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
