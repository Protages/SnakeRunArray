def solution(arr):
    res = list()
    y_bord_h = y_bord_l = x_bord_r = x_bord_l = x = y = 0
    direction_x = 'right'
    direction_y = 'down'
    direction_mov = 'x'
    for i in range(len(arr) * len(arr[0])):
        if direction_mov == 'x':
            if direction_x == 'right':
                res.append(arr[y][x])
                x += 1
                if x >= len(arr[0]) - x_bord_r:
                    x -= 1
                    direction_x = 'left'
                    y_bord_h += 1
                    direction_mov = 'y'
                    y += 1
            else:
                res.append(arr[y][x])
                x -= 1
                if x < 0 + x_bord_l:
                    x += 1
                    direction_x = 'right'
                    y_bord_l += 1
                    direction_mov = 'y'
                    y -= 1
        else:
            if direction_y == 'down':
                res.append(arr[y][x])
                y += 1
                if y >= len(arr) - y_bord_l:
                    y -= 1
                    direction_y = 'up'
                    x_bord_r += 1
                    direction_mov = 'x'
                    x -= 1
            else:
                res.append(arr[y][x])
                y -= 1
                if y < 0 + y_bord_h:
                    y += 1
                    direction_y = 'down'
                    x_bord_l += 1
                    direction_mov = 'x'
                    x += 1
    return res


arr = [
    ['0', '1', '2', '3', '4'],
    ['19', '20', '21', '22', '5'],
    ['18', ' 31', '32', '23', '6'],
    ['17', '30', '33', '24', '7'],
    ['16', '29', '34', '25', '8'],
    ['15', '28', '27', '26', '9'],
    ['14', '13', '12', '11', '10']
]
print(solution(arr))


for a in arr:
    print(''.join('%3s' % b for b in a))
