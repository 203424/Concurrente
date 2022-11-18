import pygame

W = 600

class Archer(pygame.sprite.Sprite):
    def __init__(self,team):
        super().__init__()
        self.team = team
        self.images = []            
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_walk1.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_walk2.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack1.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack2.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack3.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack4.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack5.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack6.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack7.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death1.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death2.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death3.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death4.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death5.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death6.png'),(64,64)))
        self.index = 0

        self.image = self.images[self.index]
        if self.team == "red":
            self.rect = self.image.get_rect()
        else:
            self.rect = pygame.Rect(500,0,64,64)
        self.speed = 6
        self.conta = 0

    def walk(self):
        self.index += 1

        if self.index >= 2:
            self.index = 0
        return self.index

    def attack(self):
        self.index += 1
        if self.index >= 8:
            self.index = 2
        return self.index

    def death(self):
        self.index += 1
        if self.index >= 14:
            self.index = 9
        return self.index

    def update(self):
        if self.rect.x > W-64:
            self.speed = -self.speed
        if self.rect.x <= 0:
            self.speed = 6

        self.rect.x += self.speed

        if self.speed != 0: 
            self.speed_initial = self.speed
            self.pos = self.walk()
        else:
            self.pos = self.attack()

        if self.rect.x == W/2:
            self.conta += 1
            if self.conta < 15:
                self.speed = 0
            if self.conta > 15:
                self.speed = self.speed_initial
                self.conta = 0
        self.image = pygame.transform.flip(self.images[self.pos],self.speed_initial > 0,False)

class Knight(pygame.sprite.Sprite):
    def __init__(self,team):
        super().__init__()
        self.team = team
        self.images = []            
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_walk1.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_walk2.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack1.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack2.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack3.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack4.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack5.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack6.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_death1.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_death2.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_death3.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_death4.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_death5.png'),(64,64)))
        self.index = 0

        self.image = self.images[self.index]
        if self.team == "red":
            self.rect = pygame.Rect(0,64,64,64)
        else:
            self.rect = pygame.Rect(500,64,64,64)
        self.speed = 6
        self.conta = 0

    def walk(self):
        self.index += 1

        if self.index >= 2:
            self.index = 0
        return self.index

    def attack(self):
        self.index += 1
        if self.index >= 7:
            self.index = 2
        return self.index

    def death(self):
        self.index += 1
        if self.index >= 14:
            self.index = 8
        return self.index

    def update(self):
        if self.rect.x > W-64:
            self.speed = -self.speed
        if self.rect.x <= 0:
            self.speed = 6

        self.rect.x += self.speed

        if self.speed != 0: 
            self.speed_initial = self.speed
            self.pos = self.walk()
        else:
            self.pos = self.attack()

        if self.rect.x == W/2:
            self.conta += 1
            if self.conta < 15:
                self.speed = 0
            if self.conta > 15:
                self.speed = self.speed_initial
                self.conta = 0
        self.image = pygame.transform.flip(self.images[self.pos],self.speed_initial < 0,False)

class Lancer(pygame.sprite.Sprite):
    def __init__(self,team):
        super().__init__()
        self.team = team
        self.images = []            
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_walk1.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_walk2.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_attack1.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_attack2.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_attack3.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_attack4.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_death1.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_death2.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_death3.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_death4.png'),(64,64)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_death5.png'),(64,64)))
        self.index = 0

        self.image = self.images[self.index]
        if self.team == "red":
            self.rect = pygame.Rect(0,128,64,64)
        else:
            self.rect = pygame.Rect(500,128,64,64)
        self.speed = 6
        self.conta = 0

    def walk(self):
        self.index += 1

        if self.index >= 2:
            self.index = 0
        return self.index

    def attack(self):
        self.index += 1
        if self.index >= 6:
            self.index = 2
        return self.index

    def death(self):
        self.index += 1
        if self.index >= 11:
            self.index = 6
        return self.index

    def update(self):
        if self.rect.x > W-64:
            self.speed = -self.speed
        if self.rect.x <= 0:
            self.speed = 6

        self.rect.x += self.speed

        if self.speed != 0: 
            self.speed_initial = self.speed
            self.pos = self.walk()
        else:
            self.pos = self.attack()

        if self.rect.x == W/2:
            self.conta += 1
            if self.conta < 15:
                self.speed = 0
            if self.conta > 15:
                self.speed = self.speed_initial
                self.conta = 0
        self.image = pygame.transform.flip(self.images[self.pos],self.speed_initial > 0,False)

class Dragon(pygame.sprite.Sprite):
    def __init__(self,team):
        super().__init__()
        self.team = team
        self.images = []            
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run1.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run2.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run3.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run4.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run5.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run6.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack1.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack2.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack3.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack4.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack5.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack6.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack7.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack8.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack9.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack10.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death1.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death2.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death3.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death4.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death5.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death6.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death7.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death8.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death9.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death10.png'),(128,128)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death11.png'),(128,128)))
        self.index = 0

        self.image = self.images[self.index]
        if self.team == "red":
            self.rect = pygame.Rect(0,254,128,128)
        else:
            self.rect = pygame.Rect(500,254,128,128)
        self.speed = 6
        self.conta = 0

    def walk(self):
        self.index += 1

        if self.index >= 6:
            self.index = 0
        return self.index

    def attack(self):
        self.index += 1
        if self.index >= 16:
            self.index = 6
        return self.index

    def death(self):
        self.index += 1
        if self.index >= 27:
            self.index = 16
        return self.index

    def update(self):
        if self.rect.x > W-64:
            self.speed = -self.speed
        if self.rect.x <= 0:
            self.speed = 6

        self.rect.x += self.speed

        if self.speed != 0: 
            self.speed_initial = self.speed
            self.pos = self.walk()
        else:
            self.pos = self.attack()

        if self.rect.x == W/2:
            self.conta += 1
            if self.conta < 15:
                self.speed = 0
            if self.conta > 15:
                self.speed = self.speed_initial
                self.conta = 0
        self.image = pygame.transform.flip(self.images[self.pos],self.speed_initial > 0,False)