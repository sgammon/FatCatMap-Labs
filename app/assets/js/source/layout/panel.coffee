## Layout - Panels
		
class Panel extends LayoutElement
	
	nothing: ->
		return
		
		
class SuperPanel extends LayoutElement

	nothing: ->
		return
		

class SuperBar extends SuperPanel
	
	initialize: ->
		$(@el).hover(
			=>
				$(@el).animate({opacity: 1.0})
			=>
				$(@el).animate({opacity: 0.8})
		)
		@el = $(@id)
		return


class SuperFooter extends SuperPanel
	
	initialize: ->
		$(@el).hover(
			=>
				$(@el).animate({opacity: 0.8})
			=>
				$(@el).animate({opacity: 0.5})
		)
		
		@$('#bottomFcmBranding a').hover(
			=>
				@$('#bottomFcmBranding a div').addClass('brandingHover')
			=>	
				@$('#bottomFcmBranding a div').removeClass('brandingHover')
		)
		
		return
		
		
class Sidebar extends LayoutElement
	
	constructor: (id, config) ->
		@id = id
		@el = $(@id)
		
		@state =
			hidden: false
			locked: false
			folded: false
			unfolded: false
			maximized: false
			
		@config =
			maximizable: false
			folded_width: 40
			unfolded_width: $('body').width() * .25
			maximized_width: $('body').width() * .70
			
		if config?
			_.extend @config, config
		
		@$('.enabled.expandButton').click((event) => @unfold())
		@$('.enabled.closeButton').click((event) => @fold())
		
		@hide = (animate=true) =>
			if @state.hidden == false
				@state.hidden = true
				if animate == true
					$(@el).animate({opacity: 0}, () => $(@el).addClass('hidden'))
				else
					$(@el).addClass('hidden')
			return @state.hidden
	
		@unhide = (animate=true) =>
			if @state.hidden == true
				@state.hidden = false
				if animate == true
					$(@el).animate({opacity: 1}, () => $(@el).removeClass('hidden'))
				else
					$(@el).removeClass('hidden')
			return @state.hidden
	
		@lock = () =>
			@state.locked = true
			@$('.expandButton').removeClass('enabled').unbind('click')
			return @state.locked
			
		@unlock = () =>
			@state.locked = false
			@$('.expandButton').addClass('enabled').click(() =>
				@unfold()
			)
			return @state.locked
	
		@fold = () =>
			@state.folded = true
			@state.unfolded = false
			@state.maximized = false
		
			@hideContent()
			
			if @$('.closeButton').hasClass('multiButton')
			
				@$('.closeButton').removeClass('closeButton').addClass('expandButton')
				
				@$('.closeMultiButton').removeClass('enabled').addClass('hidden')
				@$('.expandMultiButton').addClass('enabled').removeClass('hidden')
			
			else
				if !@$('.closeButton').hasClass('hidden')
					@$('.closeButton').addClass('hidden')
			
			if !@$('.expandButton').hasClass('enabled') and @state.locked != true
				@$('.expandButton').addClass('enabled')
		
			@$('.enabled.expandButton').unbind('click').click(
				(event) =>
					@unfold()
			)				
			
			$(@el).addClass('folded').removeClass('unfolded').animate({width: @config.folded_width})
		
		@unhideContent = () =>
			@$('.panelWrapper').animate({opacity: 1}).removeClass('hidden')
		
		@hideContent = () =>
			@$('.panelWrapper').animate({opacity: 0}).addClass('hidden')
		
		@unfold = () =>
			@state.folded = false
			@state.unfolded = true
			@state.maximized = false
		
			$(@el).addClass('unfolded').removeClass('folded').animate({width: @config.unfolded_width})
			@unhideContent()
			
			$('.enabled.closeButton').removeClass('hidden')
		
			if @config.maximizable != false
				@$('.enabled.expandButton').unbind('click').click(
					(event) =>
						console.log('maximize called')
						@maximize()
				)
			else
				if @$('.expandButton').hasClass('multiButton')
					@$('.expandMultiButton').addClass('hidden')
					@$('.closeMultiButton').removeClass('hidden')
					
					@$('.expandButton').removeClass('expandButton').addClass('closeButton')
					
					@$('.closeButton').unbind('click').click(() => @fold())
					
					
				else
					@$('.enabled.expandButton').removeClass('enabled')
		
		@minimize = () =>
			@$('.enabled.minimizeButton').removeClass('enabled').addClass('hidden')
			@$('.expandButton').addClass('enabled').removeClass('hidden')
			@unfold()

		@maximize = () =>
			@state.folded = false
			@state.unfolded = true
			@state.maximized = true
						
			@$('.enabled.expandButton').removeClass('enabled').addClass('hidden')
			@$('.minimizeButton').removeClass('hidden').addClass('enabled').unbind('click').click((ev) =>
			
				@minimize()
				
			)
			$(@el).addClass('maximized').removeClass('unfolded').animate({width: @config.maximized_width})


window.Layout.Panel = Panel
window.Layout.Sidebar = Sidebar
window.Layout.SuperBar = SuperBar
window.Layout.SuperPanel = SuperPanel
window.Layout.SuperFooter = SuperFooter