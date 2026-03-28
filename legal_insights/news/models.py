from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

# ==========================================================
# 1. CATEGORIES & SUBCATEGORIES
# ==========================================================

class Category(models.Model):
    """Categories: Supreme Court, High Court, Criminal, Civil, etc."""
    name = models.CharField(max_length=100, unique=True)
    # slug = models.SlugField(unique=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    # slug = models.SlugField(unique=False, blank=True, null=True, max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """Sub-categories under main categories"""
    name = models.CharField(max_length=100)
    # slug = models.SlugField(unique=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    # slug = models.SlugField(unique=False, blank=True, null=True, max_length=255)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Sub-Categories"
        ordering = ['parent_category', 'name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while SubCategory.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.parent_category.name} > {self.name}"


# ==========================================================
# 2. POST MODELS (Judgments, Laws, Articles)
# ==========================================================

class JudgmentPost(models.Model):
    """Judgment News Posts"""
    title = models.CharField(max_length=255)
    # slug = models.SlugField(unique=True, blank=True, max_length=255)
    # slug = models.SlugField(unique=False, blank=True, null=True, max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    
    court_name = models.CharField(max_length=200)
    judgment_date = models.DateField()
    case_number = models.CharField(max_length=150)
    judges = models.CharField(max_length=300, blank=True)

    summary = models.TextField()
    full_content = models.TextField()

    featured_image = models.ImageField(upload_to='judgments/images/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='judgments/pdfs/', blank=True, null=True, help_text="Upload judgment PDF")
    read_more_link = models.URLField(blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='judgments')
    tags = models.CharField(max_length=300, blank=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:200]
            slug = base_slug
            counter = 1
            # Check for existing slug in JudgmentPost to prevent IntegrityError
            while JudgmentPost.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class LawActPost(models.Model):
    """Law & Act News Posts"""
    title = models.CharField(max_length=300, help_text="Law/Act headline (e.g., New Criminal Law Amendments 2024)")
    # slug = models.SlugField(unique=True, blank=True, max_length=350)
    # slug = models.SlugField(unique=False, blank=True, null=True, max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    
    act_name = models.CharField(max_length=250, help_text="Official name of the Act")
    act_number = models.CharField(max_length=100, blank=True, help_text="e.g., Act No. 45 of 2024")
    enactment_date = models.DateField(help_text="Date of enactment/notification")
    ministry = models.CharField(max_length=200, blank=True, help_text="e.g., Ministry of Home Affairs")
    
    summary = models.TextField(help_text="Short summary (2-3 sentences)")
    full_content = models.TextField(help_text="Full article about the law/act")
    key_provisions = models.TextField(blank=True, help_text="Key highlights/provisions")
    
    featured_image = models.ImageField(upload_to='laws/images/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='laws/pdfs/', blank=True, null=True, help_text="Upload Act PDF")
    read_more_link = models.URLField(blank=True, null=True) 
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='laws')
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags")
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-published_date']
        verbose_name = "Law/Act Post"
        verbose_name_plural = "Law/Act Posts"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:340]
            slug = base_slug
            counter = 1
            while LawActPost.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class ArticlePost(models.Model):
    """General Articles - Legal Analysis, Opinion, Commentary"""
    title = models.CharField(max_length=300, help_text="Article headline")
    # slug = models.SlugField(unique=True, blank=True, max_length=350)
    # slug = models.SlugField(unique=False, blank=True, null=True, max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    
    summary = models.TextField(help_text="Short summary (2-3 sentences)")
    full_content = models.TextField(help_text="Full article content")
    
    featured_image = models.ImageField(upload_to='articles/images/', blank=True, null=True)
    read_more_link = models.URLField(blank=True, null=True, help_text="External link for more details")
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags")
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-published_date']
        verbose_name = "Article Post"
        verbose_name_plural = "Article Posts"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:340]
            slug = base_slug
            counter = 1
            while ArticlePost.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


# ==========================================================
# 3. STATIC PAGES
# ==========================================================

class Page(models.Model):
    """Custom pages - Recent, Guidelines, etc."""
    PAGE_TYPES = (
        ('recent', 'Recent Updates'),
        ('guideline', 'Good Guideline'),
        ('advocates', 'For Advocates'),
        ('common', 'For Common People'),
        ('judiciary', 'For Judiciary'),
    )
    
    page_type = models.CharField(max_length=20, choices=PAGE_TYPES, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='pages/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.get_page_type_display()
    
# ==========================================================


from django.db import models
from django.utils.text import slugify
import re


class AdvocateGuide(models.Model):
    CATEGORY_CHOICES = [
        ('bail', 'Bail Process'),
        ('fir', 'FIR Drafting'),
        ('court', 'Court Procedure'),
        ('civil', 'Civil Law'),
        ('criminal', 'Criminal Law'),
        ('evidence', 'Evidence & Documentation'),
        ('appeal', 'Appeals & Revision'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    content = models.TextField(help_text="Full guide content (HTML supported)")
    youtube_link = models.URLField(blank=True, null=True, help_text="Paste full YouTube URL")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Advocate Guide'
        verbose_name_plural = 'Advocate Guides'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while AdvocateGuide.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_embed_url(self):
        if not self.youtube_link:
            return None
        patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})',
            r'(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]{11})',
            r'(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})',
        ]
        for pattern in patterns:
            match = re.search(pattern, self.youtube_link)
            if match:
                return f"https://www.youtube.com/embed/{match.group(1)}"
        return None

    list_display = ('title', 'get_category_name', 'created_at')
    prepopulated_fields = {'slug': ('title',)} # This helps auto-fill slugs in admin

    def get_category_name(self, obj):
        return obj.get_category_display()
    get_category_name.short_description = 'Category'

class CitizenGuide(models.Model):
    CATEGORY_CHOICES = [
        ('fir_refusal', 'Police FIR Refusal'),
        ('divorce', 'Divorce & Separation'),
        ('property', 'Property Disputes'),
        ('domestic', 'Domestic Violence'),
        ('consumer', 'Consumer Rights'),
        ('labour', 'Labour & Employment'),
        ('cyber', 'Cyber Crime'),
        ('rent', 'Rent & Tenancy'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    content = models.TextField(help_text="Full guide content (HTML supported)")
    youtube_link = models.URLField(blank=True, null=True, help_text="Paste full YouTube URL")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Citizen Guide'
        verbose_name_plural = 'Citizen Guides'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while CitizenGuide.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_embed_url(self):
        if not self.youtube_link:
            return None
        patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})',
            r'(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]{11})',
            r'(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})',
        ]
        for pattern in patterns:
            match = re.search(pattern, self.youtube_link)
            if match:
                return f"https://www.youtube.com/embed/{match.group(1)}"
        return None
    
    def get_category_name(self, obj):
        return obj.get_category_display()
    get_category_name.short_description = 'Category'
