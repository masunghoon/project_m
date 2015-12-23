from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from .models import Post, Comment
from datetime import datetime

posts = Blueprint('posts', __name__, template_folder='templates')

class ListView(MethodView):
    def get(self):
        posts = Post.objects.all()
        return render_template('posts/list.html', posts=posts)

class DetailView(MethodView):
    
    form = model_form(Comment, exclude=['created_at'])

    def get_context(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('posts/detail.html', **context)

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            comment = Comment()
            form.populate_obj(comment)

            post = context.get('post')
            post.comments.append(comment)
            post.save()

            return redirect(url_for('posts.detail', slug=slug))
        return render_template('posts/detail.html', **context)


#routing
posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))
    
