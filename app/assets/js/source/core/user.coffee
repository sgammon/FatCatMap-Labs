class CoreUserAPI extends CoreAPI
	
	constructor: (@fcm) ->

		## Register FCM events
		@fcm.state.events.registerEvent('USER_CHANGE')
		
		@current_user = null
		@is_user_admin = null
		@login_url = null
		@logout_url = null
		
	setUserInfo: (user_properties) ->
		if user_properties['current_user'] isnt null
			@current_user = user_properties['current_user']

		if user_properties['is_user_admin'] isnt null
			@is_user_admin = user_properties['is_user_admin']

		if user_properties['login_url'] isnt null
			@login_url = user_properties['login_url']

		if user_properties['logout_url'] isnt null
			@logout_url = user_properties['logout_url']
			
		@fcm.state.events.triggerEvent('USER_CHANGE')