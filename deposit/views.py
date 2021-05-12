from django.shortcuts import render
from django.http import HttpResponseNotFound
# from django.http import HttpResponse


from deposit.models import Deposit



def index(request):                                   # general deposits list

    deposits = Deposit.objects.all()

    context = {
        'deposits': deposits
    }

    return render(
        template_name='deposit_list.html',
        request=request,
        context=context,
    )


def add_deposit(request):

    if request.method == 'POST':

        deposit = Deposit(
        deposit=request.POST["deposit"],
        term = request.POST["term"],
        rate = request.POST["rate"],
        )

        deposit.save()                                    # storege into DB


        context = {
            'deposit': deposit.deposit,
            'term': deposit.term,
            'rate': deposit.rate,
        }

        return render(
            template_name='deposit_list.html',            # show general deposits list
            request=request,
            context=context,
        )

    return render(
        template_name='add_deposit.html',
        request=request,
        context={},
    )


def get_deposit (request, deposit_id):

    try:
        deposit = Deposit.objects.get(id=deposit_id)


        context = {

            'deposit': deposit.deposit,
            'term': deposit.term,
            'rate': deposit.rate,

        }

        return render(
            template_name='deposit_detail.html',
            request=request,
            context=context,
        )


    except User.DoesNotExist:

        return HttpResponseNotFound("<h2>User not found</h2>")

