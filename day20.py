import fileinput
from collections import defaultdict, deque

inputs = defaultdict(list)

modules = {}
pulses = deque()

class Module:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs

    def send_to_outputs(self, pulse):
        for output in self.outputs:
            pulses.append((self.name, pulse, output))

    def recieve(self, sender, message):
        pass

class Broadcaster(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)

    def recieve(self, sender, pulse):
        for output in self.outputs:
            pulses.append((self.name, pulse, output))

class Conjunction(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.inputs = {}

    def add_inputs(self, inputs):
        self.inputs.update({input : 0 for input in inputs})

    def recieve(self, sender, pulse):
        self.inputs[sender] = pulse

        if all(self.inputs.values()):
            self.send_to_outputs(0)
        else:
            self.send_to_outputs(1)

class FlipFlop(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.state = 0

    def recieve(self, sender, pulse):
        if pulse == 1: return

        self.state = 1 - self.state
        self.send_to_outputs(self.state)

    

for line in map(str.strip, fileinput.input()):
    
    name, outputs = line.split(' -> ')
    outputs = outputs.split(', ')

    if name[0] == '&':
        name = name[1:]
        module = Conjunction(name, outputs)
    elif name[0] == '%':
        name = name[1:]
        module = FlipFlop(name, outputs)
    else:
        module = Broadcaster(name, outputs)

    for output in outputs:
        inputs[output].append(name)

    modules[name] = module

for key, vals in inputs.items():
    module = modules.get(key)
    if isinstance(module, Conjunction):
        module.add_inputs(vals)
    
output_pulses = [0, 0]

TRESHOLD = 1000
machine_activated = False

def push_button():
    global machine_activated

    pulses.append(('button', 0, 'broadcaster'))
    while pulses:
        src, pulse, dst = pulses.popleft()

        output_pulses[pulse] += 1

        if dst == 'rx':
            if pulse == 0:
                machine_activated = True

        elif dst != 'result':
            module = modules.get(dst)
            module.recieve(src, pulse)

i = 0
while not machine_activated:
    push_button()
    i += 1

    if i == TRESHOLD:
        print(output_pulses[0] * output_pulses[1])

print(i)