from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
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