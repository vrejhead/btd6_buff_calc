from tkinter import *
from tkinter import ttk
root = Tk()
root.title('bee tee dee six')
root.geometry('480x230')
#holy shit so bad lmfao
multiplier = {'damage':0, 'pierce':0, 'speed':1}
def update(type, change):
    global multiplier
    stats = allvar[type][change].get().split()
    multiplier['damage'] += float(stats[0])
    if '%' in stats[1]:
        multiplier['pierce'] += towerstat['pierce'].get() * (float(stats[1][:-1])/100)
    else: multiplier['pierce'] += float(stats[1])
    multiplier['speed'] *= float(stats[2])
    damage.config(text=f'{round(multiplier["damage"]) + towerstat["damage"].get()}')
    pierce.config(text=f'{round(multiplier["pierce"] + towerstat["pierce"].get(), 4)}')
    speed.config(text=f'{round(multiplier["speed"] * towerstat["speed"].get(), 4)}')
    speedalt.config(text=f'{round(1 / float(speed["text"]), 4)}')
    singletarget.config(text=round(float(speedalt['text']) * float(damage['text']), 4))
#variables
towerstat = {'damage':DoubleVar(), 'pierce':DoubleVar(), 'speed':DoubleVar()}
allvar = {
'normalbuff': {'pbruh':StringVar(), 'amd':StringVar(), 'temple':StringVar(), 'tsg':StringVar(), 'drums':StringVar(), 'homeland':StringVar(), 'oc':StringVar(), 'uboost':StringVar(), 'mboost':StringVar()},
'towerbuff': {'flagshit':StringVar(), 'shonob':StringVar(), 'pooplust':StringVar(), 'pmfc':StringVar(), 'tt5':StringVar()},
'debuff': {'sbruh':StringVar(), 'cripple':StringVar(), 'embrit':StringVar(), 'glorm':StringVar()},
'herobuff': {'gwen':StringVar(), 'pat':StringVar(), 'elizi':StringVar()},
}
for item in allvar:
    for iter in allvar[item]:
        allvar[item][iter].set('0 0 0')
#outputs
Label(root, text='damage: ', font=('Arial', 12)).grid(column=5, row=5)
Label(root, text='pierce: ', font=('Arial', 12)).grid(column=5, row=6)
Label(root, text='speed: ', font=('Arial', 12)).grid(column=5, row=7)
Label(root, text='atk per s:', font=('Arial', 12)).grid(column=5, row=8)
Label(root, text='single target:', font=('Arial', 12)).grid(column=5, row=9)
damage = Label(root, text='None', font=('Arial', 12))
pierce = Label(root, text='None', font=('Arial', 12))
speed = Label(root, text='None', font=('Arial', 12))
speedalt = Label(root, text='None', font=('Arial', 12))
singletarget = Label(root, text='None', font=('Arial', 12))
damage.grid(column=6, row=5)
pierce.grid(column=6, row=6)
speed.grid(column=6, row=7)
speedalt.grid(column=6, row=8)
singletarget.grid(column=6, row=9)
#label
Label(root, text='|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|').grid(column=4, row=1, rowspan=9)
Label(root, text='damage:', font=('Arial', 12)).grid(column=5, row=1)
Label(root, text='pierce:', font=('Arial', 12)).grid(column=5, row=2)
Label(root, text='speed:', font=('Arial', 12)).grid(column=5, row=3)
#entry
Entry(root, width=10, textvariable=towerstat['damage'], font=('Arial', 12)).grid(column=6, row=1)
Entry(root, width=10, textvariable=towerstat['pierce'], font=('Arial', 12)).grid(column=6, row=2)
Entry(root, width=10, textvariable=towerstat['speed'], font=('Arial', 12)).grid(column=6, row=3)
#checkboxes
#ordered in [damage, pierce, speed]
Checkbutton(root, text='pbruh no amd', variable=allvar['normalbuff']['pbruh'], onvalue='1 3 0.85', offvalue='-1 -3 1.1764705882352942', command=lambda: update('normalbuff', 'pbruh')).grid(row=1, column=1, sticky=W)
Checkbutton(root, text='amd only', variable=allvar['normalbuff']['amd'], onvalue='1 0 1', offvalue='-1 0 1', command=lambda: update('normalbuff', 'amd')).grid(row=2, column=1, sticky=W)
Checkbutton(root, text='t4 temple only', variable=allvar['normalbuff']['temple'], onvalue='2 3 0.81', offvalue='-2 -3 1.2345679012345678', command=lambda: update('normalbuff', 'temple')).grid(row=3, column=1, sticky=W)
Checkbutton(root, text='t5 temple only', variable=allvar['normalbuff']['tsg'], onvalue='2 3 0.81', offvalue='-2 -3 1.2345679012345678', command=lambda: update('normalbuff', 'tsg')).grid(row=4, column=1, sticky=W)
Checkbutton(root, text='bongos', variable=allvar['normalbuff']['drums'], onvalue='0 0 0.85', offvalue='0 0 1.1764705882352942', command=lambda: update('normalbuff', 'drums')).grid(row=5, column=1, sticky=W)
Checkbutton(root, text='homeland', variable=allvar['normalbuff']['homeland'], onvalue='0 200% 0.50', offvalue='0 0 2', command=lambda: update('normalbuff', 'homeland')).grid(row=6, column=1, sticky=W)
Checkbutton(root, text='oc', variable=allvar['normalbuff']['oc'], onvalue='0 0 0.60', offvalue='0 0 1.6666666666666667', command=lambda: update('normalbuff', 'oc')).grid(row=7, column=1, sticky=W)
Checkbutton(root, text='10 ub stacks', variable=allvar['normalbuff']['uboost'], onvalue='0 0 0.60', offvalue='0 0 1.6666666666666667', command=lambda: update('normalbuff', 'uboost')).grid(row=8, column=1, sticky=W)
Checkbutton(root, text='mboost(power)', variable=allvar['normalbuff']['mboost'], onvalue='0 0 0.50', offvalue='0 0 2', command=lambda: update('normalbuff', 'mboost')).grid(row=9, column=1, sticky=W)
#-------------------------------------------------------------------------------------------------------------------------------
Checkbutton(root, text='flagcrap', variable=allvar['towerbuff']['flagshit'], onvalue='0 0 0.85', offvalue='0 0 1.1764705882352942', command=lambda: update('towerbuff', 'flagshit')).grid(row=1, column=2, sticky=W)
Checkbutton(root, text='20x shonob', variable=allvar['towerbuff']['shonob'], onvalue='0 160% 0.1886933291627967', offvalue='0 -160% 5.299604413345433', command=lambda: update('towerbuff', 'shonob')).grid(row=2, column=2, sticky=W)
Checkbutton(root, text='5x pooplust', variable=allvar['towerbuff']['pooplust'], onvalue='0 175% 0.5714285714285714', offvalue='0 -175% 1.75', command=lambda: update('towerbuff', 'pooplust')).grid(row=3, column=2, sticky=W)
Checkbutton(root, text='pmfc', variable=allvar['towerbuff']['pmfc'], onvalue='1 3 0.0316', offvalue='-1 -3 31.645569620253163', command=lambda: update('towerbuff', 'pmfc')).grid(row=4, column=2, sticky=W)
#-------------------------------------------------------------------------------------------------------------------------------
Checkbutton(root, text='sbruh', variable=allvar['debuff']['sbruh'], onvalue='4 0 1', offvalue='-4 0 1', command=lambda: update('debuff', 'sbruh')).grid(row=6, column=2, sticky=W)
Checkbutton(root, text='embrit', variable=allvar['debuff']['embrit'], onvalue='1 0 1', offvalue='-1 0 1', command=lambda: update('debuff', 'embrit')).grid(row=7, column=2, sticky=W)
Checkbutton(root, text='cripple', variable=allvar['debuff']['cripple'], onvalue='5 0 1', offvalue='-5 0 1', command=lambda: update('debuff', 'cripple')).grid(row=8, column=2, sticky=W)
Checkbutton(root, text='glorm', variable=allvar['debuff']['glorm'], onvalue='2 0 1', offvalue='-2 0 1', command=lambda: update('debuff', 'glorm')).grid(row=9, column=2, sticky=W)
#-------------------------------------------------------------------------------------------------------------------------------
Checkbutton(root, text='gwen', variable=allvar['herobuff']['gwen'], onvalue='1 1 1', offvalue='-1 -1 1', command=lambda: update('herobuff', 'gwen')).grid(row=1, column=3, sticky=W)
Checkbutton(root, text='pat', variable=allvar['herobuff']['pat'], onvalue='3 0 1', offvalue='-3 0 1', command=lambda: update('herobuff', 'pat')).grid(row=2, column=3, sticky=W)
Checkbutton(root, text='elizi', variable=allvar['herobuff']['elizi'], onvalue='0 1 0.85', offvalue='0 -1 1.1764705882352942', command=lambda: update('herobuff', 'elizi')).grid(row=3, column=3, sticky=W)
#-------------------------------------------------------------------------------------------------------------------------------

root.mainloop()
