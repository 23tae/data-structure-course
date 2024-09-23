def is_stack_full():
    global SIZE, top

    if SIZE > top - 1:
        return False
    return True


def is_valid_range(idx):
    if top >= idx and idx >= 0:
        return True
    return False


def push_stack(element):
    global stack, SIZE, top

    if is_stack_full() == True:
        print("스택에 공간이 없습니다.")
        return
    stack[top + 1] = element
    top += 1


def pop_stack(index):
    global stack, top, SIZE
    is_popped = False

    if is_valid_range(index) == False:
        print("index가 잘못 입력됐습니다.")
        return

    for i in range(top + 1):
        if index != i:
            if is_popped == True:
                if i < SIZE - 1:
                    stack[i] = stack[i+1]
            continue
        data = stack[i]
        if i == SIZE - 1:
            stack[i] = None
        else:
            stack[i] = stack[i+1]
        is_popped = True
        top -= 1
    return data


def pop_all():
    result = ""
    for i in range(top, -1, -1):
        char = pop_stack(i)
        result += char
    return result


def pop_all():
    result = ""
    for i in range(top, -1, -1):
        char = pop_stack(i)
        result += str(char)
    return result


def reverse_word(word):
    word_len = len(word)
    new_word = ""
    for i in range(word_len):
        push_stack(word[i])
        print(stack)
    for i in range(word_len - 1, -1, -1):
        char = pop_stack(i)
        new_word += char
    return new_word


SIZE = 10
stack = [None] * SIZE
top = -1


def is_palindrome(word):
    new_word = reverse_word(word)
    if word == new_word:
        return True
    return False


input_word = input("검사할 단어: ")
print()
res_bool = is_palindrome(input_word)
res_str = "Yes" if res_bool == True else "No"
print()
print(res_str)
