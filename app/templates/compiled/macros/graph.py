from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/macros/graph.html'

    def root(context, environment=environment):
        if 0: yield None
        def macro(l_selector, l_config, l_fn, l_tags):
            t_1 = []
            pass
            t_1.append(
                u'\n', 
            )
            if l_tags:
                pass
                t_1.append(
                    u"\n<script type='text/javascript'>\n", 
                )
            t_1.append(
                u'\n\n', 
            )
            if l_fn != None:
                pass
                t_1.extend((
                    u'\n', 
                    to_string(l_fn), 
                    u' = function (nodes, edges, hints)\n{\n', 
                ))
            t_1.extend((
                u'\n\n\t/* Render Graph\n\tvar w = $("', 
                to_string(l_selector), 
                u'").width(),\n\t    h = $("', 
                to_string(l_selector), 
                u'").height(),\n\t\tcolors = d3.scale.category20();\n\t\t\n\t// 1: Create viz panel\n\tvar vis = d3.select(\'', 
                to_string(l_selector), 
                u'\')\n\t\t.append("svg:svg")\n\t\t.attr("width", w)\n\t\t.attr("height", h);\n\t\t\n\t// 2: Add force-driven layout to visualizer panel\n\tvar force = d3.layout.force()\n\t\t.charge(-100)\n\t\t.gravity(.05)\n\t\t.distance(100)\n\t\t.nodes(nodes)\n\t\t.links(edges)\n\t\t.size([w, h]);\n\t\n\t/* 4: Render line\n\tvar edge = vis.selectAll("line.link")\n\t\t.data(edges)\n\t \t.enter().append("svg:line")\n\t\t\t.attr("data-hint", function (d, i) {return hints[i].key.encoded;})\n\t\t\t.attr("data-source-node-key", function (d) {return d.source.key.encoded;})\n\t\t\t.attr("data-target-node-key", function (d) {return d.target.key.encoded;})\n\t\t\t.attr("class", "edge")\n\t\t\t.attr("x1", function (d) {return d.source.x;})\n\t\t\t.attr("y1", function (d) {return d.source.y;})\n\t\t\t.attr("x2", function (d) {return d.target.x;})\n\t\t\t.attr("y2", function (d) {return d.target.y})\n\n\t// 5: Render node\n\tvar node = vis.selectAll("g.node")\n\t\t.data(nodes)\n\t\t.enter().append("svg:g")\n\t\t\t.attr("id", function (d) {return d.key.encoded;})\n\t\t\t.attr("class", "node")\n\t\t\t.attr(\'data-kind\', function (d) {return d.kind;})\n\t\t\t.attr(\'data-label\', function (d) {return d.label;})\n\t\t\t.attr("data-object-key", function (d) {return d.key.parent;})\n\t\t\t.call(force.drag);\n\t\t\t\n\tnode.on(\'click\', function (d, i) {\n\t\t\t\t\n\t\t\t\t$(\'#nodeDetails #node_label\').text(d.label);\n\t\t\t\t$(\'#nodeDetails #node_kind\').text(d.kind);\n\n\t\t\t\toutgoing_list = _.each($.fatcatmap.api.visualizer.graph.data.edges_by_node[d.key.encoded][\'outgoing\'], function mapOutgoingEdge(edge){\n\t\t\t\t\n\t\t\t\t\tconsole.log(\'OUTGOING EDGE\', edge);\n\t\t\t\t\t\n\t\t\t\t});\n\t\t\t\t$(\'#nodeDetails #node_outgoing_edges\').html();\n\t\t\t\t\n\t\t\t})\t\n\t\t\t.on(\'mouseover\', function (d, i) {\n\t\t\t\t\n\t\t\t\t//$(this).tipsy(\'show\');\n\t\t\t\t\n\t\t\t})\n\t\t\t.on(\'dblclick\', function (d, i) {\n\t\t\t\t$.fatcatmap.api.visualizer.graph.shiftTo(d.key.encoded);\n\t\t\t});\n\t\t\t\n\tnode.append("svg:circle")\n\t\t.attr("class", "circle")\n\t\t.attr("x", \'-8px\')\n\t\t.attr("y", \'-8px\')\n\t\t.attr("r", 16);\n\t\t\t\n\tnode.append("svg:text")\n\t\t.attr(\'x\', -4)\n\t\t.attr(\'y\', 4)\n\t\t.attr(\'class\', \'label\')\t\t\n\t\t.text(function (d) {return d.index.toString();});*/\n\n\t/*force.on("tick", function () {\n\t\tedge.attr("x1", function (d, i) {return d.source.x;})\n\t\t\t.attr("y1", function (d, i) {return d.source.y;})\n\t\t\t.attr("x2", function (d, i) {return d.target.x;})\n\t\t\t.attr("y2", function (d, i) {return d.target.y;});\n\t\t\t\n\t\tnode.attr(\'transform\', function (d, i) { return \'translate(\'+d.x+\',\'+d.y+\')\'; });\n\t});*/\n\t\n\t//$.fatcatmap.api.visualizer.graph.register({visualizer: vis, force: force}, {nodes: nodes, edges: edges, hints: hints})\n\n', 
            ))
            if l_fn != None:
                pass
                t_1.append(
                    u'\n\t//return {graph: vis, force: force, node: node, edge: edge}\n}\n', 
                )
            t_1.append(
                u'\n\n', 
            )
            if l_tags:
                pass
                t_1.append(
                    u'\n</script>\n', 
                )
            t_1.append(
                u'\n', 
            )
            return concat(t_1)
        context.exported_vars.add('d3grapher')
        context.vars['d3grapher'] = l_d3grapher = Macro(environment, macro, 'd3grapher', ('selector', 'config', 'fn', 'tags'), ({}, None, False, ), False, False, False)
        yield u'\n\n\n\n'
        def macro(l_selector, l_fn, l_tags):
            t_2 = []
            pass
            t_2.append(
                u'\n', 
            )
            if l_tags:
                pass
                t_2.append(
                    u"\n<script type='text/javascript+protovis'>\n", 
                )
            t_2.append(
                u'\n\n', 
            )
            if l_fn != None:
                pass
                t_2.extend((
                    u'\n', 
                    to_string(l_fn), 
                    u' = function (nodes, edges)\n{\n', 
                ))
            t_2.extend((
                u'\n\n\t// Render Graph\n\tvar w = $("', 
                to_string(l_selector), 
                u'").width(),\n\t    h = $("', 
                to_string(l_selector), 
                u'").height(),\n\t    colors = pv.Colors.category19();\n\n\t// 1: Create viz panel\n\tvar vis = new pv.Panel($(\'', 
                to_string(l_selector), 
                u'\'))\n\t    .width(w)\n\t    .height(h)\n\t    .fillStyle("transparent")\n\t    .event("mousedown", pv.Behavior.pan())\n\t    .event("mousewheel", pv.Behavior.zoom());\n\n\t// 2: Add force-driven layout to visualizer panel\n\tvar force = vis.add(pv.Layout.Force).nodes(nodes).links(edges);\n\tforce.bound = function() true;\n\n\t// 3: Adjust force constants for layout\n\tforce.chargeConstant(function() -110);\n\tforce.chargeMaxDistance(function() 500);\n\tforce.chargeMinDistance(function() 2);\n\tforce.chargeTheta(function() 0.9);\n\tforce.dragConstant(function() 0.1);\n\tforce.springConstant(function() 0.1);\n\tforce.springDamping(function() 0.3);\n\tforce.springLength(function() 140);\n\n\t// 4: Render line\n\tline = force.link.add(pv.Line);\n\tline.strokeStyle(function() \'#667788\');\n\n\t// 5: Add node box\n\tdot = force.node.add(pv.Dot);\n\tdot.size(function() 150);\n\tdot.fillStyle(function() \'white\');\n\tdot.strokeStyle(function() \'blue\');\n\tdot.cursor(function() \'pointer\');\n\tdot.text(function (d) d.label);\n\tdot.event(\'mousedown\', pv.Behavior.drag());\n\n\n\t// 6: Add Node Events\n\tdot.event(\'click\', function (d) {\n\t\n\t\tloadContextPane(d, d.key);\n\t\n\t});\n\tdot.event(\'dblclick\', function (d) {\n\t\n\t\tbrowseToNode(d.key);\n\t\n\t});\n\tdot.event(\'drag\', force);\n\t//dot.event("mouseover", pv.Behavior.tipsy({gravity: "s", fade: true}));\t\t\t\n\n\t// 7: Add node anchor\n\tcenter = dot.anchor(\'center\');\n\tlabel = center.add(pv.Label);\n\tlabel.text(function (d) d.index+1);\n\tlabel.font(function () \'16px Cabin\');\n\n\tconsole.log(\'NODES/EDGES\', nodes, edges);\n\tconsole.log(\'VIS\', vis);\n\n\t// 8: Render\n\tvis.render();\n\t\n\treturn {panel: vis, force: force}\n', 
            ))
            if l_fn != None:
                pass
                t_2.append(
                    u'\n}\n', 
                )
            t_2.append(
                u'\n\n', 
            )
            if l_tags:
                pass
                t_2.append(
                    u'\n</script>\n', 
                )
            t_2.append(
                u'\n', 
            )
            return concat(t_2)
        context.exported_vars.add('protographer')
        context.vars['protographer'] = l_protographer = Macro(environment, macro, 'protographer', ('selector', 'fn', 'tags'), (None, False, ), False, False, False)

    blocks = {}
    debug_info = '1=8&2=14&6=22&7=26&12=31&13=33&17=35&100=38&105=46&112=58&113=64&117=72&118=76&123=81&124=83&128=85&190=88&194=96'
    return locals()