void setup() {
  fullScreen();
  background(255, 255, 255);
}

void draw() {
  int midY = height/2; 
  int midX = width/2;
  int x = 100; 
  int y = 100;
  stroke(0);
  strokeWeight(5); 
  
  line(0, midY, width, midY);
  line(midX, 0, midX, height);
  
  strokeWeight(1);
  while(midY - y > 0) {
     line(0, midY-y, width, midY-y);
     line(0, midY+y, width, midY+y);
     y = y + 100; 
  }
  while(midX - x > 0) {
     line(midX-x, 0, midX-x, height);
     line(midX+x, 0, midX+x, height);
     x = x + 100; 
  }
}
