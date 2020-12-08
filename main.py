from PIL import ImageGrab
import pyautogui


class ScreenProcessing:
    photos_data_dict = {"board": ["Photos/Board.PNG", 0.3],
                        "closed_square": ["Photos/CloseSquare.PNG", 0.65],
                        "open_square": ["Photos/OpenSquare.PNG", 0.780507],
                        "bomb": ["Photos/Bomb.png", 0.6],
                        "one": ["Photos/One.PNG", 0.71],
                        "two": ["Photos/Two.PNG", 0.757],
                        "three": ["Photos/Three.PNG", 0.7],
                        "four": ["Photos/Three.PNG", 0.757]
                        }

    def __init__(self):
        pass

    def get_image_location(self, image):
        return pyautogui.locateAllOnScreen(self.photos_data_dict[image][0], confidence=self.photos_data_dict[image][1])


class Minesweeper:
    processing = ScreenProcessing()
    BOARD_SIZE = 9
    signs = {"open_square": "0",
             "closed_square": "O",
             "one": "1",
             "two": "2",
             "three": "3",
             "four": "4",
             "bomb": "x",
             }

    board = []

    def __init__(self):
        pass

    def create_board(self):
        self.board = []
        print(list(self.processing.get_image_location("board")))
        for square in self.signs:
            locations = self.processing.get_image_location(square)
            for loc in locations:
                self.board.append({"sign": square, "location": loc})
        print(self.board)

    def print_board(self):
        board = sorted(self.board, key=lambda loc: (loc["location"][1], loc["location"][0]))
        print(len(board))
        for y in range(self.BOARD_SIZE):
            for x in range(self.BOARD_SIZE):
                print(self.signs[board[x + y * x]["sign"]], end=' ')
            print()


if __name__ == '__main__':
    # input("Press enter to start!")
    s = ScreenProcessing()
    start = Minesweeper()
    start.create_board()
    start.print_board()
