package ch.ledcom.kata.train;

import java.util.function.IntFunction;

import static java.lang.String.format;

public interface Depot {
    static IntFunction<Wagon> build() {
        return (i) -> {
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
        };
    }
}
