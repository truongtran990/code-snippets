package com.tt99.dependency_injection.before;

public class MainApplication {

    Triangle triangle;
    Circle circle;

    public MainApplication() {
        triangle = new Triangle();
        circle = new Circle();
    }

    public static void main(String[] args) {
        MainApplication app = new MainApplication();
        app.startDraw();
    }

    public void startDraw() {
        // triangle.draw();
        circle.draw();
    }

}
