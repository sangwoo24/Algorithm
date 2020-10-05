def solution(phone_book):
    book = dict()

    for i in range(len(phone_book)):
        book[i] = phone_book[i]

    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j and book[i] == book[j][:len(book[i])]:
                return False
            else:
                continue
    return True