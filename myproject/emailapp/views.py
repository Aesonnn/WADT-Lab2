# emailapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .forms import EmailForm, PersonForm
from .models import Person


# View for sending emails
def send_email(request):
    if request.method == 'POST':
        print("Executed")
        form = EmailForm(request.POST)
        if form.is_valid():
            print("Executed")
            email = form.cleaned_data['email']
            recipients = request.POST.getlist('recipients')
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            try:
                if email: # If email is provided, send email to that address
                    send_mail(subject, body, 'alexannilss@gmail.com', [email])
                if recipients: # If recipients are provided, send email to all selected recipients
                    for recipient in recipients:
                        send_mail(subject, body, 'alexannilss@gmail.com', [recipient])
                if not email and not recipients: # If no email or recipients are provided, show an error message
                    messages.error(request, 'Please provide at least one recipient.')
                else:
                    messages.success(request, 'Email sent successfully!') 
            except Exception as e:
                messages.error(request, f'Failed to send email: {str(e)}')
            return redirect('send_email')
    else:
        form = EmailForm()
    people = Person.objects.all()
    return render(request, 'send_email.html', {'form': form, 'people': people})



# View for adding a contact to the list
def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Person added successfully!')
            return redirect('add_person')
    else:
        form = PersonForm()
    people = Person.objects.all()
    return render(request, 'add_person.html', {'form': form, 'people': people})

# Provides an option to delete a contact from the list
def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    messages.success(request, 'Contact deleted successfully!')
    return redirect('add_person')

# For debugging purposes - to list all contacts in the database
def person_list(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})
    