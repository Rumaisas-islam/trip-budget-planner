import re
class PicnicPlan:
  def __init__(self,filename="plan.txt"):
    self.filename=filename
  def add_places(self):
    """Add a new picnic plan and save to file."""
    print("------Welcome to the picnic------")
    place_name=input("Enter place name: ").strip()
    total_budget=input("Enter budget: ").strip()
    while not total_budget.isdigit():
      total_budget=input("Enter budget: ").strip()
    total_people=input("Enter total people: ").strip()
    while not total_people.isdigit():
      total_people=input("Enter total people: ").strip()
    food=input("Enter food name for picnic: ").strip()
    location=input("Enter location: ").strip()

    try:
      with open(self.filename,"a") as f:
        f.write("--------------------\n")
        f.write(f"Place_name: {place_name}\n")
        f.write(f"Total budget: {total_budget}\n")
        f.write(f"Total people: {total_people}\n")
        f.write(f"Food: {food}\n")
        f.write(f"Location: {location}\n")
        f.write("--------------------\n")
    except Exception as e:
      print(f"Error saving:{e}")
  def search_plan(self):
    """ Search a picnic plan by giving name."""
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
    except FileNotFoundError:
      print("No file found")
      return
    name=input(f"Enter the place name to search plan: ").strip()
    pattern = rf"^Place_name:\s*{re.escape(name)}\b"
    found=False
    for i,line in enumerate(lines):
      if re.search(pattern,line,re.IGNORECASE):
        for j in range(i-1,i+7):
          if 0<=j<len(lines):
            print(lines[j].strip())
        found=True
        break
    if not found:
      print("No plan found with that place name")
  def delete_plan(self):
    """ Delete a picnic plan by giving name."""
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
    except FileNotFoundError:
      print("No file found")
      return 
    name=input("Enter place name to delete that plan: ").strip()
    pattern = rf"^Place_name:\s*{re.escape(name)}\b"
    new_lines=[]
    found=False
    i=0
    while i < len(lines):
      line=lines[i]
      if re.search(pattern,line,re.IGNORECASE):
        found=True
        while i>0 and not lines[i-1].startswith("--------------------"):
          i-=1
        while i < len(lines) and not lines[i].startswith("--------------------"):
          i+=1 
        if i < len(lines):
          i+=1
      else:
        new_lines.append(line)
        i+=1
    if found:
      while True:
        permission=input(f"Are you sure you want to delete plan for {name}?(yes/no): ").lower()
        if permission == "yes":
           with open(self.filename,"w") as f:
            f.write("".join(new_lines))
            print("Plan deleted successfully")
            break
        else:
          print("Deletion cancelled")
          break      
    else:
      print("No plan found with that name")
  def edit_plan(self):
    """ Edit a picnic plan by giving name."""
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
    except FileNotFoundError:
      print("No file found")
      return
    name=input("Enter the place name which plan you want to edit: ").strip()
    new_lines=[]
    pattern = rf"^Place_name:\s*{re.escape(name)}\b"
    found=False
    i=0
    while i < len(lines):
      line=lines[i]
      if re.search(pattern,line,re.IGNORECASE):
        found=True
        while i > 0 and not lines[i-1].startswith("--------------------"):
          i-=1
        while i < len(lines) and not lines[i].startswith("--------------------"):
          i+=1
        if i < len(lines) and lines[i].startswith("--------------------"):
          i+=1
      
        place_name=input("Enter place name: ").strip()
        total_budget=input("Enter budget: ").strip()
        while not total_budget.isdigit():
          total_budget=input("Enter budget: ").strip()
        total_people=input("Enter total people: ").strip()
        while not total_people.isdigit():
          total_people=input("Enter total people: ").strip()
        food=input("Enter food name for picnic: ").strip()
        location=input("Enter location: ").strip()
          
        new_lines.append("--------------------\n")
        new_lines.append(f"Place_name: {place_name}\n")
        new_lines.append(f"Total budget: {total_budget}\n")
        new_lines.append(f"Total people: {total_people}\n")
        new_lines.append(f"Food: {food}\n")
        new_lines.append(f"Location: {location}\n")
        new_lines.append("--------------------\n")
        i+=1

      else:
        new_lines.append(lines[i])
        i+=1
    if found:
      while True:
        permission=input(f"Are you sure you want to edit plan for {place_name}?(yes/no): ").lower()
        if permission == "yes":
          with open(self.filename,"w") as f:
            f.write("".join(new_lines))
          print("Plan updated successfully")
          break
        else:
          print("Edition Cancelled")
          break    
    else:
      print("No plan found with that place name")
  def view_all_places(self):
    """ View All Plan Places Names."""
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
      names=[line.strip().replace("Place_name:", "") for line in lines if line.startswith("Place_name:")]
      if names:
        print("\n---All Places Name---")
        for i,name in enumerate(names,1):
          print(f"{i}.{name}")
        print("----------------------\n")
      else:
        print("No place name found")
    except FileNotFoundError:
      print("No file found")
  def view_all_plans(self):
    """ View All Plans."""
    try:
      with open(self.filename,"r") as f:
        content=f.read().strip()
      print("\n----All Saved Parts----\n")
      parts = re.findall(r"-+\n(.*?)\n-+", content, re.DOTALL)
      if parts:
        for i,part in enumerate(parts,1):
          print(f"Plan:{i}")
          print(part.strip())
      else:
        print("No plan found")
    except FileNotFoundError:
      print("No file found")
def main():
  obj=PicnicPlan()
  while True:
    print("---Picnic Planner Menu---\n")
    print("1. Add plan\n")
    print("2. Search plan\n")
    print("3. Delete plan\n")
    print("4. Edit plan\n")
    print("5. Show all places names\n")
    print("6. View all plans\n")
    print("7. Exit\n")
    choice=input("Enter what you want to do(1/2/3/4/5/6/7): ")
    if choice == "1":
      obj.add_places()
    elif choice == "2":
      obj.search_plan()
    elif choice == "3":
      obj.delete_plan()
    elif choice == "4":
      obj.edit_plan()
    elif choice == "5":
      obj.view_all_places()
    elif choice == "6":
      obj.view_all_plans()
    elif choice == "7":
      print("Thanks for using Picnic Planner!")
      break
if __name__=="__main__":
    main()