# 프로그래머스: 동영상 재생기 (**다시보기!)
## 사용자 입력에 대한 문자열 배열 commands, 입력이 모두 끝난 후 동영상 위치를 mm:ss 형식으로 출력
## next: 현 위치에서 10초 뒤, prev: 10초 후

def solution(video_len, pos, op_start, op_end, commands):
    # mm:ss → 초 단위 변환
    def to_seconds(time_str):
        mm, ss = map(int, time_str.split(":"))
        return mm * 60 + ss

    # 초 단위 → mm:ss 변환
    def to_time_str(seconds):
        mm, ss = divmod(seconds, 60)
        return f"{mm:02}:{ss:02}"

    # 변환
    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)

    # 오프닝 건너뛰기 함수
    def skip_opening(cur):
        if op_start <= cur <= op_end:
            return op_end
        return cur

    # 시작 위치에서도 오프닝 체크
    pos = skip_opening(pos)

    # 명령어 실행
    for cmd in commands:
        if cmd == "next":
            pos = min(video_len, pos + 10)
        elif cmd == "prev":
            pos = max(0, pos - 10)
        pos = skip_opening(pos)  # 이동 후 오프닝 체크

    return to_time_str(pos)
