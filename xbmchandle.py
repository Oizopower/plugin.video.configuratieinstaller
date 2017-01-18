# -*- coding: utf-8 -*-
# Configuratie Installer By: Oizopower 2017
import xbmcgui,xbmc,shutil,os
def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'
def killxbmc():
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog = xbmcgui.Dialog();
        dialog.ok("[COLOR=red][B]OPGELET  !!![/COLOR][/B]", "Als u deze melding te zien krijgt is het niet gelukt",
                  "om uw Kodi af te sluiten. Haal uw StreamBox van het stroom af en plug deze er weer in.",
                  'Vervolgens werkt alles naar behoren en hoeft u geen verdere acties te ondernemen')
    elif myplatform == 'linux': #Linux
        print "############   try linux force close  #################"
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog = xbmcgui.Dialog();
        dialog.ok("[COLOR=red][B]OPGELET  !!![/COLOR][/B]", "Als u deze melding te zien krijgt is het niet gelukt",
                  "om uw Kodi af te sluiten. Haal uw StreamBox van het stroom af en plug deze er weer in.",
                  'Vervolgens werkt alles naar behoren en hoeft u geen verdere acties te ondernemen')
    elif myplatform == 'android': # Android
        print "############   try android force close  #################"
        try: os.system("su -c 'reboot'")
        except: pass
        dialog = xbmcgui.Dialog();
        dialog.ok("[COLOR=red][B]OPGELET  !!![/COLOR][/B]", "Als u deze melding te zien krijgt is het niet gelukt",
                  "om uw Kodi af te sluiten. Haal uw StreamBox van het stroom af en plug deze er weer in.",
                  'Vervolgens werkt alles naar behoren en hoeft u geen verdere acties te ondernemen')
    elif myplatform == 'windows': # Windows
        print "############   try windows force close  #################"
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        dialog = xbmcgui.Dialog();
        dialog.ok("[COLOR=red][B]OPGELET  !!![/COLOR][/B]", "Als u deze melding te zien krijgt is het niet gelukt",
                  "om uw Kodi af te sluiten. Haal uw StreamBox van het stroom af en plug deze er weer in.",
                  'Vervolgens werkt alles naar behoren en hoeft u geen verdere acties te ondernemen')
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR=red][B]OPGELET  !!![/COLOR][/B]", "Als u deze melding te zien krijgt is het niet gelukt",
                  "om uw Kodi af te sluiten. Haal uw StreamBox van het stroom af en plug deze er weer in.",
                  'Vervolgens werkt alles naar behoren en hoeft u geen verdere acties te ondernemen')