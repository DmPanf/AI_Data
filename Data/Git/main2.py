# python GIF/main2.py
from PIL import Image, ImageDraw, ImageSequence

gif = Image.open("facescan3.gif")
frames = []

for frame in ImageSequence.Iterator(gif):
    frame = frame.convert("RGBA")
    w, h = frame.size
    
    # Создаем слой для лазера
    laser = Image.new("RGBA", frame.size, (0,0,0,0))
    draw = ImageDraw.Draw(laser)
    
    # Позиция линии (пример - по центру, можно менять)
    y = h // 2
    
    # Лазер: яркая центральная линия + градиент по бокам
    for offset in range(-10, 11):  # толщина около 20px
        alpha = max(0, 180 - abs(offset)*18)  # чем дальше от центра, тем прозрачнее
        color = (0, 255, 180, alpha)
        draw.line([(0, y+offset), (w, y+offset)], fill=color, width=1)
    
    # Накладываем на кадр
    combined = Image.alpha_composite(frame, laser)
    frames.append(combined)

# Сохраняем новый gif
frames[0].save(
    "facescan3_laser.gif",
    save_all=True,
    append_images=frames[1:],
    duration=gif.info['duration'],
    loop=0,
    disposal=2,
    transparency=0
)
print("GIF с лазерным эффектом сохранен как facescan3_laser.gif") # Примечание: Убедись, что у тебя установлен Pillow: pip install Pillow
