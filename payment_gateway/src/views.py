from django.shortcuts import render

# Create your views here.
import razorpay
from .models import ledger
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        amount = int(request.POST['amount'])*100
        client = razorpay.Client(
            auth=("rzp_test_QxCqoQqWagP69v", "zawWawMRVo03AZV8IsvYrzK7"))
        payment = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        entry = ledger(name=name, amount=amount, payment_id=payment['id'])
        entry.save()
        return render(request, 'index.html', {'payment': payment})
    return render(request, 'index.html')


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        data = {}
        for key, val in a.items():
            if key == 'razorpay_order_id':
                data['razorpay_order_id'] = val
                order_id = val
            elif key == 'razorpay_payment_id':
                data['razorpay_payment_id'] = val
            elif key == 'razorpay_signature':
                data['razorpay_signature'] = val
        print(data)
        user = ledger.objects.filter(payment_id=order_id).first()
        client = razorpay.Client(
            auth=("rzp_test_QxCqoQqWagP69v", "zawWawMRVo03AZV8IsvYrzK7"))
        check = client.utility.verify_payment_signature(data)
        if not check:
            return render(request, 'failed.html')
        user.paid = True
        user.save()
    return render(request, 'success.html')
