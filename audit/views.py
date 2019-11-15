from django.shortcuts import *
from django.views.generic import *
from django.http import *
from django.template import loader

from .models import *
from .forms import *


# Create your views here.


def index(request):
    return HttpResponse("Hello World.")


def all_proposal_details(request):
    proposal_list = Proposals.objects.order_by('-date')[:5]
    context = {'proposal_list': proposal_list, }
    return render(request, 'all_proposals.html', context)


def all_society_details(request):
    society_list = Society.objects.order_by('soc_name')[:5]
    context = {'society_list': society_list, }
    return render(request, 'all_society.html', context)


def all_secretaries_details(request):
    sec_list = Secretaries.objects.order_by('sec_id')[:5]
    context = {'sec_list': sec_list}
    return render(request, 'all_secretary.html', context)


def proposal_details(request, proposal_no):
    proposal = get_object_or_404(Proposals, pk=proposal_no)
    return render(request, 'prop_detail.html', {'proposal': proposal})


def society_details(request, soc_id):
    society = get_object_or_404(Society, pk=soc_id)
    return render(request, 'society _detail.html', {'society': society})


def secretary_details(request, sec_id):
    secretary = get_object_or_404(Secretaries, pk=sec_id)
    return render(request, 'sec_detail.html', {'secretary': secretary})


def soc_new(request):
    if request.method == "POST":
        form = SocForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            # society = Society.objects.order_by('soc_name')[:5]
            return redirect('soc_all')
        else:
            return render(request, 'forms/soc_form.html', {'form': form})
    else:
        form = SocForm()
        return render(request, 'forms/soc_form.html', {'form': form})


def sec_new(request):
    if request.method == "POST":
        form = SecForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            # society = Society.objects.order_by('soc_name')[:5]
            return redirect('sec_all')
        else:
            return render(request, 'forms/sec_form.html', {'form': form})
    else:
        form = SecForm()
        return render(request, 'forms/sec_form.html', {'form': form})


def proposal_new(request):
    if request.method == "POST":
        form = PropForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('prop_all')
        else:
            return render(request, 'form/prop_form.html', {'form': form})
    else:
        form = PropForm()
        return render(request, 'forms/prop_form.html', {'form': form})