import math
from PIL import Image, ImageDraw, ImageSequence

gif = Image.open("facescan3.gif")
frames = []

for i, frame in enumerate(ImageSequence.Iterator(gif)):
    frame = frame.convert("RGBA")
    w, h = frame.size

    # Базовые размеры рамки
    base_w, base_h = int(w * 0.55), int(h * 0.75)

    # Пульсация (дышит): синусоида
    pulse = int(12 * math.sin(i * 0.2))  # амплитуда 12 px, скорость 0.2 рад
    head_w = base_w + pulse
    head_h = base_h + pulse

    # Центрируем рамку относительно кадра
    x1 = (w - head_w) // 2
    y1 = (h - head_h) // 2
    x2 = x1 + head_w
    y2 = y1 + head_h

    overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Цвет — тёмно-фиолетовый
    color = (90, 0, 140, 255)
    line_w = 5
    corner_len = 60
    tick_len = 20
    extra = 12

    # Уголки
    draw.line([(x1, y1), (x1+corner_len, y1)], fill=color, width=line_w)
    draw.line([(x1, y1), (x1, y1+corner_len)], fill=color, width=line_w)

    draw.line([(x2, y1), (x2-corner_len, y1)], fill=color, width=line_w)
    draw.line([(x2, y1), (x2, y1+corner_len)], fill=color, width=line_w)

    draw.line([(x1, y2), (x1+corner_len, y2)], fill=color, width=line_w)
    draw.line([(x1, y2), (x1, y2-corner_len)], fill=color, width=line_w)

    draw.line([(x2, y2), (x2-corner_len, y2)], fill=color, width=line_w)
    draw.line([(x2, y2), (x2, y2-corner_len)], fill=color, width=line_w)

    # Засечки: по три на каждую сторону
    for y in [y1 + (y2-y1)//4, (y1+y2)//2, y1 + 3*(y2-y1)//4]:
        if y == (y1+y2)//2:  # центральные длиннее внутрь
            draw.line([(x1 - tick_len, y), (x1 + extra, y)], fill=color, width=4)
            draw.line([(x2 + tick_len, y), (x2 - extra, y)], fill=color, width=4)
        else:
            draw.line([(x1, y), (x1 - tick_len, y)], fill=color, width=4)
            draw.line([(x2, y), (x2 + tick_len, y)], fill=color, width=4)

    for x in [x1 + (x2-x1)//4, (x1+x2)//2, x1 + 3*(x2-x1)//4]:
        if x == (x1+x2)//2:
            draw.line([(x, y1 - tick_len), (x, y1 + extra)], fill=color, width=4)
            draw.line([(x, y2 + tick_len), (x, y2 - extra)], fill=color, width=4)
        else:
            draw.line([(x, y1), (x, y1 - tick_len)], fill=color, width=4)
            draw.line([(x, y2), (x, y2 + tick_len)], fill=color, width=4)

    combined = Image.alpha_composite(frame, overlay)
    frames.append(combined)

frames[0].save(
    "facescan3_overlay_breathing_center.gif",
    save_all=True,
    append_images=frames[1:],
    duration=gif.info['duration'],
    loop=0,
    disposal=2
)
print("GIF с оверлеем сохранен как facescan3_overlay.gif") # Примечание: Убедись, что у тебя установлен Pillow: pip install Pillow
