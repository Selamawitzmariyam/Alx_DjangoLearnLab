from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
from .models import Post
from blog.widgets import TagWidget 
from taggit.forms import TagWidget
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only include the content field for comment creation
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Add custom validation or styling to the form fields
        self.fields['content'].widget = forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'})
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        # Ensure the comment content is not empty
        if not content.strip():
            raise forms.ValidationError("Comment content cannot be empty.")
        return content
class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Django, Python, Web Development'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        post = super().save(commit=False)
        tag_names = self.cleaned_data['tags']
        if commit:
            post.save()
            post.tags.set(*[tag.strip() for tag in tag_names.split(",") if tag.strip()])  # Add tags
        return post
