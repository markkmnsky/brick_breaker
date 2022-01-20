
from base import Base
from setup import *
from brick import Brick
import math

class Ball:
    radius = 5
    color = (255,255,255)
    
    
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0.5)

    def ballWindow_EdgeCollision(self):

        ballLeft = self.position.x - self.radius
        ballRight = self.position.x + self.radius
        ballTop = self.position.y - self.radius
        ballBottom = self.position.y + self.radius

        if ballRight > WINDOW_WIDTH:
            if self.velocity.x > 0:
                self.velocity.x *= -1

        if ballLeft < 0:
            if self.velocity.x < 0:
                self.velocity.x *= -1

        if ballBottom > WINDOW_HEIGHT:
            if self.velocity.y > 0:
                self.velocity.y *= -1

        if ballTop < 0:
            if self.velocity.y < 0:
                self.velocity.y *= -1

    
    def entity_SweepCollision(self, entity):

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

    def sweptBroadphaseBox(self, delta_time):
        min_x = min(self.position.x, self.position.x + self.velocity.x * delta_time) - self.radius
        min_y = min(self.position.y, self.position.y + self.velocity.y * delta_time) - self.radius
        max_x = max(self.position.x, self.position.x + self.velocity.x * delta_time) + self.radius
        max_y = max(self.position.y, self.position.y + self.velocity.y * delta_time) + self.radius
        #global screen
        return pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)

    def Entity_EdgeCollision(self, base, bricks, deltaTime):
        broadphaseBox = self.sweptBroadphaseBox(deltaTime)
        baseBox = pygame.Rect(base.position.x, base.position.y, base.width, base.height)

        collisionType = None
        
        if broadphaseBox.colliderect(baseBox):
            collisionNormal, collisionTime = self.entity_SweepCollision(base)
            if collisionTime < 1:
                collisionType = Base
        else:
            collisionNormal, collisionTime = pygame.Vector2(), 1

        if collisionTime >= 1:
            for row in bricks:
                keepSearching = True
                for brick in row:
                    brickBox = pygame.Rect(brick.position.x, brick.position.y, brick.width, brick.height)
                    if broadphaseBox.colliderect(brickBox):
                        collisionNormal, collisionTime = self.entity_SweepCollision(brick)
                        if collisionTime < 1:
                            row.remove(brick)
                            collisionType = Brick
                            keepSearching = False
                            break
                if not keepSearching:
                    break
            else:
                collisionNormal, collisionTime = pygame.Vector2(), 1


        self.position += self.velocity * collisionTime * deltaTime
        remainingTime = 1 - collisionTime

        if collisionType == Base:
            if collisionNormal.x != 0:
                self.velocity.x *= -1


            # vertical collision
            if collisionNormal.y != 0:
                baseCenterPos = base.position.x + base.width /2
                ballCenterPos = self.position.x
                centerPosDistance = (ballCenterPos - baseCenterPos)/(base.width / 2)

                normal = collisionNormal.rotate(centerPosDistance * 10)
                self.velocity.reflect_ip(normal)

        elif collisionType == Brick:
            self.velocity.reflect_ip(collisionNormal)

        self.position += self.velocity * remainingTime * deltaTime
        
    def update(self, deltaTime, base, bricks):
        self.Entity_EdgeCollision(base, bricks, deltaTime)
        self.ballWindow_EdgeCollision()
    
    def draw(self, window):
        pygame.draw.circle(
            window,
            self.color, 
            (self.position.x, self.position.y), 
            self.radius,
        )

        