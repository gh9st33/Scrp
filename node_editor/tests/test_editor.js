```javascript
const assert = require('assert');
const Editor = require('../editor.js');

describe('Editor', function() {
  describe('#addNode()', function() {
    it('should add a node to the editor', function() {
      let editor = new Editor();
      editor.addNode('node1');
      assert.equal(editor.nodes.length, 1);
    });
  });

  describe('#removeNode()', function() {
    it('should remove a node from the editor', function() {
      let editor = new Editor();
      editor.addNode('node1');
      editor.removeNode('node1');
      assert.equal(editor.nodes.length, 0);
    });
  });

  describe('#connectNodes()', function() {
    it('should connect two nodes', function() {
      let editor = new Editor();
      editor.addNode('node1');
      editor.addNode('node2');
      editor.connectNodes('node1', 'node2');
      assert.equal(editor.connections.length, 1);
    });
  });

  describe('#disconnectNodes()', function() {
    it('should disconnect two nodes', function() {
      let editor = new Editor();
      editor.addNode('node1');
      editor.addNode('node2');
      editor.connectNodes('node1', 'node2');
      editor.disconnectNodes('node1', 'node2');
      assert.equal(editor.connections.length, 0);
    });
  });
});
```