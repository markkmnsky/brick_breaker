### BALL.PY = encompasses everything to do with the ball, 
# including the collision detection across the entirity of the game, 
# and the draw and update methods

# various imports are used to gather data from different parts of the game for calculations
from base import Base
from setup import *
from brick import Brick

class Ball: # main class that is called
    
    # defines some starting variables that define the look, feel, speed of the ball, and also defines where the ball starts
    radius = 7.5
    color = (255,255,255)
    startingX = WINDOW_WIDTH / 2
    startingY = 550
    speed = 0.4
    
    def __init__(self): # initialization of changing variables
        self.position = pygame.Vector2(self.startingX, self.startingY) # where is the ball located? these are the coordinates
        self.velocity = pygame.Vector2(0, self.speed) # what speed is the ball moving at? in which direction?
        self.isDead = False # bool that is used to store information about if the ball has hit the floor, and if action has been taken after the ball has hit the floor
        self.lives = 4 # counter of how many lives are left, editable
        self.timer = 0 # timer var used to temporarily pause the movement of the ball
        self.scoreCounter = 0 # the score counter
        

    def ballWindow_EdgeCollision(self): # this function checks to see if the ball is hitting the edges of the window

        # defining the sides of the ball using some clever math tricks
        ballLeft = self.position.x - self.radius
        ballRight = self.position.x + self.radius
        ballTop = self.position.y - self.radius
        ballBottom = self.position.y + self.radius

        # if the ball is hitting the right side of the window
        if ballRight > WINDOW_WIDTH:
            if self.velocity.x > 0:
                self.velocity.x *= -1
                # reflect velocity

        # if the ball is hitting the left side of the window
        if ballLeft < 0:
            if self.velocity.x < 0:
                self.velocity.x *= -1
                #reflect velocity

        # if the ball is hitting the bottom side of the window
        if ballTop > WINDOW_HEIGHT:
            self.isDead = True
            # the dead status is turned true, which triggers a chain of events later on

        if ballTop < 0:
            if self.velocity.y < 0:
                self.velocity.y *= -1
                #reflect velocity

    
    def entity_SweepCollision(self, entity): # collision detection that checks to see if a collision is possible, and does many collision related calculations

        normal = pygame.Vector2() # zero vector

        # ball bounding box values
        ballRight = self.position.x + self.radius
        ballLeft = self.position.x - self.radius
        ballBottom = self.position.y + self.radius
        ballTop = self.position.y - self.radius
        # base bounding box values
        entityRight = entity.position.x + entity.width
        entityLeft = entity.position.x
        entityBottom = entity.position.y + entity.height
        entityTop = entity.position.y

        # creating default values
        hitTime = 0 # the prediction on when the ball will hit the base
        outTime = 1 # the prediction on when the ball wiill go through and exit the paddle
        overlapTime = pygame.Vector2() # overlap time on each axis

        # we are using the ball's perspective (everything moves in relative to the ball)
        # since we are treating the base as stationary (it is moved beforehand so this is ok)
        # to get the relative velocity of the base from the ball's velocity: 
        # we invert the velocity of the ball 

        v = -self.velocity # the base's velocity is the invert of the ball's velocity

        # x axis overlap ...
        if v.x < 0: # if the base is moving left relative to the ball
            if entityRight < ballLeft: # if the base is on the left of the ball
                return normal, 1 # no collision
            else: # if the base is moving right relative to the ball
                outTime = min((ballLeft - entityRight) / v.x, outTime)

            if ballRight < entityLeft: # if the ball is to the left of the base
                # calculate the normalized hit time on x axis, ranges from 0 to 1
                overlapTime.x = (ballRight - entityLeft) / v.x
                hitTime = max(overlapTime.x, hitTime)

        elif v.x > 0: # if the base is moving right relative to the ball
            if entityLeft > ballRight: # if the base is to the right of the ball
                return normal, 1 # no collision
            else: # if the base is to the left of the ball
                outTime = min((ballRight - entityLeft) /  v.x, outTime)

            if entityRight < ballLeft: # if the ball is to the right of the base
                # calculate the normalized hit time on x axis, ranges from 0 to 1
                overlapTime.x = (ballLeft - entityRight) / v.x
                hitTime = max(overlapTime.x, hitTime)

        # y axis overlap ... 
        if v.y < 0: # if the base is moving up relative to the ball
            if entityBottom < ballTop: # if the base is above the ball
                return normal, 1 # no collision
            else: # if the base is below the ball
                outTime = min((ballTop - entityBottom) / v.y, outTime)

            if ballBottom < entityTop: # if the ball is above the base
                # calculate the normalized hit time on x axis, ranges from 0 to 1
                overlapTime.y = (ballTop - entityBottom) / v.y
                hitTime = max(overlapTime.y, hitTime)
        
        elif v.y > 0: # if the base is moving down relative to the ball
            if entityTop > ballBottom: # if the base is below the ball
                return normal, 1 # no collision
            else: # if the base is above the ball
                outTime = min((ballBottom - entityTop) / v.y, outTime)
            
            if entityBottom < ballTop: # if the ball is below the base
                # calculate the normalized hit time on x axis, ranges from 0 to 1
                overlapTime.y = (ballTop - entityBottom) / v.y
                hitTime = max(overlapTime.y, hitTime)
        
        # if a collision occures we shouldn't hit the object after exiting
        if hitTime > outTime:
            return normal, 1
            
        # calculate hit normal
        if overlapTime.x > overlapTime.y:
            if v.x < 0:
                normal.x = -1
                normal.y = 0
            else:
                normal.x = 1
                normal.y = 0
        else:
            if v.y < 0:
                normal.x = 0
                normal.y = -1
            else:
                normal.x = 0
                normal.y = 1
        
        return normal, hitTime

    def sweptBroadphaseBox(self, delta_time): # creates box around the ball, used for collision detection purposes
        min_x = min(self.position.x, self.position.x + self.velocity.x * delta_time) - self.radius
        min_y = min(self.position.y, self.position.y + self.velocity.y * delta_time) - self.radius
        max_x = max(self.position.x, self.position.x + self.velocity.x * delta_time) + self.radius
        max_y = max(self.position.y, self.position.y + self.velocity.y * delta_time) + self.radius
        #global screen
        return pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)

    def Entity_EdgeCollision(self, base, bricks, deltaTime): # checks to directly see if the edges of two objects are colliding
        # sets variables for convienience
        broadphaseBox = self.sweptBroadphaseBox(deltaTime)
        baseBox = pygame.Rect(base.position.x, base.position.y, base.width, base.height)

        collisionType = None # defines the collision type
        
        # checks to see if the ball is directly colliding with the base, and if true, sets the collision type accordingly
        if broadphaseBox.colliderect(baseBox):
            collisionNormal, collisionTime = self.entity_SweepCollision(base)
            if collisionTime < 1:
                collisionType = Base # collision type: base
        else:
            collisionNormal, collisionTime = pygame.Vector2(), 1

        if collisionTime >= 1: # otherwise, it's likely a collision with a brick: takes according measure                
            for brick in bricks:
                brickBox = pygame.Rect(brick.position.x, brick.position.y, brick.width, brick.height)
                if broadphaseBox.colliderect(brickBox):
                    collisionNormal, collisionTime = self.entity_SweepCollision(brick)
                    if collisionTime < 1:
                        bricks.remove(brick) # removes brick from list
                        collisionType = Brick # sets collision type to brick
                        self.scoreCounter += 1 # adds a point to the score
                        break
            else:
                collisionNormal, collisionTime = pygame.Vector2(), 1


        self.position += self.velocity * collisionTime * deltaTime
        remainingTime = 1 - collisionTime

        if collisionType == Base: # reflect velocity if hit on base
            if collisionNormal.x != 0:
                self.velocity.x *= -1


            # vertical collision
            if collisionNormal.y != 0:
                baseCenterPos = base.position.x + base.width /2
                ballCenterPos = self.position.x
                centerPosDistance = (ballCenterPos - baseCenterPos)/(base.width / 2)

                normal = collisionNormal.rotate(centerPosDistance * 10)
                self.velocity.reflect_ip(normal)

        elif collisionType == Brick: # reflects ball if hits on brick
            self.velocity.reflect_ip(collisionNormal)

        self.position += self.velocity * remainingTime * deltaTime
        
    def reset(self): # function that resets the ball's position, called when game starts, when new level starts, and in update when isDead is true
        self.position = pygame.Vector2(self.startingX, self.startingY)
        self.velocity = pygame.Vector2(0, self.speed)
        self.timer = 0 # resets timer
        # resets everything (position, velocity, timer)
    
    def update(self, deltaTime, base, bricks): # updates all relevant info
        self.timer += deltaTime
        
        if self.isDead == True:
            self.lives -= 1
            self.reset()
            self.isDead = False
            return DEADEVENT

        if self.timer > 2500:   
            self.Entity_EdgeCollision(base, bricks, deltaTime)
            self.ballWindow_EdgeCollision()
    
    def draw(self, window): # draws ball and score on screen
        pygame.draw.circle(
            window,
            self.color, 
            (self.position.x, self.position.y), 
            self.radius,
        )
        self.drawLivesRemaining(window)
    
    
    def drawLivesRemaining(self, window): # score counter in bottom right
        
        for i in range(self.lives - 1) :#subtracts one from the lives count because it shows how many balls you have left, not the internal counter
            pygame.draw.circle(
                window,
                self.color, 
                ((WINDOW_WIDTH - 80) - i * 20, WINDOW_HEIGHT - 25), 
                self.radius,
            )

        