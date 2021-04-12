# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1616489282.0188146
_enable_loop = True
_template_filename = '/app/lazylibrarian/data/interfaces/bookstrap/series.html'
_template_uri = 'series.html'
_source_encoding = 'utf-8'
_exports = ['headerIncludes', 'body', 'headIncludes', 'javascriptIncludes']



import lazylibrarian


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headerIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        perm = context.get('perm', UNDEFINED)
        pref = context.get('pref', UNDEFINED)
        authorid = context.get('authorid', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="subhead_container" class="row">\n      <form action="search" method="get">\n        <div id="subhead_menu"  class="col-xs-12 col-md-8">\n')
        if authorid != None:
            __M_writer('          <a href="authorPage?AuthorID=')
            __M_writer(str(authorid))
            __M_writer('" class="btn btn-sm btn-primary"><i class="fa fa-chevron-left"></i> Return to Author</a>\n')
        else:
            __M_writer('          <label for="dummy" class="control-label"> </label>\n')
        if lazylibrarian.CONFIG['USER_ACCOUNTS']:
            if pref&lazylibrarian.pref_myseries:
                __M_writer('                <a href="toggleMySeries" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="All, or just mine"><i class="fa fa-user-circle"></i></a>\n')
            else:
                __M_writer('                <a href="toggleMySeries" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="All, or just mine"><i class="fa fa-users"></i></a>\n')
        __M_writer('        </div>\n        <div class="clearfix visible-xs"><hr/></div>\n')
        if perm&lazylibrarian.perm_search:
            __M_writer('        <div class="col-xs-12 col-md-4">\n        <div class="form-group">\n          <label class="sr-only">Search</label>\n          <div class="input-group">\n            <input type="text" class="form-control deletable input-sm col-xs-12" value="" onfocus="if(this.value==this.defaultValue) this.value=\'\';" name="name" placeholder="Title / Author / ISBN" id="searchbox" name="searchbox">\n            <span class="input-group-btn">\n              <button type="submit" value="Book" class="btn btn-sm btn-primary" data-toggle="tooltip" data-placement="bottom" title="Search for book"><i class="fa fa-search"></i></button>\n            </span>\n          </div>\n        </div>\n        </div>\n')
        __M_writer('      </form>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        whichStatus = context.get('whichStatus', UNDEFINED)
        authorid = context.get('authorid', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n  <form action="series" method="get" class="form-inline">\n    <div class="row">\n      <div class="col-xs-12 col-sm-5">\n        <div class="form-group">\n          <label for="whichStatus" class="control-label">Status:</label>\n          <select name="whichStatus" id="whichStatus" class="form-control input-sm">\n')
        for item in ['All', 'Complete', 'Partial', 'Empty', 'Paused', 'Wanted', 'Active', 'Ignored']:
            __M_writer('            <option value="')
            __M_writer(str(item))
            __M_writer('"\n')
            if whichStatus == item:
                __M_writer('                    selected = "selected"\n')
            __M_writer('            >')
            __M_writer(str(item))
            __M_writer('</option>\n')
        __M_writer('          </select>\n        </div>\n      </div>\n')
        if lazylibrarian.CONFIG['TOGGLES'] == True:
            __M_writer('        <div class="toggles col-xs-12 col-sm-7 text-right">\n          Toggle: <a class="toggle-vis" data-column="1"> Author</a>\n          <a class="toggle-vis" data-column="2"> Series</a>\n          <a class="toggle-vis" data-column="3"> Have</a>\n          <a class="toggle-vis" data-column="4"> Status</a>\n        </div>\n')
        __M_writer('    </div>\n  </form>\n  <br/>\n  <form action="markSeries" method="get" class="form-inline">\n    <div class="table-responsive">\n      <table class="display table table-striped table-hover table-bordered" id="book_table">\n        <thead>\n          <tr>\n')
        if perm&lazylibrarian.perm_status:
            __M_writer('            <th class="select text-center no-sort"><input type="checkbox" onClick="toggleAll(this)" /></th>\n')
        else:
            __M_writer('            <td class="hidden"></td>\n')
        __M_writer('            <th class="authorname">Author</th>\n            <th class="series">Series Name</th>\n            <th class="number text-center">Have</th>\n            <th class="status text-center">Status</th>\n          </tr>\n        </thead>\n      </table>\n    </div>\n')
        if perm&lazylibrarian.perm_status or lazylibrarian.CONFIG['USER_ACCOUNTS']:
            __M_writer('    <div class="form-group">\n      <label for="markSeries" class="control-label">Change selected series to: </label>\n      <select id="markSeries" class="markSeries form-control input-sm" name="action">\n')
            if perm&lazylibrarian.perm_status:
                for item in ['Paused', 'Wanted', 'Active', 'Ignored']:
                    __M_writer('        <option value="')
                    __M_writer(str(item))
                    __M_writer('">')
                    __M_writer(str(item))
                    __M_writer('</option>\n')
            if lazylibrarian.CONFIG['USER_ACCOUNTS']:
                __M_writer('        <option value="Unread">Unread</option>\n        <option value="Read">Read</option>\n        <option value="ToRead">To Read</option>\n        <option value="Reading">Reading</option>\n        <option value="Abandoned">Abandoned</option>\n        <option value="Subscribe">Subscribe</option>\n        <option value="Unsubscribe">Unsubscribe</option>\n')
            __M_writer('      </select>\n    </div>\n')
            if authorid != None:
                __M_writer('    <input type="hidden" name="redirect" value="')
                __M_writer(str(authorid))
                __M_writer('">\n')
            __M_writer('    <input type="submit" class="markSeries btn btn-sm btn-default" value="Go">\n')
        __M_writer('  </form>\n  <p>&nbsp;</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascriptIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        whichStatus = context.get('whichStatus', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        authorid = context.get('authorid', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <script type="text/javascript">\n\n    function reason(target) {\n        window.alert(target);\n    };\n\n    $(document).ready(function()\n    {\n         var selected = [];\n\n        $(\'#whichStatus\').change(function(){\n')
        if authorid != None:
            __M_writer("               window.location = 'series?AuthorID=")
            __M_writer(str(authorid))
            __M_writer("&whichStatus=' + $(this).val()\n")
        else:
            __M_writer("               window.location = 'series?whichStatus=' + $(this).val()\n")
        __M_writer('        })\n\n        var oTable = $(\'#book_table\').DataTable(\n            {\n                "dom": "<\'row\'<\'col-xs-6\'l><\'col-xs-6\'f>><\'row\'<\'col-sm-12\'tr>><\'row\'<\'col-sm-5\'i><\'col-sm-7\'p>>",\n                "order": [[3, \'desc\']],\n                "bAutoWidth": false,\n                "stateSave": true,\n                "rowId": 0,\n                "columnDefs":\n                    [{ targets: \'no-sort\', orderable: false },\n                    { targets: [0],\n                          \'class\': \'text-center\',\n                          \'render\': function(data, type, row) {\n                            if ( $.inArray(\'S\' + data, selected) !== -1 ) {\n                                return \'<input type="checkbox" id="S\' + data + \'" name="\' + data + \'" class="checkbox" checked=true />\'; }\n                            return \'<input type="checkbox" id="S\' + data + \'" name="\' + data + \'" class="checkbox" />\';}\n                    },\n                    { targets: [1], \'render\': function(data, type, row) {\n')
        if perm&lazylibrarian.perm_authorbooks:
            __M_writer('                        return \'<a href=\\\'authorPage?AuthorID=\' + row[4] + \'\\\'">\' + row[1] + \'</a>\';}\n')
        else:
            __M_writer('                        return row[1]\n')
        __M_writer('                    },\n                    { targets: [2], \'render\': function(data, type, row) {\n                        return \'<a href="seriesMembers?seriesid=\' + row[5] + \'">\' + row[2] + \'</a>\';}\n                    },\n                    { targets: [3], \'render\': function(data, type, row) {\n                        percent = row[9]\n                        if (percent <= 25) {css = \'danger\'}\n                        else if (percent <= 50) {css = \'warning\'}\n                        else if (percent <= 75) {css = \'info\'}\n                        else {css = \'success\'};\n                        bar = \'<div class="progress center-block" style="width: 120px;"><div class="progress-bar-\' +\n                        css + \' progress-bar progress-bar-striped" role="progressbar" aria-valuenow="\' + percent +\n                        \'" aria-valuemin="0" aria-valuemax="100" style="width: \' + percent +\n                        \'%;"><span class="sr-only">\' + percent +\n                        \'% Complete</span><span class="progressbar-front-text">\' + row[6] + \'/\' + row[7] +\n                        \'</span></div></div>\';\n                        return bar;}\n                    },\n                    { targets: [4],\n                        \'class\': \'text-center\',\n                        \'render\': function(data, type, row) {\n')
        if perm&lazylibrarian.perm_status:
            __M_writer('                            bar = \'<button onclick="reason(\\\'\' + row[8] +\n                            \'\\\')" class="button btn btn-xs btn-primary" type="button">\' + row[3] +\n                            \'</button>\';\n')
        else:
            __M_writer('                            bar = row[3];\n')
        __M_writer('                          return bar;}\n                    }\n                    ],\n                "oLanguage": {\n                    "sSearch": "Filter: ",\n                    "sLengthMenu":"_MENU_ rows per page",\n                    "sEmptyTable": "No series found",\n                    "sInfo":"Showing _START_ to _END_ of _TOTAL_ rows",\n                    "sInfoEmpty":"Showing 0 to 0 of 0 rows",\n                    "sInfoFiltered":"(filtered from _MAX_ total rows)"},\n                "sPaginationType": "full_numbers",\n                "aaSorting": [[3, \'desc\']],\n                "bServerSide": true,\n                "sAjaxSource": \'getSeries?whichStatus=')
        __M_writer(str(whichStatus))
        __M_writer('&AuthorID=')
        __M_writer(str(authorid))
        __M_writer('\',\n                "bFilter": true,\n                "aLengthMenu": [[5, 10, 15, 25, 50, 100, -1], [5, 10, 15, 25, 50, 100, "All"]],\n                "iDisplayLength": ')
        __M_writer(str(lazylibrarian.CONFIG['DISPLAYLENGTH']))
        __M_writer(',\n                "fnRowCallback": function (nRow, aData, iDisplayIndex, iDisplayIndexFull) {\n')
        if perm&lazylibrarian.perm_status == 0:
            __M_writer('                      $(\'td\', nRow).eq(0).addClass("hidden");\n')
        __M_writer('                    // hide author,status on small devices\n                    //$(\'td\', nRow).eq(1).addClass(\'hidden-xs\');\n                    //$(\'td\', nRow).eq(3).addClass(\'hidden-xs\');\n                    return nRow;\n                },\n            });\n\n          $(\'#book_table tbody\').on(\'click\', \'tr input:checkbox\', function () {\n              var id = this.id;\n              var index = $.inArray(id, selected);\n              if ( index === -1 ) {\n                  selected.push( id );\n              } else {\n                  selected.splice( index, 1 );\n              }\n              $(this).toggleClass(\'selected\');\n          } );\n\n        $(\'.dataTables_filter input\').attr("placeholder", "Results filter");\n        //$(window).resize(function() {oTable.draw(false)});\n        $(\'a.toggle-vis\').click(function (e) {\n            e.preventDefault();\n            var column = oTable.column( $(this).attr(\'data-column\') );\n            column.visible( ! column.visible() );\n        } );\n    });\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/app/lazylibrarian/data/interfaces/bookstrap/series.html", "uri": "series.html", "source_encoding": "utf-8", "line_map": {"16": 2, "17": 3, "18": 4, "19": 5, "31": 0, "36": 1, "37": 4, "38": 38, "39": 114, "40": 116, "41": 234, "47": 5, "54": 5, "55": 9, "56": 10, "57": 10, "58": 10, "59": 11, "60": 12, "61": 14, "62": 15, "63": 16, "64": 17, "65": 18, "66": 21, "67": 23, "68": 24, "69": 36, "75": 40, "83": 40, "84": 41, "85": 41, "86": 48, "87": 49, "88": 49, "89": 49, "90": 50, "91": 51, "92": 53, "93": 53, "94": 53, "95": 55, "96": 58, "97": 59, "98": 66, "99": 74, "100": 75, "101": 76, "102": 77, "103": 79, "104": 87, "105": 88, "106": 91, "107": 92, "108": 93, "109": 93, "110": 93, "111": 93, "112": 93, "113": 96, "114": 97, "115": 105, "116": 107, "117": 108, "118": 108, "119": 108, "120": 110, "121": 112, "127": 115, "131": 115, "137": 117, "144": 117, "145": 129, "146": 130, "147": 130, "148": 130, "149": 131, "150": 132, "151": 134, "152": 153, "153": 154, "154": 155, "155": 156, "156": 158, "157": 179, "158": 180, "159": 183, "160": 184, "161": 186, "162": 199, "163": 199, "164": 199, "165": 199, "166": 202, "167": 202, "168": 204, "169": 205, "170": 207, "176": 170}}
__M_END_METADATA
"""
