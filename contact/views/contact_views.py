from django.shortcuts import render,get_object_or_404
from django.http import Http404
from contact.models import Contact
# Create your views here.

def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[:10]
    
    
    context = {'contacts':contacts,'title':'Contatos -'}
    return render(request,
                  'contact/index.html',
                  context
                  )


def contact(request,contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact,pk=contact_id,show=True)
    title = f'Contato - {single_contact.first_name} -'
    context = {'contact':single_contact,'title':title}

    return render(request,
                  'contact/contact.html',
                  context
                  )