void setup() {
  fullScreen();
  //size(1024, 768);
  background(255, 255, 255);
}

void draw() {
  background(255, 255, 255);
  int midY = height/2; 
  int midX = width/2;
  int x = 100; 
  int y = 100;
  stroke(color(150, 150, 150));
  strokeWeight(1);

  line(0, midY, width, midY);
  line(midX, 0, midX, height);

  strokeWeight(1);
  while (midY - y > 0) {
    line(0, midY-y, width, midY-y);
    line(0, midY+y, width, midY+y);
    y = y + 100;
  }
  while (midX - x > 0) {
    line(midX-x, 0, midX-x, height);
    line(midX+x, 0, midX+x, height);
    x = x + 100;
  }

  strokeWeight(4);
  stroke(color(250, 50, 50));
  line(mouseX, 0, mouseX, height);
  line(0, mouseY, width, mouseY);
  text( "x: " + mouseX + " y: " + mouseY, mouseX, mouseY );
  fill(0, 0, 0);
}
