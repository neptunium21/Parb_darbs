from django.shortcuts import render
from django.http import HttpResponseNotFound
# from django.http import HttpResponse


from deposit_app.models import Deposit



def index(request):                 # common deposits list

    deposits = Deposit.objects.all()

    context = {
        'deposits': deposits
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )


def add_deposit(request):

    if request.method == 'POST':

        deposit = Deposit(
        depo=request.POST["depo"],
        term = request.POST["term"],
        rate = request.POST["rate"],
        )

        deposit.save()       # for storege in DB


        context = {
            'depo': deposit.depo,
            'term': deposit.term,
            'rate': deposit.rate,
        }

        return render(
            template_name='deposit_detail.html',
            request=request,
            context=context,
        )

    return render(
        template_name='add_deposit.html',
        request=request,
        context={},
    )

# def get_deposit (request, user_id):
def get_deposit(request):
    try:
        # user = User.objects.get(id=user_id)
        user = User.objects.get()

        context = {

            'username': user.username,
            'email': user.email,
        }

        return render(
            template_name='user_detail.html',
            request=request,
            context=context,
        )


    except User.DoesNotExist:

        return HttpResponseNotFound("<h2>User not found</h2>")

