class Animal:
    alive = True    # (живой)
    fed = False     # (накормленный)

    def __init__(self, name):
        self.name = name            # индивидуальное название каждого животного
   

class Mammal(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)


    def eat(self, food):
        self.food = food
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Predator(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)


    def eat(self, food):
        self.food = food
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    edible = False      # (съедобность)

    def __init__(self, name):
        self.name = name            # индивидуальное название каждого растения


class Flower(Plant):
    ...


class Fruit(Plant):
    edible = True




if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)

    # Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.