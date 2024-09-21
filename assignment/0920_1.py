def find_and_insert_data(friend, k_count):
    find_pos = -1
    for i in range(len(katok)):
        pair = katok[i]
        if k_count >= pair[1]:
            find_pos = i
            break
    if find_pos == -1:
        find_pos = len(katok)
    insert_data(find_pos, (friend, k_count))


def insert_data(position, friend_data):
    katok.append(None)
    k_len = len(katok)

    for i in range(k_len - 1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend_data


katok = [('민수', 200), ('철희', 190), ('영재', 180), ('경수', 30)]

if __name__ == "__main__":
    while True:
        data = input("추가할 친구: ")
        count = int(input("카톡 획수: "))
        find_and_insert_data(data, count)
        print(katok)
