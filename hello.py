from time import sleep
class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = bool(adult_mode)
class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None
    def log_in(self, nickname, password):
        if nickname in self.users:
            if self.users[nickname][0] == password:
                self.current_user = nickname
            else:
                print("Неправильный пароль или никнейм")
        else:
            print("Неправильный пароль или никнейм")
    def register(self, nickname, password, age):
        if str(nickname) in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users[str(nickname)] = [hash(password), int(age)]
            self.current_user = nickname
    def log_out(self):
        self.current_user = None
    def add(self, *video):
        for i in video:
            if i.title in self.videos:
                print("Видео с таким названием уже существует")
            else:
                self.videos[i.title] = [i.duration, i.time_now, i.adult_mode]
    def get_videos(self, word):
        video_list = []
        for i in self.videos:
            if word.upper() in i.upper():
                video_list.append(i)
        print(video_list)
    def watch_video(self, name):
        if name in self.videos:
            if self.current_user == None:
                print("Войдите в аккаунт, чтобы смотреть видео")
            else:
                if self.videos[name][2] == True:
                    if self.users[self.current_user][1] >= 18:
                        while self.videos[name][1] < self.videos[name][0]:
                            self.videos[name][1] += 1
                            sleep(1)
                            print(self.videos[name][1])
                        print("Конец видео")
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    while self.videos[name][1] <= self.videos[name][0]:
                        self.videos[name][1] += 1
                        sleep(1)
                        print(self.videos[name][1])
                    print("Конец видео")