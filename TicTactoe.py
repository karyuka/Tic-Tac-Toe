import random


class Tic:
    
    def __init__(self):
        print("Lets start Tic Tac Toe Game!")
        self.arr = [None for i in range(9)]
        self.insertion = {0: "up left", 1: "up middle", 2: "up right", 3: "middle left", 4: "middle middle", 5: "middle right", 6: "down left", 7: "down middle", 8: "down right"}

    def play(self):
        res = self.present()
        while not self.determine():
            res = self.insert(int(res))
            
     
    def present(self):
        print("Choose One Number!")
        for pos, value in self.insertion.items():
            print(f"\n{pos} for {value}\n")
        res = input()
        return int(res)
    

    def insert(self, pos):
        while pos not in self.insertion.keys():
            pos = self.present()
        
        self.arr[pos] = "x"
        print(f"You inserted in {self.insertion[pos]}\n")
        self.insertion.pop(pos)

        bot = random.choice(list(self.insertion.keys()))
        self.arr[bot] = "o"
        print(f"Computer inserted in {self.insertion[bot]}\n")
        self.insertion.pop(bot)

        count = 0
        for i in range(0, len(self.arr), 3):
            if count == 3:
                print("\n")
                count = 0
            count += 1
            print(self.arr[i], self.arr[i+1], self.arr[i+2])

        return "12"



    def determine(self):
        for i in range(3):
            if self.arr[i] == self.arr[i+3] and self.arr[i] == self.arr[i+6] and self.arr[i] != None:
                if self.arr[i] == "x":
                    print("You Won!")
                else:
                    print("The Computer Won!")
                return True
        
        for i in range(0, 9, 3):
            if self.arr[i] == self.arr[i+1] and self.arr[i] == self.arr[i+2] and self.arr[i] != None:
                if self.arr[i] == "x":
                    print("You Won!")
                else:
                    print("The Computer Won!")
                return True

        if self.arr[0] == self.arr[4] and self.arr[0] == self.arr[8] and self.arr[0] != None:
            if self.arr[2] == "x":
                print("You Won!")
            else:
                print("Computer Won!")
            return True

        if self.arr[2] == self.arr[4] and self.arr[2] == self.arr[6] and self.arr[2] != None:
            if self.arr[2] == "x":
                print("You Won!")
            else:
                print("Computer Won!")
            return True

        return False



game = Tic()
game.play()