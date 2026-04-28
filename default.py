import subprocess
import xbmc
import xbmcaddon

addon = xbmcaddon.Addon()
host = addon.getSetting('host')
app = addon.getSetting('app')

cmd = [
    'sudo', 'systemd-run', '--unit=moonlight', '--collect',
    '/bin/bash', '-c',
    f'sleep 5 && '
    f'systemctl stop mediacenter && '
    f'sudo -u osmc XDG_RUNTIME_DIR=/run/user/1000 HOME=/home/osmc moonlight-qt stream "{host}" "{app}" && '
    f'systemctl start mediacenter'
]

subprocess.Popen(
    cmd,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    start_new_session=True
)

xbmc.sleep(1000)
xbmc.executebuiltin('Quit')
