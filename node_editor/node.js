```javascript
class Node {
    constructor(id, type, inputs = [], outputs = []) {
        this.id = id;
        this.type = type;
        this.inputs = inputs;
        this.outputs = outputs;
    }

    addInput(input) {
        this.inputs.push(input);
    }

    addOutput(output) {
        this.outputs.push(output);
    }

    removeInput(input) {
        const index = this.inputs.indexOf(input);
        if (index > -1) {
            this.inputs.splice(index, 1);
        }
    }

    removeOutput(output) {
        const index = this.outputs.indexOf(output);
        if (index > -1) {
            this.outputs.splice(index, 1);
        }
    }
}

module.exports = Node;
```