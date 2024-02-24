import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
         title = "**Drink WATER now**",
         message = "Be hydrated it helps your body to regulating body temperature and protecting organs and tissues ",
         app_icon = "C:\Users\ADMIN\Desktop\icon.ico",
         timeout =12
    )
        time.sleep(60*60)