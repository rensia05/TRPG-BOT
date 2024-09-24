import json

def change_prefix(prf: chr):
    global prefix
    prefix = prf


def bot_prefix() -> chr:
    with open('bot.prefix.json','r') as f:
        prefixes = json.load(f)
        return prefixes[str()]


if __name__ == '__main__':
    print('테스트모드 작동')
else:
    print('봇 시스템이 성공적으로 불러와졌습니다.')
