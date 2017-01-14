package ch.ledcom.kata.train;

public class Locomotive implements Wagon {
    @Override
    public String print(boolean isFirst) {
        return isFirst ? "<HHHH" : "HHHH>";
    }
}
