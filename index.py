import random
import string
import requests
import time

# توليد يوزر عشوائي
def generate_username(length=4):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

# التحقق من توفر يوزر على انستجرام كمثال
def check_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    if response.status_code == 404:
        return True  # متوفر
    else:
        return False  # محجوز

# البرنامج الأساسي
def main():
    while True:
        username = generate_username(length=random.choice([3, 4]))
        if check_instagram(username):
            print(f"[متوفر] {username}")
            with open("available.txt", "a") as f:
                f.write(username + "\n")
        else:
            print(f"[محجوز] {username}")
        time.sleep(1)  # تأخير عشان ما يحظرك انستجرام

if __name__ == "__main__":
    main()
