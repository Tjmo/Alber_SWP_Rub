package Stunde7;

import java.util.ArrayList;
import java.util.List;

interface Subject {
    void registerObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers();
}

interface Observer {
    void update();
}

interface Display {
    void display();
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
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update();
        }
    }

    public float getTemperature() {
        return temperature;
    }

    public float getHumidity() {
        return humidity;
    }

    public void setMeasurements(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        measurementsChanged();
    }

    private void measurementsChanged() {
        notifyObservers();
    }
}

class ScreenDisplay implements Observer, Display {
    private WeatherData weatherData;
    private float temperature;
    private float humidity;

    public ScreenDisplay(WeatherData weatherData) {
        this.weatherData = weatherData;
        weatherData.registerObserver(this);
    }

    @Override
    public void update() {
        temperature = weatherData.getTemperature();
        humidity = weatherData.getHumidity();
        display();
    }

    @Override
    public void display() {
        System.out.println("Screen Display: Temperature = " + temperature + "F, Humidity = " + humidity + "%");
    }
}

class ColorDisplay implements Observer, Display {
    private WeatherData weatherData;
    private float temperature;
    private float humidity;

    public ColorDisplay(WeatherData weatherData) {
        this.weatherData = weatherData;
        weatherData.registerObserver(this);
    }

    @Override
    public void update() {
        temperature = weatherData.getTemperature();
        humidity = weatherData.getHumidity();
        display();
    }

    @Override
    public void display() {
        if (temperature > 75) {
            System.out.println("Color Display: Temperature = " + temperature + "F, RED");
        } else if (temperature > 60) {
            System.out.println("Color Display: Temperature = " + temperature + "F, YELLOW");
        } else {
            System.out.println("Color Display: Temperature = " + temperature + "F, GREEN");
        }
    }
}

public class Voyeur_Pattern_Pull {
    public static void main(String[] args) {
        WeatherData weatherData = new WeatherData();

        ScreenDisplay screenDisplay = new ScreenDisplay(weatherData);
        ColorDisplay colorDisplay = new ColorDisplay(weatherData);

        weatherData.setMeasurements(80, 65);
        weatherData.setMeasurements(70, 55);

        weatherData.removeObserver(colorDisplay);

        weatherData.setMeasurements(75, 60);
    }
}