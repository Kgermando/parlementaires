from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from sondage.models import Sondage, Vote

# Create your views here.
def sondage_view(request):
    sondage_list = Sondage.objects.all().order_by('-created')
    context = {
        'sondage_list': sondage_list
    }
    template_name = 'pages/sondage.html'
    return render(request, template_name, context)


def sondage_view_detail(request, sondage_id):
    sondage_list = Sondage.objects.get(id= sondage_id)
    context = {
        'sondage_list': sondage_list
    }
    template_name = 'pages/sondage-view.html'
    return render(request, template_name, context)


# @login_required(login_url='/accounts/login/')
def vote(request, sondage_id):
    # sondage = Sondage.objects.get(id= sondage_id)
    sondage = get_object_or_404(Sondage, pk=sondage_id)

    if request.method == 'POST':
        if sondage.author.username == request.user.username:
            messages.error(request, "Le créateur ne peut pas voter pour son  post !")
            return redirect('sondage:vote', sondage_id)
        else:
            try:
                vote = Vote.objects.get(sondageID=sondage_id, userID=request.user)
                messages.error(request, 'Vous avez déjà voté pour ce post!')
                return redirect('sondage:vote', sondage_id)
            except Vote.DoesNotExist:
                vote = None
                # find product by id and increment
                sondage = Sondage.objects.get(id=sondage_id)
                vote = Vote(sondageID=sondage, userID=request.user)
                selected_option = request.POST['sondage']
                if selected_option == 'option1':
                    sondage.vote_yes +=1
                elif selected_option == 'option2':
                    sondage.vote_no +=1
                elif selected_option == 'option3':
                    sondage.vote_null +=1
                else:
                    return HttpResponse(400, 'Invalid Form')

                vote.save()
                sondage.save()
                messages.success(request, 'voted successfully!')
                return redirect('sondage:vote', sondage_id)

    context = {
        'sondage' : sondage
    }
    template_name = 'pages/vote.html'
    return render(request, template_name, context)
        
