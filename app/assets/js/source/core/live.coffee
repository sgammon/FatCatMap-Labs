class CoreLiveAPI extends CoreAPI
	
	constructor: (@fcm) ->

		## Register FCM events
		@fcm.state.events.registerEvent('CHANNEL_OPEN')
		@fcm.state.events.registerEvent('CHANNEL_MESSAGE')
		@fcm.state.events.registerEvent('CHANNEL_ERROR')
		@fcm.state.events.registerEvent('CHANNEL_CLOSE')			
		
		@token = null
		@channel = null
		@socket = null

		@handlers = 

			_registry:
				default: @defaultLiveHandler

			add: (type, callback) ->
				@registry[type] = callback
				return
			
			remove: (type) ->
				@registry[type] = null
				return
			
			resolve: (type) ->
				if type in @registry
					return @registry[type]
				else
					return false
					
			handle: (type, data) ->
				return @registry[type](data)


	defaultLiveSuccessHandler: (message...) =>
		@fcm.dev.debug.log('CoreLive', 'Live API received unhandled successful push message.', message...)
		return

		
	defaultLiveFailureHandler: (message...) =>
		@fcm.dev.debug.log('CoreLive', 'Live API received unhandled push message failure.', message...)
		return
		
		
	openChannel: (@token) =>
		
		@fcm.dev.debug.log('CoreLive', 'Opening channel.', @token)

		try
			## Set up and open the channel
			@channel = new goog?.appengine?.Channel(@token)
			@socket = @channel.open()
		
			## Bind channel callbacks
			@socket.onopen = @onOpen
			@socket.onmessage = @onMessage
			@socket.onerror = @onError
			@socket.onclose = @onClose

		catch error
			@fcm.dev.debug.error('CoreLive', 'Encountered error preparing live channel.', error)
			return {channel: false, socket: false}
		
		return {channel: channel, socket: socket}
		
	
	listen: (token) =>	
		if @channel is null and @socket is null
			{channel, socket} = @openChannel(token)
			if channel? and socket?
				@fcm.state.events.registerHook('CHANNEL_OPEN', @dispatch)
			
	dispatch: (message) =>
		if message.status == 'ok'
			if @handlers.resolve(message.response.type)
				return @handlers.handle(message.response.type, message)
			else
				@defaultLiveSuccessHandler(message)
		else
			if @handlers.resolve(message.response.type)
				return @handlers.handle(message.error.type, message)
			else
				@defaultLiveFailureHandler(message)
		return
		
	onOpen: () =>
		@fcm.dev.debug.log('CoreLive', 'Channel is ready to receive live messages.')
		@fcm.state.events.triggerEvent('CHANNEL_OPEN')
		
	onMessage: (message) =>
		@fcm.dev.debug.verbose('CoreLive', 'Channel message received.', message)
		@fcm.state.events.triggerEvent('CHANNEL_MESSAGE', message)
		
	onError: (error) =>
		@fcm.dev.debug.error('CoreLive', 'Encountered channel error.', error)
		@fcm.state.events.triggerEvent('CHANNEL_ERROR', error)
		
	onClose: () =>
		@fcm.dev.debug.log('CoreLive', 'Channel has been closed.')
		@fcm.state.events.triggerEvent('CHANNEL_CLOSE')