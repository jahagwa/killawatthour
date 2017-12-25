with open('/proc/uptime') as f:
    read_data = f.read()

uptime = float(read_data.split(" ")[0]) / 3600


with open('/sys/class/powercap/intel-rapl:0/energy_uj') as d:
    read_data = d.read()
uj = int(read_data) *10**-6

print(uj/uptime * .07)