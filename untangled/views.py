from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse 
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate , logout, login	
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import CreateView, DetailView, View
from django.views.decorators.cache import cache_control
from django.template import loader
from django.contrib import messages
from django.template import loader
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.core.mail import send_mail
import json
import cv2


# from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator

from untangled.models import *
from untangled.forms import *
# Create your views here.

# now = datetime.datetime.now()

# Register, View profile and Edit profile View
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url =  reverse_lazy('untangled:successRegister')

    def form_valid(self, form_class):
        messages.success(self.request, 'Successfully Register')
        return super().form_valid(form_class)

class UserEditView(generic.UpdateView):
    form_class = EditForm
    template_name = 'registration/editprofile.html'
    success_url =  reverse_lazy('untangled:profile')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form_class):
        messages.success(self.request, 'Profile Successfully Updated')
        return super().form_valid(form_class)

class ProfileView(generic.CreateView):
    template_name = 'registration/profile.html'

# class LoginView(generic.CreateView):
#     template_name = 'registration/login.html'

# ------------------- #

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def loggedIn(request):
    if request.user.is_authenticated:
        username = request.user.username
        template = loader.get_template('untangled/landingpage.html')
        context = {
            'username': username
        }
        return HttpResponse(template.render(context,request))
    else:
        return render(request, 'untangled/landingpage.html')


def home(request):
    featured = Blogs.objects.filter(is_featured=True)
    entries = Blogs.objects.filter(is_featured=False)
    entries_count = len(entries)
    paginator = Paginator(entries, 5)
    page_number =  request.GET.get('page')
    entries = paginator.get_page(page_number)
    return render(request, 'untangled/home.html', {'featured': featured, 'entries': entries, 'entries_count': entries_count})

# @login_required(login_url='untangled/loginview')
def about(request):
    return render(request, 'untangled/about.html')

def contactPage(request):
    return render(request, 'untangled/contact.html')

def loginview(request):
    messages.warning(request, "Please log in first to continue")
    return render(request, 'registration/login.html')

def successRegister(request):
    return render(request, 'registration/login.html')
# def registerview(request):
#     return render(request, 'registration/register.html')

def process(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        messages.error(request, 'Login Failed, Incorrect Username or Password.')
        return render(request, 'registration/login.html', {
            # 'error_message': "Login Failed, Incorrect Username or Password.",
            # 'user': user
        })

def processlogout(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return HttpResponseRedirect('/blogs')

@login_required(login_url='/login') 
def add(request):
    category = Category.objects.all()
    return render(request,'untangled/add.html', {'categories': category})
    # return render(request, 'untangled/add.html')

# @login_required(login_url='/login')
class AddPostView(CreateView):
    model = Blogs
    template_name = 'untangled/add.html'
    fields = ['blog_body']
    def get_context_data(self, *args, **kwargs):
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    

@login_required(login_url='')
def processAddPost(request):
    title = request.POST.get('title')
    category = request.POST.get('category')
    description = request.POST.get('description')
    body = request.POST.get('blog_body') 
    # hey = request.POST.get('heyyyy')
    user =  request.user
    fname = user.first_name
    lname = user.last_name
    # userid = user.id

    try:
        n =  Blogs.objects.get(blog_title=title)
        messages.error(request, 'Title Exist, Be more Unique.')
        return redirect('/create')
    except ObjectDoesNotExist:
        blogcreated = Blogs.objects.create(blog_title=title.title(), blog_description=description, blog_body=body,blog_pubdate=datetime.now(), blog_author='{}'.format(fname+' '+lname),blog_user=user,blog_category=category)
        blogcreated.save()
        messages.success(request, 'Blog Succesfully Published.')
        return redirect('/create')


#Make post as Draft
def processDraftPost(request):
    title = request.POST.get('title')
    category = request.POST.getlist('tags')
    description = request.POST.get('description')
    body = request.POST.get('blog_body')
    user =  request.user
    fname = user.first_name
    lname = user.last_name
    userid = user.id

    blogcreated = Blogs.objects.create(blog_title=title, blog_description=description, blog_body=body, blog_author='{}'.format(fname+' '+lname), blog_userid_id=userid, blog_tags=category,is_draft=True)
    blogcreated.save()
    messages.success(request, 'Blog save as Draft, you can access it on "Drafts" page.')
    return redirect('/create')

@login_required(login_url='') 
def addCategory(request):
    category = Category.objects.all()
    return render(request,'untangled/addCategory.html', {'categories': category})
    # return render(request, 'untangled/addCategory.html')

def processAddCategory(request):
    category = request.POST.get('category')
    try:
        n = Category.objects.get(blog_categories=category)
        messages.error(request, 'Category Exist!')
        return redirect('/addCategory')
    except ObjectDoesNotExist:
        categorysave = Category.objects.create(blog_categories=category.title())
        categorysave.save()
        messages.success(request, 'Category Successfully Added!')
        return redirect('/addCategory')

def deleteCategories(request, id):
    category = Category.objects.filter(id=id).delete()
    return redirect('/addCategory')

# @login_required(login_url='')
def profile(request, username):
    user = request.user
    user_info = User.objects.filter(username=username)
    for user_id in user_info:
        user_id = user_id.id
    
    blog_obj = Blogs.objects.filter(blog_user_id=user_id).filter(blog_pubdate__isnull=False).filter(deleted_on__isnull=True).order_by('blog_id')
    blog_obj_count = len(blog_obj)
    # tags = tags.objects.filter(blog_id_id=blog_obj.blog_id)
    paginator = Paginator(blog_obj, 5)
    page_number =  request.GET.get('page')
    blog_obj = paginator.get_page(page_number)
    return render(request, 'untangled/profile.html', {'blog_obj': blog_obj, 'blog_obj_count': blog_obj_count, 'user_info': user_info})
    # return render(request, 'untangled/profile.html')

@login_required(login_url='/login')
def edit(request):
    # page_obj = MyUsers.objects.get(pk=id)
    return render(request, 'untangled/editprofile.html')

@login_required(login_url='/login') 
def setting(request):
    return render(request, 'untangled/settings.html')


# def save(request):
#     # profile = request.POST.get('profile')
#     firstname = request.POST.get('firstname')
#     lastname = request.POST.get('lastname')
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     bio = request.POST.get('bio')
#     user = request.user
#     id = user.id
#     if request.FILES.get('profile'):
#         profile = request.FILES.get('profile')
#     else:
#         profile = '/profile_pics/default_pfp.jpeg'
    
#     saveprofile = request.user.objects.get(pk=id)
#     saveprofile.fname = firstname
#     saveprofile.lname = lastname
#     saveprofile.username = username
#     saveprofile.email = email
#     saveprofile.profile = profile
#     saveprofile.save()

#     # savebio = UsersBio.objects.get(user_userid=id)
#     # if savebio:
#     #     savebio.user_userid = id
#     #     savebio.aboutself
#     #     savebio.save()
#     # else:
#     #     Users
#     return redirect('/profile')

# def published(request):
#     return render(request, 'untangled/published.html')

def published(request):
    user = request.user
    blog_obj = Blogs.objects.filter(blog_user=user.id).filter(blog_pubdate__isnull=False).filter(deleted_on__isnull=True).order_by('blog_id')
    # tags = tags.objects.filter(blog_id_id=blog_obj.blog_id)
    paginator = Paginator(blog_obj, 5)
    page_number =  request.GET.get('page')
    blog_obj = paginator.get_page(page_number)
    return render(request, 'untangled/published.html', {'blog_obj': blog_obj})

def drafts(request):
    user = request.user
    blog_obj = Blogs.objects.filter(is_draft=True).filter(blog_user=user.id).order_by('blog_id')
    paginator = Paginator(blog_obj, 5)
    page_number =  request.GET.get('page')
    blog_obj = paginator.get_page(page_number)
    return render(request, 'untangled/drafts.html', {'blog_obj': blog_obj})

def deleted(request):
    user = request.user
    blog_obj = Blogs.objects.filter(deleted_on__isnull=False).filter(blog_userid=user.id).order_by('blog_id')
    paginator = Paginator(blog_obj, 5)
    page_number =  request.GET.get('page')
    blog_obj = paginator.get_page(page_number)
    return render(request, 'untangled/deleted.html', {'blog_obj': blog_obj})

# def blogEntry(request, blog_id):
#     try:
#         blog_obj = Blogs.objects.get(pk=blog_id)
        
        
#     except Blogs.DoesNotExist:
#         raise Http404("Blog Entry Does not Exist!")
#     # def get_context_data(self, *args, **kwargs):
#     #         reactions = get_object_or_404(Blogs, id=self.kwargs['pk'])
#     #         liked = False
#     #         if reactions.likes.filter(id=self.request.user.id).exists():
#     #             liked = True
#     #         context['liked'] = Liked
#     #         return context
#     return render(request, 'untangled/blogEntry.html', {'blog_obj': blog_obj})

class blogEntry(DetailView):
    model = Blogs
    template_name = 'untangled/blogEntry.html'

    def get_context_data(self, *args, **kwargs):
        context = super(blogEntry, self).get_context_data(*args, **kwargs)
        reaction = get_object_or_404(Blogs, pk=self.kwargs['pk'])
        total_like = reaction.total_likes()

        liked = False
        if reaction.likes.filter(pk=self.request.user.id).exists():
            liked = True

        context['liked'] = liked
        return context

@login_required
def like_post(request, pk, blog_title):
    post = get_object_or_404(Blogs, blog_id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    # return JsonResponse(data)
    return HttpResponseRedirect(reverse('untangled:blogEntry', args=[str(pk),blog_title]))
    

class PasswordChange(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url =  reverse_lazy('untangled:change-password')

    def form_valid(self, form_class):
        messages.success(self.request, 'Password Changed Successfully')
        return super().form_valid(form_class)


def landingpage(request):
    return render(request, 'untangled/landingpage.html')


# FOR PASSWORD RESET
class PassReset(PasswordResetView):
    form_class = ResetInputEmail


#For Books
def booksSection(request):
    return render(request, 'untangled/books.html')

# def capture_image(request):
#     cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
#     cap = cv2.VideoCapture(0)
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             return render(request, 'error.html', {'error': 'Failed to access the camera'})
#         cv2.imshow("Camera", frame)
#         key = cv2.waitKey(1) & 0xFF
#         if key == ord('q'):
#             return HttpResponseRedirect(reverse('untangled:edit-profile'))
#         elif key == ord("c"):
#             cv2.imwrite("captured_image.jpg", frame)
#             # return render(request, 'registration/editprofile.html', {'image_path': 'captured_image.jpg'})
#             return HttpResponseRedirect(reverse('untangled:edit-profile') + '?image_path=frame.jpg')
#     cap.release()
#     cv2.destroyWindow("Camera")

# def display_image(request):
#     # Get the image path from the query parameters
#     image_path = request.GET.get('image_path', None)

#     # Render a template that displays the captured image
#     return render(request, 'registration/editprofile.html', {'image_path': image_path})

    # ret, frame = cap.read()
    # if not ret:
    #     return render(request, 'error.html', {'error': 'Failed to access the camera'})
    # cv2.imwrite("frame.jpg", frame)
    # cap.release()
    # return render(request, 'captured_image.html', {'image_path': 'frame.jpg'})

@login_required(login_url='') 
def sendMail(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            ['joshuadelrosario17@gmail.com'],
            fail_silently=False,
            )
        
        return render(request, 'untangled/contact.html', {'message_name': message_name})
    else:
        return render(request, 'untangled/contact.html', {})


def Author(request):
    return render(request, 'untangled/author.html')