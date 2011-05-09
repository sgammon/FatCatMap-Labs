/*
jQuery.sql - webSQL plugin for jQuery, version 0.8a

    Copyright (C) 2011 Pedro Costa Coitinho

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

(function($) {
	// util
	// counts the number of properties in the object
	function _countObj(obj) {
		var tot = 0;
		for (var i in obj) {
			if (i !== '__table') {
				tot ++;
			}
		}
		return tot;
	}
	
	// the global sql object
	$.sql = {
		/**
		* checkSupport
		*  returns (true|false);
		*
		* checks if the browser supports webSql
		**/
		checkSupport: function() {
			if (window.openDatabase) {
				return true;
			} else {
				return false;
			}
		},
		/**
		* open
		*   properties = {}
		*     name 			= 'app'					- string, the table name 
		*     version 		= '1.0'					- string, the table version
		*     description 	= 'Aplication database' - string, the application description
		*     size			= 1024 * 1024			- number, the estimated size of the databse
		*     callback	 	= function() {}			- function, the callback once the databse if open
		*  returns jQuery
		*
		* opens the connection a local database (only supports 1 database open at the moment)
		**/
		open: function(properties) {
			// checks if there is databse support
			if (window.openDatabase) {
				var db = $(window).data('db');
				if (!db) {
					// only allow to open a databse if none is open at the moment
				if (!properties) {var properties = {}};
					// set properties
					properties.name 			= properties.name 			|| 'app';
					properties.version			= properties.verstion 		|| '1.0';
					properties.description 		= properties.description 	|| 'Application database';
					properties.size				= properties.size 			|| 1024 * 1024;
					properties.callback			= properties.callback 		|| function() {};
								
					// open database
					db = openDatabase(
						properties.name,
						properties.version,
						properties.description,
						properties.size,
						properties.createCallback);
						
					// save the data
					$(window).data('db', db);
				} else {
					$.error('SQL error: Database is already open');
				}
			} else {
				$.error('SQL error: No databse support');
			}
			
			// chain me!
			return $;
		},
		/**
		* query
		*   query = (string|array of strings)
		*   properties = {
		*     arguments	= []					- array, the arguments to pass with the query
		*     success	= function(rows) {}		- function, the callback function for a successful query
		*     failure   = function(message) {}	- function, the callback for a failed query
		*  return jQuery
		*
		* runs one or a seires of queries within the same transaction
		**/
		query: function(query, properties) {
			if (!properties) {var properties = {};}
			// set properties
			properties.arguments = properties.arguments || [];
			properties.success = properties.success || function() {};
			properties.failure = properties.failure || function(message) {$.error(message);};
			
			// runs the SQL statements as array always
			if (!(query instanceof Array)) {query = [query];} 
			
			// get the db
			var db = $(window).data('db');
			
			if (!db) {
				$.error('SQL error: Database not open or not supported');
			} else if (!query) {
				$.error('SQL error: No query to parse');
			} else {
				db.transaction(function (tx) {
				// setup transactions for the queries
					for (var i = 0; i < query.length; i++) {
							tx.executeSql(
								query[i],
								properties.arguments,
								function(tx, results) {
								    if (results.rowsAffected > 0
								    		|| results.rows.length > 0) {
										properties.success(results.rows);
									} else {
										properties.success(false);
									}
								},
								function(tx, message) {
									properties.failure(message.message)
								}
							);
					}
				}, null);
			}
			// chain me!
			return $;
		},
		// active record
		setColumns: function(columns) {
			// save the columns to the active record var
			$(window).data('dbActiveRecord', columns);
			
			// dont leave me unconnected!
			return $;	
		},
		addColumn: function(name, value) {
			var columns = $(window).data('dbActiveRecord');
			if (!columns) {
				columns = {}
			}
			// add a new column
			columns[name] = value;
			// save
			$(window).data('dbActiveRecord', ar);
			
			// chain me!
			return $;
		},
		removeColumn: function(name) {
			var columns = $(window).data('dbActiveRecord');
			if (columns) {
				if (columns[name]) {
					delete columns[name];
					
					// save
					$(window).data('dbActiveRecord', columns);
				} else {
					$.error('SQL Active Record Error: Column ' + name + ' does not exist :(');
				}
			} else {
				$.error('SQL Active Record Error: No coluns to remove from');
			}
			
			// link me to the next!
			return $;
		},
		setTable: function(name) {
			var columns = $(window).data('dbActiveRecord');
			if (!columns) {columns = {};}
			// set the table
			columns.__table = name;
			//save
			$(window).data('dbActiveRecord', columns);
			
			// chain me!
			return $
		},
		createTable: function(name) {
			var columns = $(window).data('dbActiveRecord');
			if (columns) {
				if (columns.name || name) {
					// creates a table based on the columns
					var query = 'CREATE TABLE IF NOT EXISTS ' + name + ' (';
					// and get the column fields
					var length = _countObj(columns),
						count = 0;
					for (var i in columns) {
						if (i !== '__table') {
							query += i + ' ' + columns[i];
							if (count < length - 1) {query += ', '; count++;}	// increases the current count
							count++;
						}
					}
					// close the query
					query += ')';
					
					// save the query to the columns
					columns.__table = name;
					$(window).data('dbActiveRecord', columns);
					
					// run the query
					$.sql.query(query);
					
				} else {
					$.error('SQL Active Record Error: No table name specified');
				}
			} else {
				$.error('SQL Active Record Error: No columns specified');
			}
			
			// linkidy-link
			return $;
		},
		
		addRow: function() {
			// checks if the first is an array or not
			if (arguments.length > 0) {			
				var columns = $(window).data('dbActiveRecord');
				if (columns) {
					
					// function that returns the query for a row				
					function _activeRecordQuery(row) {
						var query = 'INSERT INTO ' + columns.__table + ' ('
						// insert keys
						var length = _countObj(columns),
							count = 0;
						for (i in columns) {
							if (i !== '__table') {	// ignore __table
								query += i;
								if (count < length - 1) {query += ', ';}
								count++;
							}
						}
						query += ') VALUES ('
						
						count = 0;
						for (i in columns) {
							if (i !== '__table') {
								if (typeof row[count] === 'string') {
									query += '"' + row[count] + '"';
								} else {
									query += row[count];
								}
								if (count < length - 1) {query += ', ';}
								count++;
							}
						}
						return query + ')';
										
					}
					
					if (arguments[0] instanceof Array) {
						// if it is a list of arrays
						// create an array with a bunch of queries
						var query = [];
						for (var i = 0; i < arguments.length; i++) {
							query[i] = _activeRecordQuery(arguments[i]);
						}
						
					} else {
						// if it is only a list of arguments
						var query = _activeRecordQuery(arguments);
						
					}
					// run the query or queries
					$.sql.query(query);
				} else {
					$.error('SQL Active Record Error: No properties set');
				}
			} else {
				$.error('SQL Active Record Error: No arguments in addRow()');
			}
			
			// Q: 
			//  What is the most common return statement in jQuery?
			// A:
				return $;
		}
		
	};
	
	// the local sql object
	var methods = {
		/**
		* load
		*
		* appends a whole or parital table to this element
		**/
		load: function(properties) {
			// the SQL statement
			var query = 'SELECT ' + properties.fetchColumns + ' FROM ' + properties.table;
			query += (properties.condition ? ' WHERE ' + properties.condition : '');
			query += (properties.limit ? ' LIMIT ' + properties.start + ', ' + properties.limit : '');
				
			var obj = this;
				
			// run the query with a special callback
			$.sql.query(query, {success: function(rows) {
				if (rows) {
					// assuming everything went well
					for (var i = 0; i < rows.length; i++) {
						// create the row wrapper
						var row = $(properties.rowWrap);
						for (var j in rows.item(i)) {
							row.append($(properties.columnWrap).html(rows.item(i)[j]));
						}
						// appends row
						obj.append(row);
					}
					// increase the start by limit
					if (properties.limit) {
						properties.start += properties.limit;
						// save 
						obj.data('db', properties);
					}
				} else {
					// but what if there are no results to display?
					$(obj).data('db').failure.call(obj);
				}
			}});
			
			// cha-chain!
			return $;
		},
		
	};
	/**
	* sql
	*  method 							- string, the method to invoke
	*  properties = {}
	*    columnWrap		= '<td></td>'	- the string or DOM object to wrap each returned column
	*    rowWrap 		= '<tr></tr>'	- the string or DOM object to wrap each returned row
	*    start			= 0				- number, the start index of the query results
	*	 limit			= false			- (number|false), the maximun number of resutls (false = infinite)
	*    condition		= false			- (string|false), the SQL query condition
	*    table 			= ''			- string, the databse table to fetch information from
	*    fetchColumns	= '*'			- string, which columns to fetch? in SQL notation (* = all)
	*    failure		= null			- function, what happens if there is no result?
	*  returns jQuery
	*
	* the 'face' for interfacing with databased directly to the DOM,
	* allows for a set of functions that load databse tables to the mathced objects
	**/
	$.fn.sql = function(method, propertiesDelta) {
		// sets the properties
		var properties = this.data('db');
		
		if (!properties) {
			// sets up the initial property values
			properties = {};
			properties.columnWrap   = '<td></td>';
			properties.rowWrap      = '<tr></tr>';
			properties.start        = 0;
			properties.limit        = false;
			properties.condition	= false;
			properties.table        = '';
			properties.fetchColumns = '*';
			properties.failure		= function() {$.error('SQL fn: Query returned no results');};
			
			// saves the properties
			this.data('db', properties);	
		}
	
		if (propertiesDelta)  {
			// updates the properties
			// from changes
			properties.columnWrap   = propertiesDelta.columnWrap 	|| properties.columnWrap;
			properties.rowWrap      = propertiesDelta.rowWrap 		|| properties.rowWrap;
			properties.start        = propertiesDelta.start 		|| properties.start;
			properties.limit        = propertiesDelta.limit 		|| properties.limit;
			properties.condition	= propertiesDelta.condition 	|| properties.condition;
			properties.table        = propertiesDelta.table 		|| properties.table;
			properties.fetchColumns = propertiesDelta.fetchColumns 	|| properties.fetchColumns;
			properties.failure		= propertiesDelta.failure 		|| properties.failure;
			
			// saves the properties
			this.data('db', properties);
		}
		
		
		// now runs the method of choice
		if (methods[method]) {
			methods[method].call(this, properties);
		} else {
			$.error('SQL error: Method ' + method + ' doesnt exist!');
		}
	
		// chain me!
		return $;
	};
})(jQuery);