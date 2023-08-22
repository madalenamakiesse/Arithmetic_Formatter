def add_time(start, duration, day=""):
  new_time = ""
  d = n = 0

  days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  
  if start and duration:
    
    lst = start.split()
    str = lst[0].split(':')
    du = duration.split(':')

    minute = int(str[1]) + int(du[1])
    h = int(str[0]) + int(du[0])

    if minute > 60:
      h = h + minute//60
      minute = minute - 60

    ap = lst[1].upper()

    if h == 12:
      if ap == "PM":
        lst[1] = "AM"
      else:
        lst[1] = "PM"
    
    if 12 < h <= 24 :
      h = h % 12
      if ap == "AM":
        lst[1] = "PM"
      else: 
        lst[1] = "AM"
        new_time =  " (next day)"

    if 24 < h :
      hh = h % 24
      n = h // 24
      h = hh
      if h >= 12: 
        n = n + 1
        if ap == "AM":
          lst[1] = "PM"
        else: 
          lst[1] = "AM"
          
        if h > 12:
          h = h - 12
          
      if n == 1:
        new_time =  " (next day)"
      else:
        new_time =  f" ({n} days later)"
    
    if day != "":
      dIndex = (days.index(day.capitalize()) + n)%7
      new_time = f"{h}:{minute:02d} {lst[1]}, {days[dIndex]}" + new_time
    else:
      new_time = f"{h}:{minute:02d} {lst[1]}" + new_time
    
    
  return new_time