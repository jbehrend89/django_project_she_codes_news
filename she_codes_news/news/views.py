from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import NewsStory
from .forms import StoryForm
from django.views.generic.edit import UpdateView, DeleteView


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# print(kwargs)
#         form = kwargs['form']
#         form.instance.author = self.request.user
#         form.save()
#         return super(AddStoryView, self).form_valid(*args,**kwargs)

class StoryUpdateView(UpdateView):
    model = NewsStory
    fields = ['title', 'pub_date', 'category', 'content', 'image']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('news:story', kwargs={'pk':self.object.pk})


class StoryDeleteView(DeleteView):
    model = NewsStory
    success_url = reverse_lazy('news:index')


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
