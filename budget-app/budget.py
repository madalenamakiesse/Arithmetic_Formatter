class Category:
  #Constructor function 
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def get_category(self):
    return str(self.category)

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def get_balance(self):
    s = 0
    for l in self.ledger:
      s += l["amount"]
    return s

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  def withdraw(self, amount, description=""):
    result = self.check_funds(amount)
    if result:
      self.ledger.append({"amount": -amount, "description": description})
    return result

  def transfer(self, amount, newcategory):
    result = self.check_funds(amount)
    if result:
      self.withdraw(amount, f"Transfer to {newcategory.get_category()}")
      newcategory.deposit(amount, "Transfer from "+ self.category)   
    return result
    
  def __str__(self):
    result = self.category.title().center(30,'*') +"\n"
    for l in self.ledger:
      description = "{:<23}".format(l["description"][:23])
      amount = "{:>7.2f}".format(l["amount"])
      result += f"{description}{amount}\n"
    result += f"Total: {self.get_balance()}" 
    return result

  def total_spent(self):
    s = 0
    for l in self.ledger:
      if l["amount"] < 0:
        s += l["amount"]
    return abs(s)
  
def create_spend_chart(categories):

  listC = [c.get_category() for c in categories]
  listCP = [c.total_spent() for c in categories]

  total = sum(listCP)

  maxLe = max(len(c) for c in listC)

  for i in range(len(listCP)):
    listCP[i] = ( listCP[i] / total ) * 100

  result = "Percentage spent by category\n"

  for i in range(100, -1, -10):
    result +=  "{:>3}|".format(i)
    for j in listCP:
      if j >= i:
        result += " o "
      else:
        result += "   "
    result += " \n"

  result += "    ----------"

  for i in range(maxLe):
    result += "\n    "
    
    for j in listC:
      if i < len(j):
        result += " " + j[i] + " "
      else:
        result += "   "
        
    result += " "  
  
  return result