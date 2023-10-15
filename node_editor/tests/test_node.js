```javascript
const assert = require('assert');
const Node = require('../node.js');

describe('Node', function() {
  describe('#constructor()', function() {
    it('should create a new Node with the given id', function() {
      let node = new Node(1);
      assert.equal(node.id, 1);
    });

    it('should create a new Node with an empty list of edges', function() {
      let node = new Node(1);
      assert.deepEqual(node.edges, []);
    });
  });

  describe('#addEdge()', function() {
    it('should add an edge to the node', function() {
      let node = new Node(1);
      node.addEdge(2);
      assert.deepEqual(node.edges, [2]);
    });
  });

  describe('#removeEdge()', function() {
    it('should remove an edge from the node', function() {
      let node = new Node(1);
      node.addEdge(2);
      node.removeEdge(2);
      assert.deepEqual(node.edges, []);
    });
  });
});
```