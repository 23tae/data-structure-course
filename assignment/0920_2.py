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


SIZE = 2
stack = [None] * SIZE
top = -1
print(stack)


def reverse_word(word):
    word_len = len(word)
    new_word = ""
    for i in range(word_len):
        push_stack(word[i])
    print(stack)
    for i in range(word_len - 1, -1, -1):
        char = pop_stack(i)
        print(char)
        new_word += char
    return new_word


input_word = "ab"
output_word = reverse_word(input_word)
print(output_word)
