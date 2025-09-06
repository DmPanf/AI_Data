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
    color = (0, 200, 255, 255)  # неоновый голубой

    # Уголки (толще)
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

    # Засечки: только 3 на каждую сторону
    tick_len = 18
    tick_w = 4

    # Горизонтальные стороны (слева и справа)
    for y in [h//4, h//2, 3*h//4]:
        draw.line([(offset, y), (offset - tick_len, y)], fill=color, width=tick_w)
        draw.line([(w-offset, y), (w-offset + tick_len, y)], fill=color, width=tick_w)

    # Вертикальные стороны (сверху и снизу)
    for x in [w//4, w//2, 3*w//4]:
        draw.line([(x, offset), (x, offset - tick_len)], fill=color, width=tick_w)
        draw.line([(x, h-offset), (x, h-offset + tick_len)], fill=color, width=tick_w)

    combined = Image.alpha_composite(frame, overlay)
    frames.append(combined)

frames[0].save(
    "facescan3_overlay_strong.gif",
    save_all=True,
    append_images=frames[1:],
    duration=gif.info['duration'],
    loop=0,
    disposal=2
)
print("GIF с оверлеем и засечками сохранен как facescan3_overlay_ticks.gif") # Примечание: Убедись, что у тебя установлен Pillow: pip install Pillow
