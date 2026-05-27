# 파일 이름과 문자열을 입력받고, 파일이 있으면
# 그 파일 안에 문자열이 있는지 판별하여,
#  파일 이름과 해당 문자열을 가진 라인을 출력하는 프로그램 작성

import os

folder_path = input("파일이 있는 폴더 경로를 입력하세요: ")
file_name = input("검색할 파일 이름을 입력하세요 (예: sample.txt): ")
keyword = input("검색할 단어를 입력하세요: ")

full_path = os.path.join(folder_path, file_name)

if os.path.isfile(full_path):

    with open(full_path, "r", encoding="utf-8") as f:
        found = False

        for line_num, line in enumerate(f, start=1):
            if keyword in line:
                found = True
                print(f"파일: {file_name}, {line_num}행: {line.strip()}")
        if not found:
            print(f"'{keyword}'를 포함하는 라인이 없습니다.")
else:
    print(f"파일 '{file_name}'이 존재하지 않습니다.")
