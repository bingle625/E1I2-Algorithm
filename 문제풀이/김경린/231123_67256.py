def solution(numbers, hand):
    answer = []
    left = [0, 3]
    right = [2, 3]
    pos_dict = {1: [0,0], 2: [1, 0], 3: [2, 0], 4: [0, 1], 5: [1, 1], 6: [2, 1], 7: [0, 2], 8: [1, 2], 9: [2, 2], '*': [0, 3], 0: [1, 3], '#': [2, 3]}    
    for number in numbers:
        if number % 3 == 1:
            answer.append('L')
            left = pos_dict[number]
        elif number % 3 == 2 or number == 0:
            current = pos_dict[number]
            distance_l = abs(current[0] - left[0]) + abs(current[1] - left[1])
            distance_r = abs(current[0] - right[0]) + abs(current[1] - right[1])
            if distance_l < distance_r:
                left = current
                answer.append('L')
            elif distance_l > distance_r:
                right = current
                answer.append('R')
            else:
                if hand == "right":
                    right = current
                    answer.append('R')
                else:
                    left = current
                    answer.append('L')
        else:
            answer.append('R')
            right = pos_dict[number]

    return ''.join(answer)