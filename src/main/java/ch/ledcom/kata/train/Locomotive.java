package ch.ledcom.kata.train;

public class Locomotive implements Wagon {
    @Override
    public String print(boolean isFirst) {
        if (isFirst) return "<HHHH";
        else return "HHHH>";
    }

}
