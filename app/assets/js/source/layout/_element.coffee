class LayoutElement extends Backbone.View

	id: null
	name: null
	state: {}
	config: {}
	classes: []
	element: null
	defaults: null	
	selector: null
	registered: false
	
	register: (@name) ->
		
		
if window?
	window.LayoutElement = LayoutElement
	window.Layout = {}