package ch.ledcom.kata.train;

public class CargoCar implements Wagon {

    private boolean filled = false;

    @Override
    public String print(boolean isFirst) {
        return filled ? "|^^^^|" : "|____|";
    }

    public void load() {
        if (filled) throw new IllegalStateException("wagon already full");
        filled = true;
    }

    public boolean isEmpty() {
        return !filled;
    }
}
