# !/usr/bin/env python
# -*- coding: utf-8 -*-

import fileop

'''
str = '100,4'
print str
newStr = fileop.convertLine(str)
print newStr
'''


hello = 'time,temperature,td,temp_max,temp_min,pressure,precip_1h,RH,RH_min,wind_direct_inst,wind_speed_inst,wind_direct_2m,wind_speed_2m,wind_direct_max,wind_speed_max,vis_inst,vis_min,temp_surf,temp_surf_max,temp_surf_min,temp_surf_5,temp_surf_10,temp_surf_15,temp_surf_20,temp_surf_40'
hellos = hello.split(',')
print len(hellos)
