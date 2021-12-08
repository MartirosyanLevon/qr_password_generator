import random
import qrcode


def generate_password(n_characters):
    lower = 'abcdefghiklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    numbers = '12345678901234567890'
    symbols = '!"#$%&/()={}[]'
    all_characters = lower + upper + numbers + symbols

    password = ''.join(random.sample(all_characters,n_characters))
    return  password


def image_qr(password):
    filename = input('Digit name password: ')
    img = qrcode.make(password)
    img.save(filename + '.png')


def run():
    characters = int(input('Digit number of characters: '))
    password = generate_password(characters)
    print(f'Your new password is: {password}')
    image_qr(password)
    print('the password was save as QR Code image')

if __name__ == '__main__':
    run()