with open('/sys/class/powercap/intel-rapl:0/energy_uj') as d:
    read_data = d.read()

uj = float(read_data) / 3600000000000

print(uj)