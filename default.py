# -*- coding: utf-8 -*-
# Configuratie Installer By: Oizopower 2017
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys,downloader,extract,time,shutil,xbmchandle
import configinstaller as main
AddonTitle='Configuratie Installer';
addon=main.addon; net=main.net; settings=main.settings;
RequiredHostsPath=xbmc.translatePath(os.path.join(main.AddonPath,'requiredhosts.py'))

def LOADDEFAULT():
        addonZipURL = xbmc.Keyboard("", "Voer uw profiel link in", False)
        addonZipURL.doModal()

        if addonZipURL.isConfirmed() and addonZipURL.getText() != "" and ('://' in addonZipURL.getText()):
            CustPackage = addonZipURL.getText()
            EXECUTEBUILD('Streambox',CustPackage,'Installeren van het aangepaste profiel','main');
        else: dialog=xbmcgui.Dialog(); dialog.ok("Foutieve URL","U heeft een ongeldige URL ingevoerd[CR]Open de addon nogmaals en voer een geldige URL in.")

def xEBb(t): main.xEB('Skin.SetBool(%s)'%t)
def xEBS(t,n): main.xEB('Skin.SetString(%s,%s)'%(t,n))
def EXECUTEBUILD(name,url,description,filetype):
    path=xbmc.translatePath(os.path.join('special://home','addons','packages')); confirm=xbmcgui.Dialog(); filetype=filetype.lower();

    if confirm.yesno(AddonTitle, "Er zullen addons worden geïnstalleerd. Wij adviseren alleen legale content te downloaden en wij accepteert geen enkele aansprakelijkheid. Gaat u hier mee akkoord?"):
        dp=xbmcgui.DialogProgress(); dp.create(AddonTitle,"Downloaden ",'','Een ogenblik geduld...')
        lib=os.path.join(path,name+'.zip')
        try: os.remove(lib)
        except: pass

        if main.isFile(RequiredHostsPath)==False: dialog=xbmcgui.Dialog(); dialog.ok("Error!",'Import bestand niet gevonden.'); return
        try: import requiredhosts as RequiredHosts
        except: dialog=xbmcgui.Dialog(); dialog.ok("Error!","importeren niet gelukt."); return

        url=RequiredHosts.CheckForHosts(url);

        if str(url).endswith('[error]'): dialog=xbmcgui.Dialog(); dialog.ok("Error!",url); return
        if '[error]' in url: dialog=xbmcgui.Dialog(); dialog.ok("Error!",url); return
        if not str(url).lower().startswith('http://'): dialog=xbmcgui.Dialog(); dialog.ok("Error!",url); return

        downloader.download(url,lib,dp)

        if   filetype=='main':  addonfolder=xbmc.translatePath('special://home')
        elif filetype=='addon': addonfolder=xbmc.translatePath(os.path.join('special://home','addons'))
        else: dialog=xbmcgui.Dialog(); dialog.ok("Error!",'filetype: "%s"'%str(filetype)); return

        xbmc.sleep(4000)
        dp.update(0,"","Uitpakken van ZIP bestand.")
        extract.all(lib,addonfolder,dp)

        xbmc.sleep(4000)
        dialog=xbmcgui.Dialog(); dialog.ok("Installatie Voltooid!","Uw Kodi wordt nu opnieuw opgestart om de installatie te voltooien. Hierna kunt u Kodi weer openen")

        xbmchandle.killxbmc()

def DoA(a): xbmc.executebuiltin("Action(%s)" % a) #DoA('Back'); # to move to previous screen.
def eod(): addon.end_of_directory()

params=main.get_params(); url=None; name=None; mode=None; year=None; imdb_id=None
def ParsUQP(s,Default=None):
    try: return urllib.unquote_plus(params[s])
    except: return Default

if   mode==None or url==None or len(url)<1: LOADDEFAULT()

