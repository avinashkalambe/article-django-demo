from django.shortcuts import render, redirect
from .models import Article
from author.models import Author

# Create your views here.

def home(request):
    records = Article.objects.all()
    author = None
    
    try:
        if str(request.user) != 'AnonymousUser':
            author = Author.objects.get(user=request.user)
    except Exception as e:
        author = Author.objects.create(user=request.user)
    
    context = {'records': records , 'author':author}
    return render(request,'home.html', context=context)


def about(request):
    return render(request,'about.html', {'author':request.user})


def details(request, pk):
    record = Article.objects.get(id=pk)  
    print(record)
    context = {'record':record, 'author':record.author}
    return render(request,'details.html',context)


def add(request):
    result = ''
    author_user = request.user
    if request.method == 'POST':
        name = request.POST.get('ar_name')
        body = request.POST.get('ar_body')
        result = validate(name,body)
        if result:

            logged_in_user = request.user
            print(logged_in_user)
            
            if str(logged_in_user) != 'AnonymousUser' :
                author_user = Author.objects.get(user=logged_in_user)
                record = Article.objects.create(author=author_user, name=name, body=body)
            else:
                record = Article.objects.create(name=name, body=body)
            
            result = "Your article has been saved successfully"
            record.save()

    return render(request,'add.html',{'message':result, 'author':author_user})


def validate(name, body):
    if name == '' or body == '':
        return "please enter something in fields"
    return True


def update(request, pk):
    record = Article.objects.get(id=pk)
    if request.method == 'POST':
        form_name = request.POST.get('ar_name')
        form_body = request.POST.get('ar_body')        
        record.name = form_name  #updating
        record.body = form_body  #update
        record.save()
        return redirect('/')

    context = {'record': record }
    return render(request, 'update.html', context)


def delete(request,pk):
    record = Article.objects.get(id=pk)
    record.delete()
    return redirect('/')