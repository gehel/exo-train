package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestPassengerTrain(t *testing.T) {
	var train = &Train{"HPP"}
	assert.Equal(t, "<HHHH::|OOOO|::|OOOO|", train.Print(), "Train output should match expected")

}

func TestRestaurantTrain(t *testing.T) {
	var train = &Train{"HPRP"}
	assert.Equal(t, "<HHHH::|OOOO|::|hThT|::|OOOO|", train.Print(), "Train output should match expected")
}

func TestDoubleHeadedTrain(t *testing.T) {
	var train = &Train{"HPRPH"}
	assert.Equal(t, "<HHHH::|OOOO|::|hThT|::|OOOO|::HHHH>", train.Print(), "Train output should match expected")

}

func TestModifyTrain(t *testing.T) {
	var train = &Train{"HPRPH"}
	train.DetachEnd()
	assert.Equal(t, "<HHHH::|OOOO|::|hThT|::|OOOO|", train.Print(), "Train output should match expected")

	train.DetachHead()
	assert.Equal(t, "|OOOO|::|hThT|::|OOOO|", train.Print(), "Train output should match expected")

}

func TestCargoTrain(t *testing.T) {
	var train = &Train{"HCCC"}
	require.Equal(t, "<HHHH::|____|::|____|::|____|", train.Print(), "Train output should match expected")

	train.Fill()
	require.Equal(t, "<HHHH::|^^^^|::|____|::|____|", train.Print(), "Train output should match expected")

	train.Fill()
	require.Equal(t, "<HHHH::|^^^^|::|^^^^|::|____|", train.Print(), "Train output should match expected")

	train.Fill()
	require.Equal(t, "<HHHH::|^^^^|::|^^^^|::|^^^^|", train.Print(), "Train output should match expected")

	_, err := train.Fill()
	if err == nil {
		t.Errorf("Filling a train that is already full should return an error")
	}
}

func TestMixedTrain(t *testing.T) {
	var train = &Train{"HPCPC"}
	require.Equal(t, "<HHHH::|OOOO|::|____|::|OOOO|::|____|", train.Print(), "Train output should match expected")

	train.Fill()
	require.Equal(t, "<HHHH::|OOOO|::|^^^^|::|OOOO|::|____|", train.Print(), "Train output should match expected")

	train.Fill()

	require.Equal(t, "<HHHH::|OOOO|::|^^^^|::|OOOO|::|^^^^|", train.Print(), "Train output should match expected")

	_, err := train.Fill()
	if err == nil {
		t.Errorf("Filling a train that is already full should return an error")
	}
}
