```javascript
const Editor = require('./editor.js');
const Node = require('./node.js');

class Main {
    constructor() {
        this.editor = new Editor();
    }

    createNode(id, type, data) {
        let node = new Node(id, type, data);
        this.editor.addNode(node);
    }

    removeNode(id) {
        this.editor.removeNode(id);
    }

    connectNodes(sourceId, targetId) {
        this.editor.connectNodes(sourceId, targetId);
    }

    disconnectNodes(sourceId, targetId) {
        this.editor.disconnectNodes(sourceId, targetId);
    }

    saveEditorState() {
        let state = this.editor.saveState();
        // Save state to database or file
    }

    loadEditorState(state) {
        this.editor.loadState(state);
    }
}

module.exports = Main;
```