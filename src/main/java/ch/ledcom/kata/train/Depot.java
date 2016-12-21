package ch.ledcom.kata.train;

import java.util.function.IntFunction;

import static java.lang.String.format;

public class Depot implements IntFunction<Wagon> {
    @Override
    public Wagon apply(int i) {
        char c = (char) i;
        switch (c) {
            case 'H':
                return new Locomotive();
            case 'P':
                return new PassengerCar();
            case 'R':
                return new RestaurantCar();
            case 'C':
                return new CargoCar();
            default:
                throw new IllegalArgumentException(format("Wagon type %s does not exist", c));
        }
    }
}
