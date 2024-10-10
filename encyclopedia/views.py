from typing import Final
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, HttpResponse, redirect
import markdown2
import random
from django import forms
import os
import re
from encyclopedia import admin
from . import util
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import authenticate
import math




# Form used to create a new entry/page
class NewPageForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={
            'placeholder': 'Enter title', 'id': 'new-entry-title','name':'title'}))
    data = forms.CharField(label="", widget=forms.Textarea(attrs={
        'id': 'new-entry','name':'data'}))


# controllers
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": [entry.strip('[]\"') for entry in util.list_entries() if entry == "DEPARTMENTS"]
    })

#titlepage
def entryPage(request, title):
    markDownData = util.get_entry(title)
    if(markDownData == None):
        print("No such entry")
        return render(request, "encyclopedia/invalidpage.html", {
            "title" : title
        })
    htmlData = markdown2.markdown(markDownData)
    return render(request, "encyclopedia/entry.html", {
        "title" : title,
        "html" : htmlData
    })

#searchpage

def search(request):
    search_query = request.POST.get("q")
    search_query_cleaned = re.sub(r'[<>*#]', ' ', search_query)
    # Search within Markdown files
    matched_results = search_in_md_files(search_query_cleaned)
    if matched_results:
        # Display the matched lines on the screen
        return render(request, "encyclopedia/searchresult.html", {
            "matched_results": matched_results, 
            "search_query": search_query,
            "title":search_query,
            "filename":matched_results[0][0]
            })
    else:
        # Handle case when no match is found
        return render(request, "encyclopedia/invalidpage.html", {
            "title" : search_query
        })

def search_in_md_files(query):
    matched_results = []
    # Directory where your .md files are stored
    directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'entries')
    for filename in os.listdir(directory):
        if filename == "cnnd.md":
            continue
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r',encoding='utf-8') as file:
                for line_number, line in enumerate(file, start=1):
                    if query.lower() in line.lower():
                        # If query found in line, add filename, line number, and line content to matched_results
                        if line_number % 10 == 0:
                            line_round = line_number - 10
                        else:
                            line_round = math.floor(line_number / 10) * 10
                            # Exclude <>#* and anything between them from line content
                        line_content = re.sub(r'<.*?>|#|\*|\[.*?\]\(.*?\)', '', line.strip())
                        matched_results.append((filename[:-3],line_round, line_number, line_content))
    return matched_results





def createEntry(request):
    if request.method == "POST":
        formData = NewPageForm(request.POST)
        if formData.is_valid():
            title = formData.cleaned_data['title']
            data = formData.cleaned_data['data']
            if(util.get_entry(title)!=None):
                return render(request, "encyclopedia/newpage.html", {
                    "newform" : NewPageForm(),
                    "error": "Such an entry already exists"
                })
            finalData = "#" + title + "\n" + data
            util.save_entry(title, finalData)
            return HttpResponseRedirect(reverse("entrypage", args=[title]))
    return render(request, "encyclopedia/newpage.html", {
        "title" : "Create Entry",
        "newform" : NewPageForm()
    })

def editEntry(request):
     if request.method == "GET":
         title = request.GET['title']
         data = util.get_entry(title)
         form = NewPageForm(initial={'title': title, 'data': data})
         return render(request, "encyclopedia/edit.html", {
             "title":"Edit data",
            "newform" : form
         })
     if request.method == "POST":
         formData = NewPageForm(request.POST)
         if formData.is_valid():
            title = formData.cleaned_data['title']
            data = formData.cleaned_data['data']
            if(util.get_entry(title)!=None):
                util.save_entry(title, data)
                return HttpResponseRedirect(reverse("entrypage", args=[title]))

def randomPage(request):
    entries = util.list_entries()
    value = random.choice(entries)
    return HttpResponseRedirect(reverse("entrypage", args=[value]))
def Function(request):
    return HttpResponseRedirect(reverse("entrypage", args=["Function"]))
def login(request):
    return HttpResponseRedirect(request, "entrypage")

def user(request):
    form = AuthenticationForm()
    username=request.POST.get('username')
    password=request.POST.get('password')
    flag = False
    if request.method == 'POST':
        if username in admin.logindata and admin.logindata[username] == password:
                if username == "admin":
                    flag = True
                    return redirect('index')
                else:
                    return redirect('index')
        else:
            messages.error(request, 'Username or password is incorrect')
    else:
        form = AuthenticationForm()
    return render(request, 'encyclopedia/login.html', {'form': form})