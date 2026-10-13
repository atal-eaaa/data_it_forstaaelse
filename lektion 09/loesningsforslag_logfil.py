log = [
    "08:01 INFO Server startet",
    "08:05 INFO Bruger logget ind",
    "08:17 WARNING Langsomt svar fra database",
    "08:22 ERROR Database utilgængelig",
    "08:23 ERROR Database utilgængelig",
    "08:30 INFO Database genstartet",
    "09:12 WARNING Disk 85 procent fuld",
    "09:45 ERROR Disk fuld",
    "10:02 INFO Bruger logget ud",
]

info    = 0
warning = 0
error   = 0

for linje in log:
    if "INFO" in linje:
        info += 1
    elif "WARNING" in linje:
        warning += 1
    elif "ERROR" in linje:
        error += 1
        print("Fejl kl.", linje[0:5])

print("INFO    :", info)
print("WARNING :", warning)
print("ERROR   :", error)

if error >= 3:
    status = "KRITISK"
elif error >= 1 or warning > 2:
    status = "USTABIL"
else:
    status = "STABIL"

print("Status:", status)

i = 1
fundet = False
while i < len(log) and fundet == False:
    if "ERROR" in log[i - 1] and "ERROR" in log[i]:
        fundet = True
    else:
        i += 1

if fundet:
    print("To fejl i træk kl.", log[i][0:5])
else:
    print("Ingen fejl i træk")
