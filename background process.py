import psutil
# should be installed

s = set()
for p in psutil.process_iter():
    s.add(p.name().title())

m = {'Utweb.Exe', 'Audiodg.Exe', 'Lockapp.Exe','Gamebar.Exe','Pythonw.Exe', 'Video.Ui.Exe', 'Systemsettings.Exe', 'Settingsynchost.Exe', 'Applicationframehost.Exe', 'Dllhost.Exe', 'Searchfilterhost.Exe', 'Skypeapp.Exe', 'Svchost.Exe', 'Googlecrashhandler64.Exe', 'Csrss.Exe', 'Fsnotifier64.Exe', 'Igfxem.Exe', 'Wininit.Exe', 'Runtimebroker.Exe', 'Fmapp.Exe', 'Searchprotocolhost.Exe', 'Presentationfontcache.Exe', 'Conhost.Exe', 'Shellexperiencehost.Exe', 'Memory Compression', 'Sgrmbroker.Exe', 'Winlogon.Exe', 'Igfxcuiservice.Exe', 'Smartscreen.Exe', 'Taskhostw.Exe', 'Searchui.Exe', 'Skypebackgroundhost.Exe', 'Nissrv.Exe', 'Spoolsv.Exe', 'Igfxhk.Exe', 'Syntpenh.Exe', 'Sasrv.Exe', 'Caudiofilteragent64.Exe', 'Lsass.Exe', 'Searchindexer.Exe', 'Syntphelper.Exe', 'System', 'Ctfmon.Exe', 'Dwm.Exe', 'Msmpeng.Exe', 'Services.Exe', 'Dashost.Exe', 'Securityhealthservice.Exe', 'Sihost.Exe', 'Registry', 'Systemsettingsbroker.Exe', 'Syntpenhservice.Exe', 'Fontdrvhost.Exe', 'Cxaudmsg64.Exe', 'System Idle Process', 'Smss.Exe', 'Igfxtray.Exe', 'Splwow64.Exe', 'Connect.Service.Contentservice.Exe', 'Explorer.Exe', 'Qmemulatorservice.Exe', 'Msascuil.Exe', 'Googlecrashhandler.Exe', 'Sedsvc.Exe'}
s = s - m
for i in s:
    print(i.title())

# duty --> add background processes in m
