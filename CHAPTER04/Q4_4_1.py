vote_num = 0


def vote():
    global vote_num
    vote_num += 1


def reset_box():
    global vote_num
    vote_num = 0


def check_box():
    global vote_num
    return vote_num
