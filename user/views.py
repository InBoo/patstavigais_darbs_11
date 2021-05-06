from django.shortcuts import render, HttpResponse
from user.models import User
from user.forms import UserForm
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy




"""
def index(request):

    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )
"""



# https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/#listview
class UserListView(ListView):
    model = User























"""
def get_user(request, user_id):

    user = User.objects.get(pk=user_id)

    context = {
        'user': user,
    }

    return render(
        template_name='user.html',
        request=request,
        context=context,
    )
"""



class UserDetailView(DetailView):
    model = User




























"""
def add_user(request):

    if request.method == 'POST':

        user = User(
            username=request.POST['name'],
            email=request.POST['email'],
        )

        user.save()

        context = {
            'user': user,
        }

        return render(
            template_name='user.html',
            request=request,
            context=context,

        )

    return render(
        template_name='form.html',
        request=request
    )

"""


"""
def add_user(request):

    if request.method == 'POST':
        # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#the-save-method
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            
            context = {
                'user': user,
            }

            return render(
                template_name='user.html',
                request=request,
                context=context,
            )

    # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#modelform
    user_form = UserForm()
    context = {
        'user_form': user_form,
    }
    return render(
        template_name='form.html',
        request=request,
        context=context,
    )
"""



# https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#formview
class AddUserView(FormView):

    form_class = UserForm
    template_name = 'user/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response

































"""
def edit_user(request, user_id):

    user = User.objects.get(id=user_id)

    if request.method == 'POST':

        username = request.POST['name']
        email = request.POST['email']

        if len(username) != 0:
            user.username = username

        if len(email) != 0:
            user.email = email

        user.save()

        context = {
            'user': user,
        }

        return render(
            template_name='user.html',
            request=request,
            context=context,

        )

    return render(
        template_name='form.html',
        request=request
    )
"""



"""
def edit_user(request, user_id):

    user = User.objects.get(id=user_id)

    if request.method == 'POST':

        # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#modelform
        user_form = UserForm(data=request.POST, instance=user)
        if user_form.is_valid():
            user = user_form.save()

            context = {
                'user': user,
            }

            return render(
                template_name='user.html',
                request=request,
                context=context,
            )

    # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#modelform
    user_form = UserForm(instance=user)
    context = {
        'user_form': user_form,
    }
    return render(
        template_name='form.html',
        request=request,
        context=context,
    )

"""



# https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#updateview
class EditUserView(UpdateView):

    form_class = UserForm
    model = User
    template_name = 'user/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response






















"""
def delete_user(request, user_id):

    user = User.objects.get(pk=user_id)
    user.delete()

    return HttpResponse(f'Deleted {user.username}')
"""



# https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#deleteview

class DeleteUserView(DeleteView):
    model = User
    success_url = reverse_lazy('index')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)









