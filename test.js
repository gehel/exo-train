const assert = require('assert');
const Train = require('./Train');

describe('Train Task Test', function() {
    it('Should print out passenger train', function() {
		const train = new Train("HPP");
		assert.deepStrictEqual("<HHHH::|OOOO|::|OOOO|", train.print())
    });

	it('Should print out restaurant train', function() {
		const train = new Train("HPRP");
		assert.deepStrictEqual("<HHHH::|OOOO|::|hThT|::|OOOO|", train.print())
	});

	it('Should print out double headed train', function() {
		const train = new Train("HPRPH");
		assert.deepStrictEqual("<HHHH::|OOOO|::|hThT|::|OOOO|::HHHH>", train.print())
	});

	it('Should correctly detach parts of train', function() {
		const train = new Train("HPRPH");
		train.detachEnd();
		assert.deepStrictEqual("<HHHH::|OOOO|::|hThT|::|OOOO|", train.print());
		train.detachHead();
		assert.deepStrictEqual("|OOOO|::|hThT|::|OOOO|", train.print());
	});

	it('Should throw error when filling an already full cargo train', function() {
		const train = new Train("HCCC");
		assert.deepStrictEqual("<HHHH::|____|::|____|::|____|", train.print());
		train.fill();
		assert.deepStrictEqual("<HHHH::|^^^^|::|____|::|____|", train.print());
		train.fill();
		assert.deepStrictEqual("<HHHH::|^^^^|::|^^^^|::|____|", train.print());
		train.fill();
		assert.deepStrictEqual("<HHHH::|^^^^|::|^^^^|::|^^^^|", train.print());
		try {
			train.fill();
			assert.fail("Filling a train that is already full should throw exception");
		} catch (err) { 
			assert(err instanceof Error);
			assert.deepStrictEqual(err.message, "Train is already full")
		}
	});

	it('Should throw error when filling an already full mixed train', function() {
		const train = new Train("HPCPC");
		assert.deepStrictEqual("<HHHH::|OOOO|::|____|::|OOOO|::|____|", train.print());
		train.fill();
		assert.deepStrictEqual("<HHHH::|OOOO|::|^^^^|::|OOOO|::|____|", train.print());
		train.fill();
		assert.deepStrictEqual("<HHHH::|OOOO|::|^^^^|::|OOOO|::|^^^^|", train.print());
		try {
			train.fill();
			assert.fail("Filling a train that is already full should throw exception");
		} catch (err) { 
			assert(err instanceof Error);
			assert.deepStrictEqual(err.message, "Train is already full")
		}
	});
})