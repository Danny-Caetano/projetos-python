import tkinter as tk
from datetime import datetime

current_year = datetime.now().year

def calculate_ages():
  year_of_birth = int(entry_year_of_birth.get())

  try:
      if year_of_birth > 1986:
          raise Exception("You were born after 1986.")

      # Calculates the age during the first passage of Halley
      first_passage = 1986
      age_first_passage = first_passage - year_of_birth

      # Calculates the age during the next passage of Halley
      next_passage = 2061
      age_next_passage = next_passage - year_of_birth

      result_label.config(text=f"You were {age_first_passage} years old during the first passage of Halley.\nYou will be {age_next_passage} years old during the next passage of Halley.")
  
  except Exception as e:
      result_label.config(text=str(e))
  
# Interface gráfica
root = tk.Tk()
root.title("Halley's Comet Age Calculator")
root.geometry("400x200")

year_of_birth_label = tk.Label(root, text="Enter your year of birth:")
year_of_birth_label.pack()

entry_year_of_birth = tk.Entry(root)
entry_year_of_birth.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_ages)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
