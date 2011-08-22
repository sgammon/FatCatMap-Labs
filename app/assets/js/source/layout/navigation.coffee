## Layout - navigation

class Navigation extends LayoutElement

	pane_class = '.navPane'

	
	register: (@id) ->

		## Allow navigation to turn opaque when the user hovers over it
		$(@selector).hover(
		
			->
				$(@selector).animate({opacity: 1.0})
				return
				
			->
				$(@selector).animate({opacity: 0.8})
				return
		
		)
		
		## Allow navigation to reveal content panes elsewhere on the page
		$('.SupernavLink').click(
		
			->
				navref = $(@).attr('data-navref')
				current_pane = $('#topnav').attr('data-currentpane')

				if current_pane isnt null or current_pane isnt undefined
					$('.navpane#'+current_pane+'Pane').addClass('hidden')

				$('#topnav').attr('data-currentpane', navref)

				expanded = $('#contentHeader').attr('data-expanded')
				if expanded is null or expanded is undefined or expanded != 'true'
					$('#contentHeader').slideDown().removeClass('hidden')
					$('#contentHeader').attr('data-expanded', 'true')
					
				$('.navpane#'+navref+'Pane').removeClass('hidden')					
				
		)
		
		## Allow content panes to be folded back when not in use
		$('.foldNavigation').click(
		
			->
				navref = @.getAttribute('data-navref')
				current_pane = $('#topnav').attr('data-currentpane')
				if current_pane isnt null or current_pane isnt undefined
					$('#topnav').removeAttr('data-currentpane')
				
				$('#contentHeader').slideUp()
				$('#contentHeader').removeAttr('data-expanded')
				
		)
		
window.Layout.Navigation = Navigation