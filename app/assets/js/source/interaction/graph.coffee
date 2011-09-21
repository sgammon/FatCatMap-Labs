class GraphArtifact extends RemoteModel


class Node extends GraphArtifact
	
	
class Edge extends GraphArtifact
	
	
class GraphSprite extends InteractiveWidget
	
	
class GraphNode extends GraphSprite
	
	
class GraphEdge extends GraphSprite
	
	
class NodeCollection extends ModelCollection
	
	model: Node
	
	
class EdgeCollection extends ModelCollection
	
	model: Edge
	
	
class Graph extends InteractiveWidget
	
	constructor: (id, data, config) ->
		
		@id = id
		@el = $(@id)
		
		@config =
			physics:
				theta: 0.8
				charge: -100
				gravity: .05
				distance: 100
				friction: 0.9
				
		@natives =
			node: null
			edge: null
			force: null
			visualizer: null
		
		@index =
			filled_keys: []		
			nodes_by_key: {}
			edges_by_node: {}
			encountered_nodes: []
			encountered_edges: []
			encountered_hints: []
			
		@state =
			drawn: false
			hidden: false
			locked: false
			static: false
			rendered: false
					
		@data =
			nodes: []
			edges: []
			hints: []
			
			getNodes: () =>
				return @data.nodes

			getEdges: () =>
				return @data.edges

			getHints: () =>
				return @data.hints
			
			getNode: (key) =>
				if key in @index.encountered_nodes
					return @index.nodes_by_key[key]
					
			getEdge: (key) =>
				edge_keypair = edge.source.key.encoded+'::->::'+edge.target.key.encoded
				return @index.edges_by_keypair(edge_keypair)
				
			getHint: (key) =>
				if key in @index.encountered_hints
					return @data.hints[_.indexOf(@index.encountered_hints, key)]

			setNode: (node) =>
				if node.key.encoded not in @index.encountered_nodes
					index = @data.nodes.push(node) - 1
					@index.nodes_by_key[node.key.encoded] = {nindex: index, data: @data.nodes[index]}
					@index.edges_by_node[node.key.encoded] = {outgoing: [], incoming: []}
					@index.encountered_nodes.push(node.key.encoded)

					return index
				else
					return _.indexOf(@index.encountered_nodes, node.key.encoded)
					
			setEdge: (edge, nodemap) =>
				if not nodemap?
					nodemap = @data.nodes
					
					edge =
						source: @data.nodes[edge.source]
						target: @data.nodes[edge.target]
				else
					edge =
						source: @data.nodes[nodemap[edge.source]]
						target: @data.nodes[nodemap[edge.target]]
					
				edge_keypair = edge.source.key.encoded+'::->::'+edge.target.key.encoded
				
				if edge_keypair not in @index.encountered_edges
					index = @data.edges.push(edge) - 1
					@index.edges_by_node[edge.source.key.encoded].outgoing.push({eindex: index, target: @data.getNode(edge.target.key.encoded)})
					@index.edges_by_node[edge.target.key.encoded].incoming.push({eindex: index, source: @data.getNode(edge.source.key.encoded)})
					@index.encountered_edges.push(edge_keypair)
					
					return index
				else
					return _.indexOf(@index.encountered_edges, edge_keypair)
					
			setHint: (hint, edgemap) =>
				if hint.key.encoded not in @index.encountered_hints
					index = @data.hints.push(hint) - 1
					@index.encountered_hints.push(hint.key.encoded)
					
					return index
				else
					return _.indexOf(@index.encountered_hints, hint.key.encoded)
				

	build: (rpc_params, fillNodes=true, fillEdges=false) ->
			
		request = $.fatcatmap.rpc.api.graph.construct(rpc_params)
		request.fulfill(
		
			success: (data) =>
				
				nodemap = []
				_.each( data.graph.vertices, (node, i) =>
					nodemap.push(@data.setNode(node))
				 )
				
				edgemap = []
				_.each( data.graph.vectors, (edge) =>
					edgemap.push(@data.setEdge(edge, nodemap))
				)
				
				hintmap = []
				_.each( data.graph.hints, (hint) =>
					hintmap.push(@data.setHint(hint, edgemap))
				)
				
				@draw()
				@fill(fillNodes, fillEdges)
				
				return
				
			failure: (event) =>
			
				$.fcm.dev.error('Graph', 'Could not complete graph build operation.', event)
				alert 'Could not construct graph.'
				
		)
		
		return @


	fill: (nodes=true, edges=false) ->
		keys = []
		types = []
		
		if nodes
			types.push(@index.encountered_nodes)
		
		if edges
			types.push(@index.encountered_edges)
		
		for type in types
			for key in type
				if key not in @index.filled_keys
					keys.push(key)
					
		if key.length > 0
			data_request = $.fatcatmap.rpc.api.data.get({keys: keys})
			data_request.fulfill({success: @_dataSuccessCallback, failure: @_dataFailureCallback})
		return @
		

	_dataSuccessCallback: (content) ->
		console.log('data response', content)

	_dataFailureCallback: (error) ->
		console.log('data error', error)

	render: () ->

		el = $(@el)

		if @state.rendered is not true
			# 1: Create viz panel
			@natives.visualizer = d3.select(@id)
				.append("svg:svg")
				.attr("width", @el.width())
				.attr("height", @el.height())

			@natives.visualizer.style("opacity", 1e-6)
								.transition()
									.duration(1500)
									.style("opacity", 1)				
				
		@state.rendered = true
		
		return @
	
	
	draw: () ->
		
		# 2: Add force-driven layout to visualizer panel
		@natives.force = d3.layout.force()
			.charge(@config.physics.charge)
			.gravity(@config.physics.gravity)
			.distance(@config.physics.distance)
			.theta(@config.physics.theta)
			.friction(@config.physics.friction)		
			.nodes(@data.getNodes())
			.links(@data.getEdges())
			.size([@el.width(), @el.height()])
			.start()
		
		## Build edges
		@natives.edge = @natives.visualizer.selectAll("line.link")
			.data(@data.getEdges())
		 	.enter().append("svg:line")
				.attr("data-source-node-key", (d) -> return d.source.key.encoded)
				.attr("data-target-node-key", (d) -> return d.target.key.encoded)
				.attr("class", "edge")
				.attr("x1", (d) -> return d.source.x)
				.attr("y1", (d) -> return d.source.y)
				.attr("x2", (d) -> return d.target.x)
				.attr("y2", (d) -> return d.target.y)
		
		## Build nodes
		@natives.node = @natives.visualizer.selectAll("g.node")
			.data(@data.getNodes())
			.enter().append("svg:g")
				.attr("id", (d) -> d.key.encoded)
				.attr("class", "node")
				.attr('data-kind', (d) -> d.kind)
				.attr('data-label', (d) -> d.label)
				.attr("data-object-key", (d) -> d.key.parent)
				.call(@natives.force.drag)
				.on('click', (d) =>
					$('#nodekey').text(d.key.encoded)
					$('#nodelabel').text(d.label)
					detailspane.unfold()
				)
		
		@natives.node.append("svg:circle")
			.attr("class", "circle")
			.attr("x", '-8px')
			.attr("y", '-8px')
			.attr("r", 16);

		@natives.node.append("svg:text")
			.attr('x', -4)
			.attr('y', 4)
			.attr('class', 'label')		
			.text((d) => @data.getNode(d.key.encoded).nindex.toString())
			
		@natives.force.on("tick", () =>

			## Bind edge x, y
			@natives.edge.attr("x1", (d, i) -> d.source.x)
						 .attr("y1", (d, i) -> d.source.y)
						 .attr("x2", (d, i) -> d.target.x)
						 .attr("y2", (d, i) -> d.target.y)

			## Bind node transform
			@natives.node.attr('transform', (d, i) -> 'translate('+d.x+','+d.y+')')
						 .attr('cx', (d, i) -> d.x)
						 .attr('cy', (d, i) -> d.y)

			## Bind force physics
			@natives.force.charge(@config.physics.charge)
						  .gravity(@config.physics.gravity)
						  .distance(@config.physics.distance)
						  .theta(@config.physics.theta)
						  .friction(@config.physics.friction)		
		)
		
		@state.drawn = true
		
		return @
		

## Export all of it
window.Models.GraphArtifact = GraphArtifact
window.Models.Node = Node
window.Models.Edge = Edge

window.Interaction =
	GraphSprite: GraphSprite
	GraphNode: GraphNode
	GraphEdge: GraphEdge
	NodeCollection: NodeCollection
	EdgeCollection: EdgeCollection
	Graph: Graph