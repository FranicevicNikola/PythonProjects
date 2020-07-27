class Employee:

    num_of_empls = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        Employee.num_of_empls += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount


class Developer(Employee):  # inheritance
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amount = 1.20

    def __init__(self, first, last, pay, ppl=None):
        super().__init__(first, last, pay)

        if ppl is None:
            self.ppl = []
        else:
            self.ppl = ppl

    def add_ppl(self, emp):
        if emp not in self.ppl:
            self.ppl.append(emp)

    def remove_ppl(self, emp):
        if emp in self.ppl:
            self.ppl.remove(emp)

    def see_ppl_man(self):
        for guy in self.ppl:
            print('----> ' + guy.fullname())


emp_1 = Employee('Nikola', 'Franicevic', '2000')
dev_1 = Developer('Ivan', 'Franicevic', '30000', 'Python')
man_1 = Manager('Marko', 'Franicevic', '40000')

man_1.add_ppl(emp_1)
man_1.add_ppl(dev_1)


man_1.see_ppl_man()
