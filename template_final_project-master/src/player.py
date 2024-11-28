import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, image):
        """
        Initializes the Player Object 
        Args:
            image: str - path to img file
        """
        self.image = image
        self.contact = False
        
    def movefoward(self):
        """
        Moves the face foward by 1
        Args: None 
        Return: None 
        """
        pass
    
    def moveup(self):
        """
        Moves the face up by 1
        Args: None
        Return: None 
        """
        pass 
    
    def movedown(self):
        """
        Moves the face down by 1 
        Args: None 
        Return: None 
        """
        pass
    
    def checkContact(self):
        """
        Checks for contact of the face with the tube 
        Args: None
        Returns:
            contact: boolean - If the face makes contact with the tubes or the ground it returns True or if not it returns False
        """
        return self.contact