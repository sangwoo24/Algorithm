def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            num = int(s)
            return True
        except:
            return False

    else:
        return False