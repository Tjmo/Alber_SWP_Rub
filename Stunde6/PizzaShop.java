package Stunde6;

// Die abstrakte Pizzeriaklasse, die die Schnittstelle für Pizzas definiert
abstract class Pizzeria {
    public abstract Pizza createPizza(String type);
    
    public void bakePizza(Pizza pizza) {
        System.out.println("Pizza backen...");
    }
    
    public void cutPizza(Pizza pizza) {
        System.out.println("Pizza schneiden...");
    }
    
    public void packPizza(Pizza pizza) {
        System.out.println("Pizza einpacken...");
    }
}

// Die abstrakte Klasse für Pizzas
abstract class Pizza {
    protected String name;
    
    public void prepare() {
        System.out.println("Bereite Pizza: " + name + " vor!");
    }
}

// Die spezielle Pizzeria für Berlin
class BerlinPizzeria extends Pizzeria {
    public Pizza createPizza(String type) {
        switch (type) {
            case "Salami":
                return new BerlinSalami();
            case "Hawaii":
                return new Hawaii();
            default:
                throw new IllegalArgumentException("Invalid pizza type");
        }
    }
}

// Die spezielle Pizzeria für Hamburg
class HamburgPizzeria extends Pizzeria {
    public Pizza createPizza(String type) {
        switch (type) {
            case "Salami":
                return new Salami();
            case "Quattro Stagioni":
                return new QuattroStagioni();
            default:
                throw new IllegalArgumentException("Invalid pizza type");
        }
    }
}

// Die spezielle Pizzeria für Rostock
class RostockPizzeria extends Pizzeria {
    public Pizza createPizza(String type) {
        switch (type) {
            case "Calzone":
                return new RostockCalzone();
            case "Quattro Stagioni":
                return new QuattroStagioni();
            default:
                throw new IllegalArgumentException("Invalid pizza type");
        }
    }
}

// Die konkreten Pizza-Implementierungen
class Salami extends Pizza {
    public Salami() {
        name = "Salami";
    }
}

class Hawaii extends Pizza {
    public Hawaii() {
        name = "Hawaii";
    }
}

class QuattroStagioni extends Pizza {
    public QuattroStagioni() {
        name = "Quattro Stagioni";
    }
}

class BerlinSalami extends Salami {
    public BerlinSalami() {
        name = "Berlin Salami";
    }
}

class RostockCalzone extends Pizza {
    public RostockCalzone() {
        name = "Rostock Calzone";
    }
}

// Beispielanwendung
public class PizzaShop {
        
    public static void main(String[] args) {
        Pizzeria berlinPizzeria = new BerlinPizzeria();
        Pizza berlinSalamiPizza = berlinPizzeria.createPizza("Salami");
        berlinSalamiPizza.prepare();
        berlinPizzeria.bakePizza(berlinSalamiPizza);
        berlinPizzeria.cutPizza(berlinSalamiPizza);
        berlinPizzeria.packPizza(berlinSalamiPizza);
            
        Pizzeria hamburgPizzeria = new HamburgPizzeria();
        Pizza quattroStagioniPizza = hamburgPizzeria.createPizza("Quattro Stagioni");
        quattroStagioniPizza.prepare();
        hamburgPizzeria.bakePizza(quattroStagioniPizza);
        hamburgPizzeria.cutPizza(quattroStagioniPizza);
        hamburgPizzeria.packPizza(quattroStagioniPizza);
            
        Pizzeria rostockPizzeria = new RostockPizzeria();
        Pizza rostockCalzonePizza = rostockPizzeria.createPizza("Calzone");
        rostockCalzonePizza.prepare();
        rostockPizzeria.bakePizza(rostockCalzonePizza);
        rostockPizzeria.cutPizza(rostockCalzonePizza);
        rostockPizzeria.packPizza(rostockCalzonePizza);
    }
}