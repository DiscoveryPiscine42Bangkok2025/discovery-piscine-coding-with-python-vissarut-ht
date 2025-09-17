def main(board: str):
    try:
        str_board = board.replace(" ", "").upper()
        arr_board = str_board.split("\n")
        point = {}
        point_checked = []
        for y in range(len(arr_board)):
            for x in range(len(arr_board[y])):
                point[(x, y)] = arr_board[y][x]
                if arr_board[y][x] == "P":
                    point_checked.extend([(x-1, y-1),(x+1, y-1)])
                elif arr_board[y][x] == "B":
                        for i in range(len(arr_board)):
                            for j in range(len(arr_board[i])):
                                if (i+j == y+x or i-j == y-x) and ((j, i) != (x, y)):
                                    point_checked.append((j, i))
                elif arr_board[y][x] == "R":
                        for i in range(len(arr_board)):
                            for j in range(len(arr_board[i])):
                                if (i == y or j == x) and ((j, i) != (x, y)):
                                    point_checked.append((j, i))
                elif arr_board[y][x] == "Q": 
                        for i in range(len(arr_board)):
                            for j in range(len(arr_board[i])):
                                if ((i == y or j == x) or (i+j == y+x or i-j == y-x)) and ((j, i) != (x, y)):
                                    point_checked.append((j, i))                              
            #     print(f"{list(point.items())[-1]}", end="")
            # print()
        
        point = {coor: ("X" if coor in point_checked and val in [".", "K"] else val) for coor, val in point.items()}
        
        # # uncomment to see the check board
        # print("======================================")
        # for y in range(len(arr_board)):
        #     for x in range(len(arr_board[y])):
        #         print(f"{point[(x, y)]}", end=" ")
        #     print()
        # print("======================================")
        
        if "K" in list(point.values()) or "K" not in str_board:
            print("Fail")
        else:
            print("Success")
    except:
        print()