# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1616489842.1674664
_enable_loop = True
_template_filename = '/app/lazylibrarian/data/interfaces/bookstrap/editbook.html'
_template_uri = 'editbook.html'
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
        __M_writer('\n<html><head></head><body></body></html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headerIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        config = context.get('config', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <button class="hidden" onclick="" id="myAlert" title=""><i class="fa fa-circle-notch fa-spin"></i> Searching, please wait...</button>\n    <div id="subhead_container" class="row">\n          <form action="booksearch" method="get" class="form-inline">\n            <div class="indented">\n            <input type="hidden" name="bookid" value=')
        __M_writer(str(config['BookID']))
        __M_writer('>\n            <input type="hidden" name="title" value="')
        __M_writer(str(config['BookName']))
        __M_writer('">\n            <input type="hidden" name="author" value="')
        __M_writer(str(config['AuthorName']))
        __M_writer('">\n            <div class="form-group">\n              <label for="action" class="control-label">Searches: </label>\n              <select class="booksearch form-control input-sm" id="action" name="action">\n                // would be nice to use fontawesome icons here but options are not styleable\n                // and some browsers don\'t show them, eg linux firefox, android chrome\n                // They only show icons on closed select, not in dropdown\n                <option value="e_full">eBook Title/Author</option>\n                <option value="e_title">eBook Title</option>\n                <option value="e_author">eBook Author</option>\n                <option value="g_full">General Search</option>\n')
        if lazylibrarian.SHOW_AUDIO != 0:
            __M_writer('                  <option value="a_full">Audio Title/Author</option>\n                  <option value="a_title">Audio Title</option>\n                  <option value="a_author">Audio Author</option>\n')
        __M_writer('              </select>\n            </div>\n            <button type="submit" class="btn btn-sm btn-primary" onclick="validateForm()">Go</button>\n            </div>\n          </form>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        loop = __M_loop = runtime.LoopStack()
        authors = context.get('authors', UNDEFINED)
        title = context.get('title', UNDEFINED)
        covers = context.get('covers', UNDEFINED)
        config = context.get('config', UNDEFINED)
        seriesdict = context.get('seriesdict', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<form accept-charset="UTF-8" action="bookUpdate" method="post">\n    <div class="configtable">\n        <input name="utf8" type="hidden" value="&#x2713;" />\n        <legend>')
        __M_writer(str(title))
        __M_writer('</legend>\n        <div class="form-group">\n            <label for="moveBook" class="control-label">Change author to: </label>\n            <select id="moveBook" class="moveBook form-control input" name="authorname">\n')
        for item in authors:
            __M_writer('                <option value="')
            __M_writer(str(item['AuthorName']))
            __M_writer('"\n')
            if config['AuthorName'] == item['AuthorName']:
                __M_writer('                    selected = "selected"\n')
            __M_writer('                >')
            __M_writer(str(item['AuthorName']))
            __M_writer('</option>\n')
        __M_writer('            </select>\n        </div>\n\n        <div class="form-group">\n            <input type="text" id="bookid" name="bookid" value="')
        __M_writer(str(config['BookID']))
        __M_writer('" class="hidden">\n        </div>\n        <div class="form-group">\n            <label for="bookname" class="control-label">Book Title:</label>\n            <input type="text" id="bookname" name="bookname" value="')
        __M_writer(str(config['BookName']))
        __M_writer('" class="form-control" placeholder="">\n        </div>\n        <div class="form-group">\n            <label for="booksub" class="control-label">Subtitle:</label>\n            <input type="text" id="booksub" name="booksub" value="')
        __M_writer(str(config['BookSub']))
        __M_writer('" class="form-control" placeholder="">\n        </div>\n        <div class="form-group">\n            <label for="bookgenre" class="control-label">Genre:</label>\n            <input type="text" id="bookgenre" name="bookgenre" value="')
        __M_writer(str(config['BookGenre']))
        __M_writer('" class="form-control" placeholder="Comma separated list of genres">\n        </div>\n        <div class="form-group">\n            <label for="scanresult">Added by</label>\n            <input id="scanresult" name="scanresult" class="form-control" placeholder="Reason for adding/rejecting"\n                       value="')
        __M_writer(str(config['BookAdded']))
        __M_writer(' ')
        __M_writer(str(config['ScanResult']))
        __M_writer('" readonly >\n        </div>\n        <div class="form-group">\n            <label for="importfrom" class="control-label">Import from</label>\n            <input type="text" id="importfrom" name="importfrom" value="" class="form-control" placeholder="Manual import folder">\n        </div>\n        <fieldset  class="form-group">\n          <div class="form-group col-md-6">\n            <label for="booklang" class="control-label">Language:</label>\n            <input type="text" id="booklang" name="booklang" value="')
        __M_writer(str(config['BookLang']))
        __M_writer('" class="form-control" placeholder="">\n          </div>\n          <div class="form-group col-md-6">\n            <label for="bookdate" class="control-label">Publication Date:</label>\n            <input type="text" id="bookdate" name="bookdate" value="')
        __M_writer(str(config['BookDate']))
        __M_writer('" class="form-control" placeholder="Publication Date (YYYY or YYYY-MM-DD)">\n          </div>\n        </fieldset>\n        <fieldset  class="form-group">\n          <div class="form-group col-md-6"">\n              <label for="bookisbn" class="control-label">ISBN:</label>\n              <input type="text" id="bookisbn" name="bookisbn" value="')
        __M_writer(str(config['BookIsbn']))
        __M_writer('" class="form-control" placeholder="ISBN10 or ISBN13">\n          </div>\n          <div class="form-group col-md-6"">\n              <label for="workid" class="control-label">WorkID:</label>\n              <input type="text" id="workid" name="workid" value="')
        __M_writer(str(config['WorkID']))
        __M_writer('" class="form-control" placeholder="">\n          </div>\n        </fieldset>\n        <div class="form-group">\n')
        loop = __M_loop._enter(seriesdict)
        try:
            for item in loop:
                __M_writer('              <div class="form-group col-md-6">\n                <label for="series[')
                __M_writer(str(loop.index))
                __M_writer('][name]" class="control-label">\n                Book Series ')
                __M_writer(str(loop.index))
                __M_writer('</label>\n                <input type="text" id="series[')
                __M_writer(str(loop.index))
                __M_writer('][name]" name="series[')
                __M_writer(str(loop.index))
                __M_writer('][name]" value="')
                __M_writer(str(item['SeriesName']))
                __M_writer('" class="form-control" placeholder="Series Name">\n              </div>\n              <div class="form-group col-md-6">\n                <label for="series[')
                __M_writer(str(loop.index))
                __M_writer('][number]" class="control-label">&nbsp;</label>\n                <input type="text" id="series[')
                __M_writer(str(loop.index))
                __M_writer('][number]" name="series[')
                __M_writer(str(loop.index))
                __M_writer('][number]" value="')
                __M_writer(str(item['SeriesNum']))
                __M_writer('" class="form-control" placeholder="Number">\n              </div>\n')
        finally:
            loop = __M_loop._exit()
        __M_writer('            <div class="form-group col-md-6">\n            <label for="series[new][name]" class="control-label">\n            New Series </label>\n            <input type="text" id="series[new][name]" name="series[new][name]" value="" class="form-control" placeholder="Series Name">\n            </div>\n            <div class="form-group col-md-6">\n            <label for="series[new][name]" class="control-label">&nbsp;</label>\n            <input type="text" id="series[new][number]" name="series[new][number]" value="" class="form-control" placeholder="Number">\n            </div>\n        </div>\n        <div class="form-group">\n          <!--div><p>')
        __M_writer(str(config['BookDesc']))
        __M_writer('</p></div-->\n          <label for="summernote" class="control-label">Book Description</label>\n          <textarea id="summernote" name="editordata" class="form-control" rows="10" placeholder="Nothing to see here...">')
        __M_writer(str(config['BookDesc']))
        __M_writer('</textarea>\n        </div>\n        <div class="form-group">\n            <table class="display table table-bordered" id="book_table">\n              <thead>\n                <tr>\n')
        for item in covers:
            __M_writer('                  <th class="bookart text-center no-sort">')
            __M_writer(str(item[0]))
            __M_writer('</th>\n')
        __M_writer('                </tr>\n              </thead>\n              <tbody>\n                <tr>\n')
        for item in covers:
            __M_writer('                  <td class="bookart text-center"><a href="')
            __M_writer(str(item[1]))
            __M_writer('" target="_blank" rel="noreferrer"><img src="')
            __M_writer(str(item[1]))
            __M_writer('" alt="cover" class="bookcover-sm"></a><br></td>\n')
        __M_writer('                </tr>\n              </tbody>\n            </table>\n        </div>\n        <div class="form-group">\n            <label for="changeCover" class="control-label">Change cover to: </label>\n            <select id="changeCover" class="changeCover form-control input" name="cover">\n')
        for item in covers:
            __M_writer('                <option value="')
            __M_writer(str(item[0]))
            __M_writer('"\n')
            if item[0] == 'current':
                __M_writer('                    selected = "selected"\n')
            __M_writer('                >')
            __M_writer(str(item[0]))
            __M_writer('</option>\n')
        __M_writer('            </select>\n        </div>\n        <div class="checkbox">\n            ')

        if config['Manual'] == "1":
            checked = 'checked="checked"'
        else:
            checked = ''
                    
        
        __M_writer('\n            <label for="manual" class="control-label">\n            <input type="checkbox" id="manual" name="manual" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n            Lock settings</label>\n        </div>\n        <div class="table_wrapper_button">\n          <input type="submit" value="Save changes" id="add" class="btn btn-primary">\n        </div>\n        <p>&nbsp;</p>\n    </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascriptIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n  <script type="text/javascript">\n    $(document).ready(function() {\n    });\n    function validateForm() {\n        $("#myAlert").removeClass(\'hidden\');\n        document.getElementById("markBooks").submit(); }\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/app/lazylibrarian/data/interfaces/bookstrap/editbook.html", "uri": "editbook.html", "source_encoding": "utf-8", "line_map": {"16": 2, "17": 3, "18": 4, "19": 5, "31": 0, "36": 1, "37": 4, "38": 34, "39": 171, "40": 180, "46": 5, "51": 5, "52": 10, "53": 10, "54": 11, "55": 11, "56": 12, "57": 12, "58": 23, "59": 24, "60": 28, "66": 35, "76": 35, "77": 39, "78": 39, "79": 43, "80": 44, "81": 44, "82": 44, "83": 45, "84": 46, "85": 48, "86": 48, "87": 48, "88": 50, "89": 54, "90": 54, "91": 58, "92": 58, "93": 62, "94": 62, "95": 66, "96": 66, "97": 71, "98": 71, "99": 71, "100": 71, "101": 80, "102": 80, "103": 84, "104": 84, "105": 90, "106": 90, "107": 94, "108": 94, "109": 98, "112": 99, "113": 100, "114": 100, "115": 101, "116": 101, "117": 102, "118": 102, "119": 102, "120": 102, "121": 102, "122": 102, "123": 105, "124": 105, "125": 106, "126": 106, "127": 106, "128": 106, "129": 106, "130": 106, "133": 109, "134": 120, "135": 120, "136": 122, "137": 122, "138": 128, "139": 129, "140": 129, "141": 129, "142": 131, "143": 135, "144": 136, "145": 136, "146": 136, "147": 136, "148": 136, "149": 138, "150": 145, "151": 146, "152": 146, "153": 146, "154": 147, "155": 148, "156": 150, "157": 150, "158": 150, "159": 152, "160": 155, "161": 156, "162": 157, "163": 158, "164": 159, "165": 160, "166": 161, "167": 160, "168": 162, "169": 162, "175": 172, "179": 172, "185": 179}}
__M_END_METADATA
"""
