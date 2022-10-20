from django.shortcuts import render


def home(request):

    return render(request,'calculator/index.html')

def results(request):
    monthly_salary = float(request.GET['monthly_salary1'])
    bonifications = float(request.GET['bonifications1'])
    overtime = float(request.GET['overtime1'])


    gross_pay = monthly_salary + bonifications
    gross_payot = monthly_salary + bonifications + overtime

    sfs = gross_pay * 0.0304
    afp = gross_pay * 0.0287
    isr = 0
   

    if gross_payot <= 34685:
        isr = 0

    elif (gross_payot > 34686) and (gross_payot <= 52027):
            isr = ((gross_payot - 34685) * 0.15)

    elif (gross_payot >= 52028) and (gross_payot <= 72260):
            isr = (((gross_payot - 52027) * 0.20) + 2601)

    elif (gross_payot >= 72261):
            isr = (((gross_payot - 72261) * 0.25) + 6648)

    discounts = sfs + afp + isr
    net_pay = gross_payot - discounts

    gross_payot = round(gross_payot, 2)
    gross_payot = "{:,}".format(gross_payot)

    discounts = round(discounts, 2)
    discounts = "{:,}".format(discounts)

    sfs = round(sfs, 2)
    sfs = "{:,}".format(sfs)

    net_pay = round(net_pay, 2)
    net_pay = "{:,}".format(net_pay)

    afp = round(afp, 2)
    afp = "{:,}".format(afp)

    isr = round(isr, 2)
    isr = "{:,}".format(isr)

    context = {
        'net_pay' : net_pay,
        'gross_payot' : gross_payot,
        'discounts' : discounts,
        'afp' : afp,
        'sfs' : sfs,
        'isr' : isr
    }
    return render(request, 'calculator/results.html', context)