#Convert the time entered in hh,min and sec into seconds.


time  = input("Enter the time in hh min sec format:")

hh,mm,ss = time.split(",")
total_seconds = int(hh)*3600 + int(mm)*60 + int(ss)
print("Total time in seconds:", total_seconds)