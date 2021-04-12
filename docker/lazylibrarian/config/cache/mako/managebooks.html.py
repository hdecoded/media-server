# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1616489509.4393876
_enable_loop = True
_template_filename = '/app/lazylibrarian/data/interfaces/bookstrap/managebooks.html'
_template_uri = 'managebooks.html'
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
        __M_writer('\n\n')
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
        types = context.get('types', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        library = context.get('library', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="subhead_container">\n      <form id="subhead_menu" action="search" method="get">\n        <div class="col-xs-10">\n')
        if perm&lazylibrarian.perm_force:
            if library != 'AudioBook':
                __M_writer('              <a href="importAlternate" class="button btn btn-sm btn-primary"><i class="fa fa-book"></i> Import eBooks</a>\n              <a href="includeAlternate" class="button btn btn-sm btn-primary"><i class="fa fa-book"></i> Include eBooks</a>\n')
                if lazylibrarian.CONFIG['USER_ACCOUNTS'] and lazylibrarian.CONFIG['IMP_CALIBREDB']:
                    __M_writer('                <button class="button btn btn-sm btn-primary" type="button" value="synctocalibre" id="synctocalibre">\n                <i class="fa fa-link"></i> Calibre Sync</button>\n')
            else:
                __M_writer('              <a href="importAlternate?library=AudioBook" class="button btn btn-sm btn-primary"><i class="fa fa-book"></i> Import AudioBooks</a>\n              <a href="includeAlternate?library=AudioBook" class="button btn btn-sm btn-primary"><i class="fa fa-book"></i> Include AudioBooks</a>\n')
            __M_writer('            <a href="forceWish?source=books" class="button btn btn-sm btn-primary"><i class="fa fa-search"></i> WishLists</a>\n            <button class="button btn btn-sm btn-primary" type="button" value="importcsv" id="importcsv">\n            <i class="fa fa-download"></i> Import CSV</button>\n            <button class="button btn btn-sm btn-primary" type="button" value="exportcsv" id="exportcsv">\n            <i class="fa fa-upload"></i> Export CSV</button>\n')
            if lazylibrarian.CONFIG['GR_SYNC'] == True:
                __M_writer('              <button class="button btn btn-sm btn-primary" type="button" value="synctogoodreads" id="synctogoodreads">\n              <i class="fa fa-link"></i> Goodreads Sync</button>\n')
        __M_writer('          </div>\n')
        if len(types) > 1:
            if  perm&lazylibrarian.perm_audio:
                __M_writer('                <div class="form-group pull-right">\n                <!--label for="chooselib"><small>Library</small></label-->\n                <select class="form-control input-sm" name="chooselib" id="chooselib">\n')
                for item in types:
                    __M_writer('                    <option value="')
                    __M_writer(str(item))
                    __M_writer('"\n')
                    if library == item:
                        __M_writer('                            selected = "selected"\n')
                    __M_writer('                    >')
                    __M_writer(str(item))
                    __M_writer('</option>\n')
                __M_writer('                </select>\n                </div>\n')
        __M_writer('      </form>\n    </div>\n    <button class="hidden" onclick="" id="myAlert" title=""><i class="fa fa-circle-notch fa-spin"></i> Syncing, please wait...</button>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        whichStatus = context.get('whichStatus', UNDEFINED)
        library = context.get('library', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n  <form action="manage" method="get" class="form-inline">\n    <div class="row">\n      <div class="col-xs-12 col-sm-5">\n        <div class="form-group">\n          <label for="whichStatus" class="control-label">Status:</label>\n          <select name="whichStatus" id="whichStatus" class="form-control input-sm">\n')
        for item in ['All', 'Skipped', 'Wanted', 'Open', 'Have', 'Ignored', 'Snatched']:
            __M_writer('            <option value="')
            __M_writer(str(item))
            __M_writer('"\n')
            if whichStatus == item:
                __M_writer('                        selected = "selected"\n')
            __M_writer('                >')
            __M_writer(str(item))
            __M_writer('</option>\n')
        if lazylibrarian.CONFIG['USER_ACCOUNTS'] == True:
            __M_writer('            <option value="Read"\n')
            if whichStatus == "Read":
                __M_writer('                    selected = "selected"\n')
            __M_writer('                >Read</option>\n            <option value="ToRead"\n')
            if whichStatus == "ToRead":
                __M_writer('                    selected = "selected"\n')
            __M_writer('                >To Read</option >\n            <option value="Reading"\n')
            if whichStatus == "Reading":
                __M_writer('                    selected = "selected"\n')
            __M_writer('                >Reading</option >\n            <option value="Abandoned"\n')
            if whichStatus == "Abandoned":
                __M_writer('                    selected = "selected"\n')
            __M_writer('                >Abandoned</option >\n')
        __M_writer('          </select>\n        </div>\n      </div>\n\n')
        if lazylibrarian.CONFIG['TOGGLES'] == True:
            __M_writer('        <div class="toggles col-xs-12 col-sm-7 text-right">\n          Toggle: <a class="toggle-vis" data-column="1"> Cover</a>\n          <a class="toggle-vis" data-column="2"> Author</a>\n          <a class="toggle-vis" data-column="3"> Title</a>\n          <a class="toggle-vis" data-column="4"> Series</a>\n          <a class="toggle-vis hidden-sm hidden-xs" data-column="5"> Rating</a>\n          <a class="toggle-vis" data-column="6"> Released</a>\n          <a class="toggle-vis" data-column="7"> Listed</a>\n')
            if lazylibrarian.CONFIG['DELAYSEARCH'] == True:
                __M_writer('            <a class="toggle-vis" data-column="8"> Delay</a>\n            <a class="toggle-vis" data-column="9"> Search</a>\n')
            __M_writer('        </div>\n')
        __M_writer('    </div>\n  </form>\n  <br/>\n  <form action="markBooks" method="get" class="form-inline">\n    <input type="hidden" name="redirect" value="manage">\n    <input type="hidden" name="library" value="')
        __M_writer(str(library))
        __M_writer('">\n    <div class="table-responsive">\n      <table class="display table table-striped table-hover table-bordered" id="book_table">\n        <thead>\n          <tr>\n            <th class="select text-center no-sort"><input type="checkbox" onClick="toggleAll(this)" /></th>\n            <th class="bookart text-center no-sort">Cover</th>\n            <th class="authorname">Author</th>\n            <th class="bookname">Title</th>\n            <th class="series">Series</th>\n            <th class="stars text-center hidden-sm hidden-xs">Rating</th>\n            <th class="date text-center">Released</th>\n            <th class="date text-center">Listed</th>\n')
        if lazylibrarian.CONFIG['DELAYSEARCH'] == True:
            if whichStatus == 'Wanted':
                __M_writer('                    <th class="stars text-center no-sort">Delay</th>\n                    <th class="date text-center no-sort">Last Search</th>\n')
        __M_writer('          </tr>\n        </thead>\n      </table>\n    </div>\n')
        if perm&lazylibrarian.perm_status or lazylibrarian.CONFIG['USER_ACCOUNTS']:
            __M_writer('    <div class="form-group">\n      <label for="markBooks" class="control-label">Mark selected ')
            __M_writer(str(library))
            __M_writer('s as</label>\n      <select id="markBooks" class="markBooks form-control input-sm" name="action">\n')
            if whichStatus != 'Wanted':
                if lazylibrarian.SHOW_EBOOK > 0 and library == 'AudioBook':
                    __M_writer('            <option value="WantEbook">eBook Wanted</option>\n')
                if lazylibrarian.SHOW_AUDIO > 0 and library != 'AudioBook':
                    __M_writer('            <option value="WantAudio">Audio Wanted</option>\n')
            if whichStatus not in ['Wanted', 'Snatched']:
                if lazylibrarian.SHOW_EBOOK > 0 and lazylibrarian.SHOW_AUDIO > 0:
                    __M_writer('            <option value="WantBoth">both Wanted</option>\n')
            if whichStatus != 'Snatched':
                for item in ['Skipped', 'Have', 'Ignored']:
                    __M_writer('            <option value="')
                    __M_writer(str(item))
                    __M_writer('">')
                    __M_writer(str(item))
                    __M_writer('</option>\n')
            if lazylibrarian.CONFIG['USER_ACCOUNTS'] == True:
                __M_writer('        <option value="Unread">Unread</option>\n        <option value="Read">Read</option>\n        <option value="ToRead">To Read</option>\n        <option value="Reading">Reading</option>\n        <option value="Abandoned">Abandoned</option>\n')
            if lazylibrarian.CONFIG['DELAYSEARCH'] == True:
                __M_writer('        <option value="NoDelay">No Delay</option>\n')
            __M_writer('      </select>\n    </div>\n    <input type="submit" class="markBooks btn btn-sm btn-default" value="Go">\n')
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
        perm = context.get('perm', UNDEFINED)
        whichStatus = context.get('whichStatus', UNDEFINED)
        library = context.get('library', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <script type="text/javascript">\n    $(document).ready(function()\n    {\n        var selected = [];\n\n        var show = ""+')
        __M_writer(str(lazylibrarian.CONFIG['BOOK_IMG']))
        __M_writer(';\n            if ( show != \'1\' ) { showimg = false }\n            else { showimg = true }\n\n        $(\'#chooselib\').change(function(){\n            new_settings = \'manage?whichStatus=\' + $(\'#whichStatus\').val() + \'&library=\' + $(this).val()\n            window.location = new_settings\n        })\n\n        $(\'#whichStatus\').change(function(){\n            new_settings = \'manage?whichStatus=\' + $(this).val() + \'&library=\' + $(\'#chooselib\').val()\n            window.location = new_settings\n        })\n\n        $(\'#exportcsv\').on(\'click\', function(e) {\n            $.get(\'exportCSV\', {\'library\': $(\'#chooselib\').val()}, function(data) {\n                bootbox.dialog({\n                    title: \'CSV Export Result\',\n                    message: \'<pre>\'+data+\'</pre>\',\n                    buttons: {\n                        primary: {\n                            label: "Close",\n                            className: \'btn-primary\'\n                        },\n                    }\n                });\n            });\n        });\n\n        $(\'#synctogoodreads\').on(\'click\', function(e) {\n            $("#myAlert").removeClass(\'hidden\');\n            $.get(\'syncToGoodreads\', function(data) {\n                $("#myAlert").addClass(\'hidden\');\n                bootbox.dialog({\n                    title: \'Goodreads Sync Result\',\n                    message: \'<pre>\'+data+\'</pre>\',\n                    buttons: {\n                        primary: {\n                            label: "Close",\n                            className: \'btn-primary\'\n                        },\n                    }\n                });\n            });\n        });\n\n        $(\'#synctocalibre\').on(\'click\', function(e) {\n            $("#myAlert").removeClass(\'hidden\');\n            $.get(\'syncToCalibre\', function(data) {\n                $("#myAlert").addClass(\'hidden\');\n                bootbox.dialog({\n                    title: \'Calibre Sync Result\',\n                    message: \'<pre>\'+data+\'</pre>\',\n                    buttons: {\n                        primary: {\n                            label: "Close",\n                            className: \'btn-primary\'\n                        },\n                    }\n                });\n            });\n        });\n\n        $(\'#importcsv\').on(\'click\', function(e) {\n            $.get(\'importCSV\', {\'library\': $(\'#chooselib\').val()}, function(data) {\n                var myModal = bootbox.dialog({\n                    title: \'CSV Import Info\',\n                    message: \'<pre>\'+data+\'</pre>\',\n                    buttons: {\n                        primary: {\n                            label: "Close",\n                            className: \'btn-primary\'\n                        },\n                    }\n                });\n                setTimeout(function(){\n                myModal.modal(\'hide\');\n                }, 5000);\n            });\n        });\n\n         var table = $(\'#book_table\').DataTable(\n            {\n                "dom": "<\'row\'<\'col-xs-6\'l><\'col-xs-6\'f>><\'row\'<\'col-sm-12\'tr>><\'row\'<\'col-sm-5\'i><\'col-sm-7\'p>>",\n                "bAutoWidth": false,\n                "stateSave": true,\n                "order": [[ 2, \'asc\' ]],\n                "rowId": 0,\n                "columnDefs":[\n                    { targets: \'no-sort\', orderable: false },\n                    { targets: [0],\n                        \'class\': \'text-center\',\n                        \'render\': function(data, type, row) {\n                            if ( $.inArray(\'Y\' + data, selected) !== -1 ) {\n                                return \'<input type="checkbox" id="Y\' + data + \'" name="\' + data + \'" class="checkbox" checked=true />\'; }\n                            return \'<input type="checkbox" id="Y\' + data + \'" name="\' + data + \'" class="checkbox" />\';} },\n                    { targets: [1],\n                        \'visible\': showimg,\n                        \'render\': function(data, type, row) {\n                        return \'<a href="\' + data + \'" target="_blank" rel="noreferrer"><img src="\' + data + \'" alt="Cover" class="bookcover-sm img-responsive"></a>\';} },\n                    { targets: [2], \'render\': function(data, type, row) {\n                        return \'<a href=\\\'authorPage?AuthorID=\' + row[8] + \'\\\'">\' + data + \'</a>\';}\n                    },\n                    { targets: [3], \'render\': function(data, type, row) {\n                        var pre = data.split(\'<\');\n                        var limit = window.innerWidth / 30;\n                        var title = truncateOnWord(pre[0], limit);\n                        var tail = data.slice(pre[0].length);\n                        btn = \'<button onclick="bookinfo(\\\'\' + row[9] + \'\\\')" class="button btn-link text-left" type="button" \'\n                        if (title == pre[0]) { return btn + \'>\' + title + \'</button>\' + tail ; }\n                        return btn + \' title="\' + pre[0] + \'">\' + title + \'</button>\' + tail ;\n                        }\n                    },\n                    { targets: [4], \'render\': function(data, type, row){\n                        if (row[12] === null ) { return data; }\n                        if (row[12] === \'\' ) { return row[4]; }\n                        var series = row[12].split(\'^\');\n                        var output = [];\n                        for (var index=0; index < series.length; ++index) {\n                            var link_data = series[index].split("~");\n                            output.push(\'<a href=seriesMembers?seriesid=\' + link_data[0] + \'>\' + link_data[1] + \'</a>\')\n                        }\n                        return output.join(\'<br>\');\n                    }},\n')
        if lazylibrarian.CONFIG['RATESTARS'] == True:
            __M_writer('                    { targets: [5],\n                        \'class\': \'text-center\',\n                        \'render\': function(data, type, row) {\n                        return \'<img src="images/\' + data + \'-stars.png" alt="Rating">\';} },\n')
        __M_writer("                    { targets: [6],\n                        'class': 'text-center'},\n                    { targets: [7],\n                        'class': 'text-center',\n                        'render': function(data, type, row) {\n                            return row[16] + '<br>' + row[17];} },\n")
        if lazylibrarian.CONFIG['DELAYSEARCH'] == True:
            if whichStatus == 'Wanted':
                __M_writer("                            { targets: [8],\n                                'class': 'text-center',\n                                'render': function(data, type, row) {\n                                    return row[14];} },\n                            { targets: [9],\n                                'class': 'text-center',\n                                'render': function(data, type, row) {\n                                    return row[15];} }\n")
        __M_writer('                    ],\n                "oLanguage": {\n                    "sSearch": "Filter: ",\n                    "sLengthMenu":"_MENU_ rows per page",\n                    "sEmptyTable": "No books found",\n                    "sInfo":"Showing _START_ to _END_ of _TOTAL_ rows",\n                    "sInfoEmpty":"Showing 0 to 0 of 0 rows",\n                    "sInfoFiltered":"(filtered from _MAX_ total rows)"},\n                "aLengthMenu": [[5, 10, 15, 25, 50, 100, -1], [5, 10, 15, 25, 50, 100, "All"]],\n                "iDisplayLength": ')
        __M_writer(str(lazylibrarian.CONFIG['DISPLAYLENGTH']))
        __M_writer(',\n                "sPaginationType": "full_numbers",\n                "aaSorting": [[2, \'asc\']],\n                "bServerSide": true,\n                "sAjaxSource": \'getBooks?whichStatus=')
        __M_writer(str(whichStatus))
        __M_writer('&library=')
        __M_writer(str(library))
        __M_writer('&source=Manage\',\n                "bFilter": true,\n                "fnRowCallback": function (nRow, aData, iDisplayIndex, iDisplayIndexFull) {\n')
        if perm&lazylibrarian.perm_status == 0:
            __M_writer('                      $(\'td\', nRow).eq(0).addClass("hidden");\n')
        __M_writer('                    // hide cover,stars,date on small devices\n                    //$(\'td\', nRow).eq(1).addClass(\'hidden-xs\');\n                    $(\'td\', nRow).eq(5).addClass(\'hidden-sm hidden-xs\');\n                    //$(\'td\', nRow).eq(6).addClass(\'hidden-xs\');\n                    //$(\'td\', nRow).eq(7).addClass(\'hidden-xs\');\n                    return nRow;\n                },\n            });\n\n          $(\'#book_table tbody\').on(\'click\', \'tr input:checkbox\', function () {\n              var id = this.id;\n              var index = $.inArray(id, selected);\n              if ( index === -1 ) {\n                  selected.push( id );\n              } else {\n                  selected.splice( index, 1 );\n              }\n              $(this).toggleClass(\'selected\');\n          } );\n\n        $(\'.dataTables_filter input\').attr("placeholder", "Results filter");\n        //$(window).resize(function() {oTable.draw(false)});\n        $(\'a.toggle-vis\').click(function (e) {\n            e.preventDefault();\n            var column = table.column( $(this).attr(\'data-column\') );\n            column.visible( ! column.visible() );\n        } );\n    });\n\n    function bookinfo(bookid) {\n        $.get(\'bookdesc\', {\'bookid\': bookid},\n        function(data) {\n            var $textAndPic = $(\'<div></div>\');\n            $textAndPic.append(\'<img src="./cache/book/\' + bookid + \'.jpg" class="box-shadow img-responsive" />\');\n            var res = data.split(\'^\');\n            var title = res[0]\n            var desc = res[1]\n            $textAndPic.append(\'<br>\' + desc + \' <br />\');\n            bootbox.dialog({\n                size: "large",\n                title: title,\n                message: $textAndPic,\n                buttons: {\n                   primary: {\n                        label: "Close",\n                        className: \'btn-primary\'\n                    }\n                }\n            });\n        });\n    };\n\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/app/lazylibrarian/data/interfaces/bookstrap/managebooks.html", "uri": "managebooks.html", "source_encoding": "utf-8", "line_map": {"16": 2, "17": 3, "18": 4, "19": 5, "31": 0, "36": 1, "37": 4, "38": 52, "39": 175, "40": 177, "41": 404, "47": 6, "55": 6, "56": 10, "57": 11, "58": 12, "59": 14, "60": 15, "61": 18, "62": 19, "63": 22, "64": 27, "65": 28, "66": 32, "67": 33, "68": 34, "69": 35, "70": 38, "71": 39, "72": 39, "73": 39, "74": 40, "75": 41, "76": 43, "77": 43, "78": 43, "79": 45, "80": 49, "86": 53, "94": 53, "95": 54, "96": 54, "97": 61, "98": 62, "99": 62, "100": 62, "101": 63, "102": 64, "103": 66, "104": 66, "105": 66, "106": 68, "107": 69, "108": 70, "109": 71, "110": 73, "111": 75, "112": 76, "113": 78, "114": 80, "115": 81, "116": 83, "117": 85, "118": 86, "119": 88, "120": 90, "121": 94, "122": 95, "123": 103, "124": 104, "125": 107, "126": 109, "127": 114, "128": 114, "129": 127, "130": 128, "131": 129, "132": 133, "133": 137, "134": 138, "135": 139, "136": 139, "137": 141, "138": 142, "139": 143, "140": 145, "141": 146, "142": 149, "143": 150, "144": 151, "145": 154, "146": 155, "147": 156, "148": 156, "149": 156, "150": 156, "151": 156, "152": 159, "153": 160, "154": 166, "155": 167, "156": 169, "157": 173, "163": 176, "167": 176, "173": 178, "180": 178, "181": 184, "182": 184, "183": 308, "184": 309, "185": 314, "186": 320, "187": 321, "188": 322, "189": 332, "190": 341, "191": 341, "192": 345, "193": 345, "194": 345, "195": 345, "196": 348, "197": 349, "198": 351, "204": 198}}
__M_END_METADATA
"""
