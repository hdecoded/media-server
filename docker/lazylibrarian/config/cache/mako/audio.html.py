# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1616489279.8408008
_enable_loop = True
_template_filename = '/app/lazylibrarian/data/interfaces/bookstrap/audio.html'
_template_uri = 'audio.html'
_source_encoding = 'utf-8'
_exports = ['headerIncludes', 'body', 'javascriptIncludes']



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
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headerIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        languages = context.get('languages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        pref = context.get('pref', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div id="subhead_container" class="row">\n    <form id="subhead_menu" class="form-inline">\n      <div class="col-xs-10">\n')
        if perm&lazylibrarian.perm_force:
            __M_writer('        <a id="forcesearch" class="btn btn-sm btn-primary" href="forceSearch?source=audio"><i class="fa fa-search"></i> Search</a>\n        <a id="forcepostprocess" class="btn btn-sm btn-primary" href="forceProcess?source=audio"><i class="fa fa-cogs"></i> Run Post-Processor</a>\n        <a href="libraryScan?library=AudioBook" class="btn btn-sm btn-primary" id="scan"><i class="fa fa-bolt"></i> Library Scan</a>\n')
        __M_writer('        <a href="audioWall" class="button btn btn-sm btn-primary"><i class="fa fa-calendar-check"></i> Recent AudioBooks</a>\n')
        if lazylibrarian.CONFIG['USER_ACCOUNTS'] == True:
            if lazylibrarian.CONFIG['RSS_ENABLED'] == True:
                __M_writer('            <a href="rssFeed?user=')
                __M_writer(str(user))
                __M_writer('&type=AudioBook&limit=10.xml" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="RSS feed of recent downloads"><i class="fa fa-rss"></i></a>\n            <link rel="alternate" type="application/rss+xml" title="LazyLibrarian latest AudioBooks" href="rssFeed?user=')
                __M_writer(str(user))
                __M_writer('&type=AudioBook&limit=10.xml">\n')
            if pref&lazylibrarian.pref_myafeeds:
                __M_writer('            <a href="toggleMyAFeeds" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="All, or just mine"><i class="fa fa-user-circle"></i></a>\n')
            else:
                __M_writer('            <a href="toggleMyAFeeds" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="All, or just mine"><i class="fa fa-users"></i></a>\n')
        __M_writer('      </div>\n      <div class="col-xs-2">\n')
        if len(languages) > 1:
            __M_writer('        <div class="form-group">\n          <label for="chooselanguage"><small>Language</small></label>\n          <select class="form-control input-sm" name="chooselanguage" id="chooselanguage" onchange="window.location = \'audio?BookLang=\' + this.options[this.selectedIndex].value">\n            <option value="">All</option>\n')
            for language in languages:
                __M_writer('            <option value="')
                __M_writer(str(language['BookLang']))
                __M_writer('">')
                __M_writer(str(language['BookLang']))
                __M_writer('</option>\n')
            __M_writer('          </select>\n        </div>\n')
        __M_writer('      </div>\n    </form>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        booklang = context.get('booklang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n')
        if lazylibrarian.AUDIO_UPDATE == True:
            __M_writer('      <p>\n    <button onclick="" id="myAlert" title=""><i class="fa fa-circle-notch fa-spin"></i> Libraryscan in progress ...</button>\n    </p>\n')
        __M_writer('  <form name="markBooks" id="markBooks" action="markBooks" method="get" class="form-inline" onsubmit="return false;">\n    <div class="row">\n      <div class="col-xs-12 col-sm-5">\n        <input type="hidden" name="booklang" value=')
        __M_writer(str(booklang))
        __M_writer('>\n        <input type="hidden" name="redirect" value=\'audio\'>\n')
        if perm&lazylibrarian.perm_status:
            __M_writer('        <div class="form-group">\n          <label for="markBooks" class="control-label">Mark selected as</label>\n          <select class="markBooks form-control input-sm" id="action" name="action">\n            <option value="Wanted">Wanted</option>\n            <option value="Have">Have</option>\n            <option value="Ignored">Ignored</option>\n            <option value="Skipped">Skipped</option>\n            <option value="Remove">Remove</option>\n            <option value="Delete">Delete</option>\n            <option value="Leave" hidden>Leave</option>\n          </select>\n        </div>\n        <button type="submit" class="btn btn-sm btn-primary" onclick="validateForm()">Go</button>\n      </div>\n')
        if lazylibrarian.CONFIG['TOGGLES'] == True:
            __M_writer('        <div class="toggles col-xs-12 col-sm-7 text-right">\n          Toggle: <a class="toggle-vis" data-column="1"> Cover</a>\n          <a class="toggle-vis" data-column="2"> Author</a>\n          <a class="toggle-vis" data-column="3"> Title</a>\n          <a class="toggle-vis" data-column="4"> Series</a>\n          <a class="toggle-vis hidden-sm hidden-xs" data-column="5"> Rating</a>\n          <a class="toggle-vis" data-column="6"> Released</a>\n          <a class="toggle-vis" data-column="7"> Added</a>\n          <a class="toggle-vis" data-column="8"> Status</a>\n        </div>\n')
        __M_writer('    </div>\n    <br/>\n    <div class="table-responsive">\n      <table class="display table table-striped table-hover table-bordered" id="book_table">\n        <thead>\n          <tr>\n')
        if perm&lazylibrarian.perm_status:
            __M_writer('            <th class="select text-center no-sort"><input type="checkbox" onClick="toggleAll(this)" /></th>\n')
        else:
            __M_writer('            <th class="hidden"></th>\n')
        __M_writer('            <th class="bookart text-center no-sort">Cover</th>\n            <th class="authorname">Author</th>\n            <th class="bookname">Title</th>\n            <th class="series">Series</th>\n            <th class="stars text-center hidden-sm hidden-xs">Rating</th>\n            <th class="date text-center">Released</th>\n            <th class="date text-center">Added</th>\n            <th class="status text-center">Status</th>\n          </tr>\n        </thead>\n      </table>\n    </div>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascriptIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        email = context.get('email', UNDEFINED)
        booklang = context.get('booklang', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <script type="text/javascript">\n    $(document).ready(function() {\n\n        var selected = [];\n        var intjob = 0;\n\n        $(\'#chooselanguage\').val(getUrlVars()[\'BookLang\']);\n\n        var show = ""+')
        __M_writer(str(lazylibrarian.CONFIG['BOOK_IMG']))
        __M_writer(';\n            if ( show != \'1\' ) { showimg = false }\n            else { showimg = true }\n\n        var table = $(\'#book_table\').DataTable({\n            "dom": "<\'row\'<\'col-xs-6\'l><\'col-xs-6\'f>><\'row\'<\'col-sm-12\'tr>><\'row\'<\'col-sm-5\'i><\'col-sm-7\'p>>",\n            "bAutoWidth": false,\n            "stateSave": true,\n            "order": [[ 2, \'asc\' ]],\n            "rowId": 0,\n            "columnDefs":[\n                { targets: \'no-sort\', orderable: false },\n                { targets: [0],\n                  \'class\': \'text-center\',\n                  \'render\': function(data, type, row) {\n                    if ( $.inArray(\'A\' + data, selected) !== -1 ) {\n                        return \'<input type="checkbox" id="A\' + data + \'" name="\' + data + \'" class="checkbox" checked=true />\'; }\n                    return \'<input type="checkbox" id="A\' + data + \'" name="\' + data + \'" class="checkbox" />\';} },\n                { targets: [1],\n                    \'visible\': showimg,\n                    \'render\': function(data, type, row) {\n                    return \'<a href="\' + data + \'" target="_blank" rel="noreferrer"><img src="\' + data + \'" alt="Cover" class="bookcover-sm img-responsive"></a>\';} },\n                { targets: [2], \'render\': function(data, type, row) {\n')
        if perm&lazylibrarian.perm_authorbooks:
            __M_writer('                    btn = \'<a href=\\\'authorPage?AuthorID=\' + row[8] + \'\\\'">\' + data + \'</a>\'\n')
        else:
            __M_writer("                    btn = '<a>' + data + '</a>'\n")
        __M_writer('                  return btn ;}\n                },\n                { targets: [3], \'render\': function(data, type, row) {\n                    var pre = data.split(\'<\');\n                    var limit = window.innerWidth / 30;\n                    var title = truncateOnWord(pre[0], limit);\n                    var tail = data.slice(pre[0].length);\n                    btn = \'<button onclick="bookinfo(\\\'\' + row[9] + \'\\\')" class="button btn-link text-left" type="button" \'\n                    if (title == pre[0]) { return btn + \'>\' + title + \'</button>\' + tail ; }\n                    return btn + \' title="\' + pre[0] + \'">\' + title + \'</button>\' + tail ;\n                    }\n                },\n                { targets: [4], \'render\': function(data, type, row){\n                    if (row[12] === null ) { return data; }\n                    if (row[12] === \'\' ) { return row[4]; }\n                    var series = row[12].split(\'^\');\n                    var output = [];\n                    for (var index=0; index < series.length; ++index) {\n                        var link_data = series[index].split("~");\n                        output.push(\'<a href=seriesMembers?seriesid=\' + link_data[0] + \'>\' + link_data[1] + \'</a>\')\n                    }\n                    return output.join(\'<br>\');\n                }},\n')
        if lazylibrarian.CONFIG['RATESTARS'] == True:
            __M_writer('                { targets: [5],\n                    \'class\': \'text-center\',\n                    \'render\': function(data, type, row) {\n                        return \'<img src="images/\' + data + \'-stars.png" alt="Rating">\';} },\n')
        __M_writer('                { targets: [6],\n                    \'class\': "text-center",\n                    \'render\': function(data, type, row) {\n                        return \'<a data-toggle="tooltip" title="Listed: \' + row[14] + \'\\n\' + row[15] + \'">\' + row[6] + \'</a>\';} },\n                { targets: [7],\n                    \'class\': \'text-center\',\n                    \'render\': function(data, type, row) {\n                    var str = row[10];\n                    if (str === "null"){ str = ""}\n                    return str ;} },\n                { targets: [8],\n                    \'class\': \'text-center\',\n                    \'render\': function(data, type, row) {\n                    var btn = row[11]\n                    var flag = row[13]\n                    btn = btn + flag\n                    if ( btn.indexOf(\'Open\') >= 0 ) {\n                            btn = \'<a class="button green btn btn-xs btn-warning" href="openBook?bookid=\' + row[9] +\n                                \'&library=AudioBook" target="_self"><i class="fa fa-headphones"></i> \' + btn + \'</a>\'\n')
        if len(email):
            __M_writer('                                btn += \'<a class="button green btn btn-xs btn-info" href="sendBook?bookid=\' + row[9] +\n                                    \'&library=AudioBook" target="_self">Send</a>\'\n')
        __M_writer("                    }\n                    else if ( btn.indexOf('Wanted') >= 0 ) {\n")
        if perm&lazylibrarian.perm_force:
            __M_writer('                            btn = \'<p><a class="a btn btn-xs btn-danger">\' + btn + \'</a></p><p><a class="b btn btn-xs btn-success" href="searchForBook?bookid=\' + row[9] + \'&library=AudioBook" target="_self"><i class="fa fa-search"></i> Search</a></p>\'\n')
        else:
            __M_writer('                            btn = \'<a class="button btn btn-xs btn-default grey">\' + btn + \'</a>\'\n')
        __M_writer('                    }\n                    else if ( btn.indexOf(\'Snatched\') >= 0 ) {\n                        btn = \'<a class="button btn btn-xs btn-info">\' + btn + \'</a>\'}\n                    else if ( btn.indexOf(\'Have\') >= 0 ) {\n                        btn = \'<a class="button btn btn-xs btn-info">\' + btn + \'</a>\'}\n                    else {\n                        btn = \'<a class="button btn btn-xs btn-default grey">\' + btn + \'</a>\'}\n                    return btn;} }\n                ],\n            "oLanguage": {\n                "sSearch": "Filter: ",\n                "sLengthMenu":"_MENU_ rows per page",\n                "sEmptyTable": "No books found",\n                "sInfo":"Showing _START_ to _END_ of _TOTAL_ rows",\n                "sInfoEmpty":"Showing 0 to 0 of 0 rows",\n                "sInfoFiltered":"(filtered from _MAX_ total rows)"},\n\n            "aLengthMenu": [[5, 10, 15, 25, 50, 100, -1], [5, 10, 15, 25, 50, 100, "All"]],\n            "iDisplayLength": ')
        __M_writer(str(lazylibrarian.CONFIG['DISPLAYLENGTH']))
        __M_writer(',\n            "sPaginationType": "full_numbers",\n            "aaSorting": [[0, \'asc\']],\n            "bServerSide": true,\n            "sAjaxSource": \'getBooks?source=Audio&library=AudioBook&booklang=')
        __M_writer(str(booklang))
        __M_writer('\',\n            "bFilter": true,\n            "fnRowCallback": function (nRow, aData, iDisplayIndex, iDisplayIndexFull) {\n')
        if perm&lazylibrarian.perm_status == 0:
            __M_writer('                  $(\'td\', nRow).eq(0).addClass("hidden");\n')
        __M_writer('                // hide cover,stars,date on small devices\n                //$(\'td\', nRow).eq(1).addClass(\'hidden-xs\');\n                $(\'td\', nRow).eq(5).addClass(\'hidden-sm hidden-xs\');\n                //$(\'td\', nRow).eq(6).addClass(\'hidden-xs\');\n                //$(\'td\', nRow).eq(7).addClass(\'hidden-xs\');\n                return nRow;\n            },\n        });\n\n          $(\'#book_table tbody\').on(\'click\', \'tr input:checkbox\', function () {\n              var id = this.id;\n              var index = $.inArray(id, selected);\n              if ( index === -1 ) {\n                  selected.push( id );\n              } else {\n                  selected.splice( index, 1 );\n              }\n              $(this).toggleClass(\'selected\');\n          } );\n\n            table.on( \'xhr\', function () {\n              var json = table.ajax.json();\n              if (json.loading) {\n                if (intjob === 0) {\n                  intjob = setInterval( function () {\n                    table.ajax.reload( null, false );\n                    }, 10000 );\n                }\n              }\n              else {\n                if (intjob != 0) { clearInterval( intjob )};\n                $(\'#myAlert\').addClass(\'hidden\');\n              };\n            });\n\n        $(\'.dataTables_filter input\').attr("placeholder", "Results filter");\n        //$(window).resize(function() {table.draw(\'page\')});\n\n        $(\'a.toggle-vis\').click(function (e) {\n            e.preventDefault();\n            var column = table.column( $(this).attr(\'data-column\') );\n            column.visible( ! column.visible() );\n        } );\n        //enable datatables console logging\n        //table.on(function ( e ) {\n        //   console.log( e ); } );\n    });\n\n    function validateForm() {\n        var x = document.forms["markBooks"]["action"].value;\n        var c = (document.querySelectorAll(\'input[class="checkbox"]:checked\').length);\n        if (c > 0 && x == "Delete") {\n            if (c == 1) {msg = "Are you sure you want to permanently delete the selected audiobook?"}\n            if (c > 1) {msg = "Are you sure you want to permanently delete the " + c + " selected audiobooks?"}\n            bootbox.confirm({\n                message: msg,\n                buttons: {\n                    confirm: {\n                        label: \'Yes\',\n                        className: \'btn-success\'\n                    },\n                    cancel: {\n                        label: \'No\',\n                        className: \'btn-danger\'\n                    }\n                },\n                callback: function (result) {\n                    if (result) { document.getElementById("markBooks").submit(); }\n                }\n            });\n            return false;\n        }\n        else { document.getElementById("markBooks").submit(); }\n    }\n\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/app/lazylibrarian/data/interfaces/bookstrap/audio.html", "uri": "audio.html", "source_encoding": "utf-8", "line_map": {"16": 2, "17": 3, "18": 4, "19": 5, "31": 0, "36": 1, "37": 4, "38": 42, "39": 107, "40": 308, "46": 5, "55": 5, "56": 9, "57": 10, "58": 14, "59": 15, "60": 16, "61": 17, "62": 17, "63": 17, "64": 18, "65": 18, "66": 20, "67": 21, "68": 22, "69": 23, "70": 26, "71": 28, "72": 29, "73": 33, "74": 34, "75": 34, "76": 34, "77": 34, "78": 34, "79": 36, "80": 39, "86": 43, "93": 43, "94": 44, "95": 44, "96": 45, "97": 46, "98": 50, "99": 53, "100": 53, "101": 55, "102": 56, "103": 71, "104": 72, "105": 83, "106": 89, "107": 90, "108": 91, "109": 92, "110": 94, "116": 108, "124": 108, "125": 117, "126": 117, "127": 140, "128": 141, "129": 142, "130": 143, "131": 145, "132": 168, "133": 169, "134": 174, "135": 193, "136": 194, "137": 197, "138": 199, "139": 200, "140": 201, "141": 202, "142": 204, "143": 222, "144": 222, "145": 226, "146": 226, "147": 229, "148": 230, "149": 232, "155": 149}}
__M_END_METADATA
"""
