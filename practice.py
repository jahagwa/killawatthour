# This is simply to calculate Kwh's the system is using currently #

with open('/sys/class/powercap/intel-rapl:0/energy_uj') as d:
    read_data = d.read()

uj = float(read_data) / 3600000000000

my_output = str(round(uj, 3))

print("Kwh's Used: " + str(round(uj, 3)))

print("another test: {} {}".format(my_output, "end of text"))
