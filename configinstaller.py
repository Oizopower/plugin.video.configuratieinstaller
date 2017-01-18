# -*- coding: cp1252 -*-
# Configuratie Installer By: Oizopower 2017
import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,os,xbmcaddon
try:        from addon.common.addon import Addon
except:
    try:    from t0mm0.common.addon import Addon
    except: from t0mm0_common_addon import Addon
try:        from addon.common.net   import Net
except:
    try:    from t0mm0.common.net   import Net
    except: from t0mm0_common_net   import Net
#Define common.addon
addon_id='plugin.video.configuratieinstaller';
# Global Stuff
addon=Addon(addon_id,sys.argv); net=Net(); settings=xbmcaddon.Addon(id=addon_id); net.set_user_agent('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3 Kodi');
AddonPath=settings.getAddonInfo('path')
# #
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]; cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'): params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&'); param={}
                for i in range(len(pairsofparams)):
                        splitparams={}; splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2: param[splitparams[0]]=splitparams[1]
        return param
def nolines(t):
	it=t.splitlines(); t=''
	for L in it: t=t+L
	t=((t.replace("\r","")).replace("\n","").replace("\a",""))
	return t
def isFile(filename): return os.path.isfile(filename)
def xEB(t): xbmc.executebuiltin(t)

