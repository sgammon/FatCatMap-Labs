(function() {
  var Edge, EdgeCollection, Graph, GraphArtifact, GraphEdge, GraphNode, GraphSprite, InteractiveWidget, Node, NodeCollection, RouteController;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  }, __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; }, __indexOf = Array.prototype.indexOf || function(item) {
    for (var i = 0, l = this.length; i < l; i++) {
      if (this[i] === item) return i;
    }
    return -1;
  };
  RouteController = (function() {
    __extends(RouteController, Backbone.Router);
    function RouteController() {
      RouteController.__super__.constructor.apply(this, arguments);
    }
    return RouteController;
  })();
  InteractiveWidget = (function() {
    __extends(InteractiveWidget, Backbone.View);
    function InteractiveWidget(name, path, config) {
      this.name = name;
      this.path = path;
      this.config = config;
    }
    return InteractiveWidget;
  })();
  GraphArtifact = (function() {
    __extends(GraphArtifact, RemoteModel);
    function GraphArtifact() {
      GraphArtifact.__super__.constructor.apply(this, arguments);
    }
    return GraphArtifact;
  })();
  Node = (function() {
    __extends(Node, GraphArtifact);
    function Node() {
      Node.__super__.constructor.apply(this, arguments);
    }
    return Node;
  })();
  Edge = (function() {
    __extends(Edge, GraphArtifact);
    function Edge() {
      Edge.__super__.constructor.apply(this, arguments);
    }
    return Edge;
  })();
  GraphSprite = (function() {
    __extends(GraphSprite, InteractiveWidget);
    function GraphSprite() {
      GraphSprite.__super__.constructor.apply(this, arguments);
    }
    return GraphSprite;
  })();
  GraphNode = (function() {
    __extends(GraphNode, GraphSprite);
    function GraphNode() {
      GraphNode.__super__.constructor.apply(this, arguments);
    }
    return GraphNode;
  })();
  GraphEdge = (function() {
    __extends(GraphEdge, GraphSprite);
    function GraphEdge() {
      GraphEdge.__super__.constructor.apply(this, arguments);
    }
    return GraphEdge;
  })();
  NodeCollection = (function() {
    __extends(NodeCollection, ModelCollection);
    function NodeCollection() {
      NodeCollection.__super__.constructor.apply(this, arguments);
    }
    NodeCollection.prototype.model = Node;
    return NodeCollection;
  })();
  EdgeCollection = (function() {
    __extends(EdgeCollection, ModelCollection);
    function EdgeCollection() {
      EdgeCollection.__super__.constructor.apply(this, arguments);
    }
    EdgeCollection.prototype.model = Edge;
    return EdgeCollection;
  })();
  Graph = (function() {
    __extends(Graph, InteractiveWidget);
    function Graph(id, data, config) {
      this.id = id;
      this.el = $(this.id);
      this.config = {
        physics: {
          theta: 0.8,
          charge: -100,
          gravity: .05,
          distance: 100,
          friction: 0.9
        }
      };
      this.natives = {
        node: null,
        edge: null,
        force: null,
        visualizer: null
      };
      this.index = {
        filled_keys: [],
        nodes_by_key: {},
        edges_by_node: {},
        encountered_nodes: [],
        encountered_edges: [],
        encountered_hints: []
      };
      this.state = {
        drawn: false,
        hidden: false,
        locked: false,
        static: false,
        rendered: false
      };
      this.data = {
        nodes: [],
        edges: [],
        hints: [],
        getNodes: __bind(function() {
          return this.data.nodes;
        }, this),
        getEdges: __bind(function() {
          return this.data.edges;
        }, this),
        getHints: __bind(function() {
          return this.data.hints;
        }, this),
        getNode: __bind(function(key) {
          if (__indexOf.call(this.index.encountered_nodes, key) >= 0) {
            return this.index.nodes_by_key[key];
          }
        }, this),
        getEdge: __bind(function(key) {
          var edge_keypair;
          edge_keypair = edge.source.key.encoded + '::->::' + edge.target.key.encoded;
          return this.index.edges_by_keypair(edge_keypair);
        }, this),
        getHint: __bind(function(key) {
          if (__indexOf.call(this.index.encountered_hints, key) >= 0) {
            return this.data.hints[_.indexOf(this.index.encountered_hints, key)];
          }
        }, this),
        setNode: __bind(function(node) {
          var index, _ref;
          if (_ref = node.key.encoded, __indexOf.call(this.index.encountered_nodes, _ref) < 0) {
            index = this.data.nodes.push(node) - 1;
            this.index.nodes_by_key[node.key.encoded] = {
              nindex: index,
              data: this.data.nodes[index]
            };
            this.index.edges_by_node[node.key.encoded] = {
              outgoing: [],
              incoming: []
            };
            this.index.encountered_nodes.push(node.key.encoded);
            return index;
          } else {
            return _.indexOf(this.index.encountered_nodes, node.key.encoded);
          }
        }, this),
        setEdge: __bind(function(edge, nodemap) {
          var edge_keypair, index;
          if (!(nodemap != null)) {
            nodemap = this.data.nodes;
            edge = {
              source: this.data.nodes[edge.source],
              target: this.data.nodes[edge.target]
            };
          } else {
            edge = {
              source: this.data.nodes[nodemap[edge.source]],
              target: this.data.nodes[nodemap[edge.target]]
            };
          }
          edge_keypair = edge.source.key.encoded + '::->::' + edge.target.key.encoded;
          if (__indexOf.call(this.index.encountered_edges, edge_keypair) < 0) {
            index = this.data.edges.push(edge) - 1;
            this.index.edges_by_node[edge.source.key.encoded].outgoing.push({
              eindex: index,
              target: this.data.getNode(edge.target.key.encoded)
            });
            this.index.edges_by_node[edge.target.key.encoded].incoming.push({
              eindex: index,
              source: this.data.getNode(edge.source.key.encoded)
            });
            this.index.encountered_edges.push(edge_keypair);
            return index;
          } else {
            return _.indexOf(this.index.encountered_edges, edge_keypair);
          }
        }, this),
        setHint: __bind(function(hint, edgemap) {
          var index, _ref;
          if (_ref = hint.key.encoded, __indexOf.call(this.index.encountered_hints, _ref) < 0) {
            index = this.data.hints.push(hint) - 1;
            this.index.encountered_hints.push(hint.key.encoded);
            return index;
          } else {
            return _.indexOf(this.index.encountered_hints, hint.key.encoded);
          }
        }, this)
      };
    }
    Graph.prototype.build = function(rpc_params, fillNodes, fillEdges) {
      var request;
      if (fillNodes == null) {
        fillNodes = true;
      }
      if (fillEdges == null) {
        fillEdges = false;
      }
      request = $.fatcatmap.rpc.api.graph.construct(rpc_params);
      request.fulfill({
        success: __bind(function(data) {
          var edgemap, hintmap, nodemap;
          nodemap = [];
          _.each(data.graph.vertices, __bind(function(node, i) {
            return nodemap.push(this.data.setNode(node));
          }, this));
          edgemap = [];
          _.each(data.graph.vectors, __bind(function(edge) {
            return edgemap.push(this.data.setEdge(edge, nodemap));
          }, this));
          hintmap = [];
          _.each(data.graph.hints, __bind(function(hint) {
            return hintmap.push(this.data.setHint(hint, edgemap));
          }, this));
          this.draw();
          this.fill(fillNodes, fillEdges);
        }, this),
        failure: __bind(function(event) {
          $.fcm.dev.error('Graph', 'Could not complete graph build operation.', event);
          return alert('Could not construct graph.');
        }, this)
      });
      return this;
    };
    Graph.prototype.fill = function(nodes, edges) {
      var data_request, key, keys, type, types, _i, _j, _len, _len2;
      if (nodes == null) {
        nodes = true;
      }
      if (edges == null) {
        edges = false;
      }
      keys = [];
      types = [];
      if (nodes) {
        types.push(this.index.encountered_nodes);
      }
      if (edges) {
        types.push(this.index.encountered_edges);
      }
      for (_i = 0, _len = types.length; _i < _len; _i++) {
        type = types[_i];
        for (_j = 0, _len2 = type.length; _j < _len2; _j++) {
          key = type[_j];
          if (__indexOf.call(this.index.filled_keys, key) < 0) {
            keys.push(key);
          }
        }
      }
      if (key.length > 0) {
        data_request = $.fatcatmap.rpc.api.data.get({
          keys: keys
        });
        data_request.fulfill({
          success: this._dataSuccessCallback,
          failure: this._dataFailureCallback
        });
      }
      return this;
    };
    Graph.prototype._dataSuccessCallback = function(content) {
      return console.log('data response', content);
    };
    Graph.prototype._dataFailureCallback = function(error) {
      return console.log('data error', error);
    };
    Graph.prototype.render = function() {
      var el;
      el = $(this.el);
      if (this.state.rendered === !true) {
        this.natives.visualizer = d3.select(this.id).append("svg:svg").attr("width", this.el.width()).attr("height", this.el.height());
        this.natives.visualizer.style("opacity", 1e-6).transition().duration(1500).style("opacity", 1);
      }
      this.state.rendered = true;
      return this;
    };
    Graph.prototype.draw = function() {
      this.natives.force = d3.layout.force().charge(this.config.physics.charge).gravity(this.config.physics.gravity).distance(this.config.physics.distance).theta(this.config.physics.theta).friction(this.config.physics.friction).nodes(this.data.getNodes()).links(this.data.getEdges()).size([this.el.width(), this.el.height()]).start();
      this.natives.edge = this.natives.visualizer.selectAll("line.link").data(this.data.getEdges()).enter().append("svg:line").attr("data-source-node-key", function(d) {
        return d.source.key.encoded;
      }).attr("data-target-node-key", function(d) {
        return d.target.key.encoded;
      }).attr("class", "edge").attr("x1", function(d) {
        return d.source.x;
      }).attr("y1", function(d) {
        return d.source.y;
      }).attr("x2", function(d) {
        return d.target.x;
      }).attr("y2", function(d) {
        return d.target.y;
      });
      this.natives.node = this.natives.visualizer.selectAll("g.node").data(this.data.getNodes()).enter().append("svg:g").attr("id", function(d) {
        return d.key.encoded;
      }).attr("class", "node").attr('data-kind', function(d) {
        return d.kind;
      }).attr('data-label', function(d) {
        return d.label;
      }).attr("data-object-key", function(d) {
        return d.key.parent;
      }).call(this.natives.force.drag).on('click', __bind(function(d) {
        $('#nodekey').text(d.key.encoded);
        $('#nodelabel').text(d.label);
        return detailspane.unfold();
      }, this));
      this.natives.node.append("svg:circle").attr("class", "circle").attr("x", '-8px').attr("y", '-8px').attr("r", 16);
      this.natives.node.append("svg:text").attr('x', -4).attr('y', 4).attr('class', 'label').text(__bind(function(d) {
        return this.data.getNode(d.key.encoded).nindex.toString();
      }, this));
      this.natives.force.on("tick", __bind(function() {
        this.natives.edge.attr("x1", function(d, i) {
          return d.source.x;
        }).attr("y1", function(d, i) {
          return d.source.y;
        }).attr("x2", function(d, i) {
          return d.target.x;
        }).attr("y2", function(d, i) {
          return d.target.y;
        });
        this.natives.node.attr('transform', function(d, i) {
          return 'translate(' + d.x + ',' + d.y + ')';
        }).attr('cx', function(d, i) {
          return d.x;
        }).attr('cy', function(d, i) {
          return d.y;
        });
        return this.natives.force.charge(this.config.physics.charge).gravity(this.config.physics.gravity).distance(this.config.physics.distance).theta(this.config.physics.theta).friction(this.config.physics.friction);
      }, this));
      this.state.drawn = true;
      return this;
    };
    return Graph;
  })();
  window.Models.GraphArtifact = GraphArtifact;
  window.Models.Node = Node;
  window.Models.Edge = Edge;
  window.Interaction = {
    GraphSprite: GraphSprite,
    GraphNode: GraphNode,
    GraphEdge: GraphEdge,
    NodeCollection: NodeCollection,
    EdgeCollection: EdgeCollection,
    Graph: Graph
  };
}).call(this);
