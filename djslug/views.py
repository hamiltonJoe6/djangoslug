from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse


from .models import Blog
from django.http import Http404

def BlogView(request):
	if request.method == 'GET':
		try:
			blog = Blog.objects.values()
			context = {'blog': blog}
		except Blog.DoesNotExist:
			raise Http404('Page not Found')
		return render(request, 'blogindex.html', context)

from django.views import View

class Blogdetail(View):
	def get(self, request, slug, id):
		try:
			BlogDetail = Blog.objects.get(slug=slug)
			context = {'BlogDetail': BlogDetail}
		except Blog.DoesNotExist:
			raise Http404('Page does not exist')

		return render(request, 'blogdetail.html', context)



def Blogdetail1(request, slug, id):
	if request.method == 'GET':
		try:
			BlogDetail = Blog.objects.get(slug=slug)
			context = {'BlogDetail': BlogDetail}
		except Blog.DoesNotExist:
			raise Http404('Page does not exist')
		return render(request, 'blogdetail.html', context)


"""https://stackoverflow.com/questions/45659986/django-implementing-a-form-within-a-generic-detailview"""


from django.core.mail import send_mail
from django.conf import settings
def msg1(request):

	if request.method == 'POST':
		message = request.POST['message']
		email = request.POST['email']
		name = request.POST['name']

		print(message, email, name)
		send_mail(
			'Contact Form',
			message,
			'settings.EMAIL_HOST_USER',
			[email],
			fail_silently=False,
			)


	return render(request, 'index1.html')


def msg(request):
	if request.method == 'POST':
		message = request.POST['message']
		email = request.POST['email']
		name = request.POST['name']

		print(message, email, name)
		send_mail(
			'Contact Form',
			message,
			'settings.EMAIL_HOST_USER',
			[email],
			fail_silently=False,
			)


	return render(request, 'index1.html')


def index(request):
	return HttpResponse('Hello there!!')


def index1(request):
	return render(request, 'index.html')


from djslug.forms import CommentForm
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic.detail import DetailView

"""https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/"""

class BlogDetailView(DetailView):
	model = Blog
	template_name = 'blogdetail1.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = CommentForm()

		return context

	def post(self, request, slug, *args, **kwargs):

		blog = Blog.objects.get(slug=slug)

		if request.method == 'POST':
			if not request.user.is_authenticated:
				return HttpResponseRedirect('index1/')

			form = CommentForm(request.POST)

			if form.is_valid():
				instance = form.save(commit=False)
				instance.blog = blog
				instance.createdBy = request.user
				instance.created_at = timezone.now()
				instance.save()

				#return redirect('SimpleBlog:index1')
				return redirect('SimpleBlog:detail1', slug=blog.slug, id=blog.id)

			else:
				return HttpResponse('Page does not exist')

		else:
			form = CommentForm()

		context = {'blog': blog, "form": form}

		return render(request, template_name, context)

from django.urls import reverse_lazy
from django.template.context_processors import csrf

def postComment(request, slug, id, *args, **kwargs):
	success_url = reverse_lazy('SimpleBlog:index1')

	blog = Blog.objects.get(id=id)

	if request.method == 'POST':

		print(blog.slug)
		print(blog.id)

		form = CommentForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.blog = blog
			instance.createdBy = request.user
			instance.created_at = timezone.now()
			instance.save()
			return redirect('SimpleBlog:detail', slug=blog.slug, id=blog.id)

		else:
			return HttpResponse('Page not Present')

	else:
		form = CommentForm()

	context = {'blog': blog, 'form': form}
	return render(request, 'postComment.html', context)











