from Jarra import Jarra

class GreedySearch:
    def __init__(self, problem: Jarra):
        self.open = []
        self.close = []
        self.children = []
        self.problem = problem

    def run(self):
        self.open.append(self.problem.initial)
        solution = []
        while self.open:
            # Seleccionar el nodo con la heurística más baja
            self.open.sort(key=lambda x: self.problem.heuristic(x))
            actual = self.open.pop(0)
            print("Nodo: " + str(self.problem.number) + ", " + str(actual))
            if (actual == self.problem.goal):
                while actual:
                    action = actual.action
                    actual = actual.parent
                    solution.append(action)
                solution.reverse()
                return solution
            else:
                self.close.append(actual)
                self.children = self.problem.expand(actual)
                self.clean()
                self.open.extend(self.children)

        if not self.open and not solution:
            solution = "No hay solucion"

        return solution

    def clean(self):
        for n in self.children[0:]:
            if n in self.open or n in self.close:
                self.children.remove(n)