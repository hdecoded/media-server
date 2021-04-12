# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1616489411.4864192
_enable_loop = True
_template_filename = '/app/lazylibrarian/data/interfaces/bookstrap/author.html'
_template_uri = 'author.html'
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
        __M_writer('\n\n')
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headerIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        ignored = context.get('ignored', UNDEFINED)
        languages = context.get('languages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        showseries = context.get('showseries', UNDEFINED)
        author = context.get('author', UNDEFINED)
        types = context.get('types', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="subhead_container">\n        <form id="subhead_menu" class="form-inline">\n')
        if perm&lazylibrarian.perm_force:
            if author['Status'] == 'Paused':
                __M_writer('                <a href="resumeAuthor?AuthorID=')
                __M_writer(str(author['AuthorID']))
                __M_writer('" class="btn btn-sm btn-primary"><i class="fa fa-pause"></i> Paused</a>\n')
            else:
                if author['Status'] == 'Active':
                    __M_writer('                <a href="wantAuthor?AuthorID=')
                    __M_writer(str(author['AuthorID']))
                    __M_writer('" class="btn btn-sm btn-primary"><i class="fa fa-play"></i> Active</a>\n')
                else:
                    if author['Status'] == 'Wanted':
                        __M_writer('                  <a href="ignoreAuthor?AuthorID=')
                        __M_writer(str(author['AuthorID']))
                        __M_writer('" class="btn btn-sm btn-primary"><i class="fa fa-plus"></i> Wanted</a>\n')
                    else:
                        __M_writer('                  <a href="pauseAuthor?AuthorID=')
                        __M_writer(str(author['AuthorID']))
                        __M_writer('" class="btn btn-sm btn-primary"><i class="fa fa-ban"></i> Ignored</a>\n')
            __M_writer('            <a href="refreshAuthor?AuthorID=')
            __M_writer(str(author['AuthorID']))
            __M_writer('" class="btn btn-sm btn-primary"><i class="fa fa-sync"></i> Refresh Author</a>\n            <a href="libraryScanAuthor?AuthorID=')
            __M_writer(str(author['AuthorID']))
            __M_writer('&library=eBook" class="btn btn-sm btn-primary"><i class="fa fa-sync"></i> eBook Scan</a>\n')
            if lazylibrarian.SHOW_AUDIO > 0:
                __M_writer('                <a href="libraryScanAuthor?AuthorID=')
                __M_writer(str(author['AuthorID']))
                __M_writer('&library=AudioBook" class="btn btn-sm btn-primary"><i class="fa fa-sync"></i> AudioBook Scan</a>\n')
            __M_writer('            <button class="button btn btn-sm btn-primary" type="button" value="removeme" id="removeme"><i class="fa fa-times"></i> Remove Author</button>\n')
            if ignored == 'True':
                __M_writer('                <a href="authorPage?AuthorID=')
                __M_writer(str(author['AuthorID']))
                __M_writer('&Ignored=False" class="btn btn-sm btn-primary"><i class="fa fa-book"></i> Show Active</a>\n')
            else:
                __M_writer('            <a href="authorPage?AuthorID=')
                __M_writer(str(author['AuthorID']))
                __M_writer('&Ignored=True" class="btn btn-sm btn-primary"><i class="fa fa-ban"></i> Show Ignored</a>\n')
        if showseries >= 1:
            if perm&lazylibrarian.perm_series:
                __M_writer('              <a href="series?AuthorID=')
                __M_writer(str(author['AuthorID']))
                __M_writer('" class="btn btn-sm btn-primary"><i class="fa fa-book"></i> Series</a>\n')
        if lazylibrarian.CONFIG['GR_FOLLOW'] == True:
            if author['GRfollow']:
                if author['GRfollow'] != '0':
                    __M_writer('                <a href="unfollowAuthor?AuthorID=')
                    __M_writer(str(author['AuthorID']))
                    __M_writer('" class="btn btn-sm btn-primary"><i class="fa fa-check"></i> Following</a>\n')
                else:
                    __M_writer('                <a href="followAuthor?AuthorID=')
                    __M_writer(str(author['AuthorID']))
                    __M_writer('" class="btn btn-sm btn-primary"><i class="fa fa-times"></i> Not Following</a>\n')
            else:
                __M_writer('              <a href="followAuthor?AuthorID=')
                __M_writer(str(author['AuthorID']))
                __M_writer('" class="btn btn-sm btn-primary"><i class="fa fa-times"></i> Not Following</a>\n')
        __M_writer('         <div class="form-group pull-right">\n')
        if len(types) > 1:
            if  perm&lazylibrarian.perm_audio:
                __M_writer('                <label for="chooselib"><small>&nbsp;</small></label>\n                <select class="form-control input-sm" name="chooselib" id="chooselib">\n')
                for library in types:
                    __M_writer('                    <option value="')
                    __M_writer(str(library))
                    __M_writer('">')
                    __M_writer(str(library))
                    __M_writer('</option>\n')
                __M_writer('                </select>\n')
        if len(languages) > 1:
            __M_writer('              <label for="chooselanguage"><small>&nbsp;Lang</small></label>\n              <select class="form-control input-sm" name="chooselanguage" id="chooselanguage">\n                <option value="">All</option>\n')
            for language in languages:
                __M_writer('                  <option value="')
                __M_writer(str(language['BookLang']))
                __M_writer('">')
                __M_writer(str(language['BookLang']))
                __M_writer('</option>\n')
            __M_writer('              </select>\n')
        __M_writer('         </div>\n')
        if lazylibrarian.CONFIG['USER_ACCOUNTS'] == True:
            if lazylibrarian.CONFIG['RSS_ENABLED'] == True:
                if lazylibrarian.SHOW_EBOOK > 0:
                    __M_writer('             <a href="rssFeed?user=')
                    __M_writer(str(user))
                    __M_writer('&type=eBook&authorid=')
                    __M_writer(str(author['AuthorID']))
                    __M_writer('&limit=10.xml" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="RSS feed of recent ebooks"><i class="fa fa-rss"></i>&nbsp;<i class="fa fa-book"></i></a>\n             <link rel="alternate" type="application/rss+xml" title="LazyLibrarian latest eBooks" href="rssFeed?user=')
                    __M_writer(str(user))
                    __M_writer('&type=eBook&authorid=')
                    __M_writer(str(author['AuthorID']))
                    __M_writer('&limit=10.xml">\n')
                if lazylibrarian.SHOW_AUDIO > 0:
                    __M_writer('             <a href="rssFeed?user=')
                    __M_writer(str(user))
                    __M_writer('&type=AudioBook&authorid=')
                    __M_writer(str(author['AuthorID']))
                    __M_writer('&limit=10.xml" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="RSS feed of recent audiobooks"><i class="fa fa-rss"></i>&nbsp;<i class="fa fa-headphones"></i></a>\n             <link rel="alternate" type="application/rss+xml" title="LazyLibrarian latest AudioBooks" href="rssFeed?user=')
                    __M_writer(str(user))
                    __M_writer('&type=AudioBook&authorid=')
                    __M_writer(str(author['AuthorID']))
                    __M_writer('&limit=10.xml">\n')
        __M_writer('        </form>\n    </div>\n<script type="text/javascript">\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        ignored = context.get('ignored', UNDEFINED)
        booklang = context.get('booklang', UNDEFINED)
        library = context.get('library', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        TypeError = context.get('TypeError', UNDEFINED)
        ZeroDivisionError = context.get('ZeroDivisionError', UNDEFINED)
        author = context.get('author', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n')
        if lazylibrarian.CONFIG['AUTHOR_IMG']:
            __M_writer('    <div id="authorart_container" class="col-md-3">\n        <div id="authorart_menu">\n            <button onclick="bookinfo(\'A_')
            __M_writer(str(author['AuthorID']))
            __M_writer('\')" class="button btn-link text-left" type="button" title=""><img src="')
            __M_writer(str(author['AuthorImg']))
            __M_writer('" class="box-shadow img-responsive" alt="')
            __M_writer(str(author['AuthorName']))
            __M_writer('" title="')
            __M_writer(str(author['AuthorName']))
            __M_writer('"></button>\n        </div>\n    </div>\n')
        __M_writer('    <div id="authorhead_container" class="col-md-9">\n        <div id="authorhead_menu">\n            <h1><a href="')
        __M_writer(str(author['AuthorLink']))
        __M_writer('" target="_blank" rel="noreferrer">')
        __M_writer(str(author['AuthorName']))
        __M_writer('</a>\n')
        if perm&lazylibrarian.perm_edit:
            __M_writer('            <a href="editAuthor?authorid=')
            __M_writer(str(author['AuthorID']))
            __M_writer('" target="_new"><small><i>Edit</i></small></a>\n')
        __M_writer('            </h1>\n')
        if author['AuthorDeath']:
            __M_writer('            <p><b>Born:</b> ')
            __M_writer(str(author['AuthorBorn']))
            __M_writer(', <b>Died:</b> ')
            __M_writer(str(author['AuthorDeath']))
            __M_writer('</p>\n')
        else:
            if author['AuthorBorn']:
                __M_writer('                    <p><b>Born:</b> ')
                __M_writer(str(author['AuthorBorn']))
                __M_writer('</p>\n')
        if author['Status'] == 'Loading':
            __M_writer('            <p>\n            <button onclick="" id="myAlert" title=""><i class="fa fa-circle-notch fa-spin"></i> Fetching information for this author ...</button>\n            </p>\n')
        __M_writer('            <p><b>Totalbooks:</b> ')
        __M_writer(str(author['TotalBooks']))
        __M_writer('</p>\n\n            ')

        totalbooks = author['UnignoredBooks']
        havebooks = author['HaveBooks']
        if not havebooks:
            havebooks = 0
        try:
            percent = (havebooks*100.0)/totalbooks
            if percent > 100:
                percent = 100
            if percent <= 100:
                css = "bg-success"
            if percent <= 75:
                css = "bg-info"
            if percent <= 50:
                css = "bg-warning"
            if percent <= 25:
                css = "bg-danger"
        except (ZeroDivisionError, TypeError):
            percent = 0
            totalbooks = '0'
            css = "bg-danger"
                    
        
        __M_writer('\n<div class="row" title="')
        __M_writer(str(percent))
        __M_writer('">\n  <div class="col-xs-4"><strong>Progress:</strong></div>\n  <div class="col-xs-4">\n    <div class="progress">\n      <div class="progress-bar" role="progressbar" aria-valuenow="')
        __M_writer(str(percent))
        __M_writer('" aria-valuemin="0" aria-valuemax="100" style="width: ')
        __M_writer(str(percent))
        __M_writer('%;">\n        <span class="sr-only">')
        __M_writer(str(percent))
        __M_writer('% Complete</span>\n      </div>\n    </div>\n  </div>\n  <div class="col-xs-4">\n    <span class="progressbar-front-text">')
        __M_writer(str(havebooks))
        __M_writer(' / ')
        __M_writer(str(totalbooks))
        __M_writer('</span>\n  </div>\n</div>\n</div>\n</div>\n</div>\n<form action="markBooks" method="get" class="form-inline">\n  <div class="row">\n    <input type="hidden" name="AuthorID" value="')
        __M_writer(str(author['AuthorID']))
        __M_writer('">\n    <input type="hidden" name="redirect" value="author">\n    <input type="hidden" name="booklang" value=')
        __M_writer(str(booklang))
        __M_writer('>\n    <input type="hidden" name="library" value=')
        __M_writer(str(library))
        __M_writer('>\n    <input type="hidden" name="ignored" value=')
        __M_writer(str(ignored))
        __M_writer('>\n')
        if perm&lazylibrarian.perm_status or  lazylibrarian.CONFIG['USER_ACCOUNTS']:
            __M_writer('    <div class="col-xs-12 col-sm-5">\n      <div class="form-group">\n        <label for="action" class="">Mark selected ')
            __M_writer(str(library))
            __M_writer('s as</label>\n        <select class="markBooks form-control input-sm" id="action" name="action">\n')
            if perm&lazylibrarian.perm_status:
                if lazylibrarian.SHOW_EBOOK > 0:
                    __M_writer('              <option value="WantEbook">eBook Wanted</option>\n')
                if lazylibrarian.SHOW_AUDIO > 0:
                    __M_writer('              <option value="WantAudio">Audio Wanted</option>\n')
                if lazylibrarian.SHOW_EBOOK > 0 and lazylibrarian.SHOW_AUDIO > 0:
                    __M_writer('              <option value="WantBoth">Both Wanted</option>\n')
                __M_writer('            <option value="Have">Have</option>\n            <option value="Ignored">Ignored</option>\n            <option value="Skipped">Skipped</option>\n            <option value="Remove">Remove</option>\n            <option value="Delete">Delete</option>\n            <option value="Leave" hidden>Leave</option>\n')
            if lazylibrarian.CONFIG['USER_ACCOUNTS']:
                __M_writer('            <option value="Unread">Unread</option>\n            <option value="Read">Read</option>\n            <option value="ToRead">To Read</option>\n            <option value="Reading">Reading</option>\n            <option value="Abandoned">Abandoned</option>\n')
            __M_writer('        </select>\n      </div>\n      <input type="submit" class="markBooks btn btn-sm btn-primary" value="Go">\n    </div>\n')
        if lazylibrarian.CONFIG['TOGGLES'] == True:
            __M_writer('    <div class="toggles col-xs-12 col-sm-7 text-right">\n    Toggle: <a class="toggle-vis" data-column="1"> Cover</a>\n    <a class="toggle-vis" data-column="3"> Title</a>\n    <a class="toggle-vis" data-column="4"> Series</a>\n    <a class="toggle-vis hidden-sm hidden-xs" data-column="5"> Rating</a>\n    <a class="toggle-vis" data-column="6"> Released</a>\n    <a class="toggle-vis" data-column="7"> Added</a>\n    <a class="toggle-vis" data-column="8"> Status</a>\n    </div>\n')
        __M_writer('  </div>\n  <div class="table-responsive">\n    <table class="display table table-striped table-hover table-bordered" id="book_table">\n      <thead>\n        <tr>\n          <th class="select text-center no-sort"><input type="checkbox" onClick="toggleAll(this)" /></th>\n          <th class="bookart text-center no-sort">Cover</th>\n          <th class="authorname hidden">Author</th>\n          <th class="bookname">Title</th>\n          <th class="series">Series</th>\n          <th class="stars text-center hidden-sm hidden-xs">Rating</th>\n          <th class="date text-center">Released</th>\n          <th class="date text-center">Added</th>\n          <th class="status text-center">Status</th>\n        </tr>\n      </thead>\n    </table>\n  </div>\n</form>\n<p>&nbsp;</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascriptIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        email = context.get('email', UNDEFINED)
        ignored = context.get('ignored', UNDEFINED)
        booklang = context.get('booklang', UNDEFINED)
        library = context.get('library', UNDEFINED)
        len = context.get('len', UNDEFINED)
        firstpage = context.get('firstpage', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        author = context.get('author', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <script type="text/javascript">\n    $(document).ready(function()\n    {\n      var selected = [];\n      var intjob = 0;\n\n        $(\'#removeme\').click(function () {\n            bootbox.confirm({\n                message: "Are you sure you want to permanently delete the author?",\n                buttons: {\n                    confirm: {\n                        label: \'Yes\',\n                        className: \'btn-success\'\n                    },\n                    cancel: {\n                        label: \'No\',\n                        className: \'btn-danger\'\n                    }\n                },\n                callback: function (result) {\n                  if (result) { $.get("removeAuthor", {\'AuthorID\': \'')
        __M_writer(str(author['AuthorID']))
        __M_writer("' },\n                      function (data) { }); }\n                }\n            });\n        });\n\n        $('#chooselanguage').change(function(){\n            new_settings = 'authorPage?AuthorID=")
        __M_writer(str(author['AuthorID']))
        __M_writer('&BookLang=\' + $(this).val()\n            if (typeof $("#chooselib").val() != \'undefined\') {\n            new_settings += \'&library=\' + $("#chooselib").val() }\n            window.location = new_settings\n        })\n        $(\'#chooselib\').change(function(){\n            new_settings = \'authorPage?AuthorID=')
        __M_writer(str(author['AuthorID']))
        __M_writer('&library=\' + $(this).val()\n            if (typeof $("#chooselanguage").val() != \'undefined\') {\n            new_settings += \'&BookLang=\' + $("#chooselanguage").val() }\n            window.location = new_settings\n        })\n        $(\'#chooselanguage\').val(getUrlVars()[\'BookLang\']);\n        $(\'#chooselib\').val(getUrlVars()[\'library\']);\n\n        if ($("#chooselib").val() != \'AudioBook\') {\n            $(\'#chooselib\').val(\'eBook\')\n        }\n\n        var show = ""+')
        __M_writer(str(lazylibrarian.CONFIG['BOOK_IMG']))
        __M_writer(';\n            if ( show != \'1\' ) { showimg = false }\n            else { showimg = true }\n\n        var oTable = $(\'#book_table\').DataTable(\n            {\n                "order": [[ 6, \'desc\' ]],\n                "bAutoWidth": false,\n                "stateSave": true,\n                "rowId": 0,\n                "columnDefs":[\n                    { targets: \'no-sort\', orderable: false },\n                    { targets: [0],\n                      \'class\': \'text-center\',\n                      \'render\': function(data, type, row) {\n                        if ( $.inArray(\'N\' + data, selected) !== -1 ) {\n                            return \'<input type="checkbox" id="N\' + data + \'" name="\' + data + \'" class="checkbox" checked=true />\'; }\n                        return \'<input type="checkbox" id="N\' + data + \'" name="\' + data + \'" class="checkbox" />\';} },\n                    { targets: [1],\n                        \'class\': \'text-center\',\n                        \'visible\': showimg,\n                        \'render\': function(data, type, row) {\n                        return \'<a href="\' + data + \'" target="_blank" rel="noreferrer"><img src="\' + data + \'" alt="Cover" class="bookcover-sm img-responsive"></a>\';} },\n                    { targets: [2], \'class\': "hidden" },\n                    { targets: [3], \'render\': function(data, type, row) {\n                        var pre = data.split(\'<\');\n                        var limit = window.innerWidth / 30;\n                        var title = truncateOnWord(pre[0], limit);\n                        var tail = data.slice(pre[0].length);\n                        btn = \'<button onclick="bookinfo(\\\'\' + row[9] + \'\\\')" class="button btn-link text-left" type="button" \'\n                        return btn + \' title="\' + pre[0] + \'">\' + title + \'</button>\' + tail ;\n                        }\n                    },\n                    { targets: [4], \'render\': function(data, type, row){\n                        if (row[12] === null ) { return data; }\n                        if (row[12] === \'\' ) { return row[4]; }\n                        var series = row[12].split(\'^\');\n                        var output = [];\n                        for (var index=0; index < series.length; ++index) {\n                            var link_data = series[index].split("~");\n                            output.push(\'<a href=seriesMembers?seriesid=\' + link_data[0] + \'>\' + link_data[1] + \'</a>\')\n                        }\n                        return output.join(\'<br>\');\n                    }},\n')
        if lazylibrarian.CONFIG['RATESTARS'] == True:
            __M_writer('                    { targets: [5],\n                        \'class\': \'text-center\',\n                        \'render\': function(data, type, row) {\n                            return \'<img src="images/\' + data + \'-stars.png" alt="Rating">\';} },\n')
        __M_writer('                    { targets: [6],\n                        \'class\': "text-center",\n                        \'render\': function(data, type, row) {\n                            return \'<a data-toggle="tooltip" title="Listed: \' + row[16] + \'\\n\' + row[17] + \'">\' + row[6] + \'</a>\';} },\n                    { targets: [7],\n                        \'class\': \'text-center\',\n                        \'render\': function(data, type, row) {\n                        var edate = row[10];\n                        if (edate === "null"){ edate = ""}\n                        var adate = row[15];\n                        if (adate === "null"){ adate = ""}\n')
        if lazylibrarian.SHOW_EBOOK == 0:
            __M_writer('                           edate = ""\n')
        if lazylibrarian.SHOW_AUDIO == 0:
            __M_writer('                           adate = ""\n')
        if lazylibrarian.SHOW_EBOOK > 0 and lazylibrarian.SHOW_AUDIO > 0:
            __M_writer("                           edate = edate + '<br>'\n")
        __M_writer('                        return edate + adate ;} },\n                    { targets: [8],\n                        \'class\': \'text-center\',\n                        \'render\': function(data, type, row) {\n                        var btn = row[11]\n                        var flag = row[13]\n                        var btn2 = row[14]\n                        btn = btn + flag\n                        if ( btn.indexOf(\'Open\') >= 0 ) {\n                                btn = \'<a class="button green btn btn-xs btn-warning" href="openBook?bookid=\' + row[9] +\n                                    \'&library=eBook" target="_self"><i class="fa fa-book"></i> \' + btn + \'</a>\'\n')
        if len(email):
            __M_writer('                                btn += \'<a class="button green btn btn-xs btn-info" href="sendBook?bookid=\' + row[9] +\n                                    \'&library=eBook" target="_self">Send</a>\'\n')
        __M_writer('                        }\n                        else if ( btn.indexOf(\'Wanted\') >= 0 ) {\n                            btn = \'<p><a class="a btn btn-xs btn-danger"><i class="fa fa-book"></i> \' + btn + \'</a></p><p><a class="b btn btn-xs btn-success" href="searchForBook?bookid=\' + row[9] + \'&library=eBook" target="_self"><i class="fa fa-search"></i> Search</a></p>\'}\n                        else if ( btn.indexOf(\'Snatched\') >= 0 ) {\n                            btn = \'<a class="button btn btn-xs btn-info"><i class="fa fa-book"></i> \' + btn + \'</a>\'}\n                        else if ( btn.indexOf(\'Ignored\') >= 0 ) {\n                            btn = \'<button onclick="dlinfo(\\\'\' + btn + \'^\' + row[9] +\n                            \'\\\')" class="button btn btn-xs btn-primary" type="button"><i class="fa fa-book"></i> \' + btn + \'</button>\'}\n                        else if ( btn.indexOf(\'Have\') >= 0 ) {\n')
        if perm&lazylibrarian.perm_status:
            __M_writer('                            btn = \'<a class="button btn btn-xs btn-info"><i class="fa fa-book"></i> \' + btn + \'</a>\'\n')
        else:
            __M_writer('                            btn = \'<p><a class="button btn btn-xs btn-default grey" href="requestBook?bookid=\' + row[9] + \'&library=eBook" target="_self"><i class="fa fa-book"></i> Request</a></p>\'\n')
        __M_writer('                            }\n                        else {\n')
        if perm&lazylibrarian.perm_status:
            __M_writer('                            btn = \'<a class="button btn btn-xs btn-default grey"><i class="fa fa-book"></i> \' + btn + \'</a>\'\n')
        else:
            __M_writer('                            btn = \'<p><a class="button btn btn-xs btn-default grey" href="requestBook?bookid=\' + row[9] + \'&library=eBook" target="_self"><i class="fa fa-book"></i> Request</a></p>\'\n')
        __M_writer('                            }\n                        if ( btn2.indexOf(\'Open\') >= 0 ) {\n                                btn2 = \'<a class="button green btn btn-xs btn-warning" href="openBook?bookid=\' + row[9] +\n                                    \'&library=AudioBook" target="_self"><i class="fa fa-headphones"></i> \' + btn2 + \'</a>\'\n                        }\n                        else if ( btn2.indexOf(\'Wanted\') >= 0 ) {\n                            btn2 = \'<p><a class="a btn btn-xs btn-danger"><i class="fa fa-headphones"></i> \' + btn2 + \'</a></p><p><a class="b btn btn-xs btn-success" href="searchForBook?bookid=\' + row[9] + \'&library=AudioBook" target="_self"><i class="fa fa-search"></i> Search</a></p>\'}\n                        else if ( btn2.indexOf(\'Snatched\') >= 0 ) {\n                            btn2 = \'<a class="button btn btn-xs btn-info"><i class="fa fa-headphones"></i> \' + btn2 + \'</a>\'}\n                        else if ( btn.indexOf(\'Ignored\') >= 0 ) {\n                            btn2 = \'<button onclick="dlinfo(\\\'\' + btn2 + \'^\' + row[9] +\n                            \'\\\')" class="button btn btn-xs btn-primary" type="button"><i class="fa fa-headphones"></i> \' + btn2 + \'</button>\'}\n                        else if ( btn2.indexOf(\'Have\') >= 0 ) {\n')
        if perm&lazylibrarian.perm_status:
            __M_writer('                            btn2 = \'<a class="button btn btn-xs btn-info"><i class="fa fa-headphones"></i> \' + btn2 + \'</a>\'\n')
        else:
            __M_writer('                            btn2 = \'<p><a class="button btn btn-xs btn-default grey" href="requestBook?bookid=\' + row[9] + \'&library=AudioBook" target="_self"><i class="fa fa-headphones"></i> Request</a></p>\'\n')
        __M_writer('                            }\n                        else {\n')
        if perm&lazylibrarian.perm_status:
            __M_writer('                            btn2 = \'<a class="button btn btn-xs btn-default grey"><i class="fa fa-headphones"></i> \' + btn2 + \'</a>\'\n')
        else:
            __M_writer('                            btn2 = \'<p><a class="button btn btn-xs btn-default grey" href="requestBook?bookid=\' + row[9] + \'&library=AudioBook" target="_self"><i class="fa fa-headphones"></i> Request</a></p>\'\n')
        __M_writer('                            }\n')
        if lazylibrarian.SHOW_EBOOK == 0:
            __M_writer("                           btn = ''\n")
        if lazylibrarian.SHOW_AUDIO == 0:
            __M_writer("                           btn2 = ''\n")
        if lazylibrarian.SHOW_EBOOK > 0 and lazylibrarian.SHOW_AUDIO > 0:
            __M_writer("                           btn = btn + '<br>'\n")
        __M_writer('                        return btn + btn2;} }\n                    ],\n                "oLanguage": {\n                    "sSearch": "Filter: ",\n                    "sLengthMenu":"_MENU_ rows per page",\n                    "sEmptyTable": "No books found",\n                    "sInfo":"Showing _START_ to _END_ of _TOTAL_ rows",\n                    "sInfoEmpty":"Showing 0 to 0 of 0 rows",\n                    "sInfoFiltered":"(filtered from _MAX_ total rows)"},\n                "sPaginationType": "full_numbers",\n                "aaSorting": [[6, \'desc\']],\n                "bServerSide": true,\n                "sAjaxSource": \'getBooks?source=Author&AuthorID=')
        __M_writer(str(author['AuthorID']))
        __M_writer('&booklang=')
        __M_writer(str(booklang))
        __M_writer('&library=')
        __M_writer(str(library))
        __M_writer('&ignored=')
        __M_writer(str(ignored))
        __M_writer('\',\n                "bFilter": true,\n                "aLengthMenu": [[5, 10, 15, 25, 50, 100, -1], [5, 10, 15, 25, 50, 100, "All"]],\n                "iDisplayLength": ')
        __M_writer(str(lazylibrarian.CONFIG['DISPLAYLENGTH']))
        __M_writer(',\n                "fnRowCallback": function (nRow, aData, iDisplayIndex, iDisplayIndexFull) {\n                    // hide cover,stars,date on small devices\n                    //$(\'td\', nRow).eq(1).addClass(\'hidden-xs\');\n                    $(\'td\', nRow).eq(5).addClass(\'hidden-sm hidden-xs\');\n                    //$(\'td\', nRow).eq(6).addClass(\'hidden-xs\');\n                    //$(\'td\', nRow).eq(7).addClass(\'hidden-xs\');\n                    return nRow;\n                },\n            });\n\n          $(\'#book_table tbody\').on(\'click\', \'tr input:checkbox\', function () {\n              var id = this.id;\n              var index = $.inArray(id, selected);\n              if ( index === -1 ) {\n                  selected.push( id );\n              } else {\n                  selected.splice( index, 1 );\n              }\n              $(this).toggleClass(\'selected\');\n          } );\n\n            oTable.on( \'xhr\', function () {\n              var json = oTable.ajax.json();\n              if (json.loading) {\n                if (intjob === 0) {\n                  intjob = setInterval( function () {\n                    oTable.ajax.reload( null, false );\n                    }, 10000 );\n                }\n              }\n              else {\n                if (intjob != 0) { clearInterval( intjob )};\n                $(\'#myAlert\').addClass(\'hidden\');\n              };\n            });\n\n        var page = oTable.page();\n        if ( page != \'0\' ) {\n            if (')
        __M_writer(str(firstpage))
        __M_writer(') { oTable.page( \'first\' ).draw( \'page\' ); }\n        }\n\n        $(\'.dataTables_filter input\').attr("placeholder", "Results Filter");\n        //$(window).resize(function() {oTable.draw(false)});\n        $(\'a.toggle-vis\').click(function (e) {\n            e.preventDefault();\n            var column = oTable.column( $(this).attr(\'data-column\') );\n            column.visible( ! column.visible() );\n        } );\n    });\n\n    function dlinfo(target) {\n        var res = target.split(\'^\');\n        var status = res[0]\n        var rowid = res[1]\n        $.get(\'dlinfo\', {\'target\': target},\n        function(data) {\n            bootbox.dialog({\n                title: \'Title \'+ status,\n                message: \'<pre>\'+data+\'</pre>\',\n                buttons: {\n                   primary: {\n                        label: "Close",\n                        className: \'btn-primary\'\n                    }\n                }\n            });\n        });\n    };\n\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/app/lazylibrarian/data/interfaces/bookstrap/author.html", "uri": "author.html", "source_encoding": "utf-8", "line_map": {"16": 2, "17": 3, "18": 4, "19": 5, "31": 0, "36": 1, "37": 4, "38": 87, "39": 229, "40": 503, "46": 5, "58": 5, "59": 8, "60": 9, "61": 10, "62": 10, "63": 10, "64": 11, "65": 12, "66": 13, "67": 13, "68": 13, "69": 14, "70": 15, "71": 16, "72": 16, "73": 16, "74": 17, "75": 18, "76": 18, "77": 18, "78": 22, "79": 22, "80": 22, "81": 23, "82": 23, "83": 24, "84": 25, "85": 25, "86": 25, "87": 27, "88": 28, "89": 29, "90": 29, "91": 29, "92": 30, "93": 31, "94": 31, "95": 31, "96": 34, "97": 35, "98": 36, "99": 36, "100": 36, "101": 39, "102": 40, "103": 41, "104": 42, "105": 42, "106": 42, "107": 43, "108": 44, "109": 44, "110": 44, "111": 46, "112": 47, "113": 47, "114": 47, "115": 50, "116": 51, "117": 52, "118": 53, "119": 55, "120": 56, "121": 56, "122": 56, "123": 56, "124": 56, "125": 58, "126": 61, "127": 62, "128": 65, "129": 66, "130": 66, "131": 66, "132": 66, "133": 66, "134": 68, "135": 70, "136": 71, "137": 72, "138": 73, "139": 74, "140": 74, "141": 74, "142": 74, "143": 74, "144": 75, "145": 75, "146": 75, "147": 75, "148": 77, "149": 78, "150": 78, "151": 78, "152": 78, "153": 78, "154": 79, "155": 79, "156": 79, "157": 79, "158": 83, "164": 89, "175": 89, "176": 91, "177": 92, "178": 94, "179": 94, "180": 94, "181": 94, "182": 94, "183": 94, "184": 94, "185": 94, "186": 98, "187": 100, "188": 100, "189": 100, "190": 100, "191": 101, "192": 102, "193": 102, "194": 102, "195": 104, "196": 105, "197": 106, "198": 106, "199": 106, "200": 106, "201": 106, "202": 107, "203": 108, "204": 109, "205": 109, "206": 109, "207": 112, "208": 113, "209": 117, "210": 117, "211": 117, "212": 119, "213": 120, "214": 121, "215": 122, "216": 123, "217": 124, "218": 125, "219": 126, "220": 127, "221": 128, "222": 129, "223": 130, "224": 131, "225": 132, "226": 133, "227": 134, "228": 135, "229": 136, "230": 137, "231": 138, "232": 139, "233": 140, "234": 141, "235": 140, "236": 141, "237": 141, "238": 145, "239": 145, "240": 145, "241": 145, "242": 146, "243": 146, "244": 151, "245": 151, "246": 151, "247": 151, "248": 159, "249": 159, "250": 161, "251": 161, "252": 162, "253": 162, "254": 163, "255": 163, "256": 164, "257": 165, "258": 167, "259": 167, "260": 169, "261": 170, "262": 171, "263": 173, "264": 174, "265": 176, "266": 177, "267": 179, "268": 186, "269": 187, "270": 193, "271": 198, "272": 199, "273": 209, "279": 230, "291": 230, "292": 251, "293": 251, "294": 258, "295": 258, "296": 264, "297": 264, "298": 276, "299": 276, "300": 320, "301": 321, "302": 326, "303": 337, "304": 338, "305": 340, "306": 341, "307": 343, "308": 344, "309": 346, "310": 357, "311": 358, "312": 361, "313": 370, "314": 371, "315": 372, "316": 373, "317": 375, "318": 377, "319": 378, "320": 379, "321": 380, "322": 382, "323": 395, "324": 396, "325": 397, "326": 398, "327": 400, "328": 402, "329": 403, "330": 404, "331": 405, "332": 407, "333": 408, "334": 409, "335": 411, "336": 412, "337": 414, "338": 415, "339": 417, "340": 429, "341": 429, "342": 429, "343": 429, "344": 429, "345": 429, "346": 429, "347": 429, "348": 432, "349": 432, "350": 471, "351": 471, "357": 351}}
__M_END_METADATA
"""
