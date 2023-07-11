print("*** Converting hh.mm.ss to seconds ***")
h,m,s = map(int,input("Enter hh mm ss : ").split())

if h < 0 :
    print(f"hh({h}) is invalid!")
elif m > 59 or m < 0 :
    print(f"mm({m}) is invalid!")
elif s > 59 or s < 0 :
    print(f"ss({s}) is invalid!")
else:
    sum_sec = h*3600 + m*60 + s
    sum_sec = "{:,}".format(sum_sec)

    h = str(h).zfill(2)
    m = str(m).zfill(2)
    s = str(s).zfill(2)
    time_str = f"{h}:{m}:{s}"

    print(time_str,'=',sum_sec,'seconds')