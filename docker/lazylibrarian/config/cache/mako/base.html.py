# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1616489088.660634
_enable_loop = True
_template_filename = '/app/lazylibrarian/data/interfaces/bookstrap/base.html'
_template_uri = 'base.html'
_source_encoding = 'utf-8'
_exports = ['javascriptIncludes', 'headIncludes', 'headerIncludes']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        title = context.get('title', UNDEFINED)
        next = context.get('next', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        __M_writer = context.writer()

        import lazylibrarian
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['lazylibrarian'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n<!doctype html>\n<html>\n  <head>\n    <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <title>LazyLibrarian - ')
        __M_writer(str(title))
        __M_writer('</title>\n    <meta name="description" content="">\n    <meta name="author" content="">\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <link rel="shortcut icon" type="image/png"  href="images/ll.ico">\n    <link rel="apple-touch-icon" href="images/ll.png">\n    <link rel="manifest" href="images/manifest.json">\n    <link rel="stylesheet" type="text/css" href="css/datatables.min.css"/>\n')
        if lazylibrarian.BOOKSTRAP_THEMELIST:
            __M_writer('    <link id="theme" href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/')
            __M_writer(str(lazylibrarian.CONFIG['BOOKSTRAP_THEME']))
            __M_writer('/bootstrap.min.css" rel="stylesheet">\n')
        else:
            __M_writer('    <link href="css/bootstrap.min.css" rel="stylesheet">\n')
        __M_writer('    <!--link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous"-->\n    <link href="css/fontawesome/fontawesome-all.css" rel="stylesheet">\n    <link href="css/bookstrap.css" rel="stylesheet">\n    <style>\n      input[type="search"]::-webkit-search-cancel-button {\n        -webkit-appearance: searchfield-cancel-button;\n      }\n    </style>\n    <script src="js/jquery-3.4.1.min.js"></script>\n    <script src="js/jquery-migrate-3.1.0.min.js"></script>\n    <script src="js/lazylibrarian-bs.js"></script>\n\n    <!-- include summernote css/js -->\n    <link href="css/summernote.css" rel="stylesheet">\n    <script src="js/summernote.js"></script>\n\n    ')
        __M_writer(str(next.headIncludes()))
        __M_writer('\n    <script type="text/javascript">\n      if(navigator.userAgent.toLowerCase().indexOf(\'firefox\') > -1){\n        // Allow the user to reset the search filter\n        // (-webkit-search-cancel-button does not work on firefox)\n        $(document).ready(function () {\n            $.fn.dataTableExt.oApi.clearSearch = function ( oSettings ) {\n                var table = this;\n                var clearSearch = $(\'<i id="Clear" title="Clear" class="fa fa-times" style="height:20px;width:20px;vertical-align:center;cursor:pointer;">&nbsp;</i>\');\n                $(clearSearch).click( function () {\n                                table.fnFilter(\'\');\n                                $(\'input[type=search]\').val(\'\');\n                });\n                $(oSettings.nTableWrapper).find(\'div.dataTables_filter\').append(clearSearch);\n                $(oSettings.nTableWrapper).find(\'div.dataTables_filter label\').css(\'margin-right\', \'-20px\');\n                $(oSettings.nTableWrapper).find(\'div.dataTables_filter input\').css(\'padding-right\', \'20px\');\n            }\n            //auto-execute, no code needs to be added\n            $.fn.dataTable.models.oSettings[\'aoInitComplete\'].push( {\n                "fn": $.fn.dataTableExt.oApi.clearSearch,\n                "sName": \'whatever\'\n            });\n        });\n      }\n    </script>\n\n    ')
        __M_writer(str(next.javascriptIncludes()))
        __M_writer('\n    <script type="text/javascript">\n      // Check or uncheck all checkboxes in the same table\n      function toggleAll(e) {\n          var table = $(e).closest(\'table\');\n          $(\'td input:checkbox\', table).trigger("click");\n      }\n    </script>\n    <script type="text/javascript" src="js/bootstrap.min.js"></script>\n    <script type="text/javascript" src="js/datatables.min.js"></script>\n    <script type="text/javascript" src="js/natural.js"></script>\n    <script type="text/javascript" src="js/bootbox.min.js"></script>\n    <script type="text/javascript" src="js/bootstrap-notify.min.js"></script>\n<style>\n\n#myBtn {\n  display: none;\n  position: fixed;\n  bottom: 10px;\n  right: 15px;\n  z-index: 99;\n  font-size: 18px;\n  border: none;\n  outline: none;\n  background-color: #888;\n  color: white;\n  cursor: pointer;\n  padding: 6px;\n  border-radius: 4px;\n  opacity: 0.4;\n  filter: alpha(opacity=40); /* For IE8 and earlier */\n}\n\n#myBtn:hover {\n  background-color: #555;\n  opacity: 1.0;\n  filter: alpha(opacity=100); /* For IE8 and earlier */\n}\n#Clear:hover {\n  color: #555;\n  opacity: 1.0;\n  filter: alpha(opacity=100); /* For IE8 and earlier */\n}\n\n#myAlert {\n  display: block;\n  position: fixed;\n  bottom: 48px;\n  right: 15px;\n  z-index: 99;\n  font-size: 14px;\n  border: 2px solid lightgrey;\n  outline: none;\n  background-color: #888;\n  color: white;\n  cursor: pointer;\n  padding: 6px;\n  border-radius: 8px;\n  opacity: 0.4;\n  filter: alpha(opacity=40); /* For IE8 and earlier */\n}\n\n#myAlert:hover {\n  background-color: #555;\n  opacity: 1.0;\n  filter: alpha(opacity=100); /* For IE8 and earlier */\n}\n\n#log_type{\n  min-width: 90px;\n}\n\n#log_label{\n  min-width: 70px;\n}\n@media screen  and (min-width: 768px)and (max-width: 1024px) {\n    /* Add a pseudo element with the\n       text from attribute \'data-abbr\' */\n    .shorten[data-abbr]::after {\n        content: attr(data-abbr);\n    }\n\n    /* Hide the original label */\n    .shorten > span { display: none; }\n}\n</style>\n</head>\n  <body>\n    <div id="container">\n      <header>\n        <div id="headercontainer" class="navbar navbar-default navbar-fixed-top">\n          <div class="container">\n            <div class="navbar-header">\n              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#MainNav" aria-expanded="false">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n              </button>\n              <a class="navbar-brand" href="home"><i class="fa fa-home"></i> LazyLibrarian</a>\n            </div>\n            <div class="collapse navbar-collapse" id="MainNav">\n              <ul class="nav navbar-nav">\n                <!--li><a href="home" class="navbarele">Authors</a></li-->\n')
        if perm > 0:
            if lazylibrarian.CONFIG['USER_ACCOUNTS'] == True:
                if lazylibrarian.SHOWLOGOUT == 1:
                    __M_writer('                      <li><a href="logout" class="navbarele" id="logout">Logout</a></li>\n')
                if perm&lazylibrarian.perm_config == 0:
                    __M_writer('                      <li><a href="profile" class="navbarele" id="profile">User</a></li>\n')
        if lazylibrarian.SHOW_EBOOK:
            if perm&lazylibrarian.perm_ebook:
                __M_writer('                  <li><a id="books" href="books" class="navbarele">eBooks</a></li>\n')
        if lazylibrarian.SHOW_SERIES:
            if perm&lazylibrarian.perm_series:
                __M_writer('                  <li><a id="series" href="series" class="navbarele">Series</a></li>\n')
        if lazylibrarian.SHOW_AUDIO:
            if perm&lazylibrarian.perm_audio:
                __M_writer('                  <li><a id="audio" href="audio" class="navbarele">\n                  <div class="shorten" data-abbr="Audio">\n                      <span>AudioBooks</span>\n                  </div>\n                  </a></li>\n')
        if lazylibrarian.SHOW_MAGS:
            if perm&lazylibrarian.perm_magazines:
                __M_writer('                  <li><a id="magazines" href="magazines" class="navbarele">\n                  <div class="shorten" data-abbr="Mags">\n                      <span>Magazines</span>\n                  </div>\n                  </a></li>\n')
        if lazylibrarian.SHOW_COMICS:
            if perm&lazylibrarian.perm_comics:
                __M_writer('                  <li><a id="comics" href="comics" class="navbarele">Comics</a></li>\n')
        if perm&lazylibrarian.perm_managebooks:
            if lazylibrarian.SHOW_AUDIO:
                __M_writer('                    <li><a id="manage" href="manage" class="navbarele">Manage</a></li>\n')
            elif lazylibrarian.SHOW_EBOOK:
                __M_writer('                    <li><a id="manage" href="manage" class="navbarele">Manage</a></li>\n')
        if perm&lazylibrarian.perm_history:
            __M_writer('                  <li><a id="history" href="history" class="navbarele">History</a></li>\n')
        if perm&lazylibrarian.perm_logs:
            __M_writer('                  <li><a id="logs" href="logs" class="navbarele">Logs</a></li>\n')
        if perm&lazylibrarian.perm_config:
            __M_writer('                  <li><a id="config" href="config" class="navbarcfg"><i class="fa fa-cog"></i> Config</a></li>\n')
        __M_writer('                <li><a id="help" href="help" target="_new"><i class="fa fa-question-circle"></i> Help</a></li>\n              </ul>\n            </div>\n          </div>\n          <div id="subnav" class="navbar-inverse">\n            <div id="subhead" class="container">\n              ')
        __M_writer(str(next.headerIncludes()))
        __M_writer('\n            </div>\n          </div>\n        </div>\n      </header>\n      <div id="main" class="main container">\n        ')
        __M_writer(str(next.body()))
        __M_writer('\n      </div>\n      <button onclick="topFunction()" id="myBtn" title="Go to top"><i class="fa fa-arrow-up"></i></button>\n    </div>\n    <script type="text/javascript">\n      msg = \'\';\n')
        if not lazylibrarian.SUPPRESS_UPDATE:
            if lazylibrarian.CONFIG['INSTALL_TYPE'] == 'git' or lazylibrarian.CONFIG['INSTALL_TYPE'] == 'source':
                __M_writer("          title = 'LazyLibrarian Update'\n")
                if not lazylibrarian.CONFIG['CURRENT_VERSION']:
                    __M_writer('              msg = \'<div class="input-group">You are running an unknown version of lazylibrarian</div><div class="pull-right"><a href="#" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Ignore the message for 24 hours" id="ignoreUpdate">Ignore</a>&nbsp;<a href="update" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Update to the latest release">Update</a></div>\'\n')
                elif (lazylibrarian.CONFIG['INSTALL_TYPE'] == 'source' and lazylibrarian.CONFIG['CURRENT_VERSION'] == 'No Version File' ):
                    __M_writer('              msg = \'<div class="input-group">You are running an unknown version via source install</div><div class="pull-right"><a href="#" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Ignore the message for 24 hours" id="ignoreUpdate">Ignore</a>&nbsp;<a href="update" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Update to the latest release">Update</a></div>\'\n')
                elif lazylibrarian.CONFIG['CURRENT_VERSION'] != lazylibrarian.CONFIG['LATEST_VERSION']:
                    if lazylibrarian.CONFIG['LATEST_VERSION'] == 'Not_Available_From_Git':
                        __M_writer('                  msg = \'<div class="input-group">Unable to get latest version from git</div><div class="pull-right"><a href="#" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Ignore the warning for 24 hours" id="ignoreUpdate">Ignore</a></div>\'\n')
                    elif lazylibrarian.CONFIG['COMMITS_BEHIND'] < 0:
                        __M_writer('                  msg = \'<div class="input-group">Running a local updated version. Push changes to git or rollback to Master release</div><div class="pull-right"><a href="#" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Ignore the warning for 24 hours" id="ignoreUpdate">Ignore</a></div>\'\n')
                    elif lazylibrarian.CONFIG['COMMITS_BEHIND'] > 1:
                        __M_writer('                  msg = \'<div class="input-group">New version available. You are ')
                        __M_writer(str(lazylibrarian.CONFIG['COMMITS_BEHIND']))
                        __M_writer(' commits behind.</div><div class="pull-right"><a href="#" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Ignore the update message for 24 hours" id="ignoreUpdate">Ignore</a>&nbsp;<a href="update" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Update to the latest release" id="doUpdate">Update</a>&nbsp;<button class="btn btn-xs btn-primary" type="button" id="getChangelog">Changes</button></div>\'\n')
                    elif lazylibrarian.CONFIG['COMMITS_BEHIND'] == 1:
                        __M_writer('                  msg = \'<div class="input-group">New version available. You are one commit behind.</div><div class="pull-right"><a href="#" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Ignore the update message for 24 hours" id="ignoreUpdate">Ignore</a>&nbsp;<a href="update" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Update to the latest release" id="doUpdate">Update</a>&nbsp;<button class="btn btn-xs btn-primary" type="button" id="getChangelog">Changes</button></div>\'\n')
        __M_writer('\n      $(document).ready(function() {\n        if (readCookie(\'ignoreUpdate\') != null) { msg = \'\' }\n\n        if (msg != \'\') {\n          $.notify({\n              icon: "images/ll48.png",\n              title: \'<strong>\'+title+\'</strong>\',\n              message: msg\n          },{\n              icon_type: \'image\'\n          },{\n                type: \'warning\'\n            });\n        }\n\n        $(\'#ignoreUpdate\').click(function() {\n            createCookie("ignoreUpdate", true, 1);\n        });\n\n        $(\'#doUpdate\').click(function () {\n            createCookie("ignoreUpdate", true, 0.01);  // suppress popup while updating\n        });\n       $(\'#getChangelog\').on(\'click\', function(e) {\n            $.get(\'checkForUpdates\', function(data) {\n                bootbox.dialog({\n                    title: \'Check Version\',\n                    message: \'<pre>\'+data+\'</pre>\',\n                    buttons: {\n                        primary: {\n                            label: "Close",\n                            className: \'btn-primary\',\n                            callback: function(){ location.reload(true); }\n                        },\n                    }\n                });\n            });\n        });\n      });\n\n      // Initialise tooltips\n      $(function () {\n        $(\'[data-toggle="tooltip"]\').tooltip()\n      })\n\n        function truncateOnWord(str, limit) {\n            var trimmable = \'\\u0009\\u000A\\u000B\\u000C\\u000D\\u0020\\u00A0\\u1680\\u180E\\u2000\\u2001\\u2002\\u2003\\u2004\\u2005\\u2006\\u2007\\u2008\\u2009\\u200A\\u202F\\u205F\\u2028\\u2029\\u3000\\uFEFF\';\n            var reg = new RegExp(\'(?=[\' + trimmable + \'])\');\n            var words = str.split(reg);\n            var count = 0;\n            var result = words.filter(function(word) {\n                count += word.length;\n                return count <= limit;\n            }).join(\'\');\n            if (str.length - result.length <= 4) {return str};\n            return result + \' ...\'\n        }\n\n        // When the user scrolls down 20px from the top of the document, show the button\n        window.onscroll = function() {scrollFunction()};\n\n        function scrollFunction() {\n            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {\n                document.getElementById("myBtn").style.display = "block";\n            } else {\n                document.getElementById("myBtn").style.display = "none";\n            }\n        }\n\n        // When the user clicks on the button, scroll to the top of the document\n        function topFunction() {\n            document.body.scrollTop = 0;\n            document.documentElement.scrollTop = 0;\n        }\n\n      function createCookie(name, value, days) {\n      var expires;\n\n      if (days) {\n          var date = new Date();\n          date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));\n          expires = "; expires=" + date.toGMTString();\n      } else {\n          expires = "";\n      }\n      document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";\n      }\n\n      function readCookie(name) {\n      var nameEQ = encodeURIComponent(name) + "=";\n      var ca = document.cookie.split(\';\');\n      for (var i = 0; i < ca.length; i++) {\n          var c = ca[i];\n          while (c.charAt(0) === \' \') c = c.substring(1, c.length);\n          if (c.indexOf(nameEQ) === 0) return decodeURIComponent(c.substring(nameEQ.length, c.length));\n      }\n      return null;\n      }\n\n      function eraseCookie(name) {\n      createCookie(name, "", -1);\n      }\n\n      function bookinfo(bookid) {\n        $.get(\'bookdesc\', {\'bookid\': bookid},\n        function(data) {\n            var $textAndPic = $(\'<div></div>\');\n            var res = data.split(\'^\');\n            var img = res[0]\n            var title = res[1]\n            var desc = res[2]\n            $textAndPic.append(\'<img src="./\' + img + \'" class="box-shadow img-responsive" />\');\n            $textAndPic.append(\'<br>\' + desc + \' <br />\');\n            bootbox.dialog({\n                size: "large",\n                title: title,\n                message: $textAndPic,\n                buttons: {\n                   primary: {\n                        label: "Close",\n                        className: \'btn-primary\'\n                    }\n                }\n            })\n        })\n      }\n\n    // Read a page\'s GET URL variables and return them as an associative array.\n    function getUrlVars() {\n        var vars = [], hash;\n        var hashes = window.location.href.slice(window.location.href.indexOf(\'?\') + 1).split(\'&\');\n        for(var i = 0; i < hashes.length; i++) {\n            hash = hashes[i].split(\'=\');\n            vars.push(hash[0]);\n            vars[hash[0]] = hash[1];\n        }\n        return vars;\n    }\n    </script>\n  </body>\n</html>\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascriptIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headerIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/app/lazylibrarian/data/interfaces/bookstrap/base.html", "uri": "base.html", "source_encoding": "utf-8", "line_map": {"16": 0, "24": 1, "25": 2, "26": 3, "27": 4, "30": 3, "31": 9, "32": 9, "33": 17, "34": 18, "35": 18, "36": 18, "37": 19, "38": 20, "39": 22, "40": 38, "41": 38, "42": 64, "43": 64, "44": 168, "45": 169, "46": 170, "47": 171, "48": 173, "49": 174, "50": 178, "51": 179, "52": 180, "53": 183, "54": 184, "55": 185, "56": 188, "57": 189, "58": 190, "59": 197, "60": 198, "61": 199, "62": 206, "63": 207, "64": 208, "65": 211, "66": 212, "67": 213, "68": 214, "69": 215, "70": 218, "71": 219, "72": 221, "73": 222, "74": 224, "75": 225, "76": 227, "77": 233, "78": 233, "79": 239, "80": 239, "81": 245, "82": 246, "83": 247, "84": 248, "85": 249, "86": 250, "87": 251, "88": 252, "89": 253, "90": 254, "91": 255, "92": 256, "93": 257, "94": 258, "95": 258, "96": 258, "97": 259, "98": 260, "99": 265, "100": 406, "101": 407, "102": 408, "108": 406, "117": 407, "126": 408, "135": 126}}
__M_END_METADATA
"""
