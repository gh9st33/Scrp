```javascript
import Node from './node.js';

class Editor {
    constructor() {
        this.nodes = [];
    }

    createNode(type, id, data) {
        const node = new Node(type, id, data);
        this.nodes.push(node);
        return node;
    }

    getNode(id) {
        return this.nodes.find(node => node.id === id);
    }

    deleteNode(id) {
        const index = this.nodes.findIndex(node => node.id === id);
        if (index !== -1) {
            this.nodes.splice(index, 1);
        }
    }

    connectNodes(sourceId, targetId) {
        const sourceNode = this.getNode(sourceId);
        const targetNode = this.getNode(targetId);
        if (sourceNode && targetNode) {
            sourceNode.connect(targetNode);
        }
    }

    disconnectNodes(sourceId, targetId) {
        const sourceNode = this.getNode(sourceId);
        const targetNode = this.getNode(targetId);
        if (sourceNode && targetNode) {
            sourceNode.disconnect(targetNode);
        }
    }

    serialize() {
        return this.nodes.map(node => node.serialize());
    }

    deserialize(data) {
        this.nodes = data.map(nodeData => Node.deserialize(nodeData));
        this.nodes.forEach(node => {
            node.connections.forEach(connectionId => {
                const targetNode = this.getNode(connectionId);
                if (targetNode) {
                    node.connect(targetNode);
                }
            });
        });
    }
}

export default Editor;
```