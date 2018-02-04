from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .forms import ScoreCreateForm
from .models import Score


def score_createview(request):
    form = ScoreCreateForm()
    if request.method == "POST":
      form = ScoreCreateForm(request.POST)
      if form.is_valid():
        obj = Score.objects.create(
            Call_number = form.cleaned_data.get('Call_number'),
            Score_title = form.cleaned_data.get('Score_title'),
            author = form.cleaned_data.get('author'),
            place_of_publication = form.cleaned_data.get('place_of_publication'),
            date_of_publication = form.cleaned_data.get('date_of_publication'),
            publisher = form.cleaned_data.get('publisher')
          )
      return HttpResponseRedirect("/restaurants/")
        
    template_name = 'restaurants/form.html'
    context = {"form": form}
    return render(request, template_name, context)

def score_listview(request,):
    template_name = 'restaurants/score_list.html'
    queryset = Score.objects.all()
    context = {
    }
    return render(request, template_name, context)

class ScoreListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Score.objects.filter(
                    Q(collection__iexact=slug) |
                    Q(collection__icontains=slug)
                )
        else:
            queryset = Score.objects.all()
        return queryset
class ScoreDetailView(DetailView):
    queryset = Score.objects.all()
    
    #def get_object(self, *args, **kwargs):
     #   score_id = self.kwargs.get('score_id')
      #  obj = get_object_or_404(Score, id=score_id) # pk = rest_id
       # return obj



