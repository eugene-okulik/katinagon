class Flower:
    def __init__(self, name, petals_color, height, freshness, lifetime, cost):
        self.name = name
        self.petals_color = petals_color
        self.height = height
        self.freshness = freshness
        self.lifetime = lifetime
        self.cost = cost

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Rose(Flower):

    def __init__(self, name, petals_color, height, freshness, lifetime, cost):
        super().__init__(name, petals_color, height, freshness, lifetime, cost)


class Lily(Flower):

    def __init__(self, name, petals_color, height, freshness, lifetime, cost):
        super().__init__(name, petals_color, height, freshness, lifetime, cost)


class Tulip(Flower):

    def __init__(self, name, petals_color, height, freshness, lifetime, cost):
        super().__init__(name, petals_color, height, freshness, lifetime, cost)


class Bouquet:
    def __init__(self, *args):
        self.flowers = [*args]
        self.__wilting_time = self.__wilting_time()
        self.__bouquet_cost = self.__bouquet_cost()

    def __wilting_time(self):
        return round(sum(flower.lifetime for flower in self.flowers) / len(self.flowers))

    def __bouquet_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def sorted_by_color(self):
        sorted_flowers = sorted(self.flowers, key=lambda flower: flower.petals_color)
        return f"Отсортированный список цветов по цвету: {sorted_flowers}"

    def sorted_by_freshness(self):
        sorted_flowers = sorted(self.flowers, key=lambda flower: flower.freshness)
        return f"Отсортированный список цветов по свежести: {sorted_flowers}"

    def sorted_by_height(self):
        sorted_flowers = sorted(self.flowers, key=lambda flower: flower.height)
        return f"Отсортированный список цветов по высоте: {sorted_flowers}"

    def sorted_by_cost(self):
        sorted_flowers = sorted(self.flowers, key=lambda flower: flower.cost)
        return f"Отсортированный список цветов по цене: {sorted_flowers}"

    def search_by_lifetime(self, lifetime):
        sorted_flowers = [flower for flower in self.flowers if flower.lifetime == lifetime]
        if sorted_flowers:
            return f"Цветы c параметром lifetime {lifetime} в букете: {sorted_flowers}"
        else:
            return f"В букете нет цветов с параметром lifetime {lifetime}"

    @property
    def wilting_time(self):
        return self.__wilting_time

    @property
    def bouquet_cost(self):
        return self.__bouquet_cost


yellow_lily = Lily('yellow_lily', 'yellow', 30, False, 10, 160)
red_rose = Rose('red_rose', 'red', 60, True, 12, 250)
white_tulip = Tulip('white_tulip', 'white', 25, False, 8, 194)
bouquet1 = Bouquet(yellow_lily, red_rose, white_tulip)
print(f"Среднее время увядания букета около {bouquet1.wilting_time} дней")
print(f"Стоимость букета {bouquet1.bouquet_cost} руб.")
print(bouquet1.sorted_by_color())
print(bouquet1.sorted_by_freshness())
print(bouquet1.sorted_by_height())
print(bouquet1.sorted_by_cost())
print(bouquet1.search_by_lifetime(10))
