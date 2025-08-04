import re

class PicnicPlan:
    def __init__(self, filename="plan.txt"):
        self.filename = filename

    def add_places(self):
        print("------Welcome to the picnic------")
        place_name = input("Enter place name: ").strip()

        while True:
            total_budget = input("Enter budget: ").strip()
            if total_budget.isdigit():
                break
            print("Invalid input! Budget should only contain numbers.")

        while True:
            total_people = input("Enter total people: ").strip()
            if total_people.isdigit():
                break
            print("Invalid input! Total people should only contain numbers.")

        food = input("Enter food name for picnic: ").strip()
        location = input("Enter location: ").strip()

        try:
            with open(self.filename, "a") as f:
                f.write(f"Place_name: {place_name}\n")
                f.write(f"Total budget: {total_budget}\n")
                f.write(f"Total people: {total_people}\n")
                f.write(f"Food: {food}\n")
                f.write(f"Location: {location}\n")
                f.write("--------------------\n")
        except Exception as e:
            print(f"Error saving: {e}")

    def search_plan(self):
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("No file found.")
            return

        name = input("Enter the place name to search plan: ").strip()
        pattern = rf"^Place_name:\s*{re.escape(name)}\b"
        found = False
        i = 0

        while i < len(lines):
            if re.search(pattern, lines[i], re.IGNORECASE):
                found = True
                print("\nPlan found:\n")
                while i < len(lines) and lines[i].strip() != "--------------------":
                    print(lines[i].strip())
                    i += 1
                if i < len(lines) and lines[i].strip() == "--------------------":
                    print(lines[i].strip())
                break
            i += 1

        if not found:
            print("No plan found with that place name.")

    def delete_plan(self):
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("No file found.")
            return

        name = input("Enter place name to delete that plan: ").strip()
        pattern = rf"^Place_name:\s*{re.escape(name)}\b"
        found = False
        new_lines = []
        i = 0

        while i < len(lines):
            if re.search(pattern, lines[i], re.IGNORECASE):
                found = True
                block = []
                while i < len(lines) and lines[i].strip() != "--------------------":
                    block.append(lines[i])
                    i += 1
                if i < len(lines):
                    block.append(lines[i])  # add separator
                    i += 1
                print("\nFound plan to delete:\n")
                print("".join(block))
                permission = input(f"\nAre you sure you want to delete this plan? (yes/no): ").strip().lower()
                if permission != "yes":
                    new_lines.extend(block)
                else:
                    print("Plan deleted successfully.")
            else:
                new_lines.append(lines[i])
                i += 1

        if not found:
            print("No plan found with that name.")
        else:
            with open(self.filename, "w") as f:
                f.write("".join(new_lines))

    def edit_plan(self):
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("No file found.")
            return

        name = input("Enter the place name whose plan you want to edit: ").strip()
        pattern = rf"^Place_name:\s*{re.escape(name)}\b"
        new_lines = []
        found = False
        i = 0

        while i < len(lines):
            if re.search(pattern, lines[i], re.IGNORECASE):
                found = True
                block = []
                while i < len(lines) and lines[i].strip() != "--------------------":
                    block.append(lines[i])
                    i += 1
                if i < len(lines):
                    block.append(lines[i])  # separator
                    i += 1

                print("\nPlan found:\n")
                print("".join(block))

                permission = input(f"Do you want to edit this plan? (yes/no): ").strip().lower()
                if permission != "yes":
                    new_lines.extend(block)
                    continue

                # take new input
                place_name = input("Enter new place name: ").strip()
                while True:
                    total_budget = input("Enter new budget: ").strip()
                    if total_budget.isdigit():
                        break
                    print("Invalid input! Budget should only contain numbers.")
                while True:
                    total_people = input("Enter new total people: ").strip()
                    if total_people.isdigit():
                        break
                    print("Invalid input! Total people should only contain numbers.")
                food = input("Enter new food name: ").strip()
                location = input("Enter new location: ").strip()

                new_lines.append(f"Place_name: {place_name}\n")
                new_lines.append(f"Total budget: {total_budget}\n")
                new_lines.append(f"Total people: {total_people}\n")
                new_lines.append(f"Food: {food}\n")
                new_lines.append(f"Location: {location}\n")
                new_lines.append("--------------------\n")
            else:
                new_lines.append(lines[i])
                i += 1

        if not found:
            print("No plan found with that place name.")
        else:
            with open(self.filename, "w") as f:
                f.write("".join(new_lines))
            print("All edits saved.")

    def view_all_places(self):
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
            names = [line.strip().replace("Place_name:", "").strip() for line in lines if line.startswith("Place_name:")]
            if names:
                print("\n--- All Places ---")
                for i, name in enumerate(names, 1):
                    print(f"{i}. {name}")
                print("------------------\n")
            else:
                print("No place names found.")
        except FileNotFoundError:
            print("No file found.")

    def view_all_plans(self):
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("No file found.")
            return

        print("\n---- All Saved Plans ----\n")
        current_plan = []
        plan_count = 0

        for line in lines:
            if line.strip() == "--------------------":
                if current_plan:
                    plan_count += 1
                    print(f"Plan {plan_count}:")
                    for l in current_plan:
                        print(l.strip())
                    print("--------------------")
                    current_plan = []
            else:
                current_plan.append(line)

        if not plan_count:
            print("No plans found.")

def main():
    obj = PicnicPlan()
    while True:
        print("\n--- Picnic Planner Menu ---")
        print("1. Add plan")
        print("2. Search plan")
        print("3. Delete plan")
        print("4. Edit plan")
        print("5. Show all place names")
        print("6. View all plans")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()
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
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
