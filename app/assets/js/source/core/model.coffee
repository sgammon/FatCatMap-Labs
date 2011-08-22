## FCM Model - extended from backbone
class LocalModel extends Backbone.Model

	_type: ->
		return 'local'


class RemoteModel extends Backbone.Model
	
	_type: ->
		return 'remote'
	
	
class ModelCollection extends Backbone.Collection
	
	_noop: ->
		return
	
	
class CoreModelAPI extends CoreAPI
	
	constructor: (fcm) ->
		
		## Model storage
		window.Models = {}
		
		## Bind events
		fcm.state.events.registerEvent('MODEL_DEFINE')
		fcm.state.events.registerEvent('MODEL_SYNC')
		fcm.state.events.registerEvent('ENTITY_CREATE')
		fcm.state.events.registerEvent('ENTITY_PUT')
		fcm.state.events.registerEvent('ENTITY_GET')
		fcm.state.events.registerEvent('ENTITY_DELETE')
		
		@local =
			schema: {}

		@remote =
			schema: {}
	
		@sync = _backboneSync: (method, model, options) =>
		
			## Extract success + error callbacks
			[success, error, config...] = options
		
			switch method
			
				when "create"
					fcm.state.events.triggerEvent('ENTITY_CREATE', {model: model, options: options})
					return fcm.rpc.api.data.create({object: model}).fulfill({success: success_callback, failure: failure_callback}, config)
				
				when "read"
					fcm.state.events.triggerEvent('ENTITY_GET', {model: model, options: options})
					[success_callback, failure_callback, config...] = options
					return fcm.rpc.api.data.get({key: model.id}).fulfill({success: success_callback, failure: failure_callback}, config)
				
				when "update"
					fcm.state.events.triggerEvent('ENTITY_PUT', {model:model, options:options})
					[success_callback, failure_callback, config...] = options
					return fcm.rpc.api.data.update({key: model.id, object: model.toJSON()}).fulfill({success: success_callback, failure: failure_callback}, config)
				
				when "delete"
					fcm.state.events.triggerEvent('ENTITY_DELETE', {model:model, options:options})
					[success_callback, failure_callback, config...] = options
					return fcm.rpc.api.data.delete({key: model.id}).fulfill({success: success_callback, failure: failure_callback}, config)
					
				else fcm.rpc.dev.error('Model', 'Backbone bridge model sync got an unrecognized method.', method: method, model: model, options: options)
				
		## Overwrite Backbone's sync method
		Backbone.sync = @sync
		

## Export Classes
window.LocalModel = LocalModel
window.RemoteModel = RemoteModel
window.ModelCollection = ModelCollection