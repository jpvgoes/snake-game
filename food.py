from turtle import Turtle
import random

class Food(Turtle):
    """
    aqui eu estou deixando uma herança para Food da classe Turtle.
    e na hora de criar a comida estou colocando ela em uma posição aleatoria entre
    no eixo x e y nas medidas aleatorias entre -280 e 280 pq n pode ser -300 e 300
    pq o tamanho da tela é esse.. e ficaria mt colado dos lados.
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
