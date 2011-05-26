# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy import Rule
from tipfy import HandlerPrefix

rules = [

	HandlerPrefix('momentum.platform.handlers.core.', [
	
		Rule('/_ah/start', endpoint='backend-start', handler='ifx.backends.StartHook'),
	
	]),

	HandlerPrefix('momentum.platform.handlers.console.', [
	
		Rule('/_pc/ifx/platform/console', endpoint='console-home', handler='main.Landing'),
		Rule('/_pc/ifx/platform/dashboard', endpoint='console-dashboard', handler='main.Dashboard'),

		## Data Manager
		Rule('/_pc/ifx/platform/console/data', endpoint='console-data', handler='data.Main'),
		Rule('/_pc/ifx/platform/console/data/stats', endpoint='data-stats', handler='data.MainStats'),
		
		## Data Views -- Metadata
		Rule('/_pc/ifx/platform/console/data/meta/kinds', endpoint='meta-kinds', handler='data.kinds.KindList'),
		Rule('/_pc/ifx/platform/console/data/meta/namespaces', endpoint='meta-namespaces', handler='data.namespaces.NamespaceList'),
		Rule('/_pc/ifx/platform/console/data/meta/kind/<string:kind>', endpoint='meta-kind', handler='data.kinds.KindView'),
		Rule('/_pc/ifx/platform/console/data/meta/kind/<string:kind>/stats', endpoint='meta-kind-stats', handler='data.kind.KindStat'),
		Rule('/_pc/ifx/platform/console/data/meta/namespace/<string:namespace>', endpoint='meta-namespace', handler='data.namespaces.NamespaceView'),
		Rule('/_pc/ifx/platform/console/data/meta/namespace/<string:namespace>/stats', endpoint='meta-namespace-stats', handler='data.namespaces.NamespaceStat'),
		Rule('/_pc/ifx/platform/console/data/meta/namespace/<string:namespace>/kinds', endpoint='meta-namespace-kinds', handler='data.namespaces.NamespaceKinds'),
		Rule('/_pc/ifx/platform/console/data/meta/namespace/<string:namespace>/kind/<string:kind>', endpoint='meta-namespace-kind', handler='data.namespaces.NamespaceKind'),
		Rule('/_pc/ifx/platform/console/data/meta/namespace/<string:namespace>/kind/<string:kind>/stats', endpoint='meta-namespace-kind-stats', handler='data.namespaces.NamespaceKindStats'),
		
		## Data Views -- Entities
		Rule('/_pc/ifx/platform/console/data/entities/<path:filters>/list', endpoint='data-list', handler='data.operations.ListData'),
		Rule('/_pc/ifx/platform/console/data/entities/<path:filters>/job', endpoint='data-job', handler='data.operations.DataJob'),
		Rule('/_pc/ifx/platform/console/data/entities/key/<string:key>', endpoint='entity-view', handler='data.entities.ViewEntity'),
		Rule('/_pc/ifx/platform/console/data/entities/key/<string:key>/<string:operation>', endpoint='entity-operation', handler='data.entities.EntityOperation'),
		
		## Storage Manager
		Rule('/_pc/ifx/platform/console/storage', endpoint='console-storage', handler='storage.Main'),
		Rule('/_pc/ifx/platform/console/storage/stats', endpoint='storage-stats', handler='storage.MainStats'),
		Rule('/_pc/ifx/platform/console/storage/stub/<string:stubkey>', endpoint='storage-blobstore-stub', handler='storage.ViewStub'),
		Rule('/_pc/ifx/platform/console/storage/stub/<string:stubkey>/<string:operation>', endpoint='storage-blobstore-operation', handler='storage.StubOperation'),

		## Storage Manager -- Blobstore
		Rule('/_pc/ifx/platform/console/storage/blobstore/stubs', endpoint='storage-blobstore-stubs', handler='storage.blobstore.ListStubs'),		
		Rule('/_pc/ifx/platform/console/storage/blobstore/stats', endpoint='storage-blobstore', handler='storage.blobstore.BlobstoreStats'),
		Rule('/_pc/ifx/platform/console/storage/blobstore/upload', endpoint='storage-blobstore-upload', handler='storage.blobstore.BlobstoreUpload'),
		
		## Storage Manager -- Web Storage
		Rule('/_pc/ifx/platform/console/storage/webstorage/stubs', endpoint='storage-webstorage-stubs', handler='storage.webstorage.ListStubs'),
		Rule('/_pc/ifx/platform/console/storage/webstorage/stats', endpoint='storage-webstorage-stats', handler='storage.webstorage.WebStorageStats'),
		Rule('/_pc/ifx/platform/console/storage/webstorage/upload', endpoint='storage-webstorage-upload', handler='storage.webstorage.WebStorageUpload'),
		
		
	]),
	
]