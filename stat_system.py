import glob, os
from typing import *

folder: str = os.path.abspath(f'{__file__}/../userinfo')
file_list = glob.glob(f'{folder}/user*.txt')

globals()['joinUser'] = 0

def load_stat() -> dict:
    global file_list
    print(f'{len(file_list)}개의 데이터 파일을 불러옵니다.')  
    user_data = {}
    for f in file_list:
        with open(f, 'r') as file:
            lines = file.readlines()
            userid, hp, mp, gold, exp, level = map(int, [line.strip('\n') for line in lines])
            values = [userid, hp, mp, gold, exp, level]         
            user_data[userid] = values
    print('Completed to load all save data!')
    return user_data

def create_data(user, userid):
    global joinUser
    if joinUser == 1:
        print('이미 데이터가 있는 유저입니다.')
        return '계정 생성에 실패했습니다.'
    else:
        print('신규 유저입니다. 데이터 생성을 시도합니다.')
        with open(f'{folder}/user-{user}.txt', 'w') as file:
            file.write(f'{userid}\n20\n20\n0\n0\n1')
        joinUser = 1  # 데이터 생성 후 joinUser 값을 1로 변경
        print('데이터 생성에 성공하였습니다. 데이터를 다시 불러옵니다.')
        load_stat()
        return '계정 생성에 성공했습니다.'

def save_stat(user, change):
    file_path = f'{folder}/user-{user}.txt'
    changes = {'hp': 1, 'mp': 2, 'gold': 3, 'exp': 4, 'level': 5}
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if change in changes:
        lines[changes[change]] = f'{globals()[change]}\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)

