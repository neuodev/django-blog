from django.test import TestCase

from .models import Post

from django.contrib.auth.models import User

class BlogTests (TestCase):
    @classmethod

    def setUpTestData(cls):
        testuser= User.objects.create(
            username ='testuser1',
            password = 'abc123'
        ) 
        testuser.save()    

        # create a blog post 

        test_post = Post.objects.create(
            author = testuser,
            title = 'Blog title',
            body='Blog body'
        )

        test_post.save()

    def test_blog_content(slef):

        post = Post.objects.get(id=1)

        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        slef.assertEqual(author,'testuser1')
        slef.assertEqual(title,'Blog title')
        slef.assertEqual(body,'Blog body')