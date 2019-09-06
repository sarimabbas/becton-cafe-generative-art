int count;
int rectA, rectB, rectC, rectD;

void setup() {
  // setup processing interface
  fullScreen();
}

void draw() {
  // allow user to label rectangles with text

  // export rectangles into documentation for the external display
}

void mousePressed() {
  // if clicking on existing display, text input to rename
  if (count % 2 == 0) {
    rectA = mouseX;
    rectB = mouseY;
  } else {
    rectC = mouseX - rectA;
    rectD = mouseY - rectB;
    rect(rectA, rectB, rectC, rectD);
  }
  count += 1;

  // else start drawing new object
}

void mouseReleased() {
  // if drawing object, stop drawing object

  // if drawing object, create a new display object given start and end positions
}
