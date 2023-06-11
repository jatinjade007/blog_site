from django.shortcuts import render
from blog.models import Blogs, Blog_Content, Comments
from django.http import JsonResponse
from django.views.generic.base import View

# Create your views here.

class BlogList(View):

    def get(self):

        # <YOUR_API_LINK>?
        # did=<DID_NUMBER>&
        # from=<SENDER_NUMBER>&
        # receive_time=<RECEIVE_TIME(In 10 Digit Timestamp)>&
        # message=<URLENCODED_MESSAGE>&
        # operator=<OPERATOR>&
        # circle=<CIRCLE>&
        # codeing=normal&
        # provider=Sarv

        result = []
        result_data = {}
        status = False
        try:
            blogs = Blogs.objects.all()
            if blogs:
                for blog in blogs:
                    result.append({
                        "blog_id": blog.blog_id,
                        "blog_title": blog.blog_title
                    })
                result_data = {
                    'success': True,
                    'result' : result
                }
            else:
                message = "No New Blogs"
        except Exception:
            message = "Internal Server Error"
            
        
        return JsonResponse({
            'success': status,
            'message': message,
            'result': result_data
            })
    
    # Fetching Blog Data
    def post(self, request):

        blog_id = request.POST.get("blog_id", "")

        result = {}

        try:
            blog = Blogs.objects.filter(blog_id=blog_id).first()

            result.update({
                'blog_id': blog.blog_id,
                'blog_title': blog.blog_title
            })

            blog_contents = Blog_Content.objects.filter(blog_title = blog)

            if blog_contents:
                content_data = []

                for content in blog_contents:
                    data = {
                        'blog_content_id': content.blog_content_id,
                        'blog_content': content.blog_content
                    }
                    content_data.append(data)
                result.update({
                    'paragraphs': content_data
                })
            
        except Exception:
            return JsonResponse({
                'success': False, 
                'message': 'Unable to load blog',
                'result': result
                })

        return JsonResponse({
            'success': True, 
            'result': result
            })  
    
# To Create Blog
class CreateBlog(View):

    def post(self, request):

        blog_title = request.POST.get("blog_title", None)
        blog_contents = request.POST.get("blog_contents", [])

        status = False
        message = ""

        try:
                
            if blog_title:
                if blog_contents:
                    blog = Blogs(blog_title = blog_title)
                    blog.save()
                    for content in blog_contents:
                        blog_content = Blog_Content(blog_content = content, blog = blog)
                        blog_content.save()
                    message = "Blog is created"
                else:
                    message = "Blog Content is missing"
            else:
                message = "Blog can't be created"
        except Exception:
            message = "Error occured"
        return JsonResponse({
            'success': status, 
            'message': message
            })  
        

class BlogContentAddUpdate(View):

    # Add and Update Blog paragraph
    def post(self, request):

        blog_id = request.POST.get("blog_id", "")

        blog_content_id = request.POST.get("blog_content_id", None)

        blog_content = request.POST.get("blog_content", None)

        status = False

        try:
            if blog_content_id and blog_content:
                content = Blog_Content.objects.filter(blog_content_id = blog_content_id).update(blog_content = blog_content)
                content.blog_content = blog_content
                content.save()
                status = True
                message = "Paragraph is updated"
            elif not blog_content_id and blog_content:
                blog = Blogs.objects.filter(blog_id=blog_id).first()
                content = Blog_Content(blog_content = blog_content, blog = blog)
                content.save()
                status = True
                message = "Paragraph is Created"
            else:
                message = "Paragragh can't be created or Updated"
            
        except Exception:
            message = "Internal Server Error"

        return JsonResponse({
            'success': status, 
            'message': message
            })  


class CommentView(View):

    # View Comments of a blog Paragraph
    def get(self, request):

        blog_content_id = request.GET.get("blog_content_id", "")

        result = []
        result_data = {}
        status = False
        try:
            blog_content = Blog_Content.objects.filter(blog_content_id = blog_content_id).first()
            if blog_content:
                comments = Comments.objects.filter(blog_content = blog_content)
                for comment in comments:
                    result.append({
                        "blog_id": comment.comment_id,
                        "comment": comment.comment
                    })
                result_data = {
                    'comment_data' : result
                }
                status = True
            else:
                message = "No New Comments"
        except:
            message = "Internal Server Error"
            
        
        return JsonResponse({
            'success': status,
            'message': message,
            'result': result_data
            })
    
    # Add Comment to a blog Paragraph
    def post(self, request):

        blog_content_id = request.GET.get("blog_content_id", "")
        comment = request.GET.get("comment", "")

        status = False
        message = ""

        try:
            blog_content = Blog_Content.objects.filter(blog_content_id = blog_content_id).first()

            if blog_content:

                blog_content_comment = Comments(comment = comment)
                blog_content_comment.save()
                status = True
                message = "Comment Inserted"
            else:
                message = "Unable to find Blog content"
            
        except Exception:
            message = "Comment not created"

        return JsonResponse({
            'success': status, 
            'message': message
            })  
