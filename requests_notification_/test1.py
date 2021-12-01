from plyer import notification #for getting notification on your PC


with open('input.txt','r') as file:
    out=file.readlines()

notification.notify(
            title = "Weather (toronto)",
            message = ' '.join(out),
            timeout  = 15 #seconds
)