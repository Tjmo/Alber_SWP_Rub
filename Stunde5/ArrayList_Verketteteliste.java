package Stunde5;

import java.util.ArrayList;
//implementiert verketteteliste
public class ArrayList_Verketteteliste {
    private ArrayList<Integer> list;

    //definiert arraylist mit privater instanz list (container für integer-werte)
    public ArrayList_Verketteteliste() {
        this.list = new ArrayList<Integer>();
    }

    //fügt neues element num zum ende der arraylist hinzu
    public void add(int num) {
        this.list.add(num);
    }
    //entfernt "index" aus liste
    public void remove(int index) {
        this.list.remove(index);
    }
    //gibt element an stelle index zurück
    public int get(int index) {
        return this.list.get(index);
    }
    //gibt die anzahl der elemente zurück
    public int size() {
        return this.list.size();
    }

    //erstellt eine neue arrayList und fügt werte 5,10,15 hinzu
    //gibt danach größe aus danach element an stelle 1 entfernen
    public static void main(String[] args) {
        ArrayList_Verketteteliste myArrayList = new ArrayList_Verketteteliste();
        myArrayList.add(5);
        myArrayList.add(10);
        myArrayList.add(15);

        System.out.println("Groesse: " + myArrayList.size());

        for (int i = 0; i < myArrayList.size(); i++) {
            System.out.println("Element an der Stelle " + i + ": " + myArrayList.get(i));
        }

        myArrayList.remove(1);

        System.out.println("Größe nach der Entfernung des Element an der Stelle 1: " + myArrayList.size());

        for (int i = 0; i < myArrayList.size(); i++) {
            System.out.println("Element an der Stelle " + i + ": " + myArrayList.get(i));
        }
    }
}