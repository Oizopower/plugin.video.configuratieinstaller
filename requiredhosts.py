# Configuratie Installer By: Oizopower 2017
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys,time,shutil
import configinstaller as main
addon=main.addon; net=main.net; settings=main.settings; 
UA='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:30.0) Gecko/20100101 Firefox/30.0'
def ResolveOtherHosts(url):
    try:
        if url.startswith('host://'): 
        	url=url.replace('host://','http://')
        	try: 
        		import urlresolver
        		url=urlresolver.HostedMediaFile(url).resolve()
        		return url
        	except: return url+'#[error]urlresolver'
        else: return url
    except: return url+'#[error]exception'
def PromptFile(url):
    if url.startswith('promptfile://'): url=url.replace('promptfile://','http://www.promptfile.com/l/')
    if url.startswith('http://promptfile.com/'): url=url.replace('http://promptfile.com/','http://www.promptfile.com/')
    if ('http://www.promptfile.com/l/' not in url): return url
    try:
        html=main.nolines(net.http_GET(url,headers={'User-Agent':UA}).content).replace('/>','/\n\r>').replace('</div>','</div\n\r>')
        #if '<h3 class="error_msg_title">Invalid or Deleted File.</h3>' in html: return "[error]  This file doesn't exist, or has been removed."
        r=re.search('<a href="(http\D*://.+?)" class="green_btn download_btn">\s*Download File\s*</a',html)
        if not r:
            data={}; r=re.findall(r'<input type="hidden" name="(chash)" value="(.*?)"',html)
            for name,value in r: data[name]=value
            html=main.nolines(net.http_POST(url,data,headers={'User-Agent':UA,'Referer':url}).content).replace('</div>','</div\n\r>')
            r=re.search('<a href="(http\D*://.+?)" class="green_btn download_btn">Download File</a',html)
        if r: return urllib.unquote_plus(r.group(1))
        else: return url+'#[error]r'
    except: return url+'#[error]exception'
def CheckForHosts(url):
    #DefaultUrl=""+url
    #try:
        if 'https://' in url.lower(): url=url.replace('https://','http://')
        print {'incoming url':url}
        if url.startswith('host://'): url=ResolveOtherHosts(url)
        else:
            url=PromptFile(url)
        print {'returning url':url}
        return url
    #except: return DefaultUrl+'#[error]'
