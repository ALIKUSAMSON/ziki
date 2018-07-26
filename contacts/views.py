from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

# Create your views here.
def contact(request):
	title = 'Contact'
	form = ContactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		name =  form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = "Message fro dengima.com"
		message = "%s %s" %(comment,name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(
			subject,message,emailFrom,emailTo,fail_silently=False,
			)
		title = "Thanks"
		confirm_message = "Thanks for the message. we will get back to you"
		form = None
	context = {'title' :title, 'form':form,'confirm_message':confirm_message}

	template = 'contacts/contacts.html'
	return render(request,template,context)
