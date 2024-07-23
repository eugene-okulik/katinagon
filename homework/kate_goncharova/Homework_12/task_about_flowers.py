class Flower:
    def __init__(self, petals_color, height, freshness, lifetime, cost):
        self.petals_color = petals_color
        self.height = height
        self.freshness = freshness
        self.lifetime = lifetime
        self.cost = cost


class Rose(Flower):
    name = 'rose'

    def __init__(self, petals_color, height, freshness, lifetime, cost):
        super().__init__(petals_color, height, freshness, lifetime, cost)


class Lily(Flower):
    name = 'lily'

    def __init__(self, petals_color, height, freshness, lifetime, cost):
        super().__init__(petals_color, height, freshness, lifetime, cost)


class Tulip(Flower):
    name = 'tulip'

    def __init__(self, petals_color, height, freshness, lifetime, cost):
        super().__init__(petals_color, height, freshness, lifetime, cost)


class Bouquet:
    def __init__(self, *args):
        self.flowers = [*args]
        self.__wilting_time = self.__wilting_time()
        self.__bouquet_cost = self.__bouquet_cost()

    def __wilting_time(self):
        return round(sum(flower.lifetime for flower in self.flowers) / len(self.flowers))

    def __bouquet_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def sorted_by_color(self, color):
        sorted_flowers = [flower.name for flower in self.flowers if flower.petals_color == color]
        if sorted_flowers:
            return f"Цветы c параметром color {color} в букете: {', '.join(sorted_flowers)}"
        else:
            return f"В букете нет цветов с параметром color {color}"

    def sorted_by_freshness(self, freshness):
        sorted_flowers = [flower.name for flower in self.flowers if flower.freshness == freshness]
        if sorted_flowers:
            return f"Цветы c параметром freshness {freshness} в букете: {', '.join(sorted_flowers)}"
        else:
            return f"В букете нет цветов с параметром freshness {freshness}"

    def sorted_by_height(self, height):
        sorted_flowers = [flower.name for flower in self.flowers if flower.height == height]
        if sorted_flowers:
            return f"Цветы c параметром height {height} в букете: {', '.join(sorted_flowers)}"
        else:
            return f"В букете нет цветов с параметром height {height}"

    def sorted_by_cost(self, cost):
        sorted_flowers = [flower.name for flower in self.flowers if flower.cost == cost]
        if sorted_flowers:
            return f"Цветы c параметром cost {cost} в букете: {', '.join(sorted_flowers)}"
        else:
            return f"В букете нет цветов с параметром cost {cost}"

    def search_by_lifetime(self, lifetime):
        sorted_flowers = [flower.name for flower in self.flowers if flower.lifetime == lifetime]
        if sorted_flowers:
            return f"Цветы c параметром lifetime {lifetime} в букете: {', '.join(sorted_flowers)}"
        else:
            return f"В букете нет цветов с параметром lifetime {lifetime}"

    @property
    def wilting_time(self):
        return self.__wilting_time

    @property
    def bouquet_cost(self):
        return self.__bouquet_cost


yellow_lily = Lily('yellow', 30, False, 10, 160)
red_rose = Rose('red', 60, True, 12, 250)
white_tulip = Tulip('red', 25, True, 8, 194)
bouquet1 = Bouquet(yellow_lily, red_rose, white_tulip)
print(f"Среднее время увядания букета около {bouquet1.wilting_time} дней")
print(f"Стоимость букета {bouquet1.bouquet_cost} руб.")
print(bouquet1.sorted_by_color('yellow'))
print(bouquet1.sorted_by_freshness(True))
print(bouquet1.sorted_by_height(25))
print(bouquet1.sorted_by_cost(250))
print(bouquet1.search_by_lifetime(10))
