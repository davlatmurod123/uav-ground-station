import time, math, random

lat0, lon0 = 25.2048, 55.2708   # старт (Дубай)
battery = 100.0
t = 0

while battery > 0:
    alt = min(100, t * 5)                          # набор высоты до 100 м
    speed = 12 + random.uniform(-1, 1)             # скорость м/с
    lat = lat0 + 0.0005 * math.sin(t / 20)         # полёт по кругу
    lon = lon0 + 0.0005 * math.cos(t / 20)
    battery -= 0.2
    temp = 30 + t * 0.05 + random.uniform(-0.5, 0.5)
    link = "OK" if random.random() > 0.05 else "LOST"

    print(f"t={t:3d}s | alt={alt:5.1f}m | spd={speed:4.1f}m/s | "
          f"lat={lat:.5f} lon={lon:.5f} | bat={battery:5.1f}% | "
          f"temp={temp:4.1f}C | link={link}")
    t += 1
    time.sleep(1)