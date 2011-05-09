_currentNavpane = null;
_sidebar_state = {};
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
				$('.navPane#'+navref+'Pane').slideUp();
			}
			$('#contentHeader').slideUp().slideUp();		
		}
	);
}

function closeSidebar(selector, direction)
{
	$(selector).animate({width:'35px'});
	$(selector+' div.panelWrapper').fadeOut();
	$(selector+' a.expandButton').addClass('enabled');
	if (typeof(direction) != 'undefined')
	{
		$(selector+' a.multiButton').addClass('enabled');
		$(selector+' a.multiButton').attr('href', 'javascript:expandSidebar("'+selector+'", "'+direction+'")');
		$(selector+' a.multiButton img').attr('src', '/assets/img/static/layout/sprites/arrow-'+direction+'.png');
	}
}

function expandSidebar(selector, direction)
{
	$(selector).animate({width:'200px'});
	$(selector+' div.panelWrapper').hide().removeClass('hidden').fadeIn();
	$(selector+' a.expandButton').removeClass('enabled');
	if (typeof(direction) != 'undefined')
	{
		$(selector+' a.multiButton').addClass('enabled');
		$(selector+' a.multiButton').attr('href', 'javascript:closeSidebar("'+selector+'", "'+direction+'")');
		$(selector+' a.multiButton img').attr('src', '/assets/img/static/layout/sprites/close-x.png');		
	}
}