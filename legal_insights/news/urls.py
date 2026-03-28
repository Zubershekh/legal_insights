from django.urls import path
from . import views
from . import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('judgments/', views.judgments_list, name='judgments_list'),
    path('judgment/<slug:slug>/', views.judgment_detail, name='judgment_detail'),
    path('laws/', views.laws_list, name='laws_list'),
    path('law/<slug:slug>/', views.law_detail, name='law_detail'),
    
    # ARTICLES
    path('articles/', views.articles_list, name='articles_list'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    
    path('category/<slug:slug>/', views.category_view, name='category_view'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('admin-logout/', views.admin_logout_view, name='admin_logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    path('admin-dashboard/judgments/', views.admin_judgments, name='admin_judgments'),
    path('admin-dashboard/judgments/add/', views.admin_judgment_add, name='admin_judgment_add'),
    path('admin-dashboard/judgments/<int:pk>/edit/', views.admin_judgment_edit, name='admin_judgment_edit'),
    path('admin-dashboard/judgments/<int:pk>/delete/', views.admin_judgment_delete, name='admin_judgment_delete'),
    
    path('admin-dashboard/laws/', views.admin_laws, name='admin_laws'),
    path('admin-dashboard/laws/add/', views.admin_law_add, name='admin_law_add'),
    path('admin-dashboard/laws/<int:pk>/edit/', views.admin_law_edit, name='admin_law_edit'),
    path('admin-dashboard/laws/<int:pk>/delete/', views.admin_law_delete, name='admin_law_delete'),
    
    path('admin-dashboard/articles/', views.admin_articles, name='admin_articles'),
    path('admin-dashboard/articles/add/', views.admin_article_add, name='admin_article_add'),
    path('admin-dashboard/articles/<int:pk>/edit/', views.admin_article_edit, name='admin_article_edit'),
    path('admin-dashboard/articles/<int:pk>/delete/', views.admin_article_delete, name='admin_article_delete'),
    
    path('admin-dashboard/categories/', views.admin_categories, name='admin_categories'),
    path('admin-dashboard/categories/add/', views.admin_category_add, name='admin_category_add'),
    path('admin-dashboard/categories/<int:pk>/edit/', views.admin_category_edit, name='admin_category_edit'),
    path('admin-dashboard/categories/<int:pk>/delete/', views.admin_category_delete, name='admin_category_delete'),

    # Pages
    path('page/<str:page_type>/', views.page_view, name='page_view'),

    # Admin - Pages
    path('admin-dashboard/pages/', views.admin_pages, name='admin_pages'),
    path('admin-dashboard/pages/<str:page_type>/edit/', views.admin_page_edit, name='admin_page_edit'),

    path('live-search/', views.live_search, name='live_search'),


      # ── Public: Advocate & Citizen pages ─────────────────────────────────────
    path('advocates/',           views.advocate_list,   name='advocates_detail'),
    path('advocates/<slug:slug>/', views.advocate_detail, name='advocate_detail'),
    path('citizens/',            views.citizen_list,    name='citizens_detail'),
    path('citizens/<slug:slug>/', views.citizen_detail,  name='citizen_detail'),
 
    # ── Custom Admin: Advocates ───────────────────────────────────────────────
    path('admin-panel/advocates/',                    admin.admin_advocates,      name='admin_advocates'),
    path('admin-panel/advocates/add/',                admin.admin_advocate_add,   name='admin_advocate_add'),
    path('admin-panel/advocates/<slug:slug>/edit/',   admin.admin_advocate_edit,  name='admin_advocate_edit'),
    path('admin-panel/advocates/<slug:slug>/delete/', admin.admin_advocate_delete, name='admin_advocate_delete'),
 
    # ── Custom Admin: Citizens ────────────────────────────────────────────────
    path('admin-panel/citizens/',                    admin.admin_citizens,       name='admin_citizens'),
    path('admin-panel/citizens/add/',                admin.admin_citizen_add,    name='admin_citizen_add'),
    path('admin-panel/citizens/<slug:slug>/edit/',   admin.admin_citizen_edit,   name='admin_citizen_edit'),
    path('admin-panel/citizens/<slug:slug>/delete/', admin.admin_citizen_delete, name='admin_citizen_delete'),

]