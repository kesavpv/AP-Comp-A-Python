def profile(name, id):
  print("My name is " + name)
  print("My student id is " + str(id) + "\n")
  for i in name:
    print(i)
    if i == ' ':
      break;
  print("My name all capitalized is " + name.upper())

profile("Kesav Kadalazhi", 4029243)

print()
print()

def summer_plans(plans):
  print("This summer I plan to ", end="")
  for plan in plans:
    print(plan, end="")
  print()

summer_plans({"sleep, ", "and program a robot."})}