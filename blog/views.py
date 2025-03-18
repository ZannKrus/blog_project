from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Article, Comment
from .forms import CommentForm 

def home(request):
    articles_list = Article.objects.order_by('-published_date')
    paginator = Paginator(articles_list, 5) #количество статей на странице
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    return render(request, 'blog/home.html', {'articles': articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.filter(approved=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(article.get_absolute_url())
    else:
        form = CommentForm()
    return render(request, 'blog/article_detail.html', {
        'article': article,
        'comment_form': form,
        'comments': comments,
    })
