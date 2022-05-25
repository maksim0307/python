# blueprint -> object
class Unit():
    def run(self):
        print("run")
    def die(self):
        print("die")
class Worker(Unit):
    def work(self):
        print("work")
class Warion(Unit):
    def fight(self):
        print("finght")
class Gendalf(Warion):
    def magic(self):
        print("magic")
worker1 = Worker()
worker2 = Worker()
worker1.run()
worker1.work()
warior1 = Warion()
warior1.fight()
gendalf = Gendalf()
gendalf.magic()
gendalf.fight()









