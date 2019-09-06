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
  String name;
}

Display[] displayData = new Display[100];


void setup() {
  // setup processing interface
  fullScreen();
}

void draw() {
  // draw rectangles
  for (int i = 0; i < count; i = i+1) {
    //print(i, displayData[i]);
    fill(color(displayData[i].r, displayData[i].b, displayData[i].g));
    rect(displayData[i].x, displayData[i].y, displayData[i].dWidth, displayData[i].dHeight);
    fill(color(0,0,0));
    text(i, displayData[i].x + displayData[i].dWidth/2, displayData[i].y + displayData[i].dHeight/2);
    text("(" + displayData[i].x + ", " + displayData[i].y + ")", displayData[i].x, displayData[i].y);
    text("(" + (displayData[i].x + displayData[i].dWidth) + ", " + (displayData[i].y + displayData[i].dHeight) + ")", displayData[i].x + displayData[i].dWidth, displayData[i].y + displayData[i].dHeight);
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
    
    count += 1;
  }
  
}