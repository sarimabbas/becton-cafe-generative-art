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
    addText();
  }
  
  void addText() {
    String topLeft = "(" + x + ", " + y + ")";
    String bottomRight = "(" + (x + dWidth) + ", " + (y + dHeight) + ")";
    float brWidth = textWidth(bottomRight);
    float tlHeight = 16;
    PFont f;
    f = createFont("Arial",16,true); // Arial, 16 point, anti-aliasing on
    textFont(f);
    fill(color(0,0,0));
    
    text(pos, x + dWidth/2, y + dHeight/2);
    
    //if (dWidth < brWidth*2 & dHeight < tlHeight*2) {
    //  text(topLeft, x, y); 
    //  text(bottomRight, x + dWidth, y + dHeight);
    //}
    //else {
    //  text(topLeft, x, y+20); 
    //  text(bottomRight, x + dWidth - brWidth, y + dHeight);
    //}
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
  
    PFont f;
    f = createFont("Arial",16,true); // Arial, 16 point, anti-aliasing on
    textFont(f);
    strokeWeight(3);
    stroke(color(250, 50, 50));
    line(mouseX, 0, mouseX, height);
    line(0, mouseY, width, mouseY);
    text( "x: " + mouseX + " y: " + mouseY, mouseX, mouseY );
    fill(0, 0, 0);
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
    displayData[count].r = random(255) * 1.3; // made colors lighter 
    displayData[count].b = random(255) * 1.3; // to better see the 
    displayData[count].g = random(255) * 1.3; // black font
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
    output.flush();
    output.close();
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
}
