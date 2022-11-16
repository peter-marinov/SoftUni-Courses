from static_and_class_methods_exercise.gym.customer import Customer
from static_and_class_methods_exercise.gym.equipment import Equipment
from static_and_class_methods_exercise.gym.exercise_plan import ExercisePlan
from static_and_class_methods_exercise.gym.subscription import Subscription
from static_and_class_methods_exercise.gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.__find_by_id(self.subscriptions, subscription_id)
        customer = self.__find_by_id(self.customers, subscription_id)
        trainer = self.__find_by_id(self.trainers, subscription_id)
        equipment = self.__find_by_id(self.equipment, subscription_id)
        plan = self.__find_by_id(self.plans, subscription_id)
        output = str(subscription) + '\n' + \
            str(customer) + '\n' + \
            str(trainer) + '\n' + \
            str(equipment) + '\n' + \
            str(plan)

        return output


    @staticmethod
    def __find_by_id(entities, obj_id):
        for entity in entities:
            if entity.id == obj_id:
                return entity
