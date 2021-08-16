from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Order
from django.core import serializers
import getpass
import telnetlib, os, re
from django.views.decorators.csrf import csrf_exempt

HOST = "192.168.1.66"
PORT = 23
telnet = telnetlib.Telnet()
telnetWorking = False
print("Setup done")

try:
    telnet.open(HOST)
    telnetWorking = True
except:
    print("Telnet failed")
    print(telnetWorking)    

def dashboard_with_pivot(request):
    return render(request, 'dashboard_floorplan.html', {})

def dashboard_floorplan(request):
    return render(request, 'dashboard_floorplan.html', {})

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

@csrf_exempt 
def row_1_to_4_turn_on(request):
    #run telnet command
    print("Turn on for row 1 to 4")
    data = {'is_complete' :  True}
    print(telnetWorking)
    if telnetWorking:
        telnet.write(('P 1 12\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}

    return JsonResponse(data)

@csrf_exempt 
def row_1_to_4_turn_off(request):
    #run telnet command
    print("Turn off for row 1 to 4")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 4 12\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    
    return JsonResponse(data)

@csrf_exempt 
def row_5_to_6_turn_on(request):
    #run telnet command
    print("Turn on for row 5 to 6")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 1 13\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)

@csrf_exempt 
def row_5_to_6_turn_off(request):
    #run telnet command
    print("Turn off for row 5 to 6")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 4 13\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}

    return JsonResponse(data)

@csrf_exempt 
def downlights_turn_on(request):
    #run telnet command
    print("Turn on downlights")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 1 14\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)

@csrf_exempt 
def downlights_turn_off(request):
    #run telnet command
    print("Turn off downlights")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 4 14\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)

@csrf_exempt 
def blueWallLed_turn_on(request):
    #run telnet command
    print("Turn on blueWallLed")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 1 15\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)

@csrf_exempt 
def blueWallLed_turn_off(request):
    #run telnet command
    print("Turn off blueWallLed")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 4 15\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)

@csrf_exempt 
def lightShow_turn_on(request):
    #run telnet command
    print("Turn on Light Show")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 1 17\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)

@csrf_exempt 
def lightShow_turn_off(request):
    #run telnet command
    print("Turn off Light Show")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 12 17\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)


@csrf_exempt 
def ledColorRed(request):
    #run telnet command
    print("Red")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 1 16\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)


@csrf_exempt 
def ledColorGreen(request):
    #run telnet command
    print("Green")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 2 16\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)
    
    
@csrf_exempt 
def ledColorBlue(request):
    #run telnet command
    print("Blue")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 3 16\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)


@csrf_exempt 
def ledColorPink(request):
    #run telnet command
    print("Pink")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 5 16\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)


@csrf_exempt 
def ledColorCyan(request):
    #run telnet command
    print("Cyan")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 6 16\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)


@csrf_exempt 
def ledColorYellow(request):
    #run telnet command
    print("Yellow")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 7 16\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)


@csrf_exempt 
def ledColorPurple(request):
    #run telnet command
    print("Purple")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 8 16\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)


@csrf_exempt 
def ledColorWhite(request):
    #run telnet command
    print("White")
    data = {'is_complete' :  True}
    if telnetWorking:
        telnet.write(('P 9 16\r\n').encode('ascii'))
        data = {'is_complete' :  True}
    else:
        data = {'is_complete' :  False}
    return JsonResponse(data)



