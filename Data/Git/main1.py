# python main.py
from PIL import Image, ImageDraw, ImageSequence

# Загружаем твой GIF
gif = Image.open("facescan3.gif")

frames = []
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert("RGBA")
    
    # Создаем холст со светлым фоном
    bg = Image.new("RGBA", frame.size, (240, 240, 240, 255))  # светло-серый фон
    bg.paste(frame, (0, 0), frame)
    
    # Рисуем HUD-оверлей
    draw = ImageDraw.Draw(bg)
    w, h = frame.size
    offset = 40
    
    # Углы (как на эскизе)
    draw.line([(offset, offset), (offset+40, offset)], fill=(0, 200, 255, 255), width=3)
    draw.line([(offset, offset), (offset, offset+40)], fill=(0, 200, 255, 255), width=3)

    draw.line([(w-offset, offset), (w-offset-40, offset)], fill=(0, 200, 255, 255), width=3)
    draw.line([(w-offset, offset), (w-offset, offset+40)], fill=(0, 200, 255, 255), width=3)

    draw.line([(offset, h-offset), (offset+40, h-offset)], fill=(0, 200, 255, 255), width=3)
    draw.line([(offset, h-offset), (offset, h-offset-40)], fill=(0, 200, 255, 255), width=3)

    draw.line([(w-offset, h-offset), (w-offset-40, h-offset)], fill=(0, 200, 255, 255), width=3)
    draw.line([(w-offset, h-offset), (w-offset, h-offset-40)], fill=(0, 200, 255, 255), width=3)

    # Горизонтальная "лазерная" линия по центру
    draw.line([(offset, h//2), (w-offset, h//2)], fill=(0, 255, 180, 200), width=2)

    frames.append(bg)

# Сохраняем новый gif
frames[0].save(
    "facescan3_overlay.gif",
    save_all=True,
    append_images=frames[1:],
    duration=gif.info['duration'],
    loop=0,
    disposal=2
)
print("GIF с оверлеем сохранен как facescan3_overlay.gif") # Примечание: Убедись, что у тебя установлен Pillow: pip install Pillow
