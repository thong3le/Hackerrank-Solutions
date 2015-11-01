import calendar

m, d, y = tuple(map(int, raw_input().split()))
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print days[calendar.weekday(y, m, d)]