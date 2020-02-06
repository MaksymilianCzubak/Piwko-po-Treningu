from PortalTreningowy.models import Plan, TrainingSession

p1 = Plan.objects.create(level='Początkujący', goal='Lepsza wydolność aerobowa (tlenowa)',
                         description='Program jest przewidziany dla polepszenia twojej ogólnej wydolności tlenowej'
                                     '-jest to idealny punkt wyjścia dla kolarzy, którzy wcale nie trenowali przez'
                                     ' ostatni rok lub dłużej. Intensywność ćwiczeń - łatwa do umiarkowanej - prowadzi'
                                     'stopniowo do wyższych poziomów sprawności tlenowej.', hours_per_week=8)

p2 = Plan.objects.create(level='Średnio zaawansowany', goal='Więkrza prędkość jazdy w stałym tępie',
                         description='Zacznij w tym miejscu, jeśli jeździsz sporo, ale nie masz jasnego celu'
                                     'treningu. Ten program podwyższy twój próg mleczanowy, więc będziesz mógł'
                                     'jechać szybciej bez gromadzenia się kwasu mlekowego wskutek pedałowania'
                                     'anaerobowego (beztlenowego).', hours_per_week=10)
p3 = Plan.objects.create(level='Zaawansowany', goal='Utrzymanie prędkości przymaksymalnej wymianie tlenowej',
                         description='Ten program jest przewidziany dla kolarzy, którzy są w formie i pragną dążyć'
                                     ' do określonego celu, jakim może być na przykład wyścig pod koniec sezonu.'
                                     ' Zwiększysz ogólną prędkość i dasz sobie radę z ciągłymi zmianami tępa podczs '
                                     'ataków i kontrataków', hours_per_week=14)

ts111 = TrainingSession.objects.create(week=1, day=1, details='30 minut w strefie 1 w płaskim terenie w stałym, '
                                                              'łatwym tępie')
ts112 = TrainingSession.objects.create(week=1, day=2, details='45 minut w strefie 2 z 5 minutami szybkiego pedałowania'
                                        'w płaskim terenie')
ts113 = TrainingSession.objects.create(week=1, day=3, details='1 godzina w strefie 2 ze stałą kadencją 80-85 obr./min')
ts114 = TrainingSession.objects.create(week=1, day=4, details='45 minut w strefie 2 z 5 minutami szybkiego pedałowania'
                                       'w płaskim terenie')
ts115 = TrainingSession.objects.create(week=1, day=5, details='Dzień wolny')
ts116 = TrainingSession.objects.create(week=1, day=6, details='1 godzina w strefie 2 z 10 minutami szybkiego pedałowania'
                                        'w płaskim terenie')
ts117 = TrainingSession.objects.create(week=1, day=7, details='1,5 godz. w strefie 2 w terenie pagórkowatym; spróbuj'
                                                              ' pozostać w siodełku jadąc pod górę.')
ts121 = TrainingSession.objects.create(week=2, day=1, details='30 minut w strefie 2 z 10 minutami szybkiego pedałowania'
                                        ' w płaskim terenie')
ts122 = TrainingSession.objects.create(week=2, day=2, details='45 minut w strefie 2 z 5 minutami szybkiego pedałowania'
                                        'w płaskim terenie')
ts123 = TrainingSession.objects.create(week=2, day=3, details='1 godzina w strefie 2 ze stałą kadencją 80-85 obr./min')
ts124 = TrainingSession.objects.create(week=2, day=4, details='45 minut w strefie 2 z 5 minutami szybkiego pedałowania'
                                       'w płaskim terenie')
ts125 = TrainingSession.objects.create(week=2, day=5, details='Dzień wolny')
ts126 = TrainingSession.objects.create(week=2, day=6, details='1 godzina w strefie 2 z 10 minutami szybkiego pedałowania'
                                                              'w płaskim terenie')
ts127 = TrainingSession.objects.create(week=2, day=7, details='1,5 godz. w strefie 2 w terenie pagórkowatym; spróbuj'
                                        ' pozostać w siodełku jadąc pod górę.')
ts131 = TrainingSession.objects.create(week=3, day=1, details='30 minut w strefie 2 z 10 minutami szybkiego pedałowania'
                                        ' w płaskim terenie')
ts132 = TrainingSession.objects.create(week=3, day=2, details='45 minut w strefie 2 z 10 minutami szybkiego pedałowania'
                                        'w płaskim terenie')
ts133 = TrainingSession.objects.create(week=3, day=3, details='1 godzina w strefie 2 ze stałą kadencją 80-85 obr./min')
ts134 = TrainingSession.objects.create(week=3, day=4, details='45 minut w strefie 2 z 5 minutami szybkiego pedałowania'
                                       'w płaskim terenie')
ts135 = TrainingSession.objects.create(week=3, day=5, details='Dzień wolny')
ts136 = TrainingSession.objects.create(week=3, day=6, details='1 godzina w strefie 2 z 10 minutami szybkiego pedałowania'
                                        'w płaskim terenie')
ts137 = TrainingSession.objects.create(week=3, day=7, details='2 godz. w strefie 2 w terenie pagórkowatym; na'
                                        'szczytach dojdź do strefy 3')
ts141 = TrainingSession.objects.create(week=4, day=1, details='30 minut w strefie 1; jazda odpoczynkowa')
ts142 = TrainingSession.objects.create(week=4, day=2, details='30 minut w strefie 1; jazda odpoczynkowa')
ts143 = TrainingSession.objects.create(week=4, day=3, details='Dzień wolny')
ts144 = TrainingSession.objects.create(week=4, day=4, details='30 minut w strefie 1; jazda odpoczynkowa')
ts145 = TrainingSession.objects.create(week=4, day=5, details='45 minut w strefie 2 z 2 płaskimi sprintami po 10 sekund,'
                                        ' między nimi 10 min. jazdy odpoczynkowej')
ts146 = TrainingSession.objects.create(week=4, day=6, details='1 godzina w strefie 2 z 10 minutami szybkiego pedałowania'
                                        'w płaskim terenie')
ts147 = TrainingSession.objects.create(week=4, day=7, details='1 godz. w strefie 2 w terenie pagórkowatym; na'
                                        'szczytach dojdź do strefy 3')
ts151 = TrainingSession.objects.create(week=5, day=1, details='30 minut w strefie 2 z 10 minutami szybkiego pedałowania'
                                        ' w płaskim terenie')
ts152 = TrainingSession.objects.create(week=5, day=2, details='45 minut w strefie 2 z 10 minutami ćwiczenia tempa')
ts153 = TrainingSession.objects.create(week=5, day=3, details='1 godzina w strefie 2 ze stałą kadencją 80-85 obr./min')
ts154 = TrainingSession.objects.create(week=5, day=4, details='45 minut w strefie 2 z 5 minutami szybkiego pedałowania'
                                       'w płaskim terenie')
ts155 = TrainingSession.objects.create(week=5, day=5, details='Dzień wolny')
ts156 = TrainingSession.objects.create(week=5, day=6, details='1 godzina w strefie 2 z 10 minutami szybkiego pedałowania'
                                        'w płaskim terenie')
ts157 = TrainingSession.objects.create(week=5, day=7, details='1,5 godz. w strefie 2 z 15 minutami ćwiczenia tempa')
ts161 = TrainingSession.objects.create(week=6, day=1, details='30 minut w strefie 2 z 10 minutami szybkiego pedałowania'
                                        ' w płaskim terenie')
ts162 = TrainingSession.objects.create(week=6, day=2, details='45 minut w strefie 2 z 10 minutami ćwiczenia tempa')
ts163 = TrainingSession.objects.create(week=6, day=3, details='1 godzina w strefie 2 ze stałą kadencją 80-85 obr./min')
ts164 = TrainingSession.objects.create(week=6, day=4, details='45 minut w strefie 2 z 5 minutami szybkiego pedałowania'
                                       'w płaskim terenie')
ts165 = TrainingSession.objects.create(week=6, day=5, details='Dzień wolny')
ts166 = TrainingSession.objects.create(week=6, day=6, details='1 godzina w strefie 2 z 10 minutami szybkiego pedałowania'
                                        'w płaskim terenie')
ts167 = TrainingSession.objects.create(week=6, day=7, details='1,5 godz. w strefie 2 z 20 minutami ćwiczenia tempa')
ts171 = TrainingSession.objects.create(week=7, day=1, details='30 minut w strefie 2 z 10 minutami szybkiego pedałowania'
                                                              ' w płaskim terenie')
ts172 = TrainingSession.objects.create(week=7, day=2, details='45 minut w strefie 2 z 10 minutami ćwiczenia tempa')
ts173 = TrainingSession.objects.create(week=7, day=3, details='1 godzina w strefie 2 ze stałą kadencją 80-85 obr./min')
ts174 = TrainingSession.objects.create(week=7, day=4, details='45 minut w strefie 2 z 5 minutami szybkiego pedałowania'
                                       'w płaskim terenie')
ts175 = TrainingSession.objects.create(week=7, day=5, details='Dzień wolny')
ts176 = TrainingSession.objects.create(week=7, day=6, details='1 godzina w strefie 2 z 10 minutami szybkiego pedałowania '
                                        'w płaskim terenie')
ts177 = TrainingSession.objects.create(week=7, day=7, details='1,5 godz. w strefie 2 z 30 minutami ćwiczenia tempa')


ts111.plans.add(p1)
ts112.plans.add(p1)
ts113.plans.add(p1)
ts114.plans.add(p1)
ts115.plans.add(p1)
ts116.plans.add(p1)
ts117.plans.add(p1)

ts121.plans.add(p1)
ts122.plans.add(p1)
ts123.plans.add(p1)
ts124.plans.add(p1)
ts125.plans.add(p1)
ts126.plans.add(p1)
ts127.plans.add(p1)

ts131.plans.add(p1)
ts132.plans.add(p1)
ts133.plans.add(p1)
ts134.plans.add(p1)
ts135.plans.add(p1)
ts136.plans.add(p1)
ts137.plans.add(p1)

ts141.plans.add(p1)
ts142.plans.add(p1)
ts143.plans.add(p1)
ts144.plans.add(p1)
ts145.plans.add(p1)
ts146.plans.add(p1)
ts147.plans.add(p1)

ts151.plans.add(p1)
ts152.plans.add(p1)
ts153.plans.add(p1)
ts154.plans.add(p1)
ts155.plans.add(p1)
ts156.plans.add(p1)
ts157.plans.add(p1)

ts161.plans.add(p1)
ts162.plans.add(p1)
ts163.plans.add(p1)
ts164.plans.add(p1)
ts165.plans.add(p1)
ts166.plans.add(p1)
ts167.plans.add(p1)

ts171.plans.add(p1)
ts172.plans.add(p1)
ts173.plans.add(p1)
ts174.plans.add(p1)
ts175.plans.add(p1)
ts176.plans.add(p1)
ts177.plans.add(p1)

ts211 = TrainingSession.objects.create(week=1, day=1, details='Dzień wolny')
ts212 = TrainingSession.objects.create(week=1, day=2, details='1 godzina w strefie 2 z 10 minutami ćwiczenia tempa '
                                                              'w płaskimmterenie')
ts213 = TrainingSession.objects.create(week=1, day=3, details='30 minut w strefie 1 jazda odpoczynkowa')
ts214 = TrainingSession.objects.create(week=1, day=4, details='1 godzina w strefie 2 z 10 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts215 = TrainingSession.objects.create(week=1, day=5, details='45 minut w strefie 2 z 10 minutami ćwiczenia szybkiego '
                                                              'pedałowania w płaskim terenie')
ts216 = TrainingSession.objects.create(week=1, day=6, details='1 godzina w strefie 2 z 15 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts217 = TrainingSession.objects.create(week=1, day=7, details='1,5 godz. w strefie 2 z 20 minutami ćwiczenia tempa '
                                                              'w terenie pagórkowatym')
ts221 = TrainingSession.objects.create(week=2, day=1, details='Dzień wolny')
ts222 = TrainingSession.objects.create(week=2, day=2, details='1 godzina w strefie 2 z 15 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts223 = TrainingSession.objects.create(week=2, day=3, details='30 minut w strefie 1 jazda odpoczynkowa')
ts224 = TrainingSession.objects.create(week=2, day=4, details='1 godzina w strefie 2 z 10 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts225 = TrainingSession.objects.create(week=2, day=5, details='45 minut w strefie 2 z 10 minutami ćwiczenia szybkiego '
                                                              'pedałowania w płaskim terenie')
ts226 = TrainingSession.objects.create(week=2, day=6, details='1 godzina w strefie 2 z 15 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts227 = TrainingSession.objects.create(week=2, day=7, details='1,5 godz. w strefie 2 z 25 minutami ćwiczenia tempa '
                                                              'w terenie pagórkowatym')
ts231 = TrainingSession.objects.create(week=3, day=1, details='Dzień wolny')
ts232 = TrainingSession.objects.create(week=3, day=2, details='1 godzina w strefie 2 z 20 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts233 = TrainingSession.objects.create(week=3, day=3, details='30 minut w strefie 1 jazda odpoczynkowa')
ts234 = TrainingSession.objects.create(week=3, day=4, details='1 godzina w strefie 2 z 15 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts235 = TrainingSession.objects.create(week=3, day=5, details='45 minut w strefie 2 z 10 minutami ćwiczenia szybkiego '
                                                              'pedałowania w płaskim terenie')
ts236 = TrainingSession.objects.create(week=3, day=6, details='1 godzina w strefie 2 z 15 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts237 = TrainingSession.objects.create(week=3, day=7, details='1,5 godz. w strefie 2 z 30 minutami ćwiczenia tempa '
                                                              'w terenie pagórkowatym')
ts241 = TrainingSession.objects.create(week=4, day=1, details='Dzień wolny')
ts242 = TrainingSession.objects.create(week=4, day=2, details='30 minut w strefie 1 jazda odpoczynkowa')
ts243 = TrainingSession.objects.create(week=4, day=3, details='30 minut w strefie 1 jazda odpoczynkowa')
ts244 = TrainingSession.objects.create(week=4, day=4, details='30 minut w strefie 1 jazda odpoczynkowa')
ts245 = TrainingSession.objects.create(week=4, day=5, details='1 godzina w strefie 2 z 3 płaskimi sprintami po'
                                                              '10 sekund, między nimi po 10 minut jazdy odpoczynkowej')
ts246 = TrainingSession.objects.create(week=4, day=6, details='1 godzina w strefie 2 z 15 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts247 = TrainingSession.objects.create(week=4, day=7, details='1,5 godz. w strefie 2 z 30 minutami ćwiczenia tempa '
                                                              'w terenie pagórkowatym')
ts251 = TrainingSession.objects.create(week=5, day=1, details='Dzień wolny')
ts252 = TrainingSession.objects.create(week=5, day=2, details='1 godzina w strefie 2 z 30 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts253 = TrainingSession.objects.create(week=5, day=3, details='30 minut w strefie 1 jazda odpoczynkowa')
ts254 = TrainingSession.objects.create(week=5, day=4, details='1 godzina w strefie 2 z 20 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts255 = TrainingSession.objects.create(week=5, day=5, details='45 minut w strefie 2 z 10 minutami ćwiczenia szybkiego '
                                                              'pedałowania w płaskim terenie')
ts256 = TrainingSession.objects.create(week=5, day=6, details='1 godzina w strefie 2 z 20 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts257 = TrainingSession.objects.create(week=5, day=7, details='1,5 godz. w strefie 2 z 40 minutami ćwiczenia tempa '
                                                              'w terenie pagórkowatym')
ts261 = TrainingSession.objects.create(week=6, day=1, details='Dzień wolny')
ts262 = TrainingSession.objects.create(week=6, day=2, details='1 godzina w strefie 2 z 30 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts263 = TrainingSession.objects.create(week=6, day=3, details='30 minut w strefie 1 jazda odpoczynkowa')
ts264 = TrainingSession.objects.create(week=6, day=4, details='1 godzina w strefie 2 z 20 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts265 = TrainingSession.objects.create(week=6, day=5, details='45 minut w strefie 2 z 10 minutami ćwiczenia szybkiego '
                                                              'pedałowania w płaskim terenie')
ts266 = TrainingSession.objects.create(week=6, day=6, details='1 godzina w strefie 2 z 20 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts267 = TrainingSession.objects.create(week=6, day=7, details='1,5 godz. w strefie 2 z 50 minutami ćwiczenia tempa '
                                                              'w terenie pagórkowatym')
ts271 = TrainingSession.objects.create(week=7, day=1, details='Dzień wolny')
ts272 = TrainingSession.objects.create(week=7, day=2, details='1 godzina w strefie 2 z 30 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts273 = TrainingSession.objects.create(week=7, day=3, details='30 minut w strefie 1 jazda odpoczynkowa')
ts274 = TrainingSession.objects.create(week=7, day=4, details='1 godzina w strefie 2 z 20 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts275 = TrainingSession.objects.create(week=7, day=5, details='45 minut w strefie 2 z 10 minutami ćwiczenia szybkiego '
                                                              'pedałowania w płaskim terenie')
ts276 = TrainingSession.objects.create(week=7, day=6, details='1 godzina w strefie 2 z 20 minutami ćwiczenia tempa '
                                                              'w płaskim terenie')
ts277 = TrainingSession.objects.create(week=7, day=7, details='1,5 godz. w strefie 2 z 60 minutami ćwiczenia tempa '
                                                              'w terenie pagórkowatym')

ts211.plans.add(p2)
ts212.plans.add(p2)
ts213.plans.add(p2)
ts214.plans.add(p2)
ts215.plans.add(p2)
ts216.plans.add(p2)
ts217.plans.add(p2)

ts221.plans.add(p2)
ts222.plans.add(p2)
ts223.plans.add(p2)
ts224.plans.add(p2)
ts225.plans.add(p2)
ts226.plans.add(p2)
ts227.plans.add(p2)

ts231.plans.add(p2)
ts232.plans.add(p2)
ts233.plans.add(p2)
ts234.plans.add(p2)
ts235.plans.add(p2)
ts236.plans.add(p2)
ts237.plans.add(p2)

ts241.plans.add(p2)
ts242.plans.add(p2)
ts243.plans.add(p2)
ts244.plans.add(p2)
ts245.plans.add(p2)
ts246.plans.add(p2)
ts247.plans.add(p2)

ts251.plans.add(p2)
ts252.plans.add(p2)
ts253.plans.add(p2)
ts254.plans.add(p2)
ts255.plans.add(p2)
ts256.plans.add(p2)
ts257.plans.add(p2)

ts261.plans.add(p2)
ts262.plans.add(p2)
ts263.plans.add(p2)
ts264.plans.add(p2)
ts265.plans.add(p2)
ts266.plans.add(p2)
ts267.plans.add(p2)

ts271.plans.add(p2)
ts272.plans.add(p2)
ts273.plans.add(p2)
ts274.plans.add(p2)
ts275.plans.add(p2)
ts276.plans.add(p2)
ts277.plans.add(p2)

ts311 = TrainingSession.objects.create(week=1, day=1, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts312 = TrainingSession.objects.create(week=1, day=2, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts313 = TrainingSession.objects.create(week=1, day=3, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts314 = TrainingSession.objects.create(week=1, day=4, details='2 godziny w strefie 2 z 3 interwałami wysiłkowymi po 3'
                                                              ' minuty, między nimi po 3 minuty jazdy odpoczynkowej')
ts315 = TrainingSession.objects.create(week=1, day=5, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts316 = TrainingSession.objects.create(week=1, day=6, details='2 godziny grupowej jazdy w szybkim tempie po'
                                                              ' zróżnicowanym terenie; ciągłe zmiany tępa')
ts317 = TrainingSession.objects.create(week=1, day=7, details='2 godziny grupowej jazdy w terenie pagórkowatym, w'
                                                              ' strefie 2 i 3, w tempie łatwym do średniego')
ts321 = TrainingSession.objects.create(week=2, day=1, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts322 = TrainingSession.objects.create(week=2, day=2, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts323 = TrainingSession.objects.create(week=2, day=3, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts324 = TrainingSession.objects.create(week=2, day=4, details='2 godziny w strefie 2 z 3 interwałami wysiłkowymi po 3'
                                                              ' minuty, między nimi po 3 minuty jazdy odpoczynkowej')
ts325 = TrainingSession.objects.create(week=2, day=5, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts326 = TrainingSession.objects.create(week=2, day=6, details='2 godziny grupowej jazdy w szybkim tempie po'
                                                              ' zróżnicowanym terenie; ciągłe zmiany tępa')
ts327 = TrainingSession.objects.create(week=2, day=7, details='2,5 godz grupowej jazdy w terenie pagórkowatym, w'
                                                              ' strefie 2 i 3, w tempie łatwym do średniego')
ts331 = TrainingSession.objects.create(week=3, day=1, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts332 = TrainingSession.objects.create(week=3, day=2, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts333 = TrainingSession.objects.create(week=3, day=3, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts334 = TrainingSession.objects.create(week=3, day=4, details='2 godziny w strefie 2 z 3 interwałami wysiłkowymi po 3'
                                                              ' minuty, między nimi po 3 minuty jazdy odpoczynkowej')
ts335 = TrainingSession.objects.create(week=3, day=5, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts336 = TrainingSession.objects.create(week=3, day=6, details='2 godziny grupowej jazdy w szybkim tempie po'
                                                              ' zróżnicowanym terenie; ciągłe zmiany tępa')
ts337 = TrainingSession.objects.create(week=3, day=7, details='3 godz grupowej jazdy w terenie pagórkowatym, w'
                                                              ' strefie 2 i 3, w tempie łatwym do średniego')
ts341 = TrainingSession.objects.create(week=4, day=1, details='30-45 minut w strefie 1; jazda odpoczynkowa')
ts342 = TrainingSession.objects.create(week=4, day=2, details='30-45 minut w strefie 1; jazda odpoczynkowa')
ts343 = TrainingSession.objects.create(week=4, day=3, details='dzień wolny')
ts344 = TrainingSession.objects.create(week=4, day=4, details='30-45 minut w strefie 1; jazda odpoczynkowa')
ts345 = TrainingSession.objects.create(week=4, day=5, details='60 minut w strefie 2 z 4 płaskimi sprintami po 10 sekund'
                                                              'między nimi po 5-10 minut jazdy aż do pełnej '
                                                              'regeneracji')
ts346 = TrainingSession.objects.create(week=4, day=6, details='2 godziny grupowej jazdy w szybkim tempie po'
                                                              ' zróżnicowanym terenie; ciągłe zmiany tępa')
ts347 = TrainingSession.objects.create(week=4, day=7, details='2,5 godz grupowej jazdy w terenie pagórkowatym, w'
                                                              ' strefie 2 i 3, w tempie łatwym do średniego')
ts351 = TrainingSession.objects.create(week=5, day=1, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts352 = TrainingSession.objects.create(week=5, day=2, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts353 = TrainingSession.objects.create(week=5, day=3, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts354 = TrainingSession.objects.create(week=5, day=4, details='2 godziny w strefie 2 z 3 interwałami wysiłkowymi po 3'
                                                              ' minuty, między nimi po 3 minuty jazdy odpoczynkowej')
ts355 = TrainingSession.objects.create(week=5, day=5, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts356 = TrainingSession.objects.create(week=5, day=6, details='2 godziny grupowej jazdy w szybkim tempie po'
                                                              ' zróżnicowanym terenie; ciągłe zmiany tępa')
ts357 = TrainingSession.objects.create(week=5, day=7, details='2,5 godz grupowej jazdy w terenie pagórkowatym, w'
                                                              ' strefie 2 i 3, w tempie łatwym do średniego')
ts361 = TrainingSession.objects.create(week=6, day=1, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts362 = TrainingSession.objects.create(week=6, day=2, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts363 = TrainingSession.objects.create(week=6, day=3, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts364 = TrainingSession.objects.create(week=6, day=4, details='2 godziny w strefie 2 z 3 interwałami wysiłkowymi po 3'
                                                              ' minuty, między nimi po 3 minuty jazdy odpoczynkowej')
ts365 = TrainingSession.objects.create(week=6, day=5, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts366 = TrainingSession.objects.create(week=6, day=6, details='2 godziny grupowej jazdy w szybkim tempie po'
                                                              ' zróżnicowanym terenie; ciągłe zmiany tępa')
ts367 = TrainingSession.objects.create(week=6, day=7, details='3 godz grupowej jazdy w terenie pagórkowatym, w'
                                                              ' strefie 2 i 3, w tempie łatwym do średniego')
ts371 = TrainingSession.objects.create(week=7, day=1, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts372 = TrainingSession.objects.create(week=7, day=2, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts373 = TrainingSession.objects.create(week=7, day=3, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts374 = TrainingSession.objects.create(week=7, day=4, details='2 godziny w strefie 2 z 3 interwałami wysiłkowymi po 3'
                                                              ' minuty, między nimi po 3 minuty jazdy odpoczynkowej')
ts375 = TrainingSession.objects.create(week=7, day=5, details='30-45 minut w strefie 1 stałego, spokojnego kręcenia'
                                                              'w płaskim terenie')
ts376 = TrainingSession.objects.create(week=7, day=6, details='2 godziny grupowej jazdy w szybkim tempie po'
                                                              ' zróżnicowanym terenie; ciągłe zmiany tępa')
ts377 = TrainingSession.objects.create(week=7, day=7, details='3,5 godz grupowej jazdy w terenie pagórkowatym, w'
                                                              ' strefie 2 i 3, w tempie łatwym do średniego')

ts311.plans.add(p3)
ts312.plans.add(p3)
ts313.plans.add(p3)
ts314.plans.add(p3)
ts315.plans.add(p3)
ts316.plans.add(p3)
ts317.plans.add(p3)

ts321.plans.add(p3)
ts322.plans.add(p3)
ts323.plans.add(p3)
ts324.plans.add(p3)
ts325.plans.add(p3)
ts326.plans.add(p3)
ts327.plans.add(p3)

ts331.plans.add(p3)
ts332.plans.add(p3)
ts333.plans.add(p3)
ts334.plans.add(p3)
ts335.plans.add(p3)
ts336.plans.add(p3)
ts337.plans.add(p3)

ts341.plans.add(p3)
ts342.plans.add(p3)
ts343.plans.add(p3)
ts344.plans.add(p3)
ts345.plans.add(p3)
ts346.plans.add(p3)
ts347.plans.add(p3)

ts351.plans.add(p3)
ts352.plans.add(p3)
ts353.plans.add(p3)
ts354.plans.add(p3)
ts355.plans.add(p3)
ts356.plans.add(p3)
ts357.plans.add(p3)

ts361.plans.add(p3)
ts362.plans.add(p3)
ts363.plans.add(p3)
ts364.plans.add(p3)
ts365.plans.add(p3)
ts366.plans.add(p3)
ts367.plans.add(p3)

ts371.plans.add(p3)
ts372.plans.add(p3)
ts373.plans.add(p3)
ts374.plans.add(p3)
ts375.plans.add(p3)
ts376.plans.add(p3)
ts377.plans.add(p3)