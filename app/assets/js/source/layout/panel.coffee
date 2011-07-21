## Layout - Panels
		
class Panel extends LayoutElement
	
	nothing: ->
		return
		
		
class SuperPanel extends LayoutElement

	nothing: ->
		return
		

class SuperBar extends SuperPanel
	
	register: (@id) ->
		$('#momentumSuperbar').hover(
		
			->
				$('#momentumSuperbar').animate({opacity: 1.0})
			
			->
				$('#momentumSuperbar').animate({opacity: 0.8})
		
		)
		return


class SuperFooter extends SuperPanel
	
	register: (@id) ->
		$('#momentumSuperfooter').hover(
		
			->
				$('#momentumSuperfooter').animate({opacity: 0.8})
				
			->
				$('#momentumSuperfooter').animate({opacity: 0.5})
		
		)
		
		$('#bottomFcmBranding a').hover(
		
			->
				$('#bottomFcmBranding a div').addClass('brandingHover')
				
			->
				$('#bottomFcmBranding a div').removeClass('brandingHover')
		
		)
		
		return
		
		
class Sidebar extends LayoutElement
	
	fold: () ->
		return
		
	unfold: () ->
		return
		
	minimize: () ->
		return
		
	maximize: () ->
		return


window.Panel = Panel
window.Sidebar = Sidebar
window.SuperBar = SuperBar
window.SuperPanel = SuperPanel
window.SuperFooter = SuperFooter