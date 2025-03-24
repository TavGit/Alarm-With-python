import time 
import pygame

def atur_alarm(durasi):
    print(f"Alarm akan berbunyi dalam {durasi} detik.")

    for i in range(durasi, 0, -1):
        menit, detik = divmod(i, 60)
        waktu_str = f"{menit:02d} : {detik:02d}"
        print(f"Sisa waktu:  {waktu_str}", end="\r")
        time.sleep(1)
    
    print("\nAlarm berbunyi!")

    pygame.mixer.init()
    pygame.mixer.music.load("Alarm sound.mp3")  # Ganti dengan path ke file suara yang ingin Anda gunakan
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    try:
        waktu = int(input("Masukkan durasi alarm (dalam detik): "))
        atur_alarm(waktu)
    except ValueError:
        print("Masukkan angka yang valid untuk durasi.")