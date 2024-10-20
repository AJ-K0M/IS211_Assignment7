import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Die:
    def roll(self):
        return random.randint(1, 6)

class PigGame:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.die = Die()
        self.current_player = 0  

    def playTurn(self):
        player = self.players[self.current_player]
        turn_total = 0

        print(f"\n{player.name}'s turn! Current total score: {player.score}")

        while True:
            roll = self.die.roll()
            print(f"{player.name} rolled: {roll}")

            if roll == 1:
                print(f"{player.name} rolled a 1! No points added. Turn over.")
                break  
            else:
                turn_total += roll
                print(f"Turn total so far: {turn_total}, Total game score: {player.score}")

                
                decision = input(f"{player.name}, roll again (r) or hold (h)? ").lower()

                if decision == 'h':
                    player.score += turn_total
                    print(f"{player.name} holds. New total score: {player.score}")
                    break

        
        self.current_player = (self.current_player + 1) % 2

    def gameOver(self):
        return any(player.score >= 100 for player in self.players)

    def play(self):
        print("Welcome to the game of Pig!")
        while not self.gameOver():
            self.playTurn()

        winner = max(self.players, key=lambda p: p.score)
        print(f"\n{winner.name} wins with a score of {winner.score}!")

if __name__ == "__main__":
    random.seed(0)  
   
    player1 = Player("Player 1")
    player2 = Player("Player 2")


    game = PigGame(player1, player2)
    game.play()
