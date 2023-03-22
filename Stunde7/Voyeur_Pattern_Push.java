package Stunde7;

import java.util.ArrayList;
import java.util.List;

interface Subject {
    void registerObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers(float temperature, float humidity);
}

interface Observer {
    void update(float temperature, float humidity);
}

class WeatherData implements Subject {
    private List<Observer> observers;
    private float temperature;
    private float humidity;

    public WeatherData() {
        observers = new ArrayList<>();
    }

    @Override
    public void registerObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers(float temperature, float humidity) {
        for (Observer observer : observers) {
            observer.update(temperature, humidity);
        }
    }

    public void setMeasurements(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        measurementsChanged();
    }

    private void measurementsChanged() {
        notifyObservers(temperature, humidity);
    }
}

class ScreenDisplay implements Observer {
    private float temperature;
    private float humidity;

    @Override
    public void update(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        display();
    }

    private void display() {
        System.out.println("Screen Display: Temperature = " + temperature + "F, Humidity = " + humidity + "%");
    }
}

class ColorDisplay implements Observer {
    private float temperature;
    private float humidity;

    @Override
    public void update(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        display();
    }

    private void display() {
        if (temperature > 75) {
            System.out.println("Color Display: Temperature = " + temperature + "F, RED");
        } else if (temperature > 60) {
            System.out.println("Color Display: Temperature = " + temperature + "F, YELLOW");
        } else {
            System.out.println("Color Display: Temperature = " + temperature + "F, GREEN");
        }
    }
}

public class Voyeur_Pattern_Push {
    public static void main(String[] args) {
        WeatherData weatherData = new WeatherData();

        ScreenDisplay screenDisplay = new ScreenDisplay();
        ColorDisplay colorDisplay = new ColorDisplay();

        weatherData.registerObserver(screenDisplay);
        weatherData.registerObserver(colorDisplay);

        weatherData.setMeasurements(80, 65);
        weatherData.setMeasurements(70, 55);

        weatherData.removeObserver(colorDisplay);

        weatherData.setMeasurements(75, 60);
    }
}