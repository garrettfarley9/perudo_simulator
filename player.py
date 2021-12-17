import random
class Game():
    #Constructor
    def __init__(self, total_players = 0, total_dice = 0):
        '''
        Constructs a game of Perudo
        :param total_players: number of players
        :type total_players: int
        :param total_dice: the total number of dice
        :type total_dice: int
        :returns: nothing
        '''
        self._total_players = total_players
        if total_dice == 0:
            self._total_dice = total_players * 5
        else: self._total_dice = total_dice
    #Getters
    def get_total_players(self):
        '''
        Gets the number of players
        :param total_players: number of players
        :type total_players: int
        :returns: number of players
        :rtype: int
        '''
        return int(self._total_players)
    
    def get_total_dice(self):
        '''
        Gets the number of dice
        :param total_dice: number of dice
        :type total_dice: int
        :returns: number of dice
        :rtype: int
        '''
        return int(self._total_dice)
    #Setters
    
    
    #Methods
    def next_round(self):
        self._total_dice -= 1
        
    def player_out(self):
        self._total_players -= 1

class Player(Game):
    #Constructor
    def __init__(self, dice_num = 0, dice_rolls = []):
        '''
        Constructs a Player object
        :param dice_num: number of dice a player has
        :type dice_num: int
        :returns: nothing
        '''
        self._dice_num = dice_num
        self._dice_rolls = dice_rolls
        self.roll_dice()
    
    #Getters
    def get_dice_num(self):
        '''
        Gets the number of dice
        :param dice_num: number of dice
        :type dice_num: int
        :returns: number of dice
        :rtype: int
        '''
        return int(self._dice_num)
    
    def get_dice_rolls(self):
        '''
        Gets the dice roll values
        :param dice_rolls: roll values
        :type dice_rolls: list
        :returns: roll values
        :rtype: list
        '''
        return self._dice_rolls
    #Setters
    def set_dice_num(self, dice_num = 0):
        '''
        Updates the number of dice
        :param dice_num: number of dice
        :type dice_num: int
        :returns: nothing
        '''
        self._dice_num = dice_num
    
    def set_dice_rolls(self, dice_rolls = []):
        '''
        Updates the dice roll values
        :param dice_rolls: roll values
        :type dice_rolls: list
        :returns: nothing
        '''
        self._dice_rolls = dice_rolls
    #Overrides
    # def __str__(self):
    #     return get_dice(self)
    
    #Methods
    def roll_dice(self):
        ##Roll the number of dice the class object has
        x = list(range(0, self.get_dice_num()))
        for i in x: 
            self._dice_rolls.append(random.randint(1,6))

    # def palifico(self):
    #     if self._dice_num == 1:
    #         pass

test = Player(dice_num = 5)

print(test.get_dice_rolls())
