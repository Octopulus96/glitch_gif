import os
import random
import numpy as np
from PIL import Image, ImageDraw
import imageio


def generate_glitch_frame(width, height, colors):
    """Создает кадр с глитч-эффектом."""
    frame = Image.new("RGB", (width, height), color=random.choice(colors))
    draw = ImageDraw.Draw(frame)

    # Добавляем случайные полосы и искажения
    for _ in range(random.randint(5, 20)):
        x_start = random.randint(0, width - 1)
        y_start = random.randint(0, height - 1)
        x_end = random.randint(x_start, width)
        y_end = y_start + random.randint(1, 10)  # Горизонтальные полосы

        color = random.choice(colors)
        draw.rectangle([x_start, y_start, x_end, y_end], fill=color)

    # Добавляем шум
    np_frame = np.array(frame)
    noise = np.random.randint(0, 50, (height, width, 3), dtype=np.uint8)
    np_frame = np.clip(np_frame + noise, 0, 255)

    return Image.fromarray(np_frame.astype("uint8"))


def generate_glitch_gif(output_path, width=500, height=500, frames=30, colors=None):
    """Генерирует GIF с глитч-эффектом."""
    if colors is None:
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0), (255, 255, 255)]

    gif_frames = []
    for _ in range(frames):
        frame = generate_glitch_frame(width, height, colors)
        gif_frames.append(frame)

    # Сохраняем как GIF
    gif_frames[0].save(
        output_path, save_all=True, append_images=gif_frames[1:], duration=100, loop=0
    )


if __name__ == "__main__":
    output_file = "glitch_art.gif"
    generate_glitch_gif(output_file)
    print(f"Глитч-GIF сохранен в {output_file}")
