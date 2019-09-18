from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment
from Food.models import Food
from Store.models import Store



@login_required
@require_POST
def submit_comment(request, store_id, food_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.comment = form.cleaned_data['comment']
        food = Food.objects.get(id=food_id)
        comment.food = food
        comment.save()
        return redirect('store-food-detail', pk=store_id , food_id=food_id)
