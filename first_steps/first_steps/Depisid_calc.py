#sum = depozid_sum + depozid_time * ((depozid_sum * god_lihven_procent) / 12)

depozid_sum = float(input())
depozid_time = int(input())
god_lihven_procent = float(input())

sum = depozid_sum + depozid_time * ((depozid_sum * god_lihven_procent/100)/12)

print(sum)