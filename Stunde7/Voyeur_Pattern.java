package Stunde7;

import java.util.ArrayList;
import java.util.List;
//definiert die für WeatherData zu implementierende Methoden
interface Subject {
    void registerObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers();
}

interface Observer {
    void update(float temperature, float humidity);
}
//Verwaltet liste von Observern und benachrichtigt felder
//wenn temp/humid aktualisiert werden (Aufrufen der serMeasurements)
class WeatherData implements Subject {
//setzt floats für temp und humid daten und Liste wegen Observer
    private List<Observer> observers;
    private float temperature;
    private float humidity;

    public WeatherData() {
        observers = new ArrayList<>();
    }
//fügt neuen observer hinzu
    @Override
    public void registerObserver(Observer observer) {
        observers.add(observer);
    }
//entfernt gewünschten Observer
    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }
//benachrichtigt Observer
    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(temperature, humidity);
        }
    }
//setzt die Messungen temp und humid und aktualisiert den observer
    public void setMeasurements(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        measurementsChanged();
    }
//Aktualisierung observer
    private void measurementsChanged() {
        notifyObservers();
    }
}
//Observer die Observer implementieren erhalten updates von Weatherdata
//wenn update() aufruft die temp und humid aktualisieren danach display() aufruft
class ScreenDisplay implements Observer {
    private float temperature;
    private float humidity;
//updated temp und humid
    @Override
    public void update(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        display();
    }
//stellt Werte dar
    private void display() {
        System.out.println("Screen Display: Temperature = " + temperature + "F, Humidity = " + humidity + "%");
    }
}
//Observer die Observer implementieren erhalten updates von Weatherdata
//wenn update() aufruft die temp und humid aktualisieren danach display() aufruft
class ColorDisplay implements Observer {
    private float temperature;
    private float humidity;
//updated temp und humid
    @Override
    public void update(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        display();
    }
//stellt Werte dar
    private void display() {
        if (temperature > 75) {
            System.out.println("Color Display: Temperature = " + temperature + "F, RED" + "\n" + humidity);
        } else if (temperature > 60) {
            System.out.println("Color Display: Temperature = " + temperature + "F, YELLOW");
        } else {
            System.out.println("Color Display: Temperature = " + temperature + "F, GREEN");
        }
    }
}

//Main
public class Voyeur_Pattern {
    public static void main(String[] args) {
//setzt neue "Wetterstation"
        WeatherData weatherData = new WeatherData();

        ScreenDisplay screenDisplay = new ScreenDisplay();
        ColorDisplay colorDisplay = new ColorDisplay();
//registriert 2 Observer für wetterstation
        weatherData.registerObserver(screenDisplay);
        weatherData.registerObserver(colorDisplay);
//setzt temp und humid für wetterstation
        weatherData.setMeasurements(80, 65);
        weatherData.setMeasurements(70, 55);
//entfernt colorDisplay observer
        weatherData.removeObserver(colorDisplay);
//setzt temp und humidity erneut
        weatherData.setMeasurements(75, 60);
    }
}