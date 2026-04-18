# WEEKLY EXPENSE TRACKER (Beginner-Friendly)

# ===============================
# 1. INITIAL INPUTS
# ===============================
student_name = input("Enter student name: ")
weekly_budget = float(input("Enter weekly budget: "))

# ===============================
# 2. CATEGORY LIST (Hardcoded)
# ===============================
categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

# Display categories using a loop
print("\n==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")

for i in range(len(categories)):
    print(f" {i+1}. {categories[i]}")

print("==========================================")

# ===============================
# 3. INPUT LOOP (4 ENTRIES)
# ===============================
expenses = []  # list of dictionaries

for i in range(4):
    print(f"\n--- EXPENSE {i+1} ---")
    
    category_num = int(input("Category (0 to skip): "))
    
    if category_num == 0:
        continue  # skip this entry
    
    # Get details
    description = input("Description: ")
    amount = float(input("Amount: "))
    
    # Check if high expense (more than 25% of budget)
    high_expense = False
    if amount > (weekly_budget * 0.25):
        high_expense = True
    
    # Store in dictionary
    expense = {
        "category": categories[category_num - 1],
        "description": description,
        "amount": amount,
        "high": high_expense
    }
    
    expenses.append(expense)

# ===============================
# 4. CALCULATIONS
# ===============================
total_spent = 0

for item in expenses:
    total_spent = total_spent + item["amount"]

remaining = weekly_budget - total_spent

# Status check
if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

# ===============================
# 5. OUTPUT SUMMARY
# ===============================
print("\n======================================================")
print(f"     {student_name.upper()} -- WEEKLY EXPENSE LOG")
print("======================================================")

print("  Weekly Budget  : P", weekly_budget)

# Display expenses
count = 1
for item in expenses:
    print(f"  [{count}] {item['category']}")
    
    line = "      " + item["description"] + "              P" + str(item["amount"])
    
    # Add High Expense Tag
    if item["high"]:
        line = line + "  ! High Expense Alert!"
    
    print(line)
    count = count + 1

print("------------------------------------------------------")
print("  Total Spent    : P", total_spent)
print("  Remaining      : P", remaining)
print("  Status         :", status)
print("======================================================")
