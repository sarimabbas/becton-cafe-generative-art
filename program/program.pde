int count = 0;
int rectA, rectB, rectC, rectD;
boolean isDrawing = false;
PrintWriter output;

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

  void clear() {
    exists = false;
  }
}

Display[] displayData = new Display[100];


void setup() {
  // setup processing interface
  fullScreen();
  output = createWriter("mapping_info.txt"); 

}

void draw() {
  // clear the background
  if (!isDrawing) {
    background(255, 255, 255);
  }
  // draw all rectangles/displays
  for (int i = 0; i < count; i = i+1) {
    if (displayData[i].exists) {
      displayData[i].draw();
    }
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
    
    // sets x,y coord as the top left hand corner
    if (rectA > mouseX) {
      rectA = mouseX;
      rectC = rectC * -1; 
    }
    if (rectB > mouseY) {
      rectB = mouseY;
      rectD = rectD * -1;
    }
     
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
    output.println("Rectangle " + count);
    output.println("Height: " + displayData[count].dHeight + "px");
    output.println("Width: " + displayData[count].dWidth + "px");
    output.println("x: " + displayData[count].x);
    output.println("y: " + displayData[count].y);
    output.println(""); 

    count += 1;
    
    //need to add displayData[count].dWidth to a new array of just widths with count and height
  }
  
}

void mouseMoved() {
  if (isDrawing) {
    background(255, 255, 255); 
    draw();
    rect(rectA, rectB, mouseX - rectA, mouseY - rectB);
  }
}

void keyPressed() {
  // save frame
  if (key == 'c' || key == 'C') {
    saveFrame("mapping-###.png");  
  }
  // clear all displays
  if (key == 'd' || key == 'D') {
    for (int i = 0; i < count; i = i+1) {
      displayData[i].clear();
    }
  }
  // exit
  if (key == 'e' || key == 'E') {
    exit();
  }
  output.flush();
  output.close();
}
