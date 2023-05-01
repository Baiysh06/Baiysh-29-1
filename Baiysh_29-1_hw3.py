class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f'Cpu: {self.__cpu}, Memory: {self.__memory}'

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_cards_number, call_to_number):
        print(
            f'Outgoing call to {call_to_number}, from sim card: {sim_cards_number},'
            f' number:{self.__sim_cards_list}')

    def __str__(self):
        return f'Sim cards list: {self.__sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'The route is calculated to {location}')

    def __str__(self):
       return Computer.__str__(self) + f' Sim card: {self.sim_cards_list}'


comp_1 = Computer(9, 599)
print(comp_1)
print('Computation:', comp_1.make_computations())
phone_1 = Phone([7860984566])
print(phone_1)
(phone_1.call('Beeline', "6783455633"))
smart_ph1 = SmartPhone(5, 128, 'MegaCom')
print(smart_ph1)
(smart_ph1.use_gps('Bishkek'))
smart_ph2 = SmartPhone(8, 300, 'Verizon')
print(smart_ph2)
(smart_ph2.use_gps('Almaty'))
print(comp_1 > smart_ph1)
print(comp_1 < smart_ph1)
print(comp_1 == smart_ph1)
print(comp_1 != smart_ph1)
print(comp_1 >= smart_ph1)
print(comp_1 <= smart_ph1)