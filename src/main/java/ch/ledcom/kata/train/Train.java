package ch.ledcom.kata.train;

import java.util.LinkedList;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toCollection;

public class Train {

    private final LinkedList<Wagon> wagons;

    public Train(String representation) {
        wagons = representation.chars()
                .mapToObj(Depot.build())
                .collect(toCollection(LinkedList::new));
    }

    public String print() {
        final Wagon firstWagon = wagons.isEmpty() ? null : wagons.getFirst();
        return wagons.stream()
                .map(w -> w.print(firstWagon == w))
                .collect(joining("::"));
    }

    public void detachEnd() {
        wagons.removeLast();
    }

    public void detachHead() {
        wagons.removeFirst();
    }

    public void fill() {
        wagons.stream()
                .filter(CargoCar.class::isInstance)
                .map(w -> (CargoCar) w)
                .filter(CargoCar::isEmpty)
                .findFirst()
                .orElseThrow(() -> new IllegalStateException("Train already full"))
                .load();
    }
}
