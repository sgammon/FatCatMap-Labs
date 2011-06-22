class CoreUserAPI extends CoreAPI
	
	constructor: ->
		@current_user = null
		@is_user_admin = null
		@login_url = null
		@logout_url = null
		
	setUserInfo: (@current_user, @is_user_admin, @login_url, @logout_url) ->