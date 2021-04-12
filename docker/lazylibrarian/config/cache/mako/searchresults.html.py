# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1616489284.2604947
_enable_loop = True
_template_filename = '/app/lazylibrarian/data/interfaces/bookstrap/searchresults.html'
_template_uri = 'searchresults.html'
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
        perm = context.get('perm', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="subhead_container" class="row">\n      <form action="search" method="get">\n        <div id="subhead_menu"  class="col-xs-12 col-md-8">\n        </div>\n        <div class="clearfix visible-xs"><hr/></div>\n')
        if perm&lazylibrarian.perm_search:
            __M_writer('        <div class="col-xs-12 col-md-4">\n        <div class="form-group">\n          <label class="sr-only">Search</label>\n          <div class="input-group">\n            <input type="text" class="form-control deletable input-sm col-xs-12" value="" onfocus="if(this.value==this.defaultValue) this.value=\'\';" name="name" placeholder="Title / Author / ISBN" id="searchbox" name="searchbox">\n            <span class="input-group-btn">\n              <button type="submit" value="Book" class="btn btn-sm btn-primary" data-toggle="tooltip" data-placement="bottom" title="Search for book"><i class="fa fa-search"></i></button>\n            </span>\n          </div>\n        </div>\n        </div>\n')
        __M_writer('      </form>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        loadlist = context.get('loadlist', UNDEFINED)
        title = context.get('title', UNDEFINED)
        booklist = context.get('booklist', UNDEFINED)
        searchresults = context.get('searchresults', UNDEFINED)
        booksearch = context.get('booksearch', UNDEFINED)
        authorlist = context.get('authorlist', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n<!--p>\n<button onclick="" id="myAlert" title=""><i class="fa fa-circle-notch fa-spin"></i> Author Loading ...</button>\n</p-->\n\n<div class="table-responsive">\n    <table class="display table table-striped table-hover table-bordered" id="book_table">\n        <thead>\n            <tr>\n                <th class="bookart text-center no-sort">Cover</th>\n                <th class="authorname">Author</th>\n                <th class="bookname">Title</th>\n                <th class="date text-center">Released</th>\n                <th class="stars text-center hidden-sm hidden-xs">Rating</th>\n                <th class="stars text-center hidden-sm hidden-xs">Rating count</th>\n                <th class="addAuthor text-center no-sort">Add</th>\n                <th class="fuzz text-right">Match</th>\n             </tr>\n        </thead>\n\n        <tbody>\n')
        if searchresults is not None:
            for result in searchresults:
                __M_writer('                    ')

                if result['bookrate'] < 0.5:
                    starimg = '0-stars.png'
                elif result['bookrate'] >= 0.5 and result['bookrate'] < 1.5:
                    starimg = '1-stars.png'
                elif result['bookrate'] >= 1.5 and result['bookrate'] < 2.5:
                    starimg = '2-stars.png'
                elif result['bookrate'] >= 2.5 and result['bookrate'] < 3.5:
                    starimg = '3-stars.png'
                elif result['bookrate'] >= 3.5 and result['bookrate'] < 4.5:
                    starimg = '4-stars.png'
                elif result['bookrate'] >= 4.5:
                    starimg = '5-stars.png'
                else:
                    starimg = '0-stars.png'
                
                if authorlist and result['authorid'] in authorlist:
                    destination = "authorPage?AuthorID="+result['authorid']
                    value = "Have Author"
                    but_class = "btn-info"
                elif loadlist and result['authorid'] in loadlist:
                    destination = "#"
                    value = "Loading"
                    but_class = "btn-warning"
                elif result['authorid']:
                    destination = "addAuthorID?AuthorID="+result['authorid']
                    value = "Add Author"
                    but_class = "btn-success"
                else:
                    destination = "addAuthor?AuthorName="+result['authorname']
                    value = "Add Author"
                    but_class = "btn-success"
                
                but_class2 = "btn-info hidden"
                but_class3 = "btn-info hidden"
                value2 = value
                value3 = value
                destination2 = "#"
                destination3 = "#"
                
                if value == "Loading":
                    value2 = value
                    destination2 = "#"
                    but_class2 = "btn-info hidden"
                    value3 = value
                    destination3 = "#"
                    but_class3 = "btn-info hidden"
                elif booklist:
                    if result['bookid'] in booklist:
                        for item in booksearch:
                            if item['BookID'] == result['bookid']:
                                value2 = '<i class="fa fa-book"></i> ' + item['Status']
                                value3 = '<i class="fa fa-headphones"></i> ' + item['AudioStatus']
                                valid_id = item['BookID']
                
                        if 'Open' in value2:
                            destination2 = "openBook?library=eBook&bookid="+valid_id
                            but_class2 = "btn-warning"
                        elif 'Wanted' in value2:
                            destination2 = "searchForBook?library=eBook&bookid="+valid_id
                            but_class2 = "btn-success"
                        elif 'Have' in value2 or 'Snatched' in value2:
                            destination2 = "#"
                            but_class2 = "btn-info"
                        elif 'Skipped' in value2:
                            destination2 = "addBook?library=eBook&bookid="+result['bookid']
                            if result['authorid']:
                                destination2 = destination2 + "&authorid="+result['authorid']
                            value2 = "Add Book"
                            but_class2 = "btn-success"
                        else:
                            destination2 = "#"
                            but_class2 = "btn-default"
                
                        if 'Open' in value3:
                            destination3 = "openBook?library=AudioBook&bookid="+valid_id
                            but_class3 = "btn-warning"
                        elif 'Wanted' in value3:
                            destination3 = "searchForBook?library=AudioBook&bookid="+valid_id
                            but_class3 = "btn-success"
                        elif 'Have' in value3 or 'Snatched' in value3:
                            destination3 = "#"
                            but_class3 = "btn-info"
                        elif 'Skipped' in value3:
                            destination3 = "addBook?library=AudioBook&bookid="+result['bookid']
                            if result['authorid']:
                                destination3 = destination3 + "&authorid="+result['authorid']
                            value3 = "Add Audio"
                            but_class3 = "btn-success"
                        else:
                            destination3 = "#"
                            but_class3 = "btn-default"
                    else:
                        destination2 = "addBook?library=eBook&bookid="+result['bookid']
                        if result['authorid']:
                            destination2 = destination2 + "&authorid="+result['authorid']
                        value2 = "Add Book"
                        but_class2 = "btn-success"
                
                        destination3 = "addBook?library=AudioBook&bookid="+result['bookid']
                        if result['authorid']:
                            destination3 = destination3 + "&authorid="+result['authorid']
                        value3 = "Add Audio"
                        but_class3 = "btn-success"
                
                if not lazylibrarian.SHOW_EBOOK:
                    value2 = value
                    destination2 = "#"
                    but_class2 = "btn-info hidden"
                if not lazylibrarian.SHOW_AUDIO:
                    value3 = value
                    destination3 = "#"
                    but_class3 = "btn-info hidden"
                
                
                __M_writer('\n<tr>\n  <td class="bookart text-center"><a href="')
                __M_writer(str(result['bookimg']))
                __M_writer('" target="_blank" rel="noreferrer"><img src="')
                __M_writer(str(result['bookimg']))
                __M_writer('" alt="Cover"></a></td>\n  <td class="authorname">')
                __M_writer(str(result['authorname']))
                __M_writer('</td>\n  <td class="bookname"><a href="')
                __M_writer(str(result['booklink']))
                __M_writer('" target="_blank" rel="noreferrer">')
                __M_writer(str(result['bookname']))
                __M_writer('</a></td>\n  <td class="date text-center">')
                __M_writer(str(result['bookdate']))
                __M_writer('</td>\n  <td class="stars text-center"><img src="images/')
                __M_writer(str(starimg))
                __M_writer('" alt="')
                __M_writer(str(result['bookrate']))
                __M_writer('"></td>\n  <td class="bookrate_count">')
                __M_writer(str(result.get('bookrate_count', 0)))
                __M_writer('</td>\n  <td class="addAuthor text-center">\n    <p><a class="')
                __M_writer(str(but_class))
                __M_writer(' btn btn-xs" href="')
                __M_writer(str(destination))
                __M_writer('">')
                __M_writer(str(value))
                __M_writer('</a></p>\n    <p><a class="')
                __M_writer(str(but_class2))
                __M_writer(' btn btn-xs" href="')
                __M_writer(str(destination2))
                __M_writer('">')
                __M_writer(str(value2))
                __M_writer('</a></p>\n    <p><a class="')
                __M_writer(str(but_class3))
                __M_writer(' btn btn-xs" href="')
                __M_writer(str(destination3))
                __M_writer('">')
                __M_writer(str(value3))
                __M_writer('</a></p>\n  </td>\n  <td class="fuzz text-right">')
                __M_writer(str(result['highest_fuzz']))
                __M_writer('%</td>\n</tr>\n')
        __M_writer('</tbody>\n</table>\n</div>\n<p>&nbsp;</p>\n')
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
        __M_writer = context.writer()
        __M_writer('\n  <script type="text/javascript">\n    $(document).ready(function()\n    {\n        var table = $(\'#book_table\').dataTable(\n            {\n                "responsive": true,\n                "order": [[ 6, \'desc\' ]],\n                "aoColumns": [\n                    null,\n                    null,\n                    null,\n                    null,\n                    null,\n                    null,\n                    null,\n                    null\n                    ],\n                "columnDefs":\n                    [\n                        { targets: \'no-sort\', orderable: false },\n                        {targets: 4, "type": "alt-string"},\n                    ]\n                ,\n                "oLanguage": {\n                    "sSearch": "Filter: ",\n                    "sLengthMenu":"Show _MENU_ books per page",\n                    "sEmptyTable": "No books found",\n                    "sInfo":"Showing _START_ to _END_ of _TOTAL_ results",\n                    "sInfoEmpty":"Showing 0 to 0 of 0 books",\n                    "sInfoFiltered":"(filtered from _MAX_ total books)"},\n                "iDisplayLength": ')
        __M_writer(str(lazylibrarian.CONFIG['DISPLAYLENGTH']))
        __M_writer(',\n                "sPaginationType": "full_numbers",\n                "fnRowCallback": function (nRow, aData, iDisplayIndex, iDisplayIndexFull) {\n                    // hide cover,stars on small devices\n                    $(\'td\', nRow).eq(4).addClass(\'hidden-sm hidden-xs\');\n                    $(\'td\', nRow).eq(5).addClass(\'hidden-sm hidden-xs\');\n                    return nRow;\n                },\n            });\n        $(\'.dataTables_filter input\').attr("placeholder", "Search table here");\n\n\n        //var c = (document.querySelectorAll(\'a.hidden\').length);\n        //if ( c > 0 ) {\n        //    setInterval( function () { window.location.reload( false ); }, 5000 );\n        //    document.getElementById("myAlert").style.display = "block";\n        //    } else {\n        //    document.getElementById("myAlert").style.display = "none";\n        //    }\n    });\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/app/lazylibrarian/data/interfaces/bookstrap/searchresults.html", "uri": "searchresults.html", "source_encoding": "utf-8", "line_map": {"16": 2, "17": 3, "18": 4, "19": 5, "31": 0, "36": 1, "37": 4, "38": 26, "39": 186, "40": 188, "41": 241, "47": 5, "52": 5, "53": 11, "54": 12, "55": 24, "61": 27, "71": 27, "72": 29, "73": 29, "74": 50, "75": 51, "76": 52, "77": 52, "78": 53, "79": 54, "80": 55, "81": 56, "82": 57, "83": 58, "84": 59, "85": 60, "86": 61, "87": 62, "88": 63, "89": 64, "90": 65, "91": 66, "92": 67, "93": 68, "94": 69, "95": 70, "96": 71, "97": 72, "98": 73, "99": 74, "100": 75, "101": 76, "102": 77, "103": 78, "104": 79, "105": 80, "106": 81, "107": 82, "108": 83, "109": 84, "110": 85, "111": 86, "112": 87, "113": 88, "114": 89, "115": 90, "116": 91, "117": 92, "118": 93, "119": 94, "120": 95, "121": 96, "122": 97, "123": 98, "124": 99, "125": 100, "126": 101, "127": 102, "128": 103, "129": 104, "130": 105, "131": 106, "132": 107, "133": 108, "134": 109, "135": 110, "136": 111, "137": 112, "138": 113, "139": 114, "140": 115, "141": 116, "142": 117, "143": 118, "144": 119, "145": 120, "146": 121, "147": 122, "148": 123, "149": 124, "150": 125, "151": 126, "152": 127, "153": 128, "154": 129, "155": 130, "156": 131, "157": 132, "158": 133, "159": 134, "160": 135, "161": 136, "162": 137, "163": 138, "164": 139, "165": 140, "166": 141, "167": 142, "168": 143, "169": 144, "170": 145, "171": 146, "172": 147, "173": 148, "174": 149, "175": 150, "176": 151, "177": 152, "178": 153, "179": 154, "180": 155, "181": 156, "182": 157, "183": 158, "184": 159, "185": 160, "186": 161, "187": 162, "188": 163, "189": 164, "190": 165, "191": 166, "192": 165, "193": 167, "194": 167, "195": 167, "196": 167, "197": 168, "198": 168, "199": 169, "200": 169, "201": 169, "202": 169, "203": 170, "204": 170, "205": 171, "206": 171, "207": 171, "208": 171, "209": 172, "210": 172, "211": 174, "212": 174, "213": 174, "214": 174, "215": 174, "216": 174, "217": 175, "218": 175, "219": 175, "220": 175, "221": 175, "222": 175, "223": 176, "224": 176, "225": 176, "226": 176, "227": 176, "228": 176, "229": 178, "230": 178, "231": 182, "237": 187, "241": 187, "247": 189, "251": 189, "252": 220, "253": 220, "259": 253}}
__M_END_METADATA
"""
