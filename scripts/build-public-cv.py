"""Build the public CV with the site's embedded typefaces and visual identity.

Requires reportlab. Fonts are Latin subsets converted from the installed
Fontsource packages; their SIL Open Font Licenses are included alongside them.
The static site build uses the committed PDF and does not require Python.
"""
import json
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public' / 'adam-riddick-cv.pdf'
DATA = json.loads((ROOT / 'scripts' / 'cv-content.json').read_text())
FONT_DIR = ROOT / 'scripts' / 'fonts'
FONTS = {'DM': 'DMSans-Regular', 'DM-Medium': 'DMSans-Medium',
         'DM-Bold': 'DMSans-Bold', 'Instrument': 'InstrumentSerif-Italic',
         'Plex': 'IBMPlexMono-Regular'}
for name, filename in FONTS.items():
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / f'{filename}.ttf')))
pdfmetrics.registerFontFamily('DM', normal='DM', bold='DM-Bold', italic='DM', boldItalic='DM-Bold')

W, H = 595.276, 841.89
M = 40
WIDTH = W - 2*M
PAPER = HexColor('#f7f7f0')
INK = HexColor('#203c34')
GREEN = HexColor('#174d43')
MUTED = HexColor('#5c6957')
LINE = HexColor('#d9ddd2')
SOFT = HexColor('#e9ecdf')
ACCENT = HexColor('#8a9c68')
c = canvas.Canvas(str(OUT), pagesize=(W,H), pageCompression=1)
c.setTitle('Adam Riddick - Principal Architect - Public CV')
c.setAuthor('Adam Riddick')
c.setSubject('Software architecture, SaaS modernisation and engineering leadership')

styles = {
    'body': ParagraphStyle('body', fontName='DM', fontSize=10, leading=14, textColor=INK),
    'small': ParagraphStyle('small', fontName='DM', fontSize=8.5, leading=12, textColor=MUTED),
    'title': ParagraphStyle('title', fontName='DM-Medium', fontSize=14, leading=18, textColor=INK),
    'skill': ParagraphStyle('skill', fontName='DM', fontSize=9.1, leading=13, textColor=MUTED),
    'honour': ParagraphStyle('honour', fontName='DM', fontSize=9, leading=13, textColor=INK),
    'section': ParagraphStyle('section', fontName='DM-Medium', fontSize=21, leading=28, textColor=INK),
    'profile': ParagraphStyle('profile', fontName='DM', fontSize=11, leading=16, textColor=INK),
}
y = H - M


def line(top, x=M, width=WIDTH):
    c.setStrokeColor(LINE)
    c.setLineWidth(.6)
    c.line(x,top,x+width,top)


def label(text, top, x=M, colour=MUTED, size=7):
    c.saveState()
    c.setFillColor(colour)
    textobj=c.beginText(x,top)
    textobj.setFont('Plex',size)
    textobj.setCharSpace(.8)
    textobj.textLine(text)
    c.drawText(textobj)
    c.restoreState()


def para(text, style='body', width=WIDTH, x=M, space=6):
    global y
    p=Paragraph(text,styles[style])
    _,height=p.wrap(width,H)
    assert y-height > 57, f'Content exceeds safe page boundary: {text[:65]} at {y-height}'
    p.drawOn(c,x,y-height)
    y-=height+space


def header(page):
    c.setFillColor(PAPER)
    c.rect(0,0,W,H,stroke=0,fill=1)
    if page==1:
        label('SOFTWARE ENGINEERING & ARCHITECTURE',H-43,size=8)
        c.setFillColor(INK)
        c.setFont('DM-Medium',42)
        c.drawString(M,H-94,'Adam')
        surname_x=M+pdfmetrics.stringWidth('Adam','DM-Medium',42)+10
        c.setFont('Instrument',50)
        c.drawString(surname_x,H-94,'Riddick')
        dot_x=surname_x+pdfmetrics.stringWidth('Riddick','Instrument',50)+3
        c.setFillColor(ACCENT)
        c.circle(dot_x,H-92,2.3,stroke=0,fill=1)
        c.setFillColor(INK)
        c.setFont('DM',12)
        c.drawString(M,H-117,'Principal Architect | United Kingdom')
        contact(H-54)
    else:
        c.setFillColor(INK)
        c.setFont('DM-Medium',12)
        c.drawString(M,H-43,'Adam Riddick')
        c.setFont('DM',9)
        c.setFillColor(MUTED)
        c.drawString(M,H-59,'Principal Architect')
        c.drawRightString(W-M,H-43,'adam.riddick.dev')
        c.linkURL('https://adam.riddick.dev/',(W-M-80,H-47,W-M,H-32),relative=0,thickness=0)
        line(H-76)


def footer(page):
    line(43)
    label('ADAM RIDDICK / CURRICULUM VITAE',29,size=7)
    c.setFont('Plex',7)
    c.setFillColor(MUTED)
    c.drawRightString(W-M,29,f'NOV 2026 / 0{page}')


def section(title):
    global y
    para(title,'section',space=12)


def entry(title,meta,paragraphs):
    global y
    para(title,'title',space=3)
    para(meta,'small',space=8)
    for paragraph in paragraphs:
        para(paragraph)
    y-=6


def contact(top):
    c.setFillColor(GREEN)
    c.setFont('DM-Medium',9)
    c.drawRightString(W-M,top,'adam@riddick.dev')
    c.linkURL('mailto:adam@riddick.dev',(W-M-103,top-3,W-M,top+10),relative=0,thickness=0)
    c.setFont('DM',8.5)
    c.setFillColor(MUTED)
    c.drawRightString(W-M,top-17,'linkedin.com/in/adam-riddick')
    c.linkURL('https://www.linkedin.com/in/adam-riddick/',(W-M-127,top-20,W-M,top-8),relative=0,thickness=0)
    website = 'adam.riddick.dev'
    c.drawRightString(W-M,top-32,website)
    width = pdfmetrics.stringWidth(website,'DM',8.5)
    c.linkURL(f'https://{website}/',(W-M-width,top-35,W-M,top-24),relative=0,thickness=0)


header(1)
y=H-145
para(DATA['profile'],'profile',space=18)
line(y)
y-=18
section('Selected <font name="Instrument" size="25">work.</font>')
for i,item in enumerate(DATA['achievements']):
    entry(item['title'],item['meta'],item['paragraphs'])
    if i<2:
        line(y+2)
        y-=13
assert y>58, y
footer(1)
c.showPage()

header(2)
y=H-101
section('Career <font name="Instrument" size="25">history.</font>')
for i,item in enumerate(DATA['career']):
    employer,role=item['title'].split(' | ',1)
    entry(role,f'{employer} | {item["meta"]}',item['paragraphs'])
    line(y+2)
    y-=13
para('Earlier experience','title',space=5)
for row in DATA['earlier']:
    para(row,'small',space=3)
y-=13
section('Technical <font name="Instrument" size="25">experience.</font>')
for row in DATA['technical']:
    para(row,'skill',space=4)

qualification_height=sum(Paragraph(row,styles['honour']).wrap(WIDTH-30,H)[1]+4 for row in DATA['qualifications'])
panel_height=qualification_height+45
assert y-panel_height>58,(y,panel_height)
c.setFillColor(SOFT)
c.rect(M,y-panel_height,WIDTH,panel_height,stroke=0,fill=1)
label('EDUCATION & RECOGNITION',y-19,x=M+15,size=8)
y-=32
for row in DATA['qualifications']:
    para(row,'honour',width=WIDTH-30,x=M+15,space=4)
footer(2)
c.save()
print(OUT)
