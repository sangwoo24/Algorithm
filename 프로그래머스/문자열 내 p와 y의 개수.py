def solution(s):
    if s.count('P') + s.count('p') == s.count('y') + s.count('Y'):
        return True
    else:
        return False