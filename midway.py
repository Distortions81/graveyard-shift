"""Map 2: Midway Massacre. Original art and classic DOOM geometry."""
from dataclasses import replace


def art(api):
    Image,ImageDraw=api.Image,api.ImageDraw
    out={}
    for key,lines,width in [
        ('GSHOOT',['UAC SKILL ASSESSMENT','AIM HIGH. WIN LOW.'],256),
        ('GBUMP',['COLLISION DEPARTMENT','PLEASE BUMP RESPONSIBLY'],256),
        ('GPRIZES',['PRIZE REDEMPTION','EXPECTATIONS ARE NOT REFUNDABLE'],256),
        ('GQUOTA',["TODAY'S QUOTA",'YESTERDAY + 1'],128),
        ('GREFUND',['CREDIT ISSUED','IN REGRET'],128),
        ('GBPASS',['SKILL PASS','BLUE TOKEN','PLAY TO WORK'],256),
        ('GRPASS',['PRIZE PASS','RED TOKEN','NO CASH VALUE'],256),
        ('GNEXT',['TEAM BUILDING','GHOST TRAIN','NEXT SHIFT'],128)]:
        out[key]=api.sign(lines,(api.INK,api.CREAM),size=(width,128))
    for key,color in [('GBCRED',api.RED),('GBCBLUE',api.TEAL)]:
        im=Image.new('RGBA',(128,128),color);d=ImageDraw.Draw(im)
        d.rectangle((0,0,127,3),fill=api.CREAM)
        d.line((0,4,127,4),fill=api.GOLD,width=2)
        d.rectangle((0,84,127,127),fill=(22,24,27))
        for x in range(0,128,16):d.rectangle((x+3,91,x+10,116),fill=(43,45,47))
        for x in [14,108]:d.ellipse((x,10,x+10,16),fill=api.GOLD)
        out[key]=im
    im=Image.new('RGBA',(128,128),(25,29,35));d=ImageDraw.Draw(im)
    for y in range(0,128,16):d.line((0,y,127,y),fill=(59,65,68),width=2)
    out['GRUBBER']=im
    im=Image.new('RGBA',(128,128),api.TEAL);d=ImageDraw.Draw(im)
    d.rectangle((2,2,125,125),outline=api.GOLD,width=3)
    for x,y in [(21,42),(65,76),(102,40)]:
        d.ellipse((x-14,y,x+12,y+17),fill=api.CREAM)
        d.ellipse((x+2,y-12,x+15,y+2),fill=api.CREAM)
        d.polygon([(x+14,y-7),(x+23,y-3),(x+14,y)],fill=api.GOLD)
        d.point((x+10,y-7),fill=api.INK)
    api.centered(d,'PROMOTION TARGETS',105,10,api.CREAM,128,inset=14)
    out['GDUCK']=im
    for key,color in [('GBFLOOR',(39,57,62)),('GSEAT',(83,22,32)),('GELECT',(32,36,42))]:
        im=Image.new('RGBA',(64,64),color);d=ImageDraw.Draw(im)
        for n in range(0,64,16):
            d.line((0,n,63,n),fill=(65,68,67));d.line((n,0,n,63),fill=(65,68,67))
        if key=='GELECT':d.rectangle((24,24,39,39),fill=api.CREAM,outline=api.GOLD,width=2)
        out[key]=im
    return out


def make_level(api):
    S=api.Style
    l=api.Level('E1M2','Midway Massacre')
    street=S('midway promenade',ceil=320,flat='GPLANK',wall='GFACADE',light=176)
    entry=replace(street,label='midway arrival',wall='GBRICK',flat='GASPHALT',light=160)
    gallery=S('skill assessment gallery',ceil=144,roof='GROOF',flat='GCHECK',wall='GTEAL',light=192)
    service=S('gallery service court',ceil=320,flat='GASPHALT',wall='GBRICK',light=160)
    arena=S('collision arena',floor=-16,ceil=192,roof='GELECT',flat='GBFLOOR',wall='GMETAL',light=192)
    prize=S('prize redemption hall',ceil=160,roof='GROOF',flat='GVELVET',wall='GWOOD',light=192)
    l.rect(4,-8,14,0,entry)
    l.rect(0,0,20,28,street)
    l.rect(-16,8,0,24,gallery)
    l.rect(-16,24,4,33,service)
    l.rect(20,0,46,22,arena)
    l.rect(8,28,34,40,prize)
    l.rect(26,22,34,28,replace(service,label='arena service return',wall='GMETAL'))
    # The public sides are visible through admission doors; no route bypasses keys.
    l.rect(20,0,21,22,replace(arena,label='arena frontage',floor=192))
    l.rect(20,8,21,12,S('blue midway gate',ceil=0,roof='GROOF',door=True,wall='GBPASS'))
    l.rect(8,27,20,28,replace(street,label='redemption counter',floor=144,wall='GBOOTH'))
    l.rect(12,27,16,28,S('red midway gate',ceil=0,roof='GROOF',door=True,wall='GRPASS'))
    l.rect(26,24,34,25,replace(service,label='return bulkhead',floor=128,ceil=128,roof='GROOF'))
    l.rect(28,24,32,25,S('red midway gate',ceil=0,roof='GROOF',door=True,wall='GRPASS'))
    for x in [19,21]:l.rect(x,8,x+1,12,replace(street,label='arena admission lintel',ceil=128,roof='GROOF',wall='GMETAL'))
    for y in [26,28]:l.rect(12,y,16,y+1,replace(prize,label='redemption lintel',ceil=128))
    for y in [23,25]:l.rect(26,y,34,y+1,replace(service,label='return lintel',ceil=128,roof='GROOF'))
    # Broad openings into the gallery, plus a small operator office on its return.
    l.rect(-1,8,0,24,replace(gallery,label='gallery facade',floor=144))
    l.rect(-1,10,0,14,S('gallery entrance manual door',ceil=0,roof='GROOF',door=True))
    l.rect(-1,19,0,22,S('gallery return manual door',ceil=0,roof='GROOF',door=True))
    l.rect(-16,24,0,25,replace(service,label='operator office wall',floor=128,ceil=128,roof='GROOF'))
    l.rect(0,28,4,29,S('service return manual door',ceil=0,roof='GROOF',door=True))
    l.rect(-14,24,-10,25,S('gallery manual door',ceil=0,roof='GROOF',door=True))
    for x in [2,15]:
        for y in [5,18]:
            l.rect(x,y,x+3,y+3,replace(street,label='rigged prize kiosk',floor=112,wall='GBOOTH',flat='GREDTOP'))
    l.rect(8,11,12,17,replace(street,label='quota monument',floor=80,wall='GPOLE',flat='GROOF'))
    for y in [3,10,17,24]:
        l.rect(6,y,8,y+1,replace(street,label='promenade light pools',light=224))
    # Shooting stalls have low counters, not tiny maze passages.
    for y in [10,15,20]:
        l.rect(-14,y,-11,y+2,replace(gallery,label='shooting counter',floor=48,flat='GPLANK',wall='GSTRIPE'))
    l.rect(-8,9,-7,23,replace(gallery,label='gallery aisle lights',light=224))
    for x,y in [(-15,29),(-5,27)]:
        l.rect(x,y,x+2,y+2,replace(service,label='service crates',floor=48,wall='GCRATE',flat='GPLANK'))
    # Eight rounded, rubber-rimmed bumper cars; generous lanes connect both sides.
    for i,(x,y) in enumerate([(25,5),(31,5),(39,5),(25,11),(35,11),(41,12),(28,18),(37,18)]):
        l.round_area(x,y,(x-1,y-1,x+1,y+1),[
            (60,arena),
            (48,replace(arena,label='bumper car rubber',floor=0,flat='GROOF',wall='GRUBBER',light=208)),
            (24,replace(arena,label='red bumper car' if i%2 else 'blue bumper car',floor=24,
                         flat='GREDTOP' if i%2 else 'GPLANK',wall='GBCRED' if i%2 else 'GBCBLUE',light=208)),
            (0,lambda wedge: replace(arena,label='bumper seat back' if wedge<4 else 'bumper seat cushion',floor=40 if wedge<4 else 24,flat='GSEAT',wall='GBCRED' if i%2 else 'GBCBLUE',light=208))],arena,sides=8)
    for x,y in [(23,2),(43,2),(23,19),(43,19)]:
        l.rect(x,y,x+1,y+1,replace(arena,label='arena roof support',floor=192,wall='GPOLE'))
    # Red token: a small raised control deck with ordinary 16-unit stairs.
    for i in range(3):
        l.rect(41+i,15,42+i,18,replace(arena,label=f'arena step {i+1}',floor=i*16,wall='GSTEP'))
    l.rect(44,14,46,20,replace(arena,label='collision control deck',floor=32,flat='GGRATE',wall='GMETAL',light=224))
    # Prize counters, back displays and a central aisle with two flanking routes.
    for x in [10,22]:
        l.rect(x,32,x+6,34,replace(prize,label='prize service counter',floor=48,flat='GPLANK',wall='GBOOTH'))
    l.rect(29,29,33,39,replace(prize,label='prize display plinth',floor=64,flat='GROOF',wall='GSTRIPE'))
    l.rect(16,35,19,38,replace(prize,label='executive prize stand',floor=32,wall='GPOLE',flat='GREDTOP'))
    # Secrets are rewards, not mandatory progression.
    l.rect(-23,18,-17,24,S('gallery prize cache',ceil=128,roof='GROOF',flat='GCHECK',wall='GWOOD',special=9,light=192))
    l.rect(-17,19,-16,22,S('target shutter',ceil=0,roof='GROOF',door=True,tag=40))
    l.rect(-12,34,-6,38,S('staff locker secret',ceil=128,roof='GROOF',flat='GGRATE',wall='GMETAL',special=9,light=176))
    l.rect(-10,33,-8,34,S('snack door',ceil=0,roof='GROOF',door=True))
    l.rect(47,4,52,9,S('credit office secret',ceil=128,roof='GROOF',flat='GCHECK',wall='GTEAL',special=9,light=176))
    l.rect(46,5,47,7,S('garden door',ceil=0,roof='GROOF',door=True))
    # Signs occupy existing wall faces. No coplanar or inset overlay geometry.
    for a,b,tex in [((10,-8),(8,-8),'GQUOTA'),((-16,16),(-16,18),'GDUCK'),
                    ((-12,8),(-16,8),'GSHOOT'),((4,30),(4,28),'GQUOTA'),
                    ((46,11),(46,7),'GBUMP'),((12,40),(16,40),'GPRIZES'),
                    ((24,40),(26,40),'GREFUND'),((34,38),(34,36),'GNEXT')]:
        l.sign(a,b,tex)
    l.sign((-16,12),(-16,14),'SW1GARG',46,40)
    l.sign((26,40),(28,40),'SW1EXIT',11,0)
    # Straightforward pistol start, with co-op/deathmatch starts also authored.
    for i,(x,y) in enumerate([(8,-6),(10,-6),(8,-7),(10,-7)],1):l.thing(x+.5,y+.5,i,angle=90)
    for x,y in [(7,3),(-5,16),(29,8),(20,37)]:l.thing(x+.5,y+.5,11)
    for x,y,t in [(8.5,3.5,2001),(9.5,4.5,2049),(6.5,3.5,2018),
                  (-12.5,28.5,5),(44.5,17.5,13),(-5.5,14.5,2008),
                  (-6.5,21.5,2012),(-12.5,30.5,2049),(-3.5,29.5,2011),
                  (17.5,25.5,2012),(22.5,9.5,2049),(32.5,3.5,2008),
                  (43.5,10.5,2012),(30.5,20.5,2049),(27.5,26.5,2011),
                  (18.5,29.5,2049),(9.5,37.5,2012),(26.5,37.5,2008),
                  (-20.5,20.5,2002),(-20.5,22.5,2048),(-8.5,36.5,2019),
                  (49.5,6.5,2012),(50.5,7.5,2049)]:l.thing(x,y,t)
    # Most later groups are ambush-flagged: firing at the entrance does not
    # summon the entire map. HMP counts grow with area, not density.
    groups=[
      [(5,1,3004),(12,3,3004),(4,12,3001),(14,14,3004),(6,22,3001),(14,24,9),(3,25,3004),(18,16,3001)],
      [(-4,11,3004),(-8,12,3001),(-13,13,3004),(-5,17,9),(-10,18,3001),(-14,22,3004),(-4,22,3001),(-9,9,3004),(-12,16,3001),(-8,20,3004)],
      [(-13,26,9),(-10,29,3001),(-4,27,3004),(-2,30,3001),(-14,30,3004),(-7,25,3004),(-6,30,3001),(-2,25,3004)],
      [(23,8,3004),(28,8,3001),(32,8,3004),(38,8,3001),(43,8,9),(23,14,3001),(29,14,3002),(33,16,3004),(38,15,3001),(43,13,3004),(25,20,3001),(32,20,9),(40,20,3004),(44,18,3001),(27,23,3004),(32,26,3001)],
      [(10,30,3004),(18,30,9),(26,30,3001),(10,35,3001),(20,35,3002),(25,35,3004),(13,38,3004),(21,38,3001),(27,38,3001),(9,39,3004),(20,32,3004),(28,36,9)]]
    for gi,group in enumerate(groups):
        for j,(x,y,t) in enumerate(group):
            flags=(7 if j%3 else 6)|(8 if gi else 0)
            l.thing(x+.5,y+.5,t,flags,angle=270 if gi in [2,4] else 180)
    # UV adds pressure at different heights; Easy removes one third of enemies.
    for x,y,t in [(12,9,3001),(-11,28,9),(34,12,3002),(41,20,9),(15,36,3001),(24,38,3001)]:l.thing(x+.5,y+.5,t,4|8)
    for x,y in [(-14.5,27.5),(-3.5,26.5),(24.5,2.5),(41.5,2.5)]:l.thing(x,y,2035)
    for x,y,t in [(4.5,-4.5,15),(-6.5,28.5,15),(45.5,21.5,15)]:l.thing(x,y,t)
    l.landmarks=dict(start=[544,-352],shotgun=[544,224],gallery=[-352,1056],blue_key=[-800,1824],
                     arena=[1760,800],red_key=[2848,1120],redemption=[1184,1888],exit=[1760,2528])
    # Closed sectors behind boundary posters split ONE wall at poster height.
    api.mount_wall_signs(l,covered=True)
    return l
