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
	$(selector+' a.expandButton').attr('href', 'javascript:expandSidebar("'+selector+'", "'+direction+'")');
	$(selector+' a.expandButton img').attr('src', '/assets/img/static/layout/sprites/arrow-'+direction+'.png');	
	if (typeof(direction) != 'undefined')
	{
		$(selector+' a.multiButton').addClass('enabled');
		$(selector+' a.multiButton').attr('href', 'javascript:expandSidebar("'+selector+'", "'+direction+'")');
		$(selector+' a.multiButton img').attr('src', '/assets/img/static/layout/sprites/arrow-'+direction+'.png');
	}
	$(selector).removeClass('unfolded');
	$(selector).addClass('folded');
}

function expandSidebar(selector, direction)
{	
	$(selector).animate({width:'200px'});
	$(selector+' div.panelWrapper').hide().removeClass('hidden').fadeIn();
	$(selector+' a.expandButton').attr('href', 'javascript:maximizeSidebar("'+selector+'", "'+direction+'")');
	if (typeof(direction) != 'undefined')
	{
		$(selector+' a.multiButton').addClass('enabled');
		$(selector+' a.multiButton').attr('href', 'javascript:closeSidebar("'+selector+'", "'+direction+'")');
		$(selector+' a.multiButton img').attr('src', '/assets/img/static/layout/sprites/close-x.png');		
	}
	$(selector).removeClass('folded');
	$(selector).addClass('unfolded');
}

function maximizeSidebar(selector, direction)
{
	$(selector).animate({width:'80%'});
	$(selector+' a.expandButton').attr('href', 'javascript:minimizeSidebar("'+selector+'", "'+direction+'")');
	if(direction == 'right')
	{
		arrow = 'left';
	}
	else
	{
		arrow = 'right';
	}
	$(selector+' a.expandButton img').attr('src', '/assets/img/static/layout/sprites/arrow-'+arrow+'.png');
	$(selector).removeClass('folded'); // Just in case...
	$(selector).removeClass('unfolded');
	$(selector).addClass('maximized');
}

function minimizeSidebar(selector, direction)
{
	$(selector).animate({width:'200px'});
	$(selector+' a.expandButton').attr('href', 'javascript:maximizeSidebar("'+selector+'", "'+direction+'")');
	$(selector+' a.expandButton img').attr('src', '/assets/img/static/layout/sprites/arrow-'+direction+'.png');	
	$(selector).removeClass('folded'); // Just in case...
	$(selector).removeClass('maximized');
	$(selector).addClass('unfolded');
}

function loadContextPane(node, key)
{
	$('.nodeDetailsPane #nodekey').text(key.encoded);
	$('.nodeDetailsPane #nodelabel').text(node.label);
	

	if(!$('#detailsPane').hasClass('unfolded') || !$('#detailsPane').hasClass('maximized'))
	{
		expandSidebar('#detailsPane', 'right');
		if(!$('#detailsPane a.expandButton').hasClass('enabled'))
		{
			$('#detailsPane a.expandButton').addClass('enabled');
		}
	}
}