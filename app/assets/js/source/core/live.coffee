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