from PIL import Image, ImageDraw, ImageSequence

# Загружаем твой GIF
gif = Image.open("facescan3.gif")

frames = []
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert("RGBA")
    
    # Создаем новый слой для оверлея
    overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    w, h = frame.size
    offset = 20      # ближе к голове
    corner_len = 60  # длина уголков
    
    color = (0, 200, 255, 255)  # цвет уголков и засечек (голубой неон)

    # Углы рамки (крупнее и ближе)
    # Левый верхний
    draw.line([(offset, offset), (offset+corner_len, offset)], fill=color, width=3)
    draw.line([(offset, offset), (offset, offset+corner_len)], fill=color, width=3)
    # Правый верхний
    draw.line([(w-offset, offset), (w-offset-corner_len, offset)], fill=color, width=3)
    draw.line([(w-offset, offset), (w-offset, offset+corner_len)], fill=color, width=3)
    # Левый нижний
    draw.line([(offset, h-offset), (offset+corner_len, h-offset)], fill=color, width=3)
    draw.line([(offset, h-offset), (offset, h-offset-corner_len)], fill=color, width=3)
    # Правый нижний
    draw.line([(w-offset, h-offset), (w-offset-corner_len, h-offset)], fill=color, width=3)
    draw.line([(w-offset, h-offset), (w-offset, h-offset-corner_len)], fill=color, width=3)

    # Засечки (ticks) по вертикали и горизонтали
    tick_len = 15
    step = 80  # шаг между засечками

    # Горизонтальные (слева и справа)
    for y in range(offset + corner_len, h - offset - corner_len, step):
        draw.line([(offset, y), (offset - tick_len, y)], fill=color, width=2)
        draw.line([(w-offset, y), (w-offset + tick_len, y)], fill=color, width=2)

    # Вертикальные (сверху и снизу)
    for x in range(offset + corner_len, w - offset - corner_len, step):
        draw.line([(x, offset), (x, offset - tick_len)], fill=color, width=2)
        draw.line([(x, h-offset), (x, h-offset + tick_len)], fill=color, width=2)

    # Накладываем поверх кадра
    combined = Image.alpha_composite(frame, overlay)
    frames.append(combined)

# Сохраняем новый gif
frames[0].save(
    "facescan3_overlay_ticks.gif",
    save_all=True,
    append_images=frames[1:],
    duration=gif.info['duration'],
    loop=0,
    disposal=2
)
print("GIF с оверлеем и засечками сохранен как facescan3_overlay_ticks.gif") # Примечание: Убедись, что у тебя установлен Pillow: pip install Pillow
