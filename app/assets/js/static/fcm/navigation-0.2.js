_currentNavpane = null;

function bindNavigation()
{
	$('.momentumSuperbar').hover(
		function superbarHover() {
			$(this).animate({opacity:1.0});
		},
		function superbarUnhover() {
			$(this).animate({opacity:0.8});
		}
	);

	$('.momentumSuperfooter').hover(
		function superfooterHover() {
			$(this).animate({opacity:0.8});
		},
		function superfooterUnhover() {
			$(this).animate({opacity:0.5});
		}
	);
	
	$('#bottomFcmBranding a').hover(
		function momentumHover() {
			$('#bottomFcmBranding a div').addClass('brandingHover');
		},
		function momentumUnhover() {
			$('#bottomFcmBranding a div').removeClass('brandingHover');
		}
	);
	
	$('.SupernavLink').click(
		function showNavMenu() {
			navref = this.getAttribute('data-navref');
			if (_currentNavpane == null)
			{
				_currentNavpane = navref;
			}
			else
			{
				$('.navPane').addClass('hidden');
			}
			$('.navPane#'+navref+'Pane').removeClass('hidden');
			$('#contentHeader').slideDown().removeClass('hidden');
		}
	);
	
	$('.foldNavigation').click(
		function hideNavMenu(){
			navref = this.getAttribute('data-navref');
			if (_currentNavpane != null)
			{
				$('.navPane#'+navref+'Pane').addClass('hidden');
			}
			$('#contentHeader').slideUp().addClass('hidden');		
		}
	);
}