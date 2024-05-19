package com.tt99.dependency_injection.after;

public class MainApplication {
    Shape shape;

    public MainApplication(Shape shape) {
        this.shape = shape;
    }

    public static void main(String[] args) {

        Triangle triangle = new Triangle();
        MainApplication app = new MainApplication(triangle);
        app.startDraw();
    }

    public void startDraw() {
        shape.draw();
    }
}
