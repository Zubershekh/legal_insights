from django.contrib import admin
from .models import Category, JudgmentPost, LawActPost

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(JudgmentPost)
class JudgmentPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'court_name', 'judgment_date', 'is_published')
    # list_filter = ['is_published', 'is_featured', 'category']
    # search_fields = ['title', 'case_number']
    # prepopulated_fields = {'slug': ('title',)}
    # list_editable = ['is_published', 'is_featured']

@admin.register(LawActPost)
class LawActPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'act_name', 'enactment_date', 'category', 'is_published', 'is_featured', 'views']
    list_filter = ['is_published', 'is_featured', 'category']
    search_fields = ['title', 'act_name']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published', 'is_featured']

# ========== ADD THIS AT THE END OF admin.py ==========

from .models import ArticlePost

@admin.register(ArticlePost)
class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_published', 'is_featured', 'views', 'published_date']
    list_filter = ['is_published', 'is_featured', 'category']
    search_fields = ['title', 'summary']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published', 'is_featured']

#---------------------------------------------------------


from django.contrib import admin
from .models import AdvocateGuide, CitizenGuide


@admin.register(AdvocateGuide)
class AdvocateGuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'category')
        }),
        ('Content', {
            'fields': ('content', 'youtube_link'),
            'description': 'Write the full guide content. HTML tags are supported.'
        }),
        ('Meta', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(CitizenGuide)
class CitizenGuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'category')
        }),
        ('Content', {
            'fields': ('content', 'youtube_link'),
            'description': 'Write the full guide content. HTML tags are supported.'
        }),
        ('Meta', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

# ---------------------------------------------------------

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.text import slugify
from .models import AdvocateGuide, CitizenGuide


# ── ADVOCATE ADMIN VIEWS ──────────────────────────────────────────────────────

def admin_advocates(request):
    guides = AdvocateGuide.objects.all()
    return render(request, 'news/admin_advocate.html', {'guides': guides})


def admin_advocate_add(request):
    if request.method == 'POST':
        title        = request.POST.get('title', '').strip()
        slug         = request.POST.get('slug', '').strip()
        category     = request.POST.get('category', '')
        content      = request.POST.get('content', '')
        youtube_link = request.POST.get('youtube_link', '').strip()

        if not slug:
            slug = slugify(title)

        # Ensure slug uniqueness
        base_slug = slug
        counter = 1
        while AdvocateGuide.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        AdvocateGuide.objects.create(
            title=title,
            slug=slug,
            category=category,
            content=content,
            youtube_link=youtube_link or None,
        )
        messages.success(request, f'Advocate guide "{title}" added successfully.')
        return redirect('admin_advocates')

    return render(request, 'news/admin_advocate_form.html')


def admin_advocate_edit(request, slug):
    guide = get_object_or_404(AdvocateGuide, slug=slug)

    if request.method == 'POST':
        guide.title        = request.POST.get('title', '').strip()
        guide.category     = request.POST.get('category', '')
        guide.content      = request.POST.get('content', '')
        guide.youtube_link = request.POST.get('youtube_link', '').strip() or None

        new_slug = request.POST.get('slug', '').strip()
        if new_slug and new_slug != guide.slug:
            base_slug = new_slug
            counter = 1
            while AdvocateGuide.objects.filter(slug=new_slug).exclude(pk=guide.pk).exists():
                new_slug = f"{base_slug}-{counter}"
                counter += 1
            guide.slug = new_slug

        guide.save()
        messages.success(request, f'Advocate guide "{guide.title}" updated successfully.')
        return redirect('admin_advocates')

    return render(request, 'news/admin_advocate_form.html', {'guide': guide})


def admin_advocate_delete(request, slug):
    guide = get_object_or_404(AdvocateGuide, slug=slug)
    title = guide.title
    guide.delete()
    messages.success(request, f'Advocate guide "{title}" deleted.')
    return redirect('admin_advocates')


# ── CITIZEN ADMIN VIEWS ───────────────────────────────────────────────────────

def admin_citizens(request):
    guides = CitizenGuide.objects.all()
    return render(request, 'news/admin_citizens.html', {'guides': guides})


def admin_citizen_add(request):
    if request.method == 'POST':
        title        = request.POST.get('title', '').strip()
        slug         = request.POST.get('slug', '').strip()
        category     = request.POST.get('category', '')
        content      = request.POST.get('content', '')
        youtube_link = request.POST.get('youtube_link', '').strip()

        if not slug:
            slug = slugify(title)

        base_slug = slug
        counter = 1
        while CitizenGuide.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        CitizenGuide.objects.create(
            title=title,
            slug=slug,
            category=category,
            content=content,
            youtube_link=youtube_link or None,
        )
        messages.success(request, f'Citizen guide "{title}" added successfully.')
        return redirect('admin_citizens')

    return render(request, 'news/admin_citizen_form.html')


def admin_citizen_edit(request, slug):
    guide = get_object_or_404(CitizenGuide, slug=slug)

    if request.method == 'POST':
        guide.title        = request.POST.get('title', '').strip()
        guide.category     = request.POST.get('category', '')
        guide.content      = request.POST.get('content', '')
        guide.youtube_link = request.POST.get('youtube_link', '').strip() or None

        new_slug = request.POST.get('slug', '').strip()
        if new_slug and new_slug != guide.slug:
            base_slug = new_slug
            counter = 1
            while CitizenGuide.objects.filter(slug=new_slug).exclude(pk=guide.pk).exists():
                new_slug = f"{base_slug}-{counter}"
                counter += 1
            guide.slug = new_slug

        guide.save()
        messages.success(request, f'Citizen guide "{guide.title}" updated successfully.')
        return redirect('admin_citizens')

    return render(request, 'news/admin_citizen_form.html', {'guide': guide})


def admin_citizen_delete(request, slug):
    guide = get_object_or_404(CitizenGuide, slug=slug)
    title = guide.title
    guide.delete()
    messages.success(request, f'Citizen guide "{title}" deleted.')
    return redirect('admin_citizens')