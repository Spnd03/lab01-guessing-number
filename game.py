import random

def get_player_guess():
    pass  # นักศึกษาคนที่ 1 เขียนที่นี่

def check_guess(secret_number, player_guess):
    pass  # นักศึกษาคนที่ 2 เขียนที่นี่

def play_game():
    secret_number = random.randint(1, 100)
    while True:
        guess = get_player_guess()
        result = check_guess(secret_number, guess)
        if result == "ถูกต้อง":
            print("ยินดีด้วย! คุณทายถูกต้องแล้ว")
            break
        else:
            print(result)

# play_game()
