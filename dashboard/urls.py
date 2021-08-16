from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_with_pivot, name=' dashboard_floorplan'),
    path('dashboard_floorplan', views.dashboard_floorplan, name='dashboard_floorplan'),

    path('data', views.pivot_data, name='pivot_data'),
    
    path('onR1to4', views.row_1_to_4_turn_on, name='onR1to4'),
    path('offR1to4', views.row_1_to_4_turn_off, name='offR1to4'),
    
    path('onR5to6', views.row_5_to_6_turn_on, name='onR5to6'),
    path('offR5to6', views.row_5_to_6_turn_off, name='offR5to6'),

    path('downlights_turn_on', views.downlights_turn_on, name='downlights_turn_on'),
    path('downlights_turn_off', views.downlights_turn_off, name='downlights_turn_off'),

    path('blueWallLed_turn_on', views.blueWallLed_turn_on, name='blueWallLed_turn_on'),
    path('blueWallLed_turn_off', views.blueWallLed_turn_off, name='blueWallLed_turn_off'),

    path('lightShow_turn_on', views.lightShow_turn_on, name='lightShow_turn_on'),
    path('lightShow_turn_off', views.lightShow_turn_off, name='lightShow_turn_off'),

    path('ledColorRed', views.ledColorRed, name='ledColorRed'),
    path('ledColorGreen', views.ledColorGreen, name='ledColorGreen'),
    path('ledColorBlue', views.ledColorBlue, name='ledColorBlue'),
    path('ledColorPink', views.ledColorPink, name='ledColorPink'),
    path('ledColorCyan', views.ledColorCyan, name='ledColorCyan'),
    path('ledColorYellow', views.ledColorYellow, name='ledColorYellow'),
    path('ledColorPurple', views.ledColorPurple, name='ledColorPurple'),
    path('ledColorWhite', views.ledColorWhite, name='ledColorWhite'),

]