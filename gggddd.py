from pympler import tracker

summary_Tracker = tracker.SummaryTracker()

# 1
s0 = summary_Tracker.create_summary()

lenn = int(input("Длинна: "))
lst = [i for i in range(lenn)]
m = lst[::-1]
m1 = m[0]
m2 = m[1]
print(f'Максимальные: {m1}, {m2}')
s1 = summary_Tracker.create_summary()

summary_Tracker.print_diff(summary1=s0, summary2=s1)


