from intcpu import intcpu

program = [int(string) for string in open('input.txt').read().split(",")]

cpu = intcpu(program)
cpu.provide(1)
print("Part 1: " + str(cpu.getFinal()))

cpu.reset()
cpu.provide(2)
print("Part 2: " + str(cpu.getFinal()))