# Slices mascot_sheet_source.jpg (4x2 grid) into transparent 256px sprites in mascot/
from PIL import Image, ImageDraw
im=Image.open('mascot_sheet_source.jpg').convert('RGB');W,H=im.size
names=['neutral','cheer','jump','sad','think','surprised','sleep','trophy']
cw,ch=W//4,H//2;sheet=Image.new('RGBA',(4*270,2*270),(200,200,200,255))
def segs(occ):
    r=[];s=None
    for i,o in enumerate(occ+[0]):
        if o and s is None:s=i
        if not o and s is not None:r.append([s,i]);s=None
    return r
for k,n in enumerate(names):
    c=im.crop(((k%4)*cw,(k//4)*ch,(k%4+1)*cw,(k//4+1)*ch)).convert('RGBA');w,h=c.size;mark=(255,0,255,255)
    for p in [(x,y) for x in range(0,w,3) for y in (0,h-1)]+[(x,y) for y in range(0,h,3) for x in (0,w-1)]:
        if sum(c.getpixel(p)[:3])>690: ImageDraw.floodfill(c,p,mark,thresh=40)
    px=c.load()
    for y in range(h):
        for x in range(w):
            if px[x,y]==mark: px[x,y]=(0,0,0,0)
    # alpha: treat near-transparent fringe as empty when measuring
    a=c.getchannel('A').point(lambda v:255 if v>0 else 0)
    occ=[1 if a.crop((i,0,i+1,h)).getbbox() else 0 for i in range(w)]
    for s in segs(occ):  # drop neighbouring-figure slivers near the cell's sides
        if s[1]-s[0]<16 and (s[0]<40 or s[1]>w-40): c.paste((0,0,0,0),(s[0],0,s[1],h))
    s=c.crop(c.getbbox());m=max(s.size)+12
    sq=Image.new('RGBA',(m,m),(0,0,0,0));sq.paste(s,((m-s.size[0])//2,(m-s.size[1])//2))
    sq=sq.resize((256,256),Image.LANCZOS);sq.save(f'mascot/{n}.png',optimize=True)
    sheet.alpha_composite(sq,((k%4)*270+7,(k//4)*270+7))
sheet.save('_qa/sprites_contact.png')
