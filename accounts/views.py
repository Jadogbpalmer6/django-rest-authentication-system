from django.shortcuts import render

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter

from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/accounts/github/login/callback/"
    client_class = OAuth2Client

class TwitterLogin(SocialLoginView):
    adapter_class = TwitterOAuthAdapter
    callback_url = "http://127.0.0.1:8000/accounts/twitter/login/callback/"
    
class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter
