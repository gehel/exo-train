package ch.ledcom.kata.train;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Train {

    private final Depot depot = new Depot();
    private final List<Wagon> wagons;

    public Train(String representation) {
        wagons = representation.chars().mapToObj(depot).collect(Collectors.toList());
    }

    public String print() {
        List<String> printedWagons = new ArrayList<>();
        boolean isFirst = true;
        for (Wagon w: wagons) {
            printedWagons.add(w.print(isFirst));
            isFirst = false;
        }
        return printedWagons.stream().collect(Collectors.joining("::"));
    }

    public void detachEnd() {
        wagons.remove(wagons.size() - 1);
    }

    public void detachHead() {
        wagons.remove(0);
    }

    public void fill() {
        for (Wagon w : wagons) {
            if (w.getClass().isAssignableFrom(CargoCar.class)) {
                try {
                    ((CargoCar) w).load();
                    return;
                } catch (IllegalStateException ignore) {
                    // move to next wagon
                }
            }
        }
        throw new IllegalStateException("Train already full");
    }
}
