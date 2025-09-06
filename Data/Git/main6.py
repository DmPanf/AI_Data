from PIL import Image, ImageDraw, ImageSequence

gif = Image.open("facescan3.gif")
frames = []

for i, frame in enumerate(ImageSequence.Iterator(gif)):
    frame = frame.convert("RGBA")
    w, h = frame.size

    bbox = frame.getbbox()
    overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    if bbox:
        x1, y1, x2, y2 = bbox

        # ВРЕМЕННЫЙ тест: нарисовать bbox
        draw.rectangle([x1, y1, x2, y2], outline=(255, 0, 0, 255), width=3)

        # Уголки (ярко-зелёные, толще, хорошо заметные)
        corner_len = 40
        color = (0, 255, 0, 255)

        draw.line([(x1, y1), (x1+corner_len, y1)], fill=color, width=6)
        draw.line([(x1, y1), (x1, y1+corner_len)], fill=color, width=6)

        draw.line([(x2, y1), (x2-corner_len, y1)], fill=color, width=6)
        draw.line([(x2, y1), (x2, y1+corner_len)], fill=color, width=6)

        draw.line([(x1, y2), (x1+corner_len, y2)], fill=color, width=6)
        draw.line([(x1, y2), (x1, y2-corner_len)], fill=color, width=6)

        draw.line([(x2, y2), (x2-corner_len, y2)], fill=color, width=6)
        draw.line([(x2, y2), (x2, y2-corner_len)], fill=color, width=6)

    combined = Image.alpha_composite(frame, overlay)
    frames.append(combined)

frames[0].save(
    "facescan3_debug.gif",
    save_all=True,
    append_images=frames[1:],
    duration=gif.info['duration'],
    loop=0,
    disposal=2
)
print("\nGIF с отладочным оверлеем сохранен как facescan3_debug.gif\n") # Примечание: Убедись, что у тебя установлен Pillow: pip install Pillow
