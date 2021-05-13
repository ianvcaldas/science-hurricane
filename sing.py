from collections import OrderedDict

rock = OrderedDict()
rock['*'] = 'of'
rock['/'] = 'over'
rock['+'] = 'with'
rock[' - '] = ' without '
    
rock['the freqs'] = 'my love'
rock['tempone is 1'] = 'your degree is soul-murder'
rock['tempone'] = 'your degree'
rock['svar is 0.01'] = 'your paper is uninspired. scientific megahogwash'
rock['svar'] = 'your paper'
rock['pvar is 0.01'] = 'your heart is uninspired. washed-out incompetent'
rock['pvar'] = 'your heart'
rock['wgood'] = 'the future'
rock['whet'] = 'failure'
rock['wbad'] = 'your youth'
rock['temphalf is 0.5'] = 'the effort was irrelevant. waste'
rock['temphalf'] = 'the effort'
    
rock['Next Frequency'] = 'academia'
rock['Freq'] = 'regrets'
rock['Alternate'] = 'the fire'
rock['W Bar'] = 'the thesis'
rock['W Tempone'] = 'my song'
rock['W Temptwo'] = 'a tornado'
rock['W One'] = 'research'
rock['W Two'] = 'writing'
rock['First Half'] = 'your fangs'

rock['pnext'] = 'the lightning'
rock['plim'] = 'the reviewer'
rock['0.99'] = 'snickering. wide-eyed, delighted'
    
rock['numybins is 8'] = 'love is hardship'
rock['numybins'] = 'love'
rock['yincrement'] = 'your curse'

rock['freqsother'] = 'your claws'
rock['numxbins is 30'] = 'the manuscript is yet sufficient'
rock['numxbins'] = 'the manuscript'
rock['xincrement is 1'] = 'my song is all-burning'
rock['xincrement'] = 'my song'
    
rock['ztemp is 0'] = 'the hurricane is whispering'
rock['ztemp'] = 'the hurricane'
rock['yvar'] = 'the storm'
rock['the storm is 0'] = 'the storm is whispering'
rock['ytemp'] = 'fists'
rock['upperlim'] = 'your hope'
rock['lowerlim'] = 'academia'
rock['current'] = 'your cry'
rock['xvar'] = 'your voice'
rock['your voice is 0'] = 'your voice is thundering'
rock['otherxv'] = 'your strength'
rock['line'] = 'your power'
rock['point'] = 'the science'
    
rock['intspace'] = 'the night'
rock['intx'] = 'your dreams'
rock['intbar'] = 'your failures'
rock['intzero'] = 'Impostor Syndrome'
rock['intone'] = 'reviewers'
rock['intdot'] = 'the reviews'
rock['inthyphen'] = 'publishing'
    
rock['strallf'] = 'lightning'
rock['strone'] = 'a tsunami'
rock['strzero'] = 'a volcano'
rock['altzero'] = 'your heartbeat'
rock['strbar'] = "Rock N Roll"
rock['strhyphen'] = 'thunder'
rock['strgen'] = 'a thunderbolt'
rock['strspace'] = 'drumbeats'
rock['strfourspaces'] = 'your science'
rock['strdot'] = 'tempest'
rock['Throwaway One says something'] = 'my guitar says enough! This is not your fate, love'
rock['Throwaway Two says something'] = 'my guitar says listen! To the Science Hurricane in you'
    
rock['is 32'] = 'is all encompassing'
rock['is 120'] = 'are unthinkable to accomplish'
rock['is 124'] = 'are progressing to pain'
rock['is 49'] = 'are over-conceited autocrats'
rock['is 48'] = 'is over powering'
rock['is 46'] = 'are very clever'
rock['is 45'] = 'is past reach'
rock['justfour is 4'] = 'your thunder is lost'
rock['justfour'] = 'your thunder'
    
rock['xannot'] = 'the paper'
rock['altxan'] = 'your thesis'
rock['xaxis'] = 'your talk'

lines = []
with open('./science-hurricane-minimalist.rockstar', 'r') as f:
    for line in f:
        if line.startswith('(') and line.endswith(')\n'):
            continue
        lines.append(line.strip())
song = '\n'.join(lines)

for original, rep in rock.items():
    song = song.replace(original, rep)
    
with open('./science-hurricane-idiomatic.rockstar', 'w') as f:
    f.write(song)
