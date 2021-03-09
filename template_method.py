from abc import ABC, abstractmethod


class Training(ABC):
    @abstractmethod
    def warmingup(self):
        pass

    def train(self):
        print(f"{self.muscle}のトレーニング")

    def drink_protain(self):
        print("プロテインを飲む")

    def do(self):
        self.warmingup()
        self.train()
        self.drink_protain()


class ChestTraining(Training):
    def __init__(self):
        self.muscle = "胸"

    def warmingup(self):
        print(f"{self.muscle}のウォーミングアップ")
        print("肩のウォーミングアップ")


def main():
    chest_training = ChestTraining()
    chest_training.do()


if __name__ == "__main__":
    main()
