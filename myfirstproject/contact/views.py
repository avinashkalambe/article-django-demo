from django.shortcuts import redirect, render
from django.views import View

from author.models import Author
from .forms import ContactForm
from .models import Contact
# from django.contrib.auth.decorators import login_required


# Create your views here.
class ContactFormView(View):

    template_name = 'contact.html'
    class_form = ContactForm

    def get(self, request, *args, **kargs):
        print('in class get request')
        form = self.class_form()        
        return render(self.request, self.template_name, {'form': form})

    
    def post(self, request, *args, **kargs):
        print('in class post request')
        form = self.class_form(request.POST)

        if form.is_valid():            
            n_form = form.save(commit=False)
            attachment = self.request.FILES.get('attachment')
            n_form.attachment = attachment
            n_form.save()            
            form = self.class_form()
            
            return render(self.request, self.template_name, {'form':form, 'message':'Thank you .. we will get back to you'})
        else:
            return render(self.request, self.template_name, {'form':form})
        

class ContactListContacts(View):

    template_name = 'contact_show.html'

    def get(self, request):
        all_records = Contact.objects.all()
        return render(request, self.template_name, {'data':all_records})


class DeleteContact(View):

    template_name = 'contact_show.html'

    def get(self, request, **kargs):
        print(kargs)
        record = Contact.objects.get(**kargs)
        record.delete()
        all_records = Contact.objects.all()
        return render(request, self.template_name, {'data':all_records})