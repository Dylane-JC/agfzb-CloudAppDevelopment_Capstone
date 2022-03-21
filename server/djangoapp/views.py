from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarDealer
from .restapis import get_dealers_from_cf, get_request, get_dealer_reviews_from_cf, analyze_review_sentiments, post_request
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def something(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/something.html', context)

# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/about.html', context)

# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    # handling POST request
    if request.method == "POST":
        # Colect user informations
        username = request.POST['username']
        password = request.POST['password']

        # We verify the credentials match to the one recorded in the database
        user = authenticate(username=username, password=password)
        if user is not None:
            # If the credentials are recognized we call the 'login method to login the current user
            login(request, user)
            return redirect('djangoapp:index')
        else:
            #If the user cannot be verified, run the login page again
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    context = {}
    # We get the user information about his session
    print("Loggin out of the user {}".format(request.user.username))
    # We log out the user and redirect him towarad the home page
    logout(request)
    return redirect('djangoapp:index')


# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    # If it is just a GET request :
    if request.method == "GET":
        return render(request, 'djangoapp/signup.html', context)
    # If request comes from variable (a POST request:)
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        lastname = request.POST['last_name']
        firstname = request.POST['first_name']
        user_exist = False
        try:
            #Verify if user already registered
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not already exist, write it is a new user
            logger.debug("{} is a new user".format(username))
        # IF not exists
        if not user_exist:
            #we create the new user in the db user table
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password)
            #We log the user in
            login(request, user)
            return redirect('djangoapp:index')
        else:
            return render(request, 'djangoapp/signup.html', context)


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        url = "https://eu-gb.functions.appdomain.cloud/api/v1/web/f685b25d-91a6-498c-833b-cab9cc0a36d0/api/delearship"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        context['dealerships'] = dealerships
        # Concat all dealer's short name
        dealer_names =' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return render(request, 'djangoapp/index.html', context)

# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    context = {}
    if request.method == "GET":
        url = "https://eu-gb.functions.appdomain.cloud/api/v1/web/f685b25d-91a6-498c-833b-cab9cc0a36d0/api/review"
        # Get reviews of a dealer
        reviews = get_dealer_reviews_from_cf(url)
        context['reviews'] = reviews
        # Concat all reviews
        revw = ' '.join([review.name for review in reviews])
        revw = analyze_review_sentiments(reviews)
        # Return a list of reviews
        return render(request, 'djangoapp/dealer_details.html', context)

def add_review(request, dealer_id):
    if request.method == "POST" & request.user.is_authenticated:
        review = {'id':id, 'dealerahip':dealership, 'review':review}
        json_payload = {'review':review}
