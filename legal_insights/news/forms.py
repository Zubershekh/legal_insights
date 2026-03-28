from django import forms
from .models import JudgmentPost, LawActPost, Category

class JudgmentPostForm(forms.ModelForm):
    class Meta:
        model = JudgmentPost
        fields = ['title', 'court_name', 'judgment_date', 'case_number', 'judges',
                  'summary', 'full_content', 'category', 'tags', 'featured_image',
                  'pdf_file', 'is_published', 'is_featured', 'read_more_link']
        
      
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., SC Grants Bail in XYZ Case'}),
            'court_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Supreme Court of India'}),
            'judgment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'case_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Crl. Appeal 123/2024'}),
            'judges': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Justice A, Justice B'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '2-3 sentence summary'}),
            'full_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 15, 'placeholder': 'Full article content...'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'bail, criminal, supreme court (comma-separated)'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'pdf_file': forms.FileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }

class LawActPostForm(forms.ModelForm):
    class Meta:
        model = LawActPost
        # fields = ['title', 'act_name', 'act_number', 'enactment_date', 'ministry',
        #           'summary', 'full_content', 'key_provisions', 'category', 'tags',
        #           'featured_image', 'pdf_file', 'is_published', 'is_featured']
        fields = ['title', 'summary', 'full_content', 'category', 'tags', 
                  'featured_image', 'read_more_link', 'is_published', 'is_featured']  # ADD read_more_link
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'act_name': forms.TextInput(attrs={'class': 'form-control'}),
            'act_number': forms.TextInput(attrs={'class': 'form-control'}),
            'enactment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ministry': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'full_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 15}),
            'key_provisions': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'pdf_file': forms.FileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'read_more_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com/more-details'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


# ========== ADD THIS AT THE END OF forms.py ==========

from .models import ArticlePost

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ['title', 'summary', 'full_content', 'category', 'subcategory', 'tags', 'featured_image', 'is_published', 'is_featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Article headline'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Short summary'}),
            'full_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 15, 'placeholder': 'Full article content'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'legal, analysis, opinion'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }