import json
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

out = Path(__file__).resolve().parent / 'assets'
out.mkdir(exist_ok=True)
values = json.load(sys.stdin)
font = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
bold = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
title = ImageFont.truetype(bold, 67)
small = ImageFont.truetype(font, 21)
label = ImageFont.truetype(bold, 15)
frames = []
for value in values:
    image = Image.new('RGB', (1000, 300), '#171b2b')
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((15, 15, 984, 284), radius=18, outline='#364463', width=2)
    d.line((54, 55, 946, 55), fill='#323c56', width=2)
    for x, color in [(59, '#f7768e'), (81, '#e0af68'), (103, '#9ece6a')]:
        d.ellipse((x, 31, x + 10, 41), fill=color)
    d.text((130, 28), 'ABOYPHM / GITHUB', font=label, fill='#a9b8d9')
    d.text((54, 88), 'aboyphm', font=title, fill='#edf1ff')
    d.text((58, 181), 'CODE  /  CREATE  /  EXPLORE', font=small, fill='#a9c5fa')
    d.text((60, 242), 'PUBLIC REPOSITORIES', font=label, fill='#a9b8d9')
    d.line((610, 220, 909, 220), fill='#3c4967', width=2)
    for i in range(7):
        height = 16 + ((i * 29) % 75)
        d.rounded_rectangle((640 + i * 40, 219 - height, 656 + i * 40, 219), radius=5, fill='#344462')
    x = int(634 + 260 * value)
    d.ellipse((x - 5, 215, x + 5, 225), fill='#9ece6a')
    frames.append(image)
frames[0].save(out / 'header-static.png', optimize=True)
frames[0].save(out / 'header.gif', save_all=True, append_images=frames[1:], duration=100, loop=0, optimize=True)
print(f'Rendered {len(frames)} frames to {out / "header.gif"}')
