from encapsulation_exercise.wild_cat_zoo.animal import Animal
from encapsulation_exercise.wild_cat_zoo.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        # for worker in self.workers:
        #     if worker.name == worker_name:
        #         self.workers.remove(worker)
        #         return f"{worker_name} fired successfully"
        # return f"There is no {worker_name} in the zoo"
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        # workers_salaries = 0
        # for worker in self.workers:
        #     workers_salaries += worker.salary
        workers_salaries = sum(w.salary for w in self.workers)
        if workers_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= workers_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_cost = sum(a.money_for_care for a in self.animals)

        if animals_cost > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animals_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda w: w.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda w: w.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda w: w.__class__.__name__ == "Cheetah", self.animals))

        output_string = [
            f'You have {len(self.animals)} animals',
            f'----- {len(lions)} Lions:'
        ]
        output_string.extend(lions)
        output_string.append(f'----- {len(tigers)} Tigers:')
        output_string.extend(tigers)
        output_string.append(f'----- {len(cheetahs)} Cheetahs:')
        output_string.extend(cheetahs)

        return '\n'.join(str(res) for res in output_string)

    def workers_status(self):
        info = {"Caretaker": [], "Vet": [], "Keeper": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info['Keeper'],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info['Caretaker'],
            f"----- {len(info['Vet'])} Vets:",
            *info['Vet'],
        ]

        return "\n".join(result)
