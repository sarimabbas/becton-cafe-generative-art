int count = 0;
int rectA, rectB, rectC, rectD;
boolean isDrawing = false;

class Display {
  boolean exists = false;
  float r;
  float b;
  float g;
  float x;
  float y;
  float dWidth;
  float dHeight;
  int pos;
  String name;

  void draw() {
    // draw the rectangle with fill
    fill(color(r, b, g));
    rect(x, y, dWidth, dHeight);
    // draw the text
    fill(color(0,0,0));
    text(pos, x + dWidth/2, y + dHeight/2);
    text("(" + x + ", " + y + ")", x, y);
    text("(" + (x + dWidth) + ", " + (y + dHeight) + ")", x + dWidth, y + dHeight);
  }
}

Display[] displayData = new Display[100];


void setup() {
  // setup processing interface
  fullScreen();
}

void draw() {
  // clear the background
  if (!isDrawing) {
    background(255, 255, 255);
  }
  // draw all rectangles/displays
  for (int i = 0; i < count; i = i+1) {
    displayData[i].draw();
  }
}

void mousePressed() {
  if (!isDrawing) {
    // start drawing new object
    rectA = mouseX;
    rectB = mouseY;
    isDrawing = true;
  } else {
    
    // finish drawing new object
    isDrawing = false;
    rectC = mouseX - rectA;
    rectD = mouseY - rectB;
    
    // create display object 
    displayData[count] = new Display();
    displayData[count].x = rectA;
    displayData[count].y = rectB;
    displayData[count].dWidth = rectC;
    displayData[count].dHeight = rectD;
    displayData[count].r = random(255);
    displayData[count].b = random(255);
    displayData[count].g = random(255);
    displayData[count].exists = true;
    displayData[count].pos = count;

    count += 1;
  }
  
}

void mouseMoved() {
  if (isDrawing) {
    rect(rectA, rectB, mouseX - rectA, mouseY - rectB);
  }
}
