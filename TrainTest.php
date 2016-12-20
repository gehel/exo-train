<?php

use PHPUnit\Framework\TestCase;

class TrainTest extends TestCase
{


    public function testPassengerTrain()
    {
        $train = new Train("HPP");
        $this->assertEquals("<HHHH::|OOOO|::|OOOO|", $train->print());
    }

    public function testRestaurantRrain()
    {
        $train = new Train("HPRP");
        $this->assertEquals("<HHHH::|OOOO|::|hThT|::|OOOO|", $train->print());
    }

    public function testDoubleHeadedTrain()
    {
        $train = new Train("HPRPH");
        $this->assertEquals("<HHHH::|OOOO|::|hThT|::|OOOO|::HHHH>", $train->print());
    }

    public function testModifyTrain()
    {
        $train = new Train("HPRPH");
        $train->detachEnd();
        $train->assertEquals("<HHHH::|OOOO|::|hThT|::|OOOO|", $train->print());
        $train->detachHead();
        $train->assertEquals("|OOOO|::|hThT|::|OOOO|", $train->print());
    }

    public function testCargoTrain()
    {
        $train = new Train("HCCC");
        $this->assertEquals("<HHHH::|____|::|____|::|____|", $train->print());
        $train->fill();
        $this->assertEquals("<HHHH::|^^^^|::|____|::|____|", $train->print());
        $train->fill();
        $this->assertEquals("<HHHH::|^^^^|::|^^^^|::|____|", $train->print());
        $train->fill();
        $this->assertEquals("<HHHH::|^^^^|::|^^^^|::|^^^^|", $train->print());
        $this->assertFalse($train->fill());
    }

    public function testMixedTrain()
    {
        $train = new Train("HPCPC");
        $this->assertEquals("<HHHH::|OOOO|::|____|::|OOOO|::|____|", $train->print());
        $train->fill();
        $this->assertEquals("<HHHH::|OOOO|::|^^^^|::|OOOO|::|____|", $train->print());
        $train->fill();
        $this->assertEquals("<HHHH::|OOOO|::|^^^^|::|OOOO|::|^^^^|", $train->print());
        $this->assertFalse($train->fill());
    }

}
