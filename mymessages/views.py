from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout

from .models import Message
from .forms import MessageForm, CreationForm

def index(request):
    messages = Message.objects.all()[::-1]
    form = MessageForm(request.POST or None)

    if not form.is_valid():
        return render(
            request,
            'index.html',
            context={
                'messages': messages,
                'form': form,
            }
        )

    new_message = form.save(commit=False)
    new_message.author = request.user
    new_message.save()

    return redirect('index')


def update_messages(request):
    messages = Message.objects.all()[::-1]
    return render(request, 'messages_partial.html', {'messages': messages})


def logout_view(request):
    logout(request)
    return redirect('/')


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('index')
    template_name = 'signup.html'



