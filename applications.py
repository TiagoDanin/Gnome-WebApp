applications = {}
applications['Bing'] = 'https://www.bing.com'
applications['Duckduckgo'] = 'https://duckduckgo.com'
applications['Github'] = 'https://github.com'
applications['Netflix'] = 'https://www.netflix.com'
applications['Spotify'] = 'https://www.spotify.com/br/redirect/webplayerlink/?utm_medium=www_deviceslink'
applications['Telegram'] = 'https://web.telegram.org/'
applications['Youtube'] = 'https://www.youtube.com/'
applications['YoutubeTV'] = 'http://www.youtube.com/tv'
applications['YoutubeGaming'] = 'https://gaming.youtube.com/'
applications['Twitter'] = 'https://twitter.com/'
applications['Outlook'] = 'http://outlook.com/'
applications['Riot'] = 'https://riot.im/app/'

for s in applications:
	name = s
	url = applications[s]
	text = '''#!/usr/bin/env xdg-open
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Name={name} Web
Comment={name} - WebApp
Exec=/usr/bin/gnome-webapp {name} {url} "1200" "600"
Icon={namelower}
Terminal=false
Type=Application
Categories=Network;'''.format(name=name, namelower=name.lower(), url=url)

	f = open('applications/%s-web.desktop' % s.lower(), 'w')
	f.write(text)
	f.close
