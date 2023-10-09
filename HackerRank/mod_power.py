power = []
for i in range(3):
    power.append(int(input()))

power_result = pow(power[0], power[1])
print(power_result)
print(power_result % power[2])