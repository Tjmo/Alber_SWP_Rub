package Stunde8;

// Eine Schnittstelle für einen Drucker, die die print-Methode definiert.
interface Printer {
    void print(String text);
}
// a Druckerklasse dia die Printer-Schnittstelle implementiert
// und en Text in Schwarzweiß druckt
class BlackAndWhitePrinter implements Printer {
    @Override
    public void print(String text) {
        System.out.println("Printing in black and white: " + text);
    }
}
// a Druckerklasse dia die Printer-Schnittstelle implementiert
// und en Text in Farbe druckt
class ColorPrinter implements Printer {
    @Override
    public void print(String text) {
        System.out.println("Printing in color: " + text);
    }
}
// a Proxy-Klasse für an Drucker, dia ebenfalls die Printer-Schnittstelle implementiert
// die Klasse enthält eine Referenz auf einen konkreten Drucker und bietet a Methode
// um den zugewiesenen Drucker während der Laufzeit zu ändern
class PrinterProxy implements Printer {
    private Printer printer;
    
    public PrinterProxy(Printer printer) {
        this.printer = printer;
    }
    // a verbesserte switchTo-Methode dia die aktuelle Druckerinstanz zurückgibt
    // bevor sie en neuen Drucker zuweist
    public void switchTo(Printer newPrinter) {
        this.printer = newPrinter;
    }
    
    // Implementierung der print-Methode der Printer-Schnittstelle,
    // dia die print-Methode des zugewiesenen Druckers aufruaft
    @Override
    public void print(String text) {
        printer.print(text);
    }
}
// a Beispielprogramm, das den PrinterProxy verwendet, um zwischen
// am Schwarzweiß- und einem Farbdrucker zu wechseln
public class Proxy_Muster {
    public static void main(String[] args) {
        PrinterProxy printer = new PrinterProxy(new BlackAndWhitePrinter());
        printer.print("Hallo alte Welt!");
        printer.switchTo(new ColorPrinter());
        printer.print("Hallo Farbfernsehn!");
    }
}