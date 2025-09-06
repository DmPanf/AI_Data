from PIL import Image, ImageDraw, ImageSequence

gif = Image.open("facescan3.gif")
frames = []

for frame in ImageSequence.Iterator(gif):
    frame = frame.convert("RGBA")
    
    overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    w, h = frame.size
    offset = 15       # ещё ближе к голове
    corner_len = 70   # уголки подлиннее
    
    # Цвет уголков и засечек (тёмно-фиолетовый)
    color = (90, 0, 140, 255)

    # Уголки (толще и массивнее)
    line_w = 5
    # Левый верхний
    draw.line([(offset, offset), (offset+corner_len, offset)], fill=color, width=line_w)
    draw.line([(offset, offset), (offset, offset+corner_len)], fill=color, width=line_w)
    # Правый верхний
    draw.line([(w-offset, offset), (w-offset-corner_len, offset)], fill=color, width=line_w)
    draw.line([(w-offset, offset), (w-offset, offset+corner_len)], fill=color, width=line_w)
    # Левый нижний
    draw.line([(offset, h-offset), (offset+corner_len, h-offset)], fill=color, width=line_w)
    draw.line([(offset, h-offset), (offset, h-offset-corner_len)], fill=color, width=line_w)
    # Правый нижний
    draw.line([(w-offset, h-offset), (w-offset-corner_len, h-offset)], fill=color, width=line_w)
    draw.line([(w-offset, h-offset), (w-offset, h-offset-corner_len)], fill=color, width=line_w)

    # Засечки
    tick_len = 18
    tick_w = 4
    extra = 10  # удлинение внутрь (для центральных)

    # Горизонтальные стороны
    for y in [h//4, h//2, 3*h//4]:
        if y == h//2:  # центральная засечка — длиннее внутрь
            draw.line([(offset - tick_len, y), (offset + extra, y)], fill=color, width=tick_w)
            draw.line([(w-offset + tick_len, y), (w-offset - extra, y)], fill=color, width=tick_w)
        else:
            draw.line([(offset, y), (offset - tick_len, y)], fill=color, width=tick_w)
            draw.line([(w-offset, y), (w-offset + tick_len, y)], fill=color, width=tick_w)

    # Вертикальные стороны
    for x in [w//4, w//2, 3*w//4]:
        if x == w//2:  # центральная засечка — длиннее внутрь
            draw.line([(x, offset - tick_len), (x, offset + extra)], fill=color, width=tick_w)
            draw.line([(x, h-offset + tick_len), (x, h-offset - extra)], fill=color, width=tick_w)
        else:
            draw.line([(x, offset), (x, offset - tick_len)], fill=color, width=tick_w)
            draw.line([(x, h-offset), (x, h-offset + tick_len)], fill=color, width=tick_w)

    combined = Image.alpha_composite(frame, overlay)
    frames.append(combined)

frames[0].save(
    "facescan3_overlay_purple.gif",
    save_all=True,
    append_images=frames[1:],
    duration=gif.info['duration'],
    loop=0,
    disposal=2
)
print("\nGIF с оверлеем и засечками сохранен как facescan3_overlay_purple.gif") # Примечание: Убедись, что у тебя установлен Pillow: pip install Pillow
