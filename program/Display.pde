color c = color(0); // random color
float x = 0;
float y = 0;
String name = "";

// random color
color c = color(random(255), random(255), random(255))

/*
Takes startPos and endPos object {x, y}
*/
void setup(startPos, endPos) {
  size(startPos.x-endPos.x,startPos.y-endPos.y);
  x = startPos.x
  y = startPos.y
}

void draw() {
  display();
}

void rename(newName) {
  name = newName
}

void display() {
  fill(c);
  rect(x,y,width, height);
}