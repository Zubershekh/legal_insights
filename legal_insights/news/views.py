from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from news.admin import JudgmentPostAdmin
from .models import JudgmentPost, LawActPost, Category
from .forms import JudgmentPostForm, LawActPostForm, CategoryForm

# PUBLIC VIEWS
def home(request):
    featured_judgments = JudgmentPost.objects.filter(is_published=True, is_featured=True)[:4]
    latest_judgments = JudgmentPost.objects.filter(is_published=True)[:10]
    latest_laws = LawActPost.objects.filter(is_published=True)[:6]
    categories = Category.objects.all()[:10]
    
    context = {
        'featured_judgments': featured_judgments,
        'latest_judgments': latest_judgments,
        'latest_laws': latest_laws,
        'categories': categories,
    }
    return render(request, 'news/home.html', context)

def judgments_list(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    
    judgments = JudgmentPost.objects.filter(is_published=True)
    
    if query:
        judgments = judgments.filter(
            Q(title__icontains=query) |
            Q(court_name__icontains=query) |
            Q(case_number__icontains=query) |
            Q(summary__icontains=query)
        )
    
    if category_slug:
        judgments = judgments.filter(category__slug=category_slug)
    
    categories = Category.objects.all()
    
    context = {
        'judgments': judgments,
        'categories': categories,
        'query': query,
        'selected_category': category_slug,
    }
    return render(request, 'news/judgments_list.html', context)

def judgment_detail(request, slug):
    judgment = get_object_or_404(JudgmentPost, slug=slug, is_published=True)
    judgment.views += 1
    judgment.save(update_fields=['views'])
    
    related = JudgmentPost.objects.filter(category=judgment.category, is_published=True).exclude(id=judgment.id)[:3]
    
    context = {'judgment': judgment, 'related': related}
    return render(request, 'news/judgment_detail.html', context)

def laws_list(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    
    laws = LawActPost.objects.filter(is_published=True)
    
    if query:
        laws = laws.filter(Q(title__icontains=query) | Q(act_name__icontains=query) | Q(summary__icontains=query))
    
    if category_slug:
        laws = laws.filter(category__slug=category_slug)
    
    categories = Category.objects.all()
    context = {'laws': laws, 'categories': categories, 'query': query, 'selected_category': category_slug}
    return render(request, 'news/laws_list.html', context)

def law_detail(request, slug):
    law = get_object_or_404(LawActPost, slug=slug, is_published=True)
    law.views += 1
    law.save(update_fields=['views'])
    
    related = LawActPost.objects.filter(category=law.category, is_published=True).exclude(id=law.id)[:3]
    context = {'law': law, 'related': related}
    return render(request, 'news/law_detail.html', context)

def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    judgments = JudgmentPost.objects.filter(category=category, is_published=True)[:10]
    laws = LawActPost.objects.filter(category=category, is_published=True)[:10]
    context = {'category': category, 'judgments': judgments, 'laws': laws}
    return render(request, 'news/category.html', context)

def about(request):
    return render(request, 'news/about.html')

def contact(request):
    return render(request, 'news/contact.html')

def disclaimer(request):
    return render(request, 'news/disclaimer.html')

# ADMIN
def admin_login_view(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    
    return render(request, 'news/admin_login.html')

@login_required
def admin_logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('home')

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    
    context = {
        'judgments_count': JudgmentPost.objects.count(),
        'laws_count': LawActPost.objects.count(),
        'categories_count': Category.objects.count(),
        'latest_judgments': JudgmentPost.objects.all()[:5],
        'latest_laws': LawActPost.objects.all()[:5],
    }
    return render(request, 'news/admin_dashboard.html', context)

@login_required
def admin_judgments(request):
    if not request.user.is_staff:
        return redirect('home')
    judgments = JudgmentPost.objects.all()
    return render(request, 'news/admin_judgments.html', {'judgments': judgments})

@login_required
def admin_judgment_add(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = JudgmentPostForm(request.POST, request.FILES)
        if form.is_valid():
            judgment = form.save(commit=False)
            judgment.author = request.user
            judgment.save()
            messages.success(request, 'Judgment post added!')
            return redirect('admin_judgments')
    else:
        form = JudgmentPostForm()
    
    return render(request, 'news/admin_judgment_form.html', {'form': form, 'action': 'Add'})

@login_required
def admin_judgment_edit(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    judgment = get_object_or_404(JudgmentPost, pk=pk)
    
    if request.method == 'POST':
        form = JudgmentPostForm(request.POST, request.FILES, instance=judgment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Judgment post updated!')
            return redirect('admin_judgments')
    else:
        form = JudgmentPostForm(instance=judgment)
    
    return render(request, 'news/admin_judgment_form.html', {'form': form, 'action': 'Edit'})

@login_required
def admin_judgment_delete(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    judgment = get_object_or_404(JudgmentPost, pk=pk)
    
    if request.method == 'POST':
        judgment.delete()
        messages.success(request, 'Judgment post deleted!')
        return redirect('admin_judgments')
    
    return render(request, 'news/admin_judgment_delete.html', {'judgment': judgment})

@login_required
def admin_laws(request):
    if not request.user.is_staff:
        return redirect('home')
    laws = LawActPost.objects.all()
    return render(request, 'news/admin_laws.html', {'laws': laws})

@login_required
def admin_law_add(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = LawActPostForm(request.POST, request.FILES)
        if form.is_valid():
            law = form.save(commit=False)
            law.author = request.user
            law.save()
            messages.success(request, 'Law/Act post added!')
            return redirect('admin_laws')
    else:
        form = LawActPostForm()
    
    return render(request, 'news/admin_law_form.html', {'form': form, 'action': 'Add'})

@login_required
def admin_law_edit(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    law = get_object_or_404(LawActPost, pk=pk)
    
    if request.method == 'POST':
        form = LawActPostForm(request.POST, request.FILES, instance=law)
        if form.is_valid():
            form.save()
            messages.success(request, 'Law/Act post updated!')
            return redirect('admin_laws')
    else:
        form = LawActPostForm(instance=law)
    
    return render(request, 'news/admin_law_form.html', {'form': form, 'action': 'Edit'})

@login_required
def admin_law_delete(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    law = get_object_or_404(LawActPost, pk=pk)
    
    if request.method == 'POST':
        law.delete()
        messages.success(request, 'Law/Act post deleted!')
        return redirect('admin_laws')
    
    return render(request, 'news/admin_law_delete.html', {'law': law})

@login_required
def admin_categories(request):
    if not request.user.is_staff:
        return redirect('home')
    categories = Category.objects.all()
    return render(request, 'news/admin_categories.html', {'categories': categories})

@login_required
def admin_category_add(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added!')
            return redirect('admin_categories')
    else:
        form = CategoryForm()
    
    return render(request, 'news/admin_category_form.html', {'form': form, 'action': 'Add'})

@login_required
def admin_category_edit(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated!')
            return redirect('admin_categories')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'news/admin_category_form.html', {'form': form, 'action': 'Edit'})

@login_required
def admin_category_delete(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted!')
        return redirect('admin_categories')
    
    return render(request, 'news/admin_category_delete.html', {'category': category})


# ========== ADD THESE FUNCTIONS AT THE END OF views.py ==========

# Import ArticlePost at top if not there
from .models import ArticlePost
from .forms import ArticlePostForm

# ARTICLES PUBLIC VIEWS
def articles_list(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    
    articles = ArticlePost.objects.filter(is_published=True)
    
    if query:
        articles = articles.filter(Q(title__icontains=query) | Q(summary__icontains=query))
    
    if category_slug:
        articles = articles.filter(category__slug=category_slug)
    
    categories = Category.objects.all()
    
    context = {'articles': articles, 'categories': categories, 'query': query, 'selected_category': category_slug}
    return render(request, 'news/articles_list.html', context)

def article_detail(request, slug):
    article = get_object_or_404(ArticlePost, slug=slug, is_published=True)
    article.views += 1
    article.save(update_fields=['views'])
    
    related = ArticlePost.objects.filter(category=article.category, is_published=True).exclude(id=article.id)[:3]
    
    context = {'article': article, 'related': related}
    return render(request, 'news/article_detail.html', context)

# ARTICLES ADMIN VIEWS
@login_required
def admin_articles(request):
    if not request.user.is_staff:
        return redirect('home')
    articles = ArticlePost.objects.all()
    return render(request, 'news/admin_articles.html', {'articles': articles})

@login_required
def admin_article_add(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = ArticlePostForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Article added successfully!')
            return redirect('admin_articles')
    else:
        form = ArticlePostForm()
    
    return render(request, 'news/admin_article_form.html', {'form': form, 'action': 'Add'})

@login_required
def admin_article_edit(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    article = get_object_or_404(ArticlePost, pk=pk)
    
    if request.method == 'POST':
        form = ArticlePostForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated!')
            return redirect('admin_articles')
    else:
        form = ArticlePostForm(instance=article)
    
    return render(request, 'news/admin_article_form.html', {'form': form, 'action': 'Edit'})

@login_required
def admin_article_delete(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    article = get_object_or_404(ArticlePost, pk=pk)
    
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article deleted!')
        return redirect('admin_articles')
    
    return render(request, 'news/admin_article_delete.html', {'article': article})


from .models import Page

# Context processor for categories in navbar
def navbar_context(request):
    """Makes categories available to all templates"""
    return {
        'all_categories': Category.objects.all()[:10]
    }

# Page views
def page_view(request, page_type):
    """Display custom pages"""
    try:
        page = Page.objects.get(page_type=page_type)
    except Page.DoesNotExist:
        page = None
    
    context = {'page': page, 'page_type': page_type}
    return render(request, 'news/page_view.html', context)

# Admin - Pages
@login_required
def admin_pages(request):
    if not request.user.is_staff:
        return redirect('home')
    pages = Page.objects.all()
    return render(request, 'news/admin_pages.html', {'pages': pages})

@login_required
def admin_page_edit(request, page_type):
    if not request.user.is_staff:
        return redirect('home')
    
    page, created = Page.objects.get_or_create(page_type=page_type)
    
    if request.method == 'POST':
        page.title = request.POST.get('title')
        page.content = request.POST.get('content')
        if request.FILES.get('featured_image'):
            page.featured_image = request.FILES['featured_image']
        page.save()
        messages.success(request, 'Page updated successfully!')
        return redirect('admin_pages')
    
    context = {'page': page, 'page_type_display': page.get_page_type_display()}
    return render(request, 'news/admin_page_form.html', context)


from django.http import JsonResponse
from .models import JudgmentPost

def live_search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        judgments = JudgmentPost.objects.filter(title__icontains=query)[:10]
        
        for j in judgments:
            results.append({
                'title': j.title,
                'url': f'/judgment/{j.slug}/'
            })

    return JsonResponse(results, safe=False)


# ----------------------


from django.shortcuts import render, get_object_or_404
from .models import AdvocateGuide, CitizenGuide


def advocate_list(request):
    guides = AdvocateGuide.objects.all()
    return render(request, 'news/advocate_list.html', {'guides': guides})


def advocate_detail(request, slug):
    guide = get_object_or_404(AdvocateGuide, slug=slug)
    related = AdvocateGuide.objects.exclude(slug=slug)[:5]
    return render(request, 'news/advocate_detail.html', {
        'guide': guide,
        'related': related,
    })


def citizen_list(request):
    guides = CitizenGuide.objects.all()
    return render(request, 'news/citizen_list.html', {'guides': guides})


def citizen_detail(request, slug):
    guide = get_object_or_404(CitizenGuide, slug=slug)
    related = CitizenGuide.objects.exclude(slug=slug)[:5]
    return render(request, 'news/citizen_detail.html', {
        'guide': guide,
        'related': related,
    })

# --- ADD THESE UPDATED FUNCTIONS TO YOUR views.py ---

from .models import Category, AdvocateGuide

@login_required
def admin_advocates(request):
    if not request.user.is_staff:
        return redirect('home')
    guides = AdvocateGuide.objects.all()
    return render(request, 'news/admin_advocate_list.html', {'guides': guides})

@login_required
def admin_advocate_add(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')
        youtube_link = request.POST.get('youtube_link')
        custom_slug = request.POST.get('slug')

        guide = AdvocateGuide.objects.create(
            title=title,
            category=category,
            content=content,
            youtube_link=youtube_link,
            slug=custom_slug # The model's save() method will clean this
        )

        context = {
        'categories': AdvocateGuide.CATEGORY_CHOICES, # Sending (value, label) pairs
    }
        messages.success(request, 'Advocate Guide added!')
        return redirect('admin_advocates')

    context = {
        'categories': AdvocateGuide.CATEGORY_CHOICES, # Fixes the Unpack Error
        'action': 'Add'
    }
    return render(request, 'news/admin_advocate_form.html', context)

@login_required
def admin_advocate_edit(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    guide = get_object_or_404(AdvocateGuide, pk=pk)
    
    if request.method == 'POST':
        guide.title = request.POST.get('title')
        guide.category = request.POST.get('category')
        guide.content = request.POST.get('content')
        guide.youtube_link = request.POST.get('youtube_link')
        guide.slug = request.POST.get('slug')
        guide.save()
        messages.success(request, 'Advocate Guide updated!')
        return redirect('admin_advocates')

    context = {
        'guide': guide,
        'categories': AdvocateGuide.CATEGORY_CHOICES, # Fixes the Unpack Error
        'action': 'Edit'
    }
    return render(request, 'news/admin_advocate_form.html', context)

@login_required
def admin_citizens(request):
    if not request.user.is_staff:
        return redirect('home')
    guides = CitizenGuide.objects.all()
    return render(request, 'news/admin_citizen_list.html', {'guides': guides})

@login_required
def admin_citizen_add(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        guide = CitizenGuide.objects.create(
            title=request.POST.get('title'),
            category=request.POST.get('category'),
            content=request.POST.get('content'),
            youtube_link=request.POST.get('youtube_link'),
            slug=request.POST.get('slug')
        )

        context = {
        'categories': AdvocateGuide.CATEGORY_CHOICES, # Sending (value, label) pairs
    }
        messages.success(request, 'Citizen Guide added!')
        return redirect('admin_citizens')

    return render(request, 'news/admin_citizen_form.html', {
        'categories': CitizenGuide.CATEGORY_CHOICES,
        'action': 'Add'
    })

@login_required
def admin_citizen_edit(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    guide = get_object_or_404(CitizenGuide, pk=pk)
    
    if request.method == 'POST':
        guide.title = request.POST.get('title')
        guide.category = request.POST.get('category')
        guide.content = request.POST.get('content')
        guide.youtube_link = request.POST.get('youtube_link')
        guide.slug = request.POST.get('slug')
        guide.save()
        messages.success(request, 'Citizen Guide updated!')
        return redirect('admin_citizens')

    return render(request, 'news/admin_citizen_form.html', {
        'guide': guide, 
        'categories': CitizenGuide.CATEGORY_CHOICES, 
        'action': 'Edit'
    })