import json

class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        
        # Load high score from file
        self.load_high_score()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        # self.high_score = 0
        self.level = 1
        
    def load_high_score(self):
        """Load high score from file"""
        filename = 'high_score.json'
        try:
            with open(filename, 'r') as f:
                self.high_score = int(json.load(f))
                while self.score != self.high_score:
                    return self.high_score  
        except FileNotFoundError:
            self.high_score = 0
            
    def save_high_score(self):
        """Save the high score to file"""
        filename = 'high_score.json'
        with open(filename, 'w') as f:
            json.dump(self.high_score, f)