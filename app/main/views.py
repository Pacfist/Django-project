from django.shortcuts import render
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name='main/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Home'
        context['content']='Main page of website'
        return context


def index(request):
      context={
          'title':'Home page',
         'content':'Main page of website',
        
          }
      return render(request, 'main/main.html',context)

# def about(request):
#     context={
#         'title':'About',
#         'content':'Main page of website'
#     }
#     return render(request, 'main/about.html',context)



class AboutView(TemplateView):
    template_name='main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='About'
        context['content_info']='About the sneaker shop'
        return context