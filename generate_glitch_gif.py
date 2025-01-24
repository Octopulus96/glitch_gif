import os
import random
import numpy as np
from typing import List, Optional
from PIL import Image, ImageDraw


class GlitchArtGenerator:
    def __init__(
        self,
        width: int = 500,
        height: int = 500,
        colors: Optional[List[tuple[int, int, int]]] = None,
        frames: int = 30,
        noise: bool = False,
    ):
        """Инициализация генератора глитч-арта."""
        self.width = width
        self.height = height
        self.colors = (
            colors
            if colors
            else [
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                for _ in range(10)
            ]
        )
        self.frames = frames
        self.noise = noise

    def add_noise(self, frame: Image.Image) -> Image.Image:
        """Добавляет шум к кадру."""
        # Преобразуем изображение в массив numpy
        np_frame = np.array(frame)

        # Генерируем случайный шум
        noise = np.random.randint(0, 10, (self.height, self.width, 3), dtype=np.uint8)

        # Добавляем шум к кадру и ограничиваем значения пикселей (чтобы они оставались в допустимом диапазоне)
        np_frame = np.clip(np_frame + noise, 0, 255)

        # Возвращаем кадр с добавленным шумом
        return Image.fromarray(np_frame.astype("uint8"))

    def generate_glitch_frame(self) -> Image.Image:
        """Создает кадр с глитч-эффектом."""
        frame = Image.new(
            "RGB", (self.width, self.height), color=random.choice(self.colors)
        )
        draw = ImageDraw.Draw(frame)

        # Добавляем случайные горизонтальные полосы и искажения
        for _ in range(random.randint(5, 50)):
            x_start = random.randint(0, self.width - 1)
            y_start = random.randint(0, self.height - 1)
            x_end = random.randint(x_start, self.width)
            y_end = y_start + random.randint(1, 10)  # Горизонтальные полосы

            color = random.choice(self.colors)
            draw.rectangle([x_start, y_start, x_end, y_end], fill=color)

        # Добавляем случайные вертикальные полосы и искажения
        for _ in range(random.randint(5, 50)):
            x_start = random.randint(0, self.width - 1)
            y_start = random.randint(0, self.height - 1)
            x_end = x_start + random.randint(1, 10)  # Вертикальные полосы
            y_end = random.randint(y_start, self.height)

            color = random.choice(self.colors)
            draw.rectangle([x_start, y_start, x_end, y_end], fill=color)

        # Добавляем круги
        for _ in range(random.randint(5, 20)):
            x_center = random.randint(0, self.width)
            y_center = random.randint(0, self.height)
            radius = random.randint(10, 50)
            color = random.choice(self.colors)
            draw.ellipse(
                [
                    (x_center - radius, y_center - radius),
                    (x_center + radius, y_center + radius),
                ],
                fill=color,
            )

        # Добавляем эллипсы
        for _ in range(random.randint(5, 15)):
            x_start = random.randint(0, self.width - 1)
            y_start = random.randint(0, self.height - 1)
            x_end = random.randint(x_start, self.width)
            y_end = random.randint(y_start, self.height)
            color = random.choice(self.colors)
            draw.ellipse([x_start, y_start, x_end, y_end], fill=color)

        # Добавляем треугольники
        for _ in range(random.randint(3, 10)):
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)
            x3 = random.randint(0, self.width)
            y3 = random.randint(0, self.height)
            color = random.choice(self.colors)
            draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=color)

        # Добавляем шум
        frame_with_noise = self.add_noise(frame)
        if self.noise == True:
            frame_with_noise = self.add_noise(frame)
            return frame_with_noise
        else:
            return frame

    def generate_glitch_gif(self, output_path: str) -> None:
        """Генерирует GIF с глитч-эффектом."""
        gif_frames = []
        for _ in range(self.frames):
            frame = self.generate_glitch_frame()
            gif_frames.append(frame)

        # Сохраняем как GIF
        gif_frames[0].save(
            output_path,
            save_all=True,
            append_images=gif_frames[1:],
            duration=100,
            loop=0,
        )


# Пример использования
if __name__ == "__main__":
    output_file = "glitch_art.gif"

    # Создаем объект генератора глитч-арта
    glitch_generator = GlitchArtGenerator(width=500, height=500, frames=30)

    # Генерируем и сохраняем GIF
    glitch_generator.generate_glitch_gif(output_file)

    print(f"Глитч-GIF сохранен в {output_file}")
