from pathlib import Path
from html import escape
import sys,json
sys.path.insert(0,'/tmp/pumerse-tools')
import cairosvg
from PIL import Image,ImageDraw,ImageFont
import xml.etree.ElementTree as ET
P=Path(__file__).resolve().parent; ink='#202E2B'; cream='#F6F3EA'; green='#315C4C'; orange='#C45A38'
checks=[]
class Art:
 def __init__(self,name,w,h,bg,title,a4=False):
  self.name,self.w,self.h=name,w,h; self.boxes=[]; self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{ "210mm" if a4 else str(w)}" height="{ "297mm" if a4 else str(h)}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)} — Pumerse Studio</title><desc>Original single-page design. Editable text and vector shapes. Fictional sample content.</desc>'];self.rect(0,0,w,h,bg)
 def rect(self,x,y,w,h,c,r=0):self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}"/>')
 def line(self,x,y,x2,y2,c=ink):self.parts.append(f'<path d="M{x} {y} L{x2} {y2}" fill="none" stroke="{c}" stroke-width="1.5"/>')
 def circle(self,x,y,r,c):self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>')
 def path(self,d,c,stroke='none',sw=1):self.parts.append(f'<path d="{d}" fill="{c}" stroke="{stroke}" stroke-width="{sw}"/>')
 def text(self,x,y,s,size=18,c=ink,bold=False,serif=False):
  family='DejaVu Serif' if serif else 'DejaVu Sans'; font=P/'fonts'/('DejaVuSerif.ttf' if serif else 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf');f=ImageFont.truetype(str(font),size); box=f.getbbox(s,anchor='ls'); assert x+box[0]>=0 and x+box[2]<=self.w and y+box[1]>=0 and y+box[3]<=self.h,(self.name,s,box)
  current=(x+box[0],y+box[1],x+box[2],y+box[3])
  for prior,prior_text in self.boxes:
   assert not (min(current[2],prior[2])>max(current[0],prior[0]) and min(current[3],prior[3])>max(current[1],prior[1])),(self.name,s,prior_text)
  self.boxes.append((current,s))
  self.parts.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{700 if bold else 400}" fill="{c}">{escape(s)}</text>')
 def lines(self,x,y,ss,size=18,c=ink,gap=None,**kw):
  for i,s in enumerate(ss):self.text(x,y+i*(gap or size*1.55),s,size,c,**kw)
 def foot(self,n,c=ink):self.line(48,self.h-57,self.w-48,self.h-57,c);self.text(48,self.h-30,'PUMERSE STUDIO  /  ORIGINAL DESIGN',10,c);self.text(self.w-75,self.h-30,f'{n:02}',10,c)
 def save(self):
  self.parts.append('</svg>');svg='\n'.join(self.parts);ET.fromstring(svg);(P/'svg'/f'{self.name}.svg').write_text(svg);cairosvg.svg2png(bytestring=svg.encode(),write_to=str(P/'png'/f'{self.name}.png'),output_width=self.w,output_height=self.h);checks.append({'file':self.name,'canvas':[self.w,self.h],'text_bounds':'passed','text_overlap':'passed','xml':'passed','png_render':'passed'})
def a4(n,title,bg=cream):return Art(n,794,1123,bg,title,True)
# 01
s=a4('01-minimalist-resume','Modern minimalist resume');s.rect(48,52,7,95,green);s.text(78,91,'MAYA BENNETT',36,bold=True);s.text(80,125,'PRODUCT DESIGNER',15,green);s.text(48,183,'maya.bennett@example.com  •  Bristol, UK  •  Portfolio on request',13);s.line(48,212,746,212)
s.text(48,260,'PROFILE',13,green,True);s.lines(240,260,['Product designer with 5 years of experience turning complex','workflows into clear, accessible digital experiences.','Combines customer research with practical design systems.'],16)
s.text(48,382,'EXPERIENCE',13,green,True)
for y,title,sub,lines in [(382,'Senior Product Designer','Northline Labs  |  2023–present',['Led onboarding redesign across web and mobile.','Reduced setup time by 28% in moderated usability studies.','Built a shared library of 60 accessible UI components.']),(562,'Product Designer','Fieldwork Digital  |  2020–2023',['Designed scheduling tools for independent retailers.','Partnered with engineering from discovery to release.','Ran monthly interviews with customers and support teams.'])]:
 s.text(240,y,title,20,bold=True);s.text(240,y+30,sub,13,green);s.lines(240,y+65,lines,15)
s.text(48,763,'EDUCATION',13,green,True);s.text(240,763,'BA, Communication Design',19,bold=True);s.text(240,795,'Westbridge College  |  2017–2020',14)
s.text(48,875,'SKILLS',13,green,True);s.lines(240,875,['User research  /  Interaction design  /  Prototyping','Design systems  /  Accessibility  /  Workshop facilitation'],15);s.foot(1);s.save()
#02
s=a4('02-creative-resume','Creative resume','#F4E9DB');s.rect(0,0,260,1123,'#3C3C73');s.circle(130,133,62,'#F0AD83');s.text(86,148,'AL',39,'#3C3C73',True);s.text(35,258,'CONTACT',13,'#F0AD83',True);s.lines(35,298,['alex.lee@example.com','Manchester, UK','Portfolio on request'],13,'#FFFFFF',gap=28);s.text(35,437,'TOOLKIT',13,'#F0AD83',True);s.lines(35,481,['Visual storytelling','Art direction','Editorial systems','Motion storyboards','Brand workshops'],14,'#FFFFFF',gap=34);s.text(35,730,'EDUCATION',13,'#F0AD83',True);s.lines(35,772,['BA, Graphic Design','Westbridge College','2016–2019'],14,'#FFFFFF',gap=28);s.text(300,100,'Alex Lee',50,'#3C3C73',serif=True);s.text(302,148,'BRAND & EDITORIAL DESIGNER',14,orange,True);s.lines(302,215,['I build expressive identities that','make everyday brands memorable.'],21,'#3C3C73',serif=True);s.line(302,285,744,285,'#3C3C73')
for y,num,head,sub,body in [(350,'01','Independent designer','2022–present',['Brand identities for local hospitality','and culture businesses. Delivered 14','launch-ready visual identity systems.']),(554,'02','Designer · Paperplane','2019–2022',['Created editorial layouts and campaigns.','Developed modular templates that cut','weekly production time by 30%.'])]:
 s.text(302,y,num,15,orange,True);s.text(346,y,head,19,'#3C3C73',True);s.text(346,y+32,sub,13);s.lines(302,y+76,body,16)
s.rect(302,832,442,150,'#F0AD83',12);s.text(324,872,'SELECTED STRENGTH',12,'#3C3C73',True);s.lines(324,913,['A bold idea. A clear system.','A consistent brand experience.'],20,'#3C3C73',serif=True);s.text(302,1085,'PUMERSE STUDIO  /  ORIGINAL DESIGN  /  02',10);s.save()
#03
s=Art('03-instagram-promotion',1080,1080,'#DFFA74','Instagram promotional post');s.text(64,92,'FORM & FIELD',20,bold=True);s.text(64,236,'Less clutter.',80,bold=True);s.text(64,333,'More focus.',80,bold=True);s.text(68,399,'Desk essentials for a calmer workday.',26);s.circle(787,667,222,green);s.rect(680,555,220,268,'#F5EEDF',20);s.rect(700,579,180,15,'#D8CBB5',4);s.rect(700,613,180,15,'#D8CBB5',4);s.rect(700,647,180,15,'#D8CBB5',4);s.path('M610 826 L681 590 L709 598 L638 834 Z',orange);s.circle(848,775,67,'#DFFA74');s.circle(848,775,45,'#365042');s.rect(68,526,287,110,ink,12);s.text(91,600,'20% OFF',49,'#DFFA74',True);s.lines(68,703,['The fresh-start edit','12–18 May 2027'],25);s.text(68,873,'SHOP THE COLLECTION  →',24,bold=True);s.text(68,918,'Use code FOCUS20 · Selected desk accessories.',17);s.foot(3);s.save()
#04
s=Art('04-carousel-cover',1080,1080,'#304EC8','Educational carousel cover');s.text(64,91,'THE SMALL BRAND PLAYBOOK',18,'#FFFFFF',True);s.rect(843,53,173,55,'#DDE8FF',27);s.text(869,89,'GUIDE 01',17,'#304EC8',True);s.text(64,262,'5 ways to',80,'#FFFFFF',True);s.text(64,361,'make your',80,'#FFFFFF',True);s.text(64,460,'brand clearer',80,'#FFFFFF',True);s.lines(68,554,['Simple choices. Stronger recognition.','A practical guide for small businesses.'],25,'#DDE8FF');
for x,y,w,h,c,label in [(110,702,200,180,'#BBD6FF','Aa'),(374,748,236,132,'#FFCA94','01'),(672,685,280,220,'#DFFA74','→')]:s.rect(x,y,w,h,c,24);s.text(x+40,y+110,label,68,'#233582',True)
s.text(68,973,'START HERE  /  SWIPE TO LEARN →',19,'#FFFFFF',True);s.foot(4,'#FFFFFF');s.save()
#05
s=a4('05-coffee-poster','Coffee shop promotional poster','#F3E4CE');s.text(48,81,'DAYBREAK COFFEE',17,orange,True);s.text(48,182,'A slower',70,serif=True);s.text(48,269,'kind of morning.',62,serif=True);s.text(51,326,'Fresh coffee. Warm pastries. A little time for you.',19);s.circle(403,570,207,'#D8AA78');s.path('M254 491 L518 491 L494 667 Q386 720 277 667 Z',cream);s.path('M516 510 C623 488 619 640 504 631','none',cream,22);s.path('M329 455 C290 410 359 406 325 360 M392 455 C353 410 422 406 389 360 M455 455 C416 410 485 406 452 360','none',orange,5);s.rect(48,823,698,108,green,8);s.text(77,864,'MORNING PAIRING',13,'#FFFFFF',True);s.text(77,905,'Flat white + butter croissant',25,'#FFFFFF');s.text(620,899,'£6.50',26,'#FFFFFF',True);s.lines(48,979,['Weekdays, 7–11 am  ·  Dine in or take away','18 Willow Lane, Bristol  ·  Offer ends 31 May 2027'],15);s.foot(5);s.save()
#06
s=a4('06-wellness-poster','Wellness event poster','#E8EFE5');s.circle(648,200,212,'#D4DDCB');s.path('M545 406 Q430 270 510 145 Q618 266 545 406',green);s.path('M565 429 Q693 269 742 327 Q719 454 565 429','#8B9E73');s.text(48,79,'THE STILLNESS COLLECTIVE',14,green,True);s.text(48,189,'Room to',64,green,serif=True);s.text(48,270,'breathe.',73,green,serif=True);s.lines(48,356,['A gentle morning of movement,','reflection and connection.'],20);s.rect(48,487,698,151,green,14);s.text(75,537,'SATURDAY  /  22 MAY 2027',20,'#FFFFFF',True);s.text(75,579,'9:00–12:00  ·  Willow Community Hall',21,'#FFFFFF');s.text(75,610,'Bristol  ·  All experience levels welcome',15,'#DCE8DA');
for y,t,d in [(705,'01  Move gently','45-minute guided mobility session'),(790,'02  Find your focus','Breathwork and reflective journaling'),(875,'03  Connect','Herbal tea and a welcoming conversation')]:s.text(48,y,t,23,green,True);s.text(48,y+32,d,17)
s.text(48,998,'£18 per person  ·  Bring a mat and water.',17);s.text(48,1029,'Reserve: hello@example.com  ·  Limited to 20 guests.',15);s.foot(6);s.save()
#07
s=Art('07-business-pitch',1600,900,ink,'Business pitch presentation slide');s.text(64,85,'NORTHLINE  /  PITCH OVERVIEW',18,'#B8D1C0',True);s.text(64,210,'Local shops.',78,'#FFFFFF',True);s.text(64,303,'Smarter stock.',78,'#FFFFFF',True);s.lines(68,397,['A simple inventory workspace for independent retailers.','Know what is selling. Reorder with confidence.'],26,'#CAD8D0');s.rect(1010,149,526,542,'#DFFA74',22);s.text(1050,210,'THE OPPORTUNITY',18,ink,True);s.text(1050,334,'12 hours',64,ink,True);s.lines(1050,386,['of weekly admin targeted','for reduction per shop.'],24);s.line(1050,451,1496,451);s.text(1050,513,'ONE WORKSPACE',18,ink,True);s.lines(1050,562,['Stock visibility','Reorder reminders','Simple sales reporting'],25);
for x,num,label in [(68,'01','Connect your catalog'),(374,'02','Spot low stock'),(680,'03','Plan your next order')]:s.text(x,613,num,23,'#DFFA74',True);s.text(x,666,label,20,'#FFFFFF',True)
s.text(68,758,'Pilot plan: 20 shops · 8 weeks · Measure admin time and stock availability.',20,'#CAD8D0');s.text(68,802,'Illustrative concept and targets; no market-performance claims.',14,'#CAD8D0');s.foot(7,'#CAD8D0');s.save()
#08
s=Art('08-educational-slide',1600,900,'#F7F2E8','Educational presentation slide');s.text(64,81,'DESIGN FOUNDATIONS  /  LESSON 02',18,green,True);s.text(64,180,'Hierarchy helps people find their way.',52,bold=True);s.text(66,239,'Use size, contrast and space to make the next step obvious.',26)
for x,n,t,b in [(64,'01','Size',['Make the main idea the','largest element on the page.']),(574,'02','Contrast',['Use a distinct tone to','highlight what matters.']),(1084,'03','Space',['Group related information.','Give key ideas room.'])]:
 s.rect(x,310,450,430,'#E7E4D8',16);s.text(x+28,365,n,18,green,True);s.text(x+28,421,t,31,bold=True);s.lines(x+28,465,b,19)
 if n=='01':s.text(x+28,585,'Main idea',40,bold=True);s.text(x+28,626,'Supporting information',18);s.line(x+28,660,x+310,660,green)
 elif n=='02':s.rect(x+28,560,394,116,green,8);s.text(x+51,606,'Start with one clear action.',19,'#FFFFFF',True);s.text(x+51,645,'Read the full guide →',18,'#FFFFFF')
 else:
  for yy,ww in [(558,320),(580,270),(652,320),(674,210)]:s.rect(x+28,yy,ww,10,green,5)
s.text(64,795,'TRY IT  →  Identify the first thing you notice on this slide. Which cue draws your eye?',22,green);s.foot(8);s.save()
#09
s=a4('09-daily-planner','Daily productivity planner','#FFFFFF');s.text(48,94,'Make space for today.',38,green,serif=True);s.text(48,142,'DATE',12,green,True);s.line(95,145,326,145);s.text(441,142,'TODAY I WANT TO FEEL',12,green,True);s.line(441,177,746,177);s.rect(48,210,698,160,'#EEF2E9',10);s.text(68,242,'MY THREE PRIORITIES',13,green,True)
for i in range(3):s.circle(75,273+i*32,7,'#FFFFFF');s.line(96,282+i*32,722,282+i*32,'#B5C2AE')
s.text(48,418,'TIME BLOCKS',14,green,True);s.text(444,418,'TASKS & FOLLOW-UPS',14,green,True)
for i in range(9):
 y=458+i*48;s.text(48,y,f'{9+i:02}:00',13);s.line(100,y+4,404,y+4,'#B5C2AE');s.rect(445,y-12,13,13,'#EEF2E9',2);s.line(472,y+4,746,y+4,'#B5C2AE')
s.text(48,931,'ONE SMALL WIN',13,green,True);s.line(48,973,404,973,'#B5C2AE');s.text(445,931,'TOMORROW CAN WAIT',13,green,True);s.line(445,973,746,973,'#B5C2AE');s.text(48,1020,'Progress over perfection. Leave a little breathing room.',14,green);s.foot(9);s.save()
#10
s=a4('10-service-price-list','Small business service price list','#FCF1E7');s.rect(0,0,794,15,orange);s.text(48,83,'PUMERSE STUDIO',18,orange,True);s.text(48,182,'Good design.',58,serif=True);s.text(48,253,'Clear pricing.',58,serif=True);s.text(48,309,'Thoughtful visual design for small businesses.',18)
for y,n,t,price,lines in [(392,'01','Brand starter','£450',['Wordmark, color palette and typography guide.','One direction · Two revision rounds · 10 business days']),(567,'02','Social essentials','£180',['Six coordinated social post layouts for your brand.','One platform size · Two revision rounds · 5 business days']),(742,'03','Print essentials','£240',['One flyer and one service menu, ready for print.','A4 or A5 · Two revision rounds · 7 business days'])]:
 s.line(48,y-25,746,y-25,'#DAB9A4');s.text(48,y+8,n,14,orange,True);s.text(93,y+8,t,28,bold=True);s.text(620,y+8,price,28,orange,True);s.lines(93,y+52,lines,15)
s.rect(48,925,698,102,green,8);s.text(72,963,'LET’S MAKE SOMETHING USEFUL.',15,'#FFFFFF',True);s.text(72,998,'Request a quote: hello@example.com',19,'#FFFFFF');s.text(48,1051,'Sample rates in GBP. Final scope and any tax confirmed in writing.',11);s.foot(10);s.save()
# Contact sheet, generous cards and native-aspect previews
sheet=Image.new('RGB',(1800,1550),'#E7E5DF');d=ImageDraw.Draw(sheet);f=lambda n:ImageFont.truetype(str(P/'fonts/DejaVuSans.ttf'),n);d.text((45,25),'PUMERSE STUDIO',font=f(34),fill=ink);d.text((45,77),'10 original, editable single-page design samples',font=f(18),fill=green)
for i,c in enumerate(checks):
 x=35+(i%5)*350;y=135+(i//5)*685;d.rounded_rectangle((x,y,x+330,y+655),12,fill='white');im=Image.open(P/'png'/f'{c["file"]}.png').convert('RGB');im.thumbnail((302,565));sheet.paste(im,(x+(330-im.width)//2,y+20+(565-im.height)//2));label=c['file'].replace('-',' ').split(' ',1);d.text((x+15,y+605),label[0]+'  '+label[1],font=f(15),fill=ink)
sheet.save(P/'contact-sheet.png');(P/'validation.json').write_text(json.dumps(checks,indent=2));print('Rendered and bounds-checked',len(checks),'single-page SVGs.')
