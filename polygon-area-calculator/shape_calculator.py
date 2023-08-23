class Rectangle:
  #constructor
  def __init__(self, width, height):
    if isinstance(width, str) or isinstance(height, str):
      self.width = 5
      self.height = 10
    else:
      self.width = width
      self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return 2 * self.height + 2 * self.width

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    result = ""
    if self.width > 50 or self.height > 50:
      result = "Too big for picture."
    else:
      result += ("*"*self.width +"\n") * self.height
    return result

  def get_amount_inside(self, shape):
    h = self.height // shape.height
    w = self.width // shape.width
    return w * h

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    
    
class Square(Rectangle):
  #constructor
  def __init__(self, side):
    if isinstance(side, str):
      Rectangle.__init__(self, 9, 9)
    else:
      Rectangle.__init__(self, side, side)

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    if isinstance(side, str):
      self.set_width(9)
    else:
      self.set_width(side)

  def set_height(self, side):
    self.set_width(side)

  def __str__(self):
    return f"Square(side={self.width})"