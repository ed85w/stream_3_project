from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm, AddPaymentDetailsForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
from models import User

stripe.api_key = settings.STRIPE_SECRET


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # add test here to see if username already exists!!!
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'),)

            if user:
                messages.success(request, "You have successfully registered")
                auth.login(request, user)
                return redirect(reverse('index'))


            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('index'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return render(request, 'index.html')


@login_required
def payment_details(request):
    if request.method == 'POST':
        form = AddPaymentDetailsForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Customer.create(
                        card=form.cleaned_data['stripe_id'],  # this is currently the card token/id
                )

                if customer:
                    User.objects.filter(pk=request.user.id).update(stripe_id=customer.id)
                    messages.success(request, 'Card details accepted')
                    return render(request, 'index.html')

            except stripe.error.CardError, e:
                form.add_error(request, "Your card was declined!")

    else:
        form = AddPaymentDetailsForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'payment_details.html', args)



