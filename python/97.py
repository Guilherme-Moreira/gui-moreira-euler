a = 1
for i in range(7830457):
    a = (2 * a) % int(1e10)

print(28433 * a + 1) % int(1e10)  # 8739992577
