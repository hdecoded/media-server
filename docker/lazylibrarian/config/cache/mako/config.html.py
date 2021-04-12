# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1616489098.5906043
_enable_loop = True
_template_filename = '/app/lazylibrarian/data/interfaces/bookstrap/config.html'
_template_uri = 'config.html'
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
        __M_writer = context.writer()
        __M_writer('\n<div id="subhead_container">\n    <div id="subhead_menu">\n')
        if lazylibrarian.DOCKER == False:
            __M_writer('        <a onclick="self.shutdownQA(this)" class="button btn btn-sm btn-danger" data-toggle="tooltip" data-placement="bottom" title="Terminate the LazyLibrarian process - Be careful if you\'re doing this remotely"><i class="fa fa-power-off"></i> Shutdown</a>\n')
        __M_writer('      <a class="button btn btn-sm btn-warning" onclick="self.restartQA(this, \'\', \'\')"><i class="fa fa-sync"></i> Restart</a>\n      <button class="button btn btn-sm btn-primary" type="button" value="System Info" id="sysinfo"><i class="fa fa-cogs"></i> System Info</button>\n      <button class="button btn btn-sm btn-primary" type="button" value="Show Jobs" id="show_Jobs"><i class="fa fa-list-ul"></i> Job Status</button>\n      <button class="button btn btn-sm btn-primary" type="button" value="Show Stats" id="show_Stats"><i class="fa fa-list-ul"></i> DB Stats</button>\n      <button class="button btn btn-sm btn-primary" type="button" value="checkforupdates" id="checkforupdates"><i class="fa fa-list-alt"></i> Check Version</button>\n')
        if lazylibrarian.CONFIG['USER_ACCOUNTS'] == True:
            __M_writer('      <a class="button btn btn-sm btn-primary" href="userAdmin"><i class="fa fa-user"></i> User Admin</a>\n')
        if lazylibrarian.CONFIG['BOOK_API'] == "GoodReads":
            __M_writer('      <button class="button btn btn-sm btn-primary" type="button" value="move_to_ol" id="move_to_ol"></i>Move to OpenLibrary</button>\n')
        __M_writer('     <button class="hidden" onclick="" id="myAlert" title=""><i class="fa fa-circle-notch fa-spin"></i> Checking, please wait...</button>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        loop = __M_loop = runtime.LoopStack()
        title = context.get('title', UNDEFINED)
        config = context.get('config', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <!-- ensure the browser sends form-submission data in the UTF-8 encoding,\n       even if the user fiddles with the page encoding -->\n  <form accept-charset="UTF-8" action="configUpdate" method="post">\n<h1>')
        __M_writer(str(title))
        __M_writer('\n    <div class="pull-right table_wrapper_button">\n      <input type="submit" value="Save changes" id="add" class="btn btn-primary">\n    </div>\n</h1>\n    <div role="tab-table" class="hidden">\n      <!-- if the browser is IE and the user switched the page encoding, force utf8 by adding\n      a hidden input to the form with a value such as &#x2713; which can only be from the Unicode charset-->\n      <input name="utf8" type="hidden" value="&#x2713;" />\n      <div>\n        <ul class="nav nav-tabs" role="tablist" id="configtabs">\n        <li role="presentation" id="1" aria-controls="webinterface"><a role="tab" data-toggle="tab" aria-controls="webinterface" href="#webinterface">Interface</a></li>\n        <li role="presentation" id="2" aria-controls="importoptions"><a role="tab" data-toggle="tab" aria-controls="importoptions" href="#importoptions">Importing</a></li>\n        <li role="presentation" id="3" aria-controls="downloadsettings"><a role="tab" data-toggle="tab" aria-controls="downloadsettings" href="#downloadsettings">Downloaders</a></li>\n        <li role="presentation" id="4" aria-controls="providers"><a role="tab" data-toggle="tab" aria-controls="providers" href="#providers">Providers</a></li>\n        <li role="presentation" id="5" aria-controls="searchprocessing"><a role="tab" data-toggle="tab" aria-controls="searchprocessing" href="#searchprocessing">Processing</a></li>\n        <li role="presentation" id="6" aria-controls="notifications"><a role="tab" data-toggle="tab" aria-controls="notifications" href="#notifications">Notifications</a></li>\n        <li role="presentation" id="7" aria-controls="capabilities"><a role="tab" data-toggle="tab" aria-controls="capabilities" href="#capabilities">Categories</a></li>\n        <li role="presentation" id="8" aria-controls="filters"><a role="tab" data-toggle="tab" aria-controls="filters" href="#filters">Filters</a></li>\n')
        if lazylibrarian.CONFIG['SHOW_GENRES'] == True:
            __M_writer('        <li role="presentation" id="9" aria-controls="genres"><a role="tab" data-toggle="tab" aria-controls="genres" href="#genres">Genres</a></li>\n')
        __M_writer('        </ul>\n        <div class="tab-content">\n          <div role="tabpanel" class="tab-pane" id="webinterface">\n            <div class="configtable">\n              <div class="row">\n                <div class="col-md-6">\n                  <fieldset>\n                    <legend>Server Details</legend>\n                    <input type="text" id="current_tab" name="current_tab" value="')
        __M_writer(str(lazylibrarian.CURRENT_TAB))
        __M_writer('" class="hidden">\n                    <div class="input-group">\n                      <label for="http_host" class="input-group-addon">Host</label>\n                      <input type="text" id="http_host" name="http_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['HTTP_HOST']))
        __M_writer('" class="form-control" placeholder="Hostname">\n                      <label for="http_port" class="input-group-addon">Port</label>\n                      <input type="number" id="http_port" name="http_port" value="')
        __M_writer(str(lazylibrarian.CONFIG['HTTP_PORT']))
        __M_writer('" class="form-control" placeholder="Port Number (Default 5299)">\n                    </div>\n                    <div class="input-group">\n                      <label for="http_root" class="input-group-addon">Web Root</label>\n                      <input type="text" id="http_root" name="http_root" value="')
        __M_writer(str(lazylibrarian.CONFIG['HTTP_ROOT']))
        __M_writer('" class="form-control" placeholder="Web Root">\n                    </div>\n                    <div class="input-group">\n                      <label for="user_agent" class="input-group-addon">User Agent</label>\n                      <input type="text" id="user_agent" name="user_agent" value="')
        __M_writer(str(lazylibrarian.CONFIG['USER_AGENT']))
        __M_writer('" class="form-control" placeholder="">\n                    </div>\n                  </fieldset>\n                  <fieldset>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['HTTP_PROXY'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="http_proxy" class="control-label">\n                      <input type="checkbox" id="http_proxy" name="http_proxy" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      HTTP proxy (see wiki)</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['HTTPS_ENABLED'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="https_enabled" class="control-label">\n                        <input type="checkbox" id="https_enabled" name="https_enabled" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        HTTPS access to lazylibrarian</label>\n                    </div>\n                    </div>\n                  </fieldset>\n                    <fieldset id="https_options">\n                      <div class="form-group">\n                        <label for="https_cert" class="control-label">Https Certificate:</label>\n                        <input type="text" id="https_cert" name="https_cert" value="')
        __M_writer(str(lazylibrarian.CONFIG['HTTPS_CERT']))
        __M_writer('" class="form-control" placeholder="https certificate">\n                      </div>\n                      <div class="form-group">\n                        <label for="https_key" class="control-label">Https Key:</label>\n                        <input type="text" id="https_key" name="https_key" value="')
        __M_writer(str(lazylibrarian.CONFIG['HTTPS_KEY']))
        __M_writer('" class="form-control" placeholder="https key">\n                      </div>\n                    </fieldset>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['SSL_VERIFY'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="ssl_verify" class="control-label">\n                        <input type="checkbox" id="ssl_verify" name="ssl_verify" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Verify ssl certificates</label>\n                    </div>\n                    </div>\n                    <fieldset id="ssl_options">\n                      <div class="form-group">\n                        <label for="ssl_certs" class="control-label">SSL Certificates:</label>\n                        <input type="text" id="ssl_certs" name="ssl_certs" value="')
        __M_writer(str(lazylibrarian.CONFIG['SSL_CERTS']))
        __M_writer('" class="form-control" placeholder="leave empty to use requests certificate">\n                      </div>\n                    </fieldset>\n                    <fieldset>\n                      <legend>Logs</legend>\n                      <div class="input-group">\n                        <label for="logdir" id="log_label" class="input-group-addon">Folder</label>\n                        <input type="text" id="logdir" name="logdir" value="')
        __M_writer(str(lazylibrarian.CONFIG['LOGDIR']))
        __M_writer('" class="form-control" placeholder="Log Folder">\n                      </div>\n                      <div class="input-group">\n                        <label for="log_type" id="log_label" class="input-group-addon">Level</label>\n                        <select id="log_type" name="log_type" class="form-control">\n                          ')

        if lazylibrarian.LOGLEVEL == 0:
            selected = 'selected="selected"'
        else:
            selected = ''
                                  
        
        __M_writer('\n                          <option value="Quiet" ')
        __M_writer(str(selected))
        __M_writer('>Quiet</option>\n                          ')

        if lazylibrarian.LOGLEVEL == 1:
            selected = 'selected="selected"'
        else:
            selected = ''
                                  
        
        __M_writer('\n                          <option value="Normal" ')
        __M_writer(str(selected))
        __M_writer('>Normal</option>\n                          ')

        if lazylibrarian.LOGLEVEL > 1:
            selected = 'selected="selected"'
        else:
            selected = ''
                                  
        
        __M_writer('\n                          <option value="Debug" ')
        __M_writer(str(selected))
        __M_writer('>Debug</option>\n                        </select>\n                        <label for="loglimit" class="input-group-addon">Screen Log</label>\n                        <input type="number" id="loglimit" name="loglimit" value="')
        __M_writer(str(lazylibrarian.CONFIG['LOGLIMIT']))
        __M_writer('" class="form-control" placeholder="Number of lines">\n                      </div>\n                      <div class="input-group">\n                        <label for="logfiles" id="log_label" class="input-group-addon">Files</label>\n                        <input type="number" id="logfiles" name="logfiles" value="')
        __M_writer(str(lazylibrarian.CONFIG['LOGFILES']))
        __M_writer('" class="form-control" placeholder="Number of files">\n                        <label for="logsize" class="input-group-addon">File Size</label>\n                        <input type="number" id="logsize" name="logsize" value="')
        __M_writer(str(lazylibrarian.CONFIG['LOGSIZE']))
        __M_writer('" class="form-control" placeholder="Log File Size">\n                      </div>\n')
        if lazylibrarian.LOGLEVEL > 1:
            __M_writer('                      <br>\n                      <fieldset id=debug_options>\n                      <legend>Detailed Debug Options</legend>\n                      <div class="row checkbox">\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_matching:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_matching" class="control-label">\n                          <input type="checkbox" id="log_matching" name="log_matching" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Name Matching</label>\n                        </div>\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_searching:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_searching" class="control-label">\n                          <input type="checkbox" id="log_searching" name="log_searching" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Search Results</label>\n                        </div>\n                      </div>\n                      <div class="row checkbox">\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_dlcomms:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_dlcomms" class="control-label">\n                          <input type="checkbox" id="log_dlcomms" name="log_dlcomms" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Downloader Messages</label>\n                        </div>\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_dbcomms:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_dbcomms" class="control-label">\n                          <input type="checkbox" id="log_dbcomms" name="log_dbcomms" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Database Commands</label>\n                        </div>\n                      </div>\n                      <div class="row checkbox">\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_postprocess:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_postprocess" class="control-label">\n                          <input type="checkbox" id="log_postprocess" name="log_postprocess" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          PostProcessor</label>\n                        </div>\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_fuzz:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_fuzz" class="control-label">\n                          <input type="checkbox" id="log_fuzz" name="log_fuzz" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Fuzzy Matching</label>\n                        </div>\n                      </div>\n                      <div class="row checkbox">\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_serverside:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_serverside" class="control-label">\n                          <input type="checkbox" id="log_serverside" name="log_serverside" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Serverside Processing</label>\n                        </div>\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_fileperms:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_fileperms" class="control-label">\n                          <input type="checkbox" id="log_fileperms" name="log_fileperms" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          File Permissions</label>\n                        </div>\n                      </div>\n                      <div class="row checkbox">\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_grsync:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_grsync" class="control-label">\n                          <input type="checkbox" id="log_grsync" name="log_grsync" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Goodreads Sync</label>\n                        </div>\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_cache:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_cache" class="control-label">\n                          <input type="checkbox" id="log_cache" name="log_cache" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Caching</label>\n                        </div>\n                      </div>\n                      <div class="row checkbox">\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_libsync:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_libsync" class="control-label">\n                          <input type="checkbox" id="log_libsync" name="log_libsync" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Library Scan</label>\n                        </div>\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_admin:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_admin" class="control-label">\n                          <input type="checkbox" id="log_admin" name="log_admin" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Admin Messages</label>\n                        </div>\n                      </div>\n                      <div class="row checkbox">\n                        <div class="col-md-6">\n                          ')

            if lazylibrarian.LOGLEVEL & lazylibrarian.log_cherrypy:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="log_cherrypy" class="control-label">\n                          <input type="checkbox" id="log_cherrypy" name="log_cherrypy" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Cherrypy Logging (needs restart)</label>\n                        </div>\n                      </div>\n')
        __M_writer('                    </fieldset>\n                  </fieldset>\n                  <br>\n                  <fieldset>\n                    <legend>Proxy Details</legend>\n                    <div class="form-group">\n                      <label for="proxy_host" class="control-label">Proxy Host:</label>\n                      <input type="text" id="proxy_host" name="proxy_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['PROXY_HOST']))
        __M_writer('" class="form-control" placeholder="Proxy Host">\n                    </div>\n                    <div class="form-group">\n                      <label for="proxy_type" class="control-label">Proxy Type:</label>\n                      <input type="text" id="proxy_type" name="proxy_type" value="')
        __M_writer(str(lazylibrarian.CONFIG['PROXY_TYPE']))
        __M_writer('" class="form-control" placeholder="Proxy Types">\n                      <span class="help-block">Comma separated list http, https, etc</span>\n                    </div>\n                  </fieldset>\n                    <fieldset id=rss_options>\n                    <legend>RSS Server</legend>\n                        <div class="checkbox">\n                          ')

        if lazylibrarian.CONFIG['RSS_ENABLED'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                  
        
        __M_writer('\n                          <label for="rss_enabled" title="Provide RSS feeds">\n                          <input type="checkbox" id="rss_enabled" name="rss_enabled" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Enable RSS</label>\n                        </div>\n                        <fieldset id="rssoptions">\n                            <div class="input-group col-md-6">\n                            <span class="input-group-addon">RSS Host/Port</span>\n                            <input type="text" id="rss_host" name="rss_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['RSS_HOST']))
        __M_writer('" class="form-control" placeholder="mywebsite.org:port">\n                            </div>\n                            <span class="help-block">Use if you need to override rss link address</span>\n')
        if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
            __M_writer('                        <div class="checkbox">\n                          ')

            if lazylibrarian.CONFIG['RSS_PODCAST'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
                                      
            
            __M_writer('\n                          <label for="rss_podcast" title="Send audiobook RSS feeds as podcasts">\n                          <input type="checkbox" id="rss_podcast" name="rss_podcast" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Send AudioBook RSS as Podcasts</label>\n                        </div>\n')
        __M_writer('                        </fieldset>\n                    </fieldset>\n                    <fieldset>\n                    <legend>OPDS Server</legend>\n                        <div class="checkbox">\n                          ')

        if lazylibrarian.CONFIG['OPDS_ENABLED'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                  
        
        __M_writer('\n                          <label for="opds_enabled" title="Allow remote applications to interface with LazyLibrarian">\n                          <input type="checkbox" id="opds_enabled" name="opds_enabled" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Enable OPDS</label>\n                        </div>\n                        <small>Enabling/Disabling OPDS or changing credentials requires restart</small><br>\n                        <fieldset id="opdsoptions">\n                            <div class="checkbox">\n                              ')

        if lazylibrarian.CONFIG['OPDS_AUTHENTICATION'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                      
        
        __M_writer('\n                              <label for="opds_authentication" title="OPDS requires username and password">\n                              <input type="checkbox" id="opds_authentication" name="opds_authentication" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                              OPDS Requires Credentials</label>\n                            </div>\n                            <div id="opdscredentials">\n                              <small>If the user/pass below are blank the webserver user/pass will be used</small>\n                              <div class="input-group">\n                                <label for="opds_username" class="input-group-addon">User</label>\n                                <input type="text" id="opds_username" name="opds_username" value="')
        __M_writer(str(lazylibrarian.CONFIG['OPDS_USERNAME']))
        __M_writer('" class="form-control" placeholder="Username">\n                                <label for="opds_password" class="input-group-addon">Pass</label>\n                                <input type="password" id="opds_password" name="opds_password" value="')
        __M_writer(str(lazylibrarian.CONFIG['OPDS_PASSWORD']))
        __M_writer('" class="form-control" placeholder="Password">\n                              </div>\n                              <small>NOTE - some OPDS readers do not send authentication for cover images or searches, so we don\'t send them. If you are getting lists with no images try disabling authentication or upgrading your reader</small>\n                            </div>\n                            <div class="checkbox">\n                              ')

        if lazylibrarian.CONFIG['OPDS_METAINFO'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                      
        
        __M_writer('\n                              <label for="opds_metainfo" title="OPDS extra metainfo">\n                              <input type="checkbox" id="opds_metainfo" name="opds_metainfo" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                              OPDS Include MetaInfo</label><br><small>This will include book summary, cover, author details</small>\n                            </div>\n                            <div class="input-group col-md-6">\n                            <label for="opds_page" class="input-group-addon">Page Size</label>\n                            <input type="number" id="opds_page" name="opds_page" value="')
        __M_writer(str(lazylibrarian.CONFIG['OPDS_PAGE']))
        __M_writer('" class="form-control" placeholder="Page Size">\n                            </div>\n                        </fieldset>\n                    </fieldset>\n                </div>\n                <div class="col-md-6">\n                  <fieldset>\n                    <legend>Access Control</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['USER_ACCOUNTS'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="user_accounts" title="User accounts">\n                      <input type="checkbox" id="user_accounts" name="user_accounts" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Enable user accounts</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['SINGLE_USER'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="single_user" title="Bypass login">\n                      <input type="checkbox" id="single_user" name="single_user" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Single user bypass login</label>\n                    </div>\n                    </div>\n                  </fieldset>\n                  <fieldset>\n                    <fieldset id="admin_options">\n                    <div class="form-group">\n                      <label for="admin_email" class="control-label">Contact Email:</label>\n                      <input type="text" id="admin_email" name="admin_email" value="')
        __M_writer(str(lazylibrarian.CONFIG['ADMIN_EMAIL']))
        __M_writer('" class="form-control" placeholder="Contact email for requests/registration">\n                    </div>\n                    </fieldset>\n                    <fieldset id="webserver_options">\n                    WebServer Options:\n                    <div class="input-group">\n                      <label for="http_user" class="input-group-addon">User</label>\n                      <input type="text" id="http_user" name="http_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['HTTP_USER']))
        __M_writer('" class="form-control" placeholder="Username">\n                      <label for="http_pass" class="input-group-addon">Pass</label>\n                      <input type="password" id="http_pass" name="http_pass" value="')
        __M_writer(str(lazylibrarian.CONFIG['HTTP_PASS']))
        __M_writer('" class="form-control" placeholder="Password">\n                    </div>\n                    <legend>Authentication</legend>\n                    <div class="input-group col-md-6">\n                      <label for="auth_type" class="input-group-addon">Auth Type:</label>\n                      <select id="auth_type" name="auth_type" class="form-control">\n                        ')

        if lazylibrarian.CONFIG['AUTH_TYPE'] == 'BASIC':
            selected = 'selected="selected"'
        else:
            selected = ''
        
        
        __M_writer('\n                        <option value="BASIC" ')
        __M_writer(str(selected))
        __M_writer('>Basic (Browser Popup)</option>\n                        ')

        if lazylibrarian.CONFIG['AUTH_TYPE'] == 'FORM':
            selected = 'selected="selected"'
        else:
            selected = ''
        
        
        __M_writer('\n                        <option value="FORM" ')
        __M_writer(str(selected))
        __M_writer('>Form (Login Page)</option>\n                      </select>\n                    </div>\n\n                    </fieldset>\n                    <small>Enabling/Disabling user accounts or changing webserver user/pass requires restart<br></small>\n                  </fieldset>\n                  <fieldset>\n                    <legend>Startup</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['LAUNCH_BROWSER'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="launch_browser" class="control-label">\n                      <input type="checkbox" id="launch_browser" name="launch_browser" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Launch browser</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['API_ENABLED'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="api_enabled" title="Allow remote applications to interface with LazyLibrarian">\n                      <input type="checkbox" id="api_enabled" name="api_enabled" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Enable API</label>\n                    </div>\n                    </div>\n                  </fieldset>\n                  <fieldset>\n                    <fieldset id="api_options">\n                      <div class="form-group">\n                        <label for="api_key">API key</label>\n                        <input type="text" name="api_key" id="api_key" value="')
        __M_writer(str(lazylibrarian.CONFIG['API_KEY']))
        __M_writer('" size="36">\n                        <input class="button btn btn-sm btn-primary" type="button" value="Generate" id="generateAPI" onClick="document.location.reload(true)">\n                        <br>\n                        <small>Current API key: <strong>')
        __M_writer(str(lazylibrarian.CONFIG['API_KEY']))
        __M_writer('</strong></small>\n                      </div>\n                    </fieldset>\n                  </fieldset>\n                  <fieldset>\n                    <legend>Appearance</legend>\n                    <div class="form-group">\n                      <label for="http_look">Interface:</label>\n                      <select id="http_look" name="http_look" class="form-control">\n')
        for http_look in config['http_look_list']:
            __M_writer('                        ')

            if http_look == lazylibrarian.CONFIG['HTTP_LOOK']:
                selected = 'selected="selected"'
            else:
                selected = ''
            
            
            __M_writer('\n                        <option value="')
            __M_writer(str(http_look))
            __M_writer('" ')
            __M_writer(str(selected))
            __M_writer('>')
            __M_writer(str(http_look))
            __M_writer('</option>\n')
        __M_writer('                      </select>\n                    </div>\n                    <div class="checkbox hidden"> <!-- Not really required? -->\n                      <label for="bookstrap" class="control-label">\n                        <input type="checkbox" name="use_bookstrap" id="bookstrap" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Use Bookstrap</label>\n                    </div>\n                    <fieldset id="bookstrap_options">\n                      <div class="form_group">\n                        <label for="bookstrap_theme" class="control-label">Bootswatch Theme:</label>\n                        <select name="bookstrap_theme" id="bookstrap_theme" class="form-control">\n')
        for bookstrap_theme in lazylibrarian.BOOKSTRAP_THEMELIST:
            __M_writer('                          ')

            if bookstrap_theme == lazylibrarian.CONFIG['BOOKSTRAP_THEME']:
                selected = 'selected="selected"'
            else:
                selected = ''
                                      
            
            __M_writer('\n                          <option value="')
            __M_writer(str(bookstrap_theme))
            __M_writer('" ')
            __M_writer(str(selected))
            __M_writer('>')
            __M_writer(str(bookstrap_theme))
            __M_writer('</option>\n')
        __M_writer('                        </select>\n                      </div>\n                    </fieldset>\n                    <div class="row checkbox">\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['AUTHOR_IMG'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="author_img" class="control-label">\n                        <input type="checkbox" id="author_img" name="author_img" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Show Author Images</label>\n                      </div>\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['BOOK_IMG'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="book_img" class="control-label">\n                        <input type="checkbox" id="book_img" name="book_img" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Show Book Images</label>\n                      </div>\n                    </div>\n                    <div class="row checkbox">\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['EBOOK_TAB'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="ebook_tab" class="control-label">\n                          <input type="checkbox" id="ebook_tab" name="ebook_tab" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Show eBooks</label>\n                      </div>\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="audio_tab" class="control-label">\n                          <input type="checkbox" id="audio_tab" name="audio_tab" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Show AudioBooks</label>\n                      </div>\n                    </div>\n                    <div class="row checkbox">\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['MAG_TAB'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="mag_tab" class="control-label">\n                          <input type="checkbox" id="mag_tab" name="mag_tab" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Show Magazines</label>\n                      </div>\n')
        if lazylibrarian.CONFIG['MAG_TAB'] == True:
            __M_writer('                      <div class="col-md-6">\n                        ')

            if lazylibrarian.CONFIG['MAG_IMG'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
                                    
            
            __M_writer('\n                        <label for="mag_img" class="control-label">\n                          <input type="checkbox" id="mag_img" name="mag_img" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Show Magazine Images</label>\n                      </div>\n')
        __M_writer('                    </div>\n                    <div class="row checkbox">\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['COMIC_TAB'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="comic_tab" class="control-label">\n                          <input type="checkbox" id="comic_tab" name="comic_tab" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Show Comics</label>\n                      </div>\n')
        if lazylibrarian.CONFIG['COMIC_TAB'] == True:
            __M_writer('                      <div class="col-md-6">\n                        ')

            if lazylibrarian.CONFIG['COMIC_IMG'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
                                    
            
            __M_writer('\n                        <label for="comic_img" class="control-label">\n                          <input type="checkbox" id="comic_img" name="comic_img" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Show Comic Images</label>\n                      </div>\n')
        __M_writer('                    </div>\n                    <div class="row checkbox">\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['SERIES_TAB'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="series_tab" class="control-label">\n                          <input type="checkbox" id="series_tab" name="series_tab" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Show Series</label>\n                      </div>\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['RATESTARS'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="ratestars" class="control-label">\n                          <input type="checkbox" id="ratestars" name="ratestars" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Show rating as stars</label>\n                      </div>\n                    </div>\n                    <div class="row checkbox">\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['TOGGLES'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="toggles" class="control-label">\n                          <input type="checkbox" id="toggles" name="toggles" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Show column toggles</label>\n                      </div>\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['SORT_SURNAME'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="sort_surname" class="control-label">\n                          <input type="checkbox" id="sort_surname" name="sort_surname" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Show author surname first</label>\n                      </div>\n                    </div>\n                    <div class="row checkbox">\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['SHOW_GENRES'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="show_genres" class="control-label">\n                          <input type="checkbox" id="show_genres" name="show_genres" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Show genres</label>\n                      </div>\n')
        if lazylibrarian.APPRISE and lazylibrarian.APPRISE[0].isdigit():
            __M_writer('                      <div class="col-md-6">\n                        ')

            if lazylibrarian.CONFIG['HIDE_OLD_NOTIFIERS'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
                                    
            
            __M_writer('\n                        <label for="hide_old_notifiers" class="control-label">\n                          <input type="checkbox" id="hide_old_notifiers" name="hide_old_notifiers" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                          Hide old notifiers</label>\n                      </div>\n                    </div>\n                    <div class="row checkbox">\n')
        __M_writer('                      <div class="col-md-12">\n                      ')

        if lazylibrarian.CONFIG['SORT_DEFINITE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="sort_definite" class="control-label">\n                        <input type="checkbox" id="sort_definite" name="sort_definite" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Show titles ignoring definite article (The, A)</label>\n                      </div>\n                      <div class="col-md-12">\n                      ')

        if lazylibrarian.CONFIG['IGNORE_PAUSED'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="ignore_paused" class="control-label">\n                        <input type="checkbox" id="ignore_paused" name="ignore_paused" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Ignore paused authors</label>\n                      </div>\n                    </div>\n                  </fieldset>\n                </div>\n              </div>\n            </div>\n          </div> <!-- end of web interface tab panel -->\n          <div role="tabpanel" class="tab-pane" id="importoptions">\n            <div class="configtable">\n              <div class="row">\n                <div class="col-md-4">\n                <fieldset>\n                  <legend>Information Sources</legend>\n                  <div class="form-group">\n                    ')

        if lazylibrarian.CONFIG['BOOK_API'] == "GoodReads":
            gr_selected = 'selected="selected"'
            gb_selected = ''
            ol_selected = ''
        elif lazylibrarian.CONFIG['BOOK_API'] == "GoogleBooks":
            gr_selected = ''
            gb_selected = 'selected="selected"'
            ol_selected = ''
        elif lazylibrarian.CONFIG['BOOK_API'] == "OpenLibrary":
            gr_selected = ''
            gb_selected = ''
            ol_selected = 'selected="selected"'
        
        
        __M_writer('\n                    <label for="book_api" class="control-label">Book Information</label>\n                    <select id="book_api" name="book_api" class="form-control">\n                      <option value = "GoodReads" ')
        __M_writer(str(gr_selected))
        __M_writer('>GoodReads</option>\n                      <option value = "GoogleBooks" ')
        __M_writer(str(gb_selected))
        __M_writer('>GoogleBooks</option>\n                      <option value = "OpenLibrary" ')
        __M_writer(str(ol_selected))
        __M_writer('>OpenLibrary</option>\n                    </select>\n                  </div>\n                  <fieldset id="gb_options">\n                  <div class="form-group">\n                    <label for="gb_api" class="control-label">GoogleBooks API:</label>\n                    <input type="text" id="gb_api" name="gb_api" value="')
        __M_writer(str(lazylibrarian.CONFIG['GB_API']))
        __M_writer('" class="form-control">\n                  </div>\n                  <div class="form-group">\n                    <label for="gb_country" class="control-label">GoogleBooks Country:</label>\n                    <input type="text" id="gb_country" name="gb_country" value="')
        __M_writer(str(lazylibrarian.CONFIG['GB_COUNTRY']))
        __M_writer('" class="form-control">\n                    <span class="help-block">Two letter country code for geographically restricted content e.g: US GB ES</span>\n                  </div>\n                  </fieldset>\n                  <fieldset id="gr_options">\n                  <div class="form-group">\n                    <label for="gr_api">Goodreads API:</label>\n                    <input type="text" id="gr_api" name="gr_api" value="')
        __M_writer(str(lazylibrarian.CONFIG['GR_API']))
        __M_writer('" class="form-control"     placeholder="Goodreads API">\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['GR_SYNC'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="gr_sync" class="control-label">\n                        <input type="checkbox" id="gr_sync" name="gr_sync" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Enable GoodReads Sync</label>\n                    </div>\n                    <fieldset id="grsync_options">\n                      <div class="checkbox">\n                        ')

        if lazylibrarian.CONFIG['GR_SYNCREADONLY'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="gr_syncreadonly" class="control-label">\n                          <input type="checkbox" id="gr_syncreadonly" name="gr_syncreadonly" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Use GoodReads shelves as read-only</label>\n                      </div>\n                      <label for="gr_secret">Goodreads Secret:</label>\n                      <input type="text" id="gr_secret" name="gr_secret" value="')
        __M_writer(str(lazylibrarian.CONFIG['GR_SECRET']))
        __M_writer('" class="form-control">\n                      <label for="gr_oauth_token">Goodreads OAuth Token:</label>\n                      <input type="text" id="gr_oauth_token" name="gr_oauth_token" value="')
        __M_writer(str(lazylibrarian.CONFIG['GR_OAUTH_TOKEN']))
        __M_writer('" class="form-control">\n                      <label for="gr_oauth_secret">Goodreads OAuth Secret:</label>\n                      <input type="text" id="gr_oauth_secret" name="gr_oauth_secret" value="')
        __M_writer(str(lazylibrarian.CONFIG['GR_OAUTH_SECRET']))
        __M_writer('" class="form-control">\n                      <div class="checkbox">\n                        ')

        if lazylibrarian.CONFIG['GR_SYNCUSER'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="GR_SYNCUSER" class="control-label">\n                          <input type="checkbox" id="gr_syncuser" name="gr_syncuser" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Use GoodReads shelves as user reading list\n')
        if not lazylibrarian.CONFIG['USER_ACCOUNTS']:
            __M_writer('                           <p>(enable USER_ACCOUNTS to get user ID)\n')
        __M_writer('                        </label>\n                      </div>\n                      <fieldset id="gruser_options">\n                      <label for="gr_user">UserID to sync:</label>\n                        <input type="text" id="gr_user" name="gr_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['GR_USER']))
        __M_writer('" class="form-control">\n                        </fieldset>\n                      <fieldset id="grlibrary_options">\n')
        if lazylibrarian.CONFIG['EBOOK_TAB'] == True:
            __M_writer('                      <label for="gr_wanted">Sync Wanted eBooks to Goodreads shelf:</label>\n                      <input type="text" id="gr_wanted" name="gr_wanted" value="')
            __M_writer(str(lazylibrarian.CONFIG['GR_WANTED']))
            __M_writer('" class="form-control" placeholder="eg: to-read">\n                      <label for="gr_owned">Sync Owned eBooks to Goodreads shelf:</label>\n                      <input type="text" id="gr_owned" name="gr_owned" value="')
            __M_writer(str(lazylibrarian.CONFIG['GR_OWNED']))
            __M_writer('" class="form-control" placeholder="eg: owned">\n')
        if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
            __M_writer('                      <fieldset id="graudio_options">\n                        <label for="gr_awanted">Sync Wanted AudioBooks to Goodreads shelf:</label>\n                        <input type="text" id="gr_awanted" name="gr_awanted" value="')
            __M_writer(str(lazylibrarian.CONFIG['GR_AWANTED']))
            __M_writer('" class="form-control" placeholder="eg: audio_wanted">\n                        <label for="gr_owned">Sync Owned AudioBooks to Goodreads shelf:</label>\n                        <input type="text" id="gr_aowned" name="gr_aowned" value="')
            __M_writer(str(lazylibrarian.CONFIG['GR_AOWNED']))
            __M_writer(' "class="form-control" placeholder="eg: audio_owned">\n                      </fieldset>\n')
        __M_writer('                        <div class="checkbox">\n                          ')

        if lazylibrarian.CONFIG['GR_UNIQUE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                  
        
        __M_writer('\n                          <label for="gr_unique" class="control-label">\n                            <input type="checkbox" id="gr_unique" name="gr_unique" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                            Delete from GoodReads Wanted shelf if also on Open/Have shelf</label>\n                        </div>\n                      </fieldset>\n                      <div class="form-group">\n                        <label for="goodreads_interval" class="control-label">Goodreads Sync Interval:</label>\n                        <div class="input-group">\n                          <input type="number" id="goodreads_interval" name="goodreads_interval" value="')
        __M_writer(str(lazylibrarian.CONFIG['GOODREADS_INTERVAL']))
        __M_writer('" class="form-control" placeholder="Goodreads Sync interval (hours)" >\n                          <span class="input-group-addon">Hours</span>\n                        </div>\n                      </div>\n                      <div class="form-group">\n                        <input type="button" value="Request oAuth1" id="grauthStep1" class="btn btn-default" />\n                        <input type="button" value="Request oAuth2" id="grauthStep2" class="btn btn-default" />\n                      </div>\n                      <div class="form-group">\n                        <input type="button" value="Test Authorization" id="testgrauth" class="btn btn-default" />\n                      </div>\n                    </fieldset>\n                  </div>\n                  </fieldset>\n                  <div class="form-group">\n                    <label for="lt_devkey" class="control-label">LibraryThing Developer Key:</label>\n                    <input type="text" id="lt_devkey" name="lt_devkey" value="')
        __M_writer(str(lazylibrarian.CONFIG['LT_DEVKEY']))
        __M_writer('" class="form-control" placeholder="optional, for book covers">\n                  </div>\n                </fieldset>\n                <fieldset>\n')
        if lazylibrarian.CONFIG['COMIC_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="cv_apikey" class="control-label">ComicVine Api Key:</label>\n                    <input type="text" id="cv_apikey" name="cv_apikey" value="')
            __M_writer(str(lazylibrarian.CONFIG['CV_APIKEY']))
            __M_writer('" class="form-control" placeholder="optional">\n                  </div>\n                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['CV_WEBSEARCH'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                    <label for="cv_websearch">\n                      <input type="checkbox" id="cv_websearch" name="cv_websearch" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Try web search if api returns no results<br><small>WARNING this may get your api key blocked</small></label>\n                  </div>\n')
        __M_writer('                </fieldset>\n              </div>\n              <div class="col-md-4">\n                <fieldset>\n                  <legend>File Formats</legend>\n')
        if lazylibrarian.CONFIG['EBOOK_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="ebook_type" class="control-label">eBooks:</label>\n                    <input type="text" id="ebook_type" name="ebook_type" value="')
            __M_writer(str(lazylibrarian.CONFIG['EBOOK_TYPE']))
            __M_writer('" class="form-control" placeholder="eBook file formats">\n                    <span class="help-block">Comma separated file extensions</span>\n                  </div>\n')
        if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="audiobook_type" class="control-label">AudioBooks:</label>\n                    <input type="text" id="audiobook_type" name="audiobook_type" value="')
            __M_writer(str(lazylibrarian.CONFIG['AUDIOBOOK_TYPE']))
            __M_writer('" class="form-control" placeholder="AudioBook file formats">\n                    <span class="help-block">Comma separated file extensions</span>\n                  </div>\n')
        if lazylibrarian.CONFIG['MAG_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="mag_type" class="control-label">Magazines:</label>\n                    <input type="text" id="mag_type" name="mag_type" value="')
            __M_writer(str(lazylibrarian.CONFIG['MAG_TYPE']))
            __M_writer('" class="form-control"       placeholder="Magazine file formats">\n                    <span class="help-block">Comma separated file extensions</span>\n                  </div>\n')
        if lazylibrarian.CONFIG['COMIC_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="mag_type" class="control-label">Comics:</label>\n                    <input type="text" id="comic_type" name="comic_type" value="')
            __M_writer(str(lazylibrarian.CONFIG['COMIC_TYPE']))
            __M_writer('" class="form-control"       placeholder="Comic file formats">\n                    <span class="help-block">Comma separated file extensions</span>\n                  </div>\n')
        __M_writer('                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['NO_FUTURE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="no_future">\n                      <input type="checkbox" id="no_future" name="no_future" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Ignore books with future publication date</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['NO_PUBDATE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="no_pubdate">\n                      <input type="checkbox" id="no_pubdate" name="no_pubdate" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Ignore books with unknown publication date</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['NO_ISBN'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="no_isbn">\n                      <input type="checkbox" id="no_isbn" name="no_isbn" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Ignore books with no isbn</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['NO_SETS'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="no_sets">\n                      <input type="checkbox" id="no_sets" name="no_sets" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Ignore part books and sets</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['NO_LANG'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="no_lang">\n                      <input type="checkbox" id="no_lang" name="no_lang" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Treat invalid language as ignored</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_IGNORE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="imp_ignore">\n                      <input type="checkbox" id="imp_ignore" name="imp_ignore" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Add ignored books to database (marked Ignored)</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_GOOGLEIMAGE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="imp_googleimage">\n                      <input type="checkbox" id="imp_googleimage" name="imp_googleimage" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Try google image search as final option for missing book covers</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['DELETE_CSV'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="delete_csv">\n                      <input type="checkbox" id="delete_csv" name="delete_csv" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Delete csv file or wishlist after successful import</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['BLACKLIST_FAILED'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="blacklist_failed">\n                      <input type="checkbox" id="blacklist_failed" name="blacklist_failed" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Blacklist failed downloads in history table</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['BLACKLIST_PROCESSED'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="blacklist_processed">\n                      <input type="checkbox" id="blacklist_processed" name="blacklist_processed" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Blacklist processed downloads in history table</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['DELAYSEARCH'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="delaysearch">\n                      <input type="checkbox" id="delaysearch" name="delaysearch" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Increase delay for previously failed searches</label>\n                  </div>\n                </fieldset>\n              </div>\n              <div class="col-md-4">\n                <fieldset>\n                  <legend>Language</legend>\n                  <div class="form-group">\n                    <label for="imp_preflang" class="control-label">Import languages:</label>\n                    <input type="text" id="imp_preflang" name="imp_preflang" value="')
        __M_writer(str(lazylibrarian.CONFIG['IMP_PREFLANG']))
        __M_writer('" class="form-control" placeholder="Import Languages">\n                    <span class="help-block">Comma separated country shortcodes:<br/>\n                      GoodReads e.g: eng, en-US, spa, ita<br/>\n                      GoogleBooks e.g: en, es, it<br/>\n                      Default: en, eng, en-US<br/>\n                      Try adding "Unknown" to list if GoodReads is missing results, or "All" if you don\'t want to check for language</span>\n                  </div>\n                  <div class="form-group">\n                    <label for="imp_monthlang" class="control=label">Languages for month names:</label>\n                    <input type="text" id="imp_monthlang" name="imp_monthlang" value="')
        __M_writer(str(lazylibrarian.CONFIG['IMP_MONTHLANG']))
        __M_writer('" class="form-control" placeholder="Languages for month names">\n                    <span class="help-block">Comma separated language codes for magazine issues:<br/>\n                      e.g: fr_FR.utf8, es_ES.utf8<br/>\n                      English month names are preloaded<br/>Changes to this setting require a restart</span>\n                  </div>\n                  <legend>Date Formats</legend>\n                    <div class="row">\n                   <div class="col-md-6">\n                    <label for="date_format" class="control=label">Added Dates:</label>\n                    <input type="text" id="date_format" name="date_format" value="')
        __M_writer(str(lazylibrarian.CONFIG['DATE_FORMAT']))
        __M_writer('" class="form-control" placeholder="Format for column dates">\n                   </div>\n                   <div class="col-md-6">\n                    <label for="iss_format" class="control=label">Issue Dates:</label>\n                    <input type="text" id="iss_format" name="iss_format" value="')
        __M_writer(str(lazylibrarian.CONFIG['ISS_FORMAT']))
        __M_writer('" class="form-control" placeholder="Format for issue dates">\n                  </div>\n                  </div>\n                  <span class="help-block">$d Day of the month as a number<br>$b Month as abbreviated name<br>$B Month as full name<br>$m Month as a number<br>$y\tYear without century<br>$Y\tYear with century<br>eg $Y-$m-$d</span>\n                </fieldset>\n              </div>\n            </div>\n          </div>\n        </div>\n        <div role="tabpanel" class="tab-pane" id="downloadsettings">\n          <div class="configtable">\n            <div class="row">\n              <div class="col-md-6">\n                <fieldset>\n                  <legend>Usenet</legend>\n                  <fieldset class="usenet_options">\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['NZB_DOWNLOADER_SABNZBD'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="nzb_downloader_sabnzbd" class="control-label">\n                        <input type="checkbox" id="nzb_downloader_sabnzbd" name="nzb_downloader_sabnzbd" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Use Sabnzbd+</label>\n                    </div>\n                    <fieldset id="sabnzbd_options">\n                      <legend>SABnzbd+</legend>\n                      <div class="row">\n                        <div class="form-group col-md-8">\n                          <label for="sab_host" class="control-label">SABnzbd Host:</label>\n                          <input type="text" id="sab_host" name="sab_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['SAB_HOST']))
        __M_writer('" class="form-control" placeholder="SABnzbd Host">\n                        </div>\n                        <div class="form-group col-md-4">\n                          <label for="sab_port" class="control-label">SABnzbd Port:</label>\n                          <input type="number" id="sab_port" name="sab_port" value="')
        __M_writer(str(lazylibrarian.CONFIG['SAB_PORT']))
        __M_writer('" class="form-control"     placeholder="SABnzbd Port">\n                        </div>\n                      </div>\n                      <div class="row">\n                        <div class="form-group col-md-6">\n                          <label for="sab_user">SABnzbd Username</label>\n                          <input type="text" id="sab_user" name="sab_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['SAB_USER']))
        __M_writer('" class="form-control" placeholder="SABnzbd Username">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="sab_pass" class="control-label">SABnzbd Password:</label>\n                          <input type="password" id="sab_pass" name="sab_pass" value="')
        __M_writer(str(lazylibrarian.CONFIG['SAB_PASS']))
        __M_writer('" class="form-control"     placeholder="SABnzbd Password">\n                        </div>\n                      </div>\n                      <div class="form-group">\n                        <label for="sab_api" class="control-label">SABnzbd API Key:</label>\n                        <input type="text" id="sab_api" name="sab_api" value="')
        __M_writer(str(lazylibrarian.CONFIG['SAB_API']))
        __M_writer('" class="form-control"      placeholder="SABnzbd API Key">\n                      </div>\n                      <div class="row">\n                        <div class="form-group col-md-6">\n                          <label for="sab_cat">SABnzbd Category:</label>\n                          <input type="text" id="sab_cat" name="sab_cat" value="')
        __M_writer(str(lazylibrarian.CONFIG['SAB_CAT']))
        __M_writer('" class="form-control"      placeholder="SABnzbd Category">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="sab_subdir" class="control-label">SABnzbd URL Base:</label>\n                          <input type="text" id="sab_subdir" name="sab_subdir" value="')
        __M_writer(str(lazylibrarian.CONFIG['SAB_SUBDIR']))
        __M_writer('" class="form-control"     placeholder="URL Base">\n                        </div>\n                      </div>\n                      <div class="row">\n                        <div class="col-md-6">\n                        <div class="input-group">\n                          <span class="input-group-addon">Ext Host/Port</span>\n                          <input type="text" id="sab_external_host" name="sab_external_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['SAB_EXTERNAL_HOST']))
        __M_writer('" class="form-control" placeholder="mywebsite.org:port">\n                        </div>\n                        <span class="help-block">Use if you need to get sab to download the nzb file from lazylibrarian</span>\n                        </div>\n                        <div class="col-md-6">\n                          <button class="button btn btn-sm btn-primary" type="button" value="Test SABnzbd" id="testSABnzbd"><i class="fa fa-list-ul"></i> Test SABnzbd</button>\n                          <br>\n                        </div>\n                      </div>\n                      <div class="checkbox">\n                        ')

        if lazylibrarian.CONFIG['SAB_DELETE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="sab_delete" class="control-label">\n                        <input type="checkbox" id="sab_delete" name="sab_delete" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Delete from sabnzbd history</label>\n                      </div>\n                    </fieldset>\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['NZB_DOWNLOADER_NZBGET'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="nzb_downloader_nzbget" class="control-label">\n                      <input type="checkbox" id="nzb_downloader_nzbget" name="nzb_downloader_nzbget" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Use NZBGet</label>\n                    </div>\n                    <fieldset id="nzbget_options">\n                      <legend>NZBGet</legend>\n                      <div class="row">\n                        <div class="form-group col-md-8">\n                          <label for="nzbget_host" class="control-label">NZBGet Host:</label>\n                          <input type="text" id="nzbget_host" name="nzbget_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['NZBGET_HOST']))
        __M_writer('" class="form-control" placeholder="NZBGet Host">\n                        </div>\n                        <div class="form-group col-md-4">\n                          <label for="nzbget_port" class="control-label">Port</label>\n                          <input type="number" id="nzbget_port" name="nzbget_port" value="')
        __M_writer(str(lazylibrarian.CONFIG['NZBGET_PORT']))
        __M_writer('" class="form-control" placeholder="NZBGet Port">\n                        </div>\n                      </div>\n                      <div class="row">\n                        <div class="form-group col-md-6">\n                          <label for="nzbget_user" class="control-label">Username</label>\n                          <input type="text" id="nzbget_user" name="nzbget_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['NZBGET_USER']))
        __M_writer('" class="form-control" placeholder="NZBGet Username">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="nzbget_pass">Password:</label>\n                          <input type="password" id="nzbget_pass" name="nzbget_pass" value="')
        __M_writer(str(lazylibrarian.CONFIG['NZBGET_PASS']))
        __M_writer('" class="form-control" placeholder="NZBGet Password">\n                        </div>\n                      </div>\n                      <div class="row">\n                        <div class="form-group col-md-6">\n                          <label for="nzbget_category" class="control-label">Category:</label>\n                          <input type="text" id="nzbget_category" name="nzbget_category" value="')
        __M_writer(str(lazylibrarian.CONFIG['NZBGET_CATEGORY']))
        __M_writer('" class="form-control" placeholder="NZBGet Category">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="nzbget_priority">Priority:</label>\n                          <input type="text" id="nzbget_priority" name="nzbget_priority" value="')
        __M_writer(str(lazylibrarian.CONFIG['NZBGET_PRIORITY']))
        __M_writer('" class="form-control" placeholder="NZBGet Priority">\n                        </div>\n                      </div>\n                      <div class="row">\n                      <div class="col-md-6">\n                        <button class="button btn btn-sm btn-primary" type="button" value="Test NZBget" id="testNZBget"><i class="fa fa-list-ul"></i> Test NZBget</button>\n                        <br>\n                        <br>\n                      </div>\n                      </div>\n                    </fieldset>\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['USE_SYNOLOGY'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="use_synology" class="control-label">\n                        <input type="checkbox" id="use_synology" name="use_synology" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Use Synology DownloadStation</label>\n                    </div>\n                    <fieldset id="synology_options">\n                      <legend>Synology</legend>\n                      <div class="row">\n                        <div class="form-group col-md-8">\n                          <label for="synology_host" class="control-label">Synology Host:</label>\n                          <input type="text" id="synology_host" name="synology_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['SYNOLOGY_HOST']))
        __M_writer('" class="form-control" placeholder="Synology Host">\n                        </div>\n                        <div class="form-group col-md-4">\n                          <label for="synology_port" class="control-label">Port</label>\n                          <input type="number" id="synology_port" name="synology_port" value="')
        __M_writer(str(lazylibrarian.CONFIG['SYNOLOGY_PORT']))
        __M_writer('" class="form-control" placeholder="Synology Port">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="synology_user" class="control-label">Username</label>\n                          <input type="text" id="synology_user" name="synology_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['SYNOLOGY_USER']))
        __M_writer('" class="form-control" placeholder="Synology Username">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="synology_pass">Password:</label>\n                          <input type="password" id="synology_pass" name="synology_pass" value="')
        __M_writer(str(lazylibrarian.CONFIG['SYNOLOGY_PASS']))
        __M_writer('" class="form-control" placeholder="Synology Password">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="synology_dir">Directory:</label>\n                          <input type="text" id="synology_dir" name="synology_dir" value="')
        __M_writer(str(lazylibrarian.CONFIG['SYNOLOGY_DIR']))
        __M_writer('" class="form-control" placeholder="Synology Directory">\n                        </div>\n                      </div>\n                      <div class="row checkbox">\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['NZB_DOWNLOADER_SYNOLOGY'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                        <label for="nzb_downloader_synology" class="control-label">\n                          <input type="checkbox" id="nzb_downloader_synology" name="nzb_downloader_synology" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Use DownloadStation for usenet</label>\n                      </div>\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['TOR_DOWNLOADER_SYNOLOGY'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                        <label for="tor_downloader_synology" class="control-label">\n                          <input type="checkbox" id="tor_downloader_synology" name="tor_downloader_synology" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Use DownloadStation for torrents</label>\n                      </div>\n                      </div>\n                      <div class="row">\n                      <div class="col-md-6">\n                        <button class="button btn btn-sm btn-primary" type="button" value="Test Synology" id="testSynology"><i class="fa fa-list-ul"></i> Test Synology</button>\n                        <br>\n                        <br>\n                      </div>\n                      </div>\n                    </fieldset>\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['NZB_DOWNLOADER_BLACKHOLE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                      <label for="nzb_downloader_blackhole" class="control-label">\n                        <input type="checkbox" id="nzb_downloader_blackhole" name="nzb_downloader_blackhole" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Use NZB Blackhole</label>\n                    </div>\n                    <fieldset id="nzb_blackhole_options">\n                      <legend>NZB Blackhole</legend>\n                      <div class="form-group">\n                        <label for="nzb_blackholedir" class="control-label">NZB Blackhole Directory:</label>\n                        <input type="text" id="nzb_blackholedir" name="nzb_blackholedir" value="')
        __M_writer(str(lazylibrarian.CONFIG['NZB_BLACKHOLEDIR']))
        __M_writer('" class="form-control" placeholder="NZB Blackhole Directory">\n                      </div>\n                    </fieldset>\n                    <div class="input-group col-md-8">\n                      <label for="usenet_retention" class="input-group-addon">Usenet Retention</label>\n                      <input type="number" id="usenet_retention" name="usenet_retention" value="')
        __M_writer(str(lazylibrarian.CONFIG['USENET_RETENTION']))
        __M_writer('" class="form-control" placeholder="Retention Maximum Age">\n                      <span class="input-group-addon">Days</span>\n                    </div>\n                  </fieldset>\n                </fieldset>\n              </div>\n              <div class="col-md-6">\n              <fieldset>\n              <legend>Torrents</legend>\n              <fieldset id="torrent_options">\n                <div class="checkbox">\n                  ')

        if lazylibrarian.CONFIG['TOR_DOWNLOADER_DELUGE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                  <label for="tor_downloader_deluge" class="control-label">\n                    <input type="checkbox" id="tor_downloader_deluge" name="tor_downloader_deluge" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                    Use Deluge</label>\n                </div>\n                  <fieldset id="deluge_options">\n                    <legend>Deluge</legend>\n                    <div class="row">\n                      <div class="form-group col-md-8">\n                        <label for="deluge_host">Deluge Host:</label>\n                        <input type="text" id="deluge_host" name="deluge_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['DELUGE_HOST']))
        __M_writer('" class="form-control" placeholder="Deluge Host">\n                      </div>\n                      <div class="form-group col-md-4">\n                        <label for="deluge_port" class="control-label">Daemon or webUI Port:</label>\n                        <input type="number" id="deluge_port" name="deluge_port" value="')
        __M_writer(str(lazylibrarian.CONFIG['DELUGE_PORT']))
        __M_writer('" class="form-control" placeholder="Deluge Port">\n                      </div>\n                    </div>\n                    <div class="row">\n                      <div class="form-group col-md-8">\n                        <label for="deluge_cert">Deluge Certificate:</label>\n                        <input type="text" id="deluge_cert" name="deluge_cert" value="')
        __M_writer(str(lazylibrarian.CONFIG['DELUGE_CERT']))
        __M_writer('" class="form-control" placeholder="webUI only">\n                      </div>\n                      <div class="form-group col-md-4">\n                        <label for="deluge_base">Deluge URL Base:</label>\n                        <input type="text" id="deluge_base" name="deluge_base" value="')
        __M_writer(str(lazylibrarian.CONFIG['DELUGE_BASE']))
        __M_writer('" class="form-control" placeholder="URL Base">\n                      </div>\n                    </div>\n                    <div class="row">\n                      <div class="form-group col-md-6">\n                        <label for="deluge_user" class="controllabel">Username:</label>\n                        <input type="text" id="deluge_user" name="deluge_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['DELUGE_USER']))
        __M_writer('" class="form-control" placeholder="daemon only">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="deluge_pass" class="control-label">Password:</label>\n                        <input type="password" id="deluge_pass" name="deluge_pass" value="')
        __M_writer(str(lazylibrarian.CONFIG['DELUGE_PASS']))
        __M_writer('" class="form-control" placeholder="Deluge Password">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="deluge_label" class="control-label">Deluge Label:</label>\n                        <input type="text" id="deluge_label" name="deluge_label" value="')
        __M_writer(str(lazylibrarian.CONFIG['DELUGE_LABEL']))
        __M_writer('" class="form-control" placeholder="Deluge Label">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="deluge_dir" class="control-label">Download directory :</label>\n                        <input type="text" id="deluge_dir" name="deluge_dir" value="')
        __M_writer(str(lazylibrarian.CONFIG['DELUGE_DIR']))
        __M_writer('" class="form-control" placeholder="use deluge default">\n                      </div>\n                      <div class="col-md-6">\n                        <button class="button btn btn-sm btn-primary" type="button" value="Test Deluge" id="testDeluge"><i class="fa fa-list-ul"></i> Test Deluge</button>\n                        <br>\n                        <br>\n                      </div>\n                    </div>\n                  </fieldset>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['TOR_DOWNLOADER_TRANSMISSION'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="tor_downloader_transmission" class="control-label">\n                    <input type="checkbox" id="tor_downloader_transmission" name="tor_downloader_transmission" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                    Use Transmission</label>\n                  </div>\n                  <fieldset id="transmission_options">\n                    <legend>Transmission</legend>\n                    <div class="row">\n                      <div class="form-group col-md-8">\n                        <label for="transmission_host" class="control-label">Transmission Host:</label>\n                        <input type="text" id="transmission_host" name="transmission_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['TRANSMISSION_HOST']))
        __M_writer('" class="form-control" placeholder="Transmission host">\n                      </div>\n                      <div class="form-group col-md-4">\n                        <label for="transmission_port" class="control-label">Transmission Port :</label>\n                        <input type="number" id="transmission_port" name="transmission_port" value="')
        __M_writer(str(lazylibrarian.CONFIG['TRANSMISSION_PORT']))
        __M_writer('" class="form-control" placeholder="Transmission port">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="transmission_user" class="control-label">Username :</label>\n                        <input type="text" id="transmission_user" name="transmission_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['TRANSMISSION_USER']))
        __M_writer('" class="form-control" placeholder="Transmission Username">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="transmission_pass" class="control-label">Password :</label>\n                        <input type="password" id="transmission_pass" name="transmission_pass" value="')
        __M_writer(str(lazylibrarian.CONFIG['TRANSMISSION_PASS']))
        __M_writer('" class="form-control" placeholder="Transmission Password">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="transmission_dir" class="control-label">Download directory :</label>\n                        <input type="text" id="transmission_dir" name="transmission_dir" value="')
        __M_writer(str(lazylibrarian.CONFIG['TRANSMISSION_DIR']))
        __M_writer('" class="form-control" placeholder="use transmission default">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="transmission_base" class="control-label">Transmission URL Base:</label>\n                        <input type="text" id="transmission_base" name="transmission_base" value="')
        __M_writer(str(lazylibrarian.CONFIG['TRANSMISSION_BASE']))
        __M_writer('" class="form-control" placeholder="/transmission">\n                      </div>\n                    </div>\n                    <div class="row">\n                      <div class="col-md-6">\n                        <button class="button btn btn-sm btn-primary" type="button" value="Test Transmission" id="testTransmission"><i class="fa fa-list-ul"></i> Test Transmission</button>\n                        <br>\n                        <br>\n                      </div>\n                    </div>\n                  </fieldset>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['TOR_DOWNLOADER_RTORRENT'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="tor_downloader_rtorrent" class="control-label">\n                      <input type="checkbox" id="tor_downloader_rtorrent" name="tor_downloader_rtorrent" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Use rTorrent</label>\n                  </div>\n                  <fieldset id="rtorrent_options">\n                    <legend>rTorrent</legend>\n                    <div class="row">\n                      <div class="form-group col-md-8">\n                        <label for="rtorrent_host" class="control-label">rTorrent Host:</label>\n                        <input type="text" id="rtorrent_host" name="rtorrent_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['RTORRENT_HOST']))
        __M_writer('" class="form-control" placeholder="rTorrent Host">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="rtorrent_user" class="control-label">rTorrent User:</label>\n                        <input type="text" id="rtorrent_user" name="rtorrent_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['RTORRENT_USER']))
        __M_writer('" class="form-control" placeholder="rTorrent User">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="rtorrent_pass" class="control-label">rTorrent Password:</label>\n                        <input type="password" id="rtorrent_pass" name="rtorrent_pass" value="')
        __M_writer(str(lazylibrarian.CONFIG['RTORRENT_PASS']))
        __M_writer('" class="form-control" placeholder="rTorrent Password">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="rtorrent_label" class="control-label">rTorrent Label:</label>\n                        <input type="text" id="rtorrent_label" name="rtorrent_label" value="')
        __M_writer(str(lazylibrarian.CONFIG['RTORRENT_LABEL']))
        __M_writer('" class="form-control" placeholder="rTorrent Label">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="rtorrent_dir" class="control-label">rTorrent Directory:</label>\n                        <input type="text" id="rtorrent_dir" name="rtorrent_dir" value="')
        __M_writer(str(lazylibrarian.CONFIG['RTORRENT_DIR']))
        __M_writer('" class="form-control" placeholder="use rtorrent default">\n                      </div>\n                      <div>\n                        <div class="col-md-6">\n                          <button class="button btn btn-sm btn-primary" type="button" value="Test rTorrent" id="testrTorrent"><i class="fa fa-list-ul"></i> Test rTorrent</button>\n                          <br>\n                          <br>\n                        </div>\n                      </div>\n                    </div>\n                  </fieldset>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['TOR_DOWNLOADER_UTORRENT'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="tor_downloader_utorrent" class="control-label">\n                    <input type="checkbox" id="tor_downloader_utorrent" name="tor_downloader_utorrent" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                    Use uTorrent</label>\n                  </div>\n                  <fieldset id="utorrent_options">\n                    <legend>uTorrent</legend>\n                    <div class="row">\n                      <div class="form-group col-md-8">\n                        <label for="utorrent_host" class="control-label">uTorrent Host:</label>\n                        <input type="text" id="utorrent_host" name="utorrent_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['UTORRENT_HOST']))
        __M_writer('" class="form-control" placeholder="uTorrent Host">\n                      </div>\n                      <div class="form-group col-md-4">\n                        <label for="utorrent_port" class="control-label">uTorrent Port:</label>\n                        <input type="number" id="utorrent_port" name="utorrent_port" value="')
        __M_writer(str(lazylibrarian.CONFIG['UTORRENT_PORT']))
        __M_writer('" class="form-control" placeholder="uTorrent Port">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="utorrent_user" class="control-label">Username:</label>\n                        <input type="text" id="utorrent_user" name="utorrent_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['UTORRENT_USER']))
        __M_writer('" class="form-control" placeholder="uTorrent Username">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label>Password:</label>\n                        <input type="password" id="utorrent_pass" name="utorrent_pass" value="')
        __M_writer(str(lazylibrarian.CONFIG['UTORRENT_PASS']))
        __M_writer('" class="form-control" placeholder="uTorrent Password">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="utorrent_label" class="control-label">uTorrent Label:</label>\n                        <input type="text" id="utorrent_label" name="utorrent_label" value="')
        __M_writer(str(lazylibrarian.CONFIG['UTORRENT_LABEL']))
        __M_writer('" class="form-control" placeholder="uTorrent Label">\n                      </div>\n                      <div class="form-group col-md-6">\n                        <label for="utorrent_base" class="control-label">uTorrent URL Base:</label>\n                        <input type="text" id="utorrent_base" name="utorrent_base" value="')
        __M_writer(str(lazylibrarian.CONFIG['UTORRENT_BASE']))
        __M_writer('" class="form-control" placeholder="URL base">\n                      </div>\n                    </div>\n                    <div class="row">\n                      <div class="col-md-6">\n                        <button class="button btn btn-sm btn-primary" type="button" value="Test uTorrent" id="testuTorrent"><i class="fa fa-list-ul"></i> Test uTorrent</button>\n                        <br>\n                        <br>\n                      </div>\n                    </div>\n                  </fieldset>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['TOR_DOWNLOADER_QBITTORRENT'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="tor_downloader_qbittorrent" class="control-label">\n                    <input type="checkbox" id="tor_downloader_qbittorrent" name="tor_downloader_qbittorrent" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                    Use qBitTorrent</label>\n                  </div>\n                    <fieldset id="qbittorrent_options">\n                      <legend>qBitTorrent</legend>\n                      <div class="row">\n                        <div class="form-group col-md-8">\n                          <label for="qbittorrent_host" class="control-label">qBitTorrent Host:</label>\n                          <input type="text" id="qbittorrent_host" name="qbittorrent_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['QBITTORRENT_HOST']))
        __M_writer('" class="form-control" placeholder="qBitTorrent Host">\n                        </div>\n                        <div class="form-group col-md-4">\n                          <label for="qbittorrent_port" class="control-label">qBitTorrent Port:</label>\n                          <input type="number" id="qbittorrent_port" name="qbittorrent_port" value="')
        __M_writer(str(lazylibrarian.CONFIG['QBITTORRENT_PORT']))
        __M_writer('" class="form-control" placeholder="qBitTorrent Port">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="qbittorrent_user" class="control-label">Username:</label>\n                          <input type="text" id="qbittorrent_user" name="qbittorrent_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['QBITTORRENT_USER']))
        __M_writer('" class="form-control" placeholder="qBitTorrent Username">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="qbittorrent_pass" class="control-label">Password:</label>\n                          <input type="password" id="qbittorrent_pass" name="qbittorrent_pass" value="')
        __M_writer(str(lazylibrarian.CONFIG['QBITTORRENT_PASS']))
        __M_writer('" class="form-control" placeholder="qBitTorrent Password">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="qbittorrent_label" class="control-label">qBitTorrent Label/Category:</label>\n                          <input type="text" id="qbittorrent_label" name="qbittorrent_label" value="')
        __M_writer(str(lazylibrarian.CONFIG['QBITTORRENT_LABEL']))
        __M_writer('" class="form-control" placeholder="qBitTorrent Label/Category">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="qbittorrent_base" class="control-label">qBitTorrent URL Base:</label>\n                          <input type="text" id="qbittorrent_base" name="qbittorrent_base" value="')
        __M_writer(str(lazylibrarian.CONFIG['QBITTORRENT_BASE']))
        __M_writer('" class="form-control" placeholder="URL base">\n                        </div>\n                        <div class="form-group col-md-6">\n                          <label for="qbittorrent_dir" class="control-label">Download directory :</label>\n                          <input type="text" id="qbittorrent_dir" name="qbittorrent_dir" value="')
        __M_writer(str(lazylibrarian.CONFIG['QBITTORRENT_DIR']))
        __M_writer('" class="form-control" placeholder="use qbittorrent default">\n                        </div>\n                      </div>\n                      <div class="row">\n                        <div class="col-md-6">\n                          <button class="button btn btn-sm btn-primary" type="button" value="Test qBittorrent" id="testqBittorrent"><i class="fa fa-list-ul"></i> Test qBittorrent</button>\n                          <br>\n                          <br>\n                        </div>\n                      </div>\n                    </fieldset>\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['TOR_DOWNLOADER_BLACKHOLE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="tor_downloader_blackhole" class="control-label">\n                        <input type="checkbox" id="tor_downloader_blackhole" name="tor_downloader_blackhole" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Use Torrent Blackhole</label>\n                    </div>\n                    <fieldset id="tor_blackhole_options">\n                      <legend>Torrent Blackhole</legend>\n                      <div class="form-group">\n                        <label for="torrent_dir" class="control-label">Torrent Blackhole Directory:</label>\n                        <input type="text" id="torrent_dir" name="torrent_dir" value="')
        __M_writer(str(lazylibrarian.CONFIG['TORRENT_DIR']))
        __M_writer('" class="form-control" placeholder="Torrent Blackhole Directory">\n                      </div>\n                      <div class="checkbox">\n                        ')

        if lazylibrarian.CONFIG['TOR_CONVERT_MAGNET'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="tor_convert_magnet" class="control-label">\n                          <input type="checkbox" id="tor_convert_magnet" name="tor_convert_magnet" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Convert magnet links into torrent files</label>\n                      </div>\n                    </fieldset>\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['PREFER_MAGNET'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                      <label for="prefer_magnet" class="control-label">\n                        <input type="checkbox" id="prefer_magnet" name="prefer_magnet" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Prefer magnet links to torrent files</label>\n                    </div>\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['KEEP_SEEDING'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                      <label for="keep_seeding" class="control-label">\n                        <input type="checkbox" id="keep_seeding" name="keep_seeding" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Keep seeding after processing</label>\n                    </div>\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['SEED_WAIT'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="seed_wait" class="control-label">\n                      <input type="checkbox" id="seed_wait" name="seed_wait" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Do not delete if still seeding</label>\n                    </div>\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['DEL_COMPLETED'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="del_completed" class="control-label">\n                      <input type="checkbox" id="del_completed" name="del_completed" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Delete completed tasks from downloader</label>\n                    </div>\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['DEL_FAILED'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="del_failed" class="control-label">\n                      <input type="checkbox" id="del_failed" name="del_failed" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Delete failed tasks from downloader</label>\n                    </div>\n                  </fieldset>\n                </fieldset>\n              </div>\n            </div>\n          </div>\n        </div>\n        <div role="tabpanel" class="tab-pane" id="providers">\n          <div class="configtable">\n            <div class="row">\n              <div class="usenet_providers">\n                <fieldset>\n                  <div class="col-md-12">\n                  <legend>Newznab Providers</legend>\n                  </div>\n')
        loop = __M_loop._enter(lazylibrarian.NEWZNAB_PROV)
        try:
            for provider in loop:
                __M_writer('                  ')

                checked = ''
                if provider['ENABLED'] == True:
                    checked = 'checked="checked"'
                                    
                
                __M_writer('\n                  <div class="col-md-4 form-group">\n                    <div class="input-group">\n                      <span class="input-group-addon">Name</span>\n                      <label for="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" class="sr-only">Newznab Name</label>\n                      <input type="text" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" value="')
                __M_writer(str(provider['DISPNAME']))
                __M_writer('" class="form-control" placeholder="display name">\n                      <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                      &nbsp;<input type="checkbox" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_enabled" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_enabled" value="1" ')
                __M_writer(str(checked))
                __M_writer(' />&nbsp;\n                      </span>\n                    </div>\n                    <div class="input-group">\n                    <span class="input-group-addon"></span>\n                      <label for="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_host" class="sr-only">Newznab URL</label>\n                      <input type="text" placeholder="Newznab URL #')
                __M_writer(str(loop.index))
                __M_writer('" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_host" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_host" value="')
                __M_writer(str(provider['HOST']))
                __M_writer('" class="form-control">\n                      <span class="input-group-addon"></span>\n                    </div>\n                    <div class="input-group">\n                    <span class="input-group-addon"></span>\n                    <label for="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_api" class="sr-only">Newznab API Key</label>\n                    <input type="text" placeholder="Newznab API #')
                __M_writer(str(loop.index))
                __M_writer('" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_api" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_api" value="')
                __M_writer(str(provider['API']))
                __M_writer('" class="form-control">\n                    <span class="input-group-addon"></span>\n                      </div>\n                    <div class="input-group">\n                      <span class="input-group-addon">Priority</span>\n                      <input type="number" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_dlpriority" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_dlpriority" value="')
                __M_writer(str(provider['DLPRIORITY']))
                __M_writer('" class="form-control" placeholder="0">\n                      <span class="input-group-addon">Types</span>\n                      <input type="text" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_dltypes" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_dltypes" value="')
                __M_writer(str(provider['DLTYPES']))
                __M_writer('" class="form-control" placeholder="">\n                      <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="newznab_')
                __M_writer(str(loop.index))
                __M_writer('"> Test</button>\n                      </span>\n                    </div>\n                  </div>\n')
        finally:
            loop = __M_loop._exit()
        __M_writer('                </fieldset>\n              </div>\n              <div class="torznab_providers">\n                <fieldset>\n                  <div class="col-md-12">\n                  <legend>Torznab Providers</legend>\n                  </div>\n')
        loop = __M_loop._enter(lazylibrarian.TORZNAB_PROV)
        try:
            for provider in loop:
                __M_writer('                  ')

                checked = ''
                if provider['ENABLED'] == True:
                  checked = 'checked="checked"'
                                    
                
                __M_writer('\n                  <div class="col-md-4 form-group">\n                    <div class="input-group">\n                      <span class="input-group-addon">Name</span>\n                      <label for="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_host" class="sr-only">Torznab Name</label>\n                      <input type="text" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" value="')
                __M_writer(str(provider['DISPNAME']))
                __M_writer('" class="form-control" placeholder="display name">\n                      <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                        &nbsp;<input type="checkbox" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_enabled" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_enabled" value="1" ')
                __M_writer(str(checked))
                __M_writer(' />&nbsp;\n                        </span>\n                    </div>\n                    <div class="input-group">\n                      <span class="input-group-addon"></span>\n                      <label for="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_host" class="sr-only">Torznab URL</label>\n                      <input type="text" placeholder="Torznab URL #')
                __M_writer(str(loop.index))
                __M_writer('" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_host" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_host" value="')
                __M_writer(str(provider['HOST']))
                __M_writer('" class="form-control">\n                      <span class="input-group-addon"></span>\n                    </div>\n                    <div class="input-group">\n                    <span class="input-group-addon"></span>\n                    <label for="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_api" class="sr-only">Torznab API Key</label>\n                    <input type="text" placeholder="Torznab API #')
                __M_writer(str(loop.index))
                __M_writer('" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_api" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_api" value="')
                __M_writer(str(provider['API']))
                __M_writer('" class="form-control">\n                    <span class="input-group-addon"></span>\n                    </div>\n                    <div class="input-group">\n                      <span class="input-group-addon">Priority</span>\n                      <input type="number" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_dlpriority" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_dlpriority" value="')
                __M_writer(str(provider['DLPRIORITY']))
                __M_writer('" class="form-control" placeholder="0">\n                      <span class="input-group-addon">Seeders</span>\n                      <input type="number" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_seeders" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_seeders" value="')
                __M_writer(str(provider['SEEDERS']))
                __M_writer('" class="form-control" placeholder="0">\n                      <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="torznab_')
                __M_writer(str(loop.index))
                __M_writer('"> Test</button>\n                      </span>\n                    </div>\n                    <div class="input-group">\n                      <span class="input-group-addon">Types</span>\n                      <input type="text" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_dltypes" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_dltypes" value="')
                __M_writer(str(provider['DLTYPES']))
                __M_writer('" class="form-control" placeholder="">\n                    </div>\n                  </div>\n')
        finally:
            loop = __M_loop._exit()
        __M_writer('                </fieldset>\n              </div>\n              <div class="rss_providers">\n                <fieldset>\n                  <div class="col-md-12">\n                  <legend>RSS/Wishlist Providers</legend>\n                  </div>\n')
        loop = __M_loop._enter(lazylibrarian.RSS_PROV)
        try:
            for provider in loop:
                __M_writer('                  ')

                checked = ''
                if provider['ENABLED'] == True:
                    checked = 'checked="checked"'
                                  
                
                __M_writer('\n                  <div class="col-md-4 form-group">\n                    <div class="input-group">\n                      <span class="input-group-addon">Name</span>\n                      <label for="rss_')
                __M_writer(str(loop.index))
                __M_writer('_host" class="sr-only">RSS Name</label>\n                      <input type="text" id="rss_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" name="rss_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" value="')
                __M_writer(str(provider['DISPNAME']))
                __M_writer('" class="form-control" placeholder="display name">\n                      <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                        &nbsp;<input type="checkbox" id="rss_')
                __M_writer(str(loop.index))
                __M_writer('_enabled" name="rss_')
                __M_writer(str(loop.index))
                __M_writer('_enabled" value="1" ')
                __M_writer(str(checked))
                __M_writer(' />&nbsp;\n                      </span>\n                    </div>\n                    <div class="input-group">\n                      <span class="input-group-addon"></span>\n                      <label for="rss_')
                __M_writer(str(loop.index))
                __M_writer('_host" class="sr-only">RSS URL</label>\n                      <input type="text" placeholder="RSS URL #')
                __M_writer(str(loop.index))
                __M_writer('" id="rss_')
                __M_writer(str(loop.index))
                __M_writer('_host" name="rss_')
                __M_writer(str(loop.index))
                __M_writer('_host" value="')
                __M_writer(str(provider['HOST']))
                __M_writer('" class="form-control" />\n                      <span class="input-group-addon"></span>\n                    </div>\n                      ')

                label = 'Priority'
                if 'list_rss' in provider['HOST']:
                  label = 'Pages'
                if '/book/' in provider['HOST']:
                  label = 'Pages'
                if '/show/' in provider['HOST']:
                  label = 'Pages'
                                      
                
                __M_writer('\n                    <div class="input-group">\n                      <span class="input-group-addon">')
                __M_writer(str(label))
                __M_writer('</span>\n                      <input type="number" id="rss_')
                __M_writer(str(loop.index))
                __M_writer('_dlpriority" name="rss_')
                __M_writer(str(loop.index))
                __M_writer('_dlpriority" value="')
                __M_writer(str(provider['DLPRIORITY']))
                __M_writer('" class="form-control" placeholder="0">\n                      <span class="input-group-addon">Types</span>\n                      <input type="text" id="rss_')
                __M_writer(str(loop.index))
                __M_writer('_dltypes" name="rss_')
                __M_writer(str(loop.index))
                __M_writer('_dltypes" value="')
                __M_writer(str(provider['DLTYPES']))
                __M_writer('" class="form-control" placeholder="">\n                      <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="rss_')
                __M_writer(str(loop.index))
                __M_writer('"> Test</button>\n                      </span>\n                    </div>\n                  </div>\n')
        finally:
            loop = __M_loop._exit()
        __M_writer('                </fieldset>\n                <div class="torrent_providers">\n                  <fieldset>\n                    <div class="col-md-12">\n                    <legend>Torrent Providers</legend>\n                    </div>\n                    ')

        if lazylibrarian.CONFIG['KAT'] == True:
          checked = 'checked="checked"'
        else:
          checked = ''
                            
        
        __M_writer('\n                    <div class="col-md-4 form-group">\n                      <label for="kat_host" class="sr-only">KAT Host</label>\n                      <div class="input-group">\n                        <input type="text" placeholder="KAT Host" id="kat_host" name="kat_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['KAT_HOST']))
        __M_writer('" class="form-control">\n                        <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                        <input type="checkbox" id="kat" name="kat" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        </span>\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Priority</span>\n                        <input type="number" id="kat_dlpriority" name="kat_dlpriority" value="')
        __M_writer(str(lazylibrarian.CONFIG['KAT_DLPRIORITY']))
        __M_writer('" class="form-control" placeholder="0">\n                        <span class="input-group-addon">Seeders</span>\n                        <input type="number" id="kat_seeders" name="kat_seeders" value="')
        __M_writer(str(lazylibrarian.CONFIG['KAT_SEEDERS']))
        __M_writer('" class="form-control" placeholder="0">\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Types</span>\n                        <input type="text" id="kat_dltypes" name="kat_dltypes" value="')
        __M_writer(str(lazylibrarian.CONFIG['KAT_DLTYPES']))
        __M_writer('" class="form-control" placeholder="">\n                        <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="KAT"> Test</button>\n                        </span>\n                      </div>\n                    </div>\n                    ')

        if lazylibrarian.CONFIG['TPB'] == True:
          checked = 'checked="checked"'
        else:
          checked = ''
                            
        
        __M_writer('\n                    <div class="col-md-4 form-group">\n                      <label for="tpb_host" class="sr-only">TPB Host</label>\n                      <div class="input-group">\n                        <input type="text" placeholder="TPB Host" id="tpb_host" name="tpb_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['TPB_HOST']))
        __M_writer('" class="form-control">\n                        <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                          <input type="checkbox" id="tpb" name="tpb" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        </span>\n                      </div>\n                      <div class="input-group">\n                      <span class="input-group-addon">Priority</span>\n                        <input type="number" id="tpb_dlpriority" name="tpb_dlpriority" value="')
        __M_writer(str(lazylibrarian.CONFIG['TPB_DLPRIORITY']))
        __M_writer('" class="form-control" placeholder="0">\n                        <span class="input-group-addon">Seeders</span>\n                        <input type="number" id="tpb_seeders" name="tpb_seeders" value="')
        __M_writer(str(lazylibrarian.CONFIG['TPB_SEEDERS']))
        __M_writer('" class="form-control" placeholder="0">\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Types</span>\n                        <input type="text" id="tpb_dltypes" name="tpb_dltypes" value="')
        __M_writer(str(lazylibrarian.CONFIG['TPB_DLTYPES']))
        __M_writer('" class="form-control" placeholder="">\n                        <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="TPB"> Test</button>\n                        </span>\n                      </div>\n                    </div>\n                   ')

        if lazylibrarian.CONFIG['WWT'] == True:
          checked = 'checked="checked"'
        else:
          checked = ''
                            
        
        __M_writer('\n                    <div class="col-md-4 form-group">\n                      <label for="wwt_host" class="sr-only">WWT Host</label>\n                      <div class="input-group">\n                        <input type="text" placeholder="WWT Host" id="wwt_host" name="wwt_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['WWT_HOST']))
        __M_writer('" class="form-control">\n                        <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                          <input type="checkbox" id="wwt" name="wwt" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        </span>\n                      </div>\n                      <div class="input-group">\n                      <span class="input-group-addon">Priority</span>\n                        <input type="number" id="wwt_dlpriority" name="wwt_dlpriority" value="')
        __M_writer(str(lazylibrarian.CONFIG['WWT_DLPRIORITY']))
        __M_writer('" class="form-control" placeholder="0">\n                        <span class="input-group-addon">Seeders</span>\n                        <input type="number" id="wwt_seeders" name="wwt_seeders" value="')
        __M_writer(str(lazylibrarian.CONFIG['WWT_SEEDERS']))
        __M_writer('" class="form-control" placeholder="0">\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Types</span>\n                        <input type="text" id="wwt_dltypes" name="wwt_dltypes" value="')
        __M_writer(str(lazylibrarian.CONFIG['WWT_DLTYPES']))
        __M_writer('" class="form-control" placeholder="">\n                        <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="WWT"> Test</button>\n                        </span>\n                      </div>\n                    </div>\n                    ')

        if lazylibrarian.CONFIG['ZOO'] == True:
          checked = 'checked="checked"'
        else:
          checked = ''
                            
        
        __M_writer('\n                    <div class="col-md-4 form-group">\n                      <label for="zoo_host" class="sr-only">zooqle host</label>\n                      <div class="input-group">\n                        <input type="text" placeholder="zooqle host" id="zoo_host" name="zoo_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['ZOO_HOST']))
        __M_writer('" class="form-control">\n                        <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                        <input type="checkbox" id="zoo" name="zoo" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        </span>\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Priority</span>\n                        <input type="number" id="zoo_dlpriority" name="zoo_dlpriority" value="')
        __M_writer(str(lazylibrarian.CONFIG['ZOO_DLPRIORITY']))
        __M_writer('" class="form-control" placeholder="0">\n                        <span class="input-group-addon">Seeders</span>\n                        <input type="number" id="zoo_seeders" name="zoo_seeders" value="')
        __M_writer(str(lazylibrarian.CONFIG['ZOO_SEEDERS']))
        __M_writer('" class="form-control" placeholder="0">\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Types</span>\n                        <input type="text" id="zoo_dltypes" name="zoo_dltypes" value="')
        __M_writer(str(lazylibrarian.CONFIG['ZOO_DLTYPES']))
        __M_writer('" class="form-control" placeholder="">\n                        <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="ZOO"> Test</button>\n                        </span>\n                      </div>\n                    </div>\n                    ')

        if lazylibrarian.CONFIG['TDL'] == True:
          checked = 'checked="checked"'
        else:
          checked = ''
                            
        
        __M_writer('\n                    <div class="col-md-4 form-group">\n                      <label for="tdl_host" class="sr-only">torrentdownload host</label>\n                      <div class="input-group">\n                        <input type="text" placeholder="torrentdownload host" id="tdl_host" name="tdl_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['TDL_HOST']))
        __M_writer('" class="form-control">\n                        <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                        <input type="checkbox" id="tdl" name="tdl" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        </span>\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Priority</span>\n                        <input type="number" id="tdl_dlpriority" name="tdl_dlpriority" value="')
        __M_writer(str(lazylibrarian.CONFIG['TDL_DLPRIORITY']))
        __M_writer('" class="form-control" placeholder="0">\n                        <span class="input-group-addon">Seeders</span>\n                        <input type="number" id="tdl_seeders" name="tdl_seeders" value="')
        __M_writer(str(lazylibrarian.CONFIG['TDL_SEEDERS']))
        __M_writer('" class="form-control" placeholder="0">\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Types</span>\n                        <input type="text" id="tdl_dltypes" name="tdl_dltypes" value="')
        __M_writer(str(lazylibrarian.CONFIG['TDL_DLTYPES']))
        __M_writer('" class="form-control" placeholder="">\n                        <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="TDL"> Test</button>\n                        </span>\n                      </div>\n                    </div>\n                     ')

        if lazylibrarian.CONFIG['TRF'] == True:
          checked = 'checked="checked"'
        else:
          checked = ''
                            
        
        __M_writer('\n                    <div class="col-md-4 form-group">\n                      <label for="trf_host" class="sr-only">torrof host</label>\n                      <div class="input-group">\n                        <input type="text" placeholder="torrof host" id="trf_host" name="trf_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['TRF_HOST']))
        __M_writer('" class="form-control">\n                        <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                        <input type="checkbox" id="trf" name="trf" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        </span>\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Priority</span>\n                        <input type="number" id="trf_dlpriority" name="trf_dlpriority" value="')
        __M_writer(str(lazylibrarian.CONFIG['TRF_DLPRIORITY']))
        __M_writer('" class="form-control" placeholder="0">\n                        <span class="input-group-addon">Seeders</span>\n                        <input type="number" id="trf_seeders" name="trf_seeders" value="')
        __M_writer(str(lazylibrarian.CONFIG['TRF_SEEDERS']))
        __M_writer('" class="form-control" placeholder="0">\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Types</span>\n                        <input type="text" id="trf_dltypes" name="trf_dltypes" value="')
        __M_writer(str(lazylibrarian.CONFIG['TRF_DLTYPES']))
        __M_writer('" class="form-control" placeholder="">\n                        <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="TRF"> Test</button>\n                        </span>\n                      </div>\n                    </div>\n                    ')

        if lazylibrarian.CONFIG['LIME'] == True:
          checked = 'checked="checked"'
        else:
          checked = ''
                            
        
        __M_writer('\n                    <div class="col-md-4 form-group">\n                      <label for="lime_host" class="sr-only">limetorrent host</label>\n                      <div class="input-group">\n                        <input type="text" placeholder="limetorrent host" id="lime_host" name="lime_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['LIME_HOST']))
        __M_writer('" class="form-control">\n                        <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                        <input type="checkbox" id="lime" name="lime" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        </span>\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Priority</span>\n                        <input type="number" id="lime_dlpriority" name="lime_dlpriority" value="')
        __M_writer(str(lazylibrarian.CONFIG['LIME_DLPRIORITY']))
        __M_writer('" class="form-control" placeholder="0">\n                        <span class="input-group-addon">Seeders</span>\n                        <input type="number" id="lime_seeders" name="lime_seeders" value="')
        __M_writer(str(lazylibrarian.CONFIG['LIME_SEEDERS']))
        __M_writer('" class="form-control" placeholder="0">\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Types</span>\n                        <input type="text" id="lime_dltypes" name="lime_dltypes" value="')
        __M_writer(str(lazylibrarian.CONFIG['LIME_DLTYPES']))
        __M_writer('" class="form-control" placeholder="">\n                        <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="LIME"> Test</button>\n                        </span>\n                      </div>\n                    </div>\n                </fieldset>\n              </div>\n              <div class="irc_providers">\n                <fieldset>\n                  <div class="col-md-12">\n                  <legend>IRC Providers</legend>\n                  </div>\n')
        loop = __M_loop._enter(lazylibrarian.IRC_PROV)
        try:
            for provider in loop:
                __M_writer('                  ')

                checked = ''
                if provider['ENABLED'] == True:
                    checked = 'checked="checked"'
                                  
                
                __M_writer('\n                  <div class="col-md-4 form-group">\n                    <div class="input-group">\n                      <span id="log_type" class="input-group-addon">Name</span>\n                      <label for="irc_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" class="sr-only">IRC Name</label>\n                      <input type="text" id="irc_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" name="irc_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" value="')
                __M_writer(str(provider['DISPNAME']))
                __M_writer('" class="form-control" placeholder="display name">\n                      <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                        &nbsp;<input type="checkbox" id="irc_')
                __M_writer(str(loop.index))
                __M_writer('_enabled" name="irc_')
                __M_writer(str(loop.index))
                __M_writer('_enabled" value="1" ')
                __M_writer(str(checked))
                __M_writer(' />&nbsp;\n                      </span>\n                    </div>\n                    <div class="input-group">\n                      <span id="log_type" class="input-group-addon">Server</span>\n                      <label for="irc_')
                __M_writer(str(loop.index))
                __M_writer('_server" class="sr-only">Server</label>\n                      <input type="text" placeholder="IRC Server #')
                __M_writer(str(loop.index))
                __M_writer('" id="irc_')
                __M_writer(str(loop.index))
                __M_writer('_server" name="irc_')
                __M_writer(str(loop.index))
                __M_writer('_server" value="')
                __M_writer(str(provider['SERVER']))
                __M_writer('" class="form-control" />\n                      <span class="input-group-addon"></span>\n                    </div>\n                    <div class="input-group">\n                      <span id="log_type" class="input-group-addon">Channel</span>\n                      <label for="irc_')
                __M_writer(str(loop.index))
                __M_writer('_channel" class="sr-only">Channel</label>\n                      <input type="text" placeholder="IRC Channel #')
                __M_writer(str(loop.index))
                __M_writer('" id="irc_')
                __M_writer(str(loop.index))
                __M_writer('_channel" name="irc_')
                __M_writer(str(loop.index))
                __M_writer('_channel" value="')
                __M_writer(str(provider['CHANNEL']))
                __M_writer('" class="form-control">\n                      <span class="input-group-addon"></span>\n                    </div>\n                    <div class="input-group">\n                      <span id="log_type" class="input-group-addon">BotNick</span>\n                      <label for="irc_')
                __M_writer(str(loop.index))
                __M_writer('_botnick" class="sr-only">BotNick</label>\n                      <input type="text" placeholder="IRC BotNick #')
                __M_writer(str(loop.index))
                __M_writer('" id="irc_')
                __M_writer(str(loop.index))
                __M_writer('_botnick" name="irc_')
                __M_writer(str(loop.index))
                __M_writer('_botnick" value="')
                __M_writer(str(provider['BOTNICK']))
                __M_writer('" class="form-control">\n                      <span class="input-group-addon"></span>\n                    </div>\n                    <div class="input-group">\n                      <span id="log_type" class="input-group-addon">BotPass</span>\n                      <label for="irc_')
                __M_writer(str(loop.index))
                __M_writer('_botpass" class="sr-only">BotPass</label>\n                      <input type="password" placeholder="IRC BotPass #')
                __M_writer(str(loop.index))
                __M_writer('" id="irc_')
                __M_writer(str(loop.index))
                __M_writer('_botpass" name="irc_')
                __M_writer(str(loop.index))
                __M_writer('_botpass" value="')
                __M_writer(str(provider['BOTPASS']))
                __M_writer('" class="form-control">\n                      <span class="input-group-addon"></span>\n                    </div>\n                    <div class="input-group">\n                      <span class="input-group-addon">Priority</span>\n                      <input type="number" id="irc_')
                __M_writer(str(loop.index))
                __M_writer('_dlpriority" name="irc_')
                __M_writer(str(loop.index))
                __M_writer('_dlpriority" value="')
                __M_writer(str(provider['DLPRIORITY']))
                __M_writer('" class="form-control" placeholder="0">\n                      <span class="input-group-addon">Types</span>\n                      <input type="text" id="irc_')
                __M_writer(str(loop.index))
                __M_writer('_dltypes" name="irc_')
                __M_writer(str(loop.index))
                __M_writer('_dltypes" value="')
                __M_writer(str(provider['DLTYPES']))
                __M_writer('" class="form-control" placeholder="">\n                      <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="irc_')
                __M_writer(str(loop.index))
                __M_writer('"> Test</button>\n                      </span>\n                    </div>\n                  </div>\n')
        finally:
            loop = __M_loop._exit()
        __M_writer('                </fieldset>\n              </div>\n              <div class="direct_providers">\n                  <fieldset>\n                    <div class="col-md-12">\n                    <legend>Direct Download Providers</legend>\n                    </div>\n                    ')

        if lazylibrarian.CONFIG['BOK'] == True:
          checked = 'checked="checked"'
        else:
          checked = ''
                            
        
        __M_writer('\n                    <div class="col-md-4 form-group">\n                      <label for="bok_host" class="sr-only">zlibrary host</label>\n                      <div class="input-group">\n                        <span class="input-group-addon">ZLibrary</span>\n                        <input type="text" placeholder="zlibrary host" id="bok_host" name="bok_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['BOK_HOST']))
        __M_writer('" class="form-control">\n                        <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                        <input type="checkbox" id="bok" name="bok" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        </span>\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Priority</span>\n                        <input type="number" id="bok_dlpriority" name="bok_dlpriority" value="')
        __M_writer(str(lazylibrarian.CONFIG['BOK_DLPRIORITY']))
        __M_writer('" class="form-control" placeholder="0">\n                        <span class="input-group-addon">Types</span>\n                        <input type="text" id="bok_dltypes" name="bok_dltypes" value="')
        __M_writer(str(lazylibrarian.CONFIG['BOK_DLTYPES']))
        __M_writer('" class="form-control" placeholder="">\n                        <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="BOK"> Test</button>\n                        </span>\n                      </div>\n                      <div class="input-group">\n                      <span class="input-group-addon">Daily Downloads: (used ')
        __M_writer(str(lazylibrarian.BOK_DLCOUNT))
        __M_writer(')</span>\n                      <input type="number" placeholder="API Limit" id="bok_dllimit" name="bok_dllimit" value="')
        __M_writer(str(lazylibrarian.CONFIG['BOK_DLLIMIT']))
        __M_writer('" class="form-control">\n                      </div>\n                    </div>\n                    ')

        if lazylibrarian.CONFIG['BFI'] == True:
          checked = 'checked="checked"'
        else:
          checked = ''
                            
        
        __M_writer('\n                    <div class="col-md-4 form-group">\n                      <label for="bok_host" class="sr-only">bookfi host</label>\n                      <div class="input-group">\n                        <span class="input-group-addon">BookFi</span>\n                        <input type="text" placeholder="bookfi host" id="bfi_host" name="bfi_host" value="')
        __M_writer(str(lazylibrarian.CONFIG['BFI_HOST']))
        __M_writer('" class="form-control">\n                        <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                        <input type="checkbox" id="bfi" name="bfi" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        </span>\n                      </div>\n                      <div class="input-group">\n                        <span class="input-group-addon">Priority</span>\n                        <input type="number" id="bfi_dlpriority" name="bfi_dlpriority" value="')
        __M_writer(str(lazylibrarian.CONFIG['BFI_DLPRIORITY']))
        __M_writer('" class="form-control" placeholder="0">\n                        <span class="input-group-addon">Types</span>\n                        <input type="text" id="bfi_dltypes" name="bfi_dltypes" value="')
        __M_writer(str(lazylibrarian.CONFIG['BFI_DLTYPES']))
        __M_writer('" class="form-control" placeholder="">\n                        <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="BFI"> Test</button>\n                        </span>\n                      </div>\n                    </div>\n')
        loop = __M_loop._enter(lazylibrarian.GEN_PROV)
        try:
            for provider in loop:
                __M_writer('                  ')

                checked = ''
                if provider['ENABLED'] == True:
                    checked = 'checked="checked"'
                                  
                
                __M_writer('\n                  <div class="col-md-4 form-group">\n                    <div class="input-group">\n                      <span id="log_type" class="input-group-addon">LibGen</span>\n                      <label for="gen_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" class="sr-only">Name</label>\n                      <input type="text" id="gen_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" name="gen_')
                __M_writer(str(loop.index))
                __M_writer('_dispname" value="')
                __M_writer(str(provider['DISPNAME']))
                __M_writer('" class="form-control" placeholder="name">\n                      <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="Enable provider">\n                        &nbsp;<input type="checkbox" id="gen_')
                __M_writer(str(loop.index))
                __M_writer('_enabled" name="gen_')
                __M_writer(str(loop.index))
                __M_writer('_enabled" value="1" ')
                __M_writer(str(checked))
                __M_writer(' />&nbsp;\n                      </span>\n                    </div>\n                    <div class="input-group">\n                      <span id="log_type" class="input-group-addon">Server</span>\n                      <label for="gen_')
                __M_writer(str(loop.index))
                __M_writer('_host" class="sr-only">Server</label>\n                      <input type="text" placeholder="GEN server #')
                __M_writer(str(loop.index))
                __M_writer('" id="gen_')
                __M_writer(str(loop.index))
                __M_writer('_host" name="gen_')
                __M_writer(str(loop.index))
                __M_writer('_host" value="')
                __M_writer(str(provider['HOST']))
                __M_writer('" class="form-control" />\n                      <span class="input-group-addon"></span>\n                    </div>\n                    <div class="input-group">\n                      <span id="log_type" class="input-group-addon">Search</span>\n                      <label for="gen_')
                __M_writer(str(loop.index))
                __M_writer('_search" class="sr-only">Search</label>\n                      <input type="text" placeholder="GEN Search #')
                __M_writer(str(loop.index))
                __M_writer('" id="gen_')
                __M_writer(str(loop.index))
                __M_writer('_search" name="gen_')
                __M_writer(str(loop.index))
                __M_writer('_search" value="')
                __M_writer(str(provider['SEARCH']))
                __M_writer('" class="form-control">\n                      <span class="input-group-addon"></span>\n                    </div>\n                    <div class="input-group">\n                      <span class="input-group-addon">Priority</span>\n                      <input type="number" id="gen_')
                __M_writer(str(loop.index))
                __M_writer('_dlpriority" name="gen_')
                __M_writer(str(loop.index))
                __M_writer('_dlpriority" value="')
                __M_writer(str(provider['DLPRIORITY']))
                __M_writer('" class="form-control" placeholder="0">\n                      <span class="input-group-addon">Types</span>\n                      <input type="text" id="gen_')
                __M_writer(str(loop.index))
                __M_writer('_dltypes" name="gen_')
                __M_writer(str(loop.index))
                __M_writer('_dltypes" value="')
                __M_writer(str(provider['DLTYPES']))
                __M_writer('" class="form-control" placeholder="">\n                      <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="gen_')
                __M_writer(str(loop.index))
                __M_writer('"> Test</button>\n                      </span>\n                    </div>\n                  </div>\n')
        finally:
            loop = __M_loop._exit()
        __M_writer('                  </fieldset>\n                </div>\n              </div>\n            </div>\n            <button class="button btn btn-sm btn-warning btn-primary" type="button" value="showblocked" id="showblocked"> Blocked Providers</button>\n            <br>\n            <br>\n          </div>\n        </div>\n        <div role="tabpanel" class="tab-pane" id="searchprocessing">\n          <div class="configtable">\n            <div class="row">\n              <div class="col-md-4">\n                <fieldset>\n                  <legend>Intervals</legend>\n                  <div class="form-group">\n                    <label for="search_bookinterval" class="control-label">Book Search Interval:</label>\n                    <div class="input-group">\n                      <input type="number" id="search_bookinterval" name="search_bookinterval" value="')
        __M_writer(str(lazylibrarian.CONFIG['SEARCH_BOOKINTERVAL']))
        __M_writer('" class="form-control" placeholder="0 to disable">\n                      <span class="input-group-addon">Minutes</span>\n                    </div>\n                  </div>\n')
        if lazylibrarian.CONFIG['MAG_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="search_maginterval" class="control-label">Magazine Search Interval:</label>\n                    <div class="input-group">\n                      <input type="number" id="search_maginterval" name="search_maginterval" value="')
            __M_writer(str(lazylibrarian.CONFIG['SEARCH_MAGINTERVAL']))
            __M_writer('" class="form-control" placeholder="0 to disable">\n                      <span class="input-group-addon">Minutes</span>\n                    </div>\n                  </div>\n')
        if lazylibrarian.CONFIG['COMIC_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="search_comicinterval" class="control-label">Comic Search Interval:</label>\n                    <div class="input-group">\n                      <input type="number" id="search_comicinterval" name="search_comicinterval" value="')
            __M_writer(str(lazylibrarian.CONFIG['SEARCH_COMICINTERVAL']))
            __M_writer('" class="form-control" placeholder="0 to disable">\n                      <span class="input-group-addon">Hours</span>\n                    </div>\n                  </div>\n')
        __M_writer('                  <div class="form-group">\n                    <label for="searchrss_interval" class="control-label">RSS Search Interval:</label>\n                    <div class="input-group">\n                      <input type="number" id="searchrss_interval" name="searchrss_interval" value="')
        __M_writer(str(lazylibrarian.CONFIG['SEARCHRSS_INTERVAL']))
        __M_writer('" class="form-control" placeholder="0 to disable">\n                      <span class="input-group-addon">Minutes</span>\n                    </div>\n                  </div>\n                  <div class="form-group">\n                    <label for="wishlist_interval" class="control-label">Wishlist Search Interval:</label>\n                    <div class="input-group">\n                      <input type="number" id="wishlist_interval" name="wishlist_interval" value="')
        __M_writer(str(lazylibrarian.CONFIG['WISHLIST_INTERVAL']))
        __M_writer('" class="form-control" placeholder="0 to disable">\n                      <span class="input-group-addon">Hours</span>\n                    </div>\n                  </div>\n                  <div class="form-group">\n                    <label class="control-label">Post-Processing Interval:</label>\n                    <div class="input-group">\n                      <input type="number" id="scan_interval" name="scan_interval" value="')
        __M_writer(str(lazylibrarian.CONFIG['SCAN_INTERVAL']))
        __M_writer('" class="form-control" placeholder="0 to disable">\n                      <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="How often to check for new downloads">Minutes</span>\n                    </div>\n                  </div>\n                  <div class="form-group">\n                    <label class="control-label">Post-Processing Delay:</label>\n                    <div class="input-group">\n                      <input type="number" id="pp_delay" name="pp_delay" value="')
        __M_writer(str(lazylibrarian.CONFIG['PP_DELAY']))
        __M_writer('" class="form-control" placeholder="0 to disable">\n                      <span class="input-group-addon" data-toggle="tooltip" data-placement="bottom" title="How long to wait after download is complete before processing">Seconds</span>\n                    </div>\n                  </div>\n                  <div class="form-group">\n                    <label for="versioncheck_interval" class="control-label">Version Check Interval:</label>\n                    <div class="input-group">\n                      <input type="number" id="versioncheck_interval" name="versioncheck_interval" value="')
        __M_writer(str(lazylibrarian.CONFIG['VERSIONCHECK_INTERVAL']))
        __M_writer('" class="form-control" placeholder="0 to disable" >\n                      <span class="input-group-addon">Hours</span>\n                    </div>\n                    ')

        if lazylibrarian.CONFIG['AUTO_UPDATE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="auto_update" class="control-label">\n                      <input type="checkbox" id="auto_update" name="auto_update" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Auto Update when new version found</label>\n                    <span class="help-block">This will auto update if the task finds a new version. Does not apply to manual version checks</span>\n                  </div>\n                  <div class="help-block">Setting a scan interval to zero disables the task</div>\n                </fieldset>\n                <legend>Status</legend>\n                  <div class="form-group">\n                    <label for="notfound_status">Missing Book Status:</label>\n                    <select id="notfound_status" name="notfound_status" class="form-control">\n')
        for nf_status in config['status_list']:
            __M_writer('                      ')

            selected = ''
            if nf_status == lazylibrarian.CONFIG['NOTFOUND_STATUS']:
                    selected = 'selected="selected"'
                                    
            
            __M_writer('\n                      <option value="')
            __M_writer(str(nf_status))
            __M_writer('" ')
            __M_writer(str(selected))
            __M_writer('>')
            __M_writer(str(nf_status))
            __M_writer('</option>\n')
        __M_writer('                    </select>\n                    <span class="help-block">Status for missing/deleted ebooks</span>\n                  </div>\n')
        if lazylibrarian.CONFIG['EBOOK_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="newbook_status">New Book Status:</label>\n                    <select id="newbook_status" name="newbook_status" class="form-control">\n')
            for nb_status in config['status_list']:
                __M_writer('                      ')

                selected = ''
                if nb_status == lazylibrarian.CONFIG['NEWBOOK_STATUS']:
                        selected = 'selected="selected"'
                                        
                
                __M_writer('\n                      <option value="')
                __M_writer(str(nb_status))
                __M_writer('" ')
                __M_writer(str(selected))
                __M_writer('>')
                __M_writer(str(nb_status))
                __M_writer('</option>\n')
            __M_writer('                    </select>\n                    <span class="help-block">Status for new ebooks by existing authors</span>\n                  </div>\n')
        if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="newaudio_status">New AudioBook Status:</label>\n                    <select id="newaudio_status" name="newaudio_status" class="form-control">\n')
            for nb_status in config['status_list']:
                __M_writer('                      ')

                selected = ''
                if nb_status == lazylibrarian.CONFIG['NEWAUDIO_STATUS']:
                    selected = 'selected="selected"'
                                        
                
                __M_writer('\n                      <option value="')
                __M_writer(str(nb_status))
                __M_writer('" ')
                __M_writer(str(selected))
                __M_writer('>')
                __M_writer(str(nb_status))
                __M_writer('</option>\n')
            __M_writer('                    </select>\n                    <span class="help-block">Status for new audiobooks by existing authors</span>\n                  </div>\n')
        if lazylibrarian.CONFIG['EBOOK_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="newauthor_status">New Authors eBook Status:</label>\n                    <select id="newauthor_status" name="newauthor_status" class="form-control">\n')
            for na_status in config['status_list']:
                __M_writer('                      ')

                selected = ''
                if na_status == lazylibrarian.CONFIG['NEWAUTHOR_STATUS']:
                    selected = 'selected="selected"'
                                      
                
                __M_writer('\n                      <option value="')
                __M_writer(str(na_status))
                __M_writer('" ')
                __M_writer(str(selected))
                __M_writer('>')
                __M_writer(str(na_status))
                __M_writer('</option>\n')
            __M_writer('                    </select>\n                    <span class="help-block">Status for ebooks by new authors</span>\n                  </div>\n')
        if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="newauthor_audio">New Authors AudioBook Status:</label>\n                    <select id="newauthor_audio" name="newauthor_audio" class="form-control">\n')
            for na_status in config['status_list']:
                __M_writer('                      ')

                selected = ''
                if na_status == lazylibrarian.CONFIG['NEWAUTHOR_AUDIO']:
                    selected = 'selected="selected"'
                                      
                
                __M_writer('\n                      <option value="')
                __M_writer(str(na_status))
                __M_writer('" ')
                __M_writer(str(selected))
                __M_writer('>')
                __M_writer(str(na_status))
                __M_writer('</option>\n')
            __M_writer('                    </select>\n                    <span class="help-block">Status for audiobooks by new authors</span>\n                  </div>\n')
        __M_writer('                  <div class="form-group">\n                    <label for="found_status">New Found Status:</label>\n                    <select id="found_status" name="found_status" class="form-control">\n')
        for na_status in ['Open', 'Have']:
            __M_writer('                      ')

            selected = ''
            if na_status == lazylibrarian.CONFIG['FOUND_STATUS']:
                selected = 'selected="selected"'
                                  
            
            __M_writer('\n                      <option value="')
            __M_writer(str(na_status))
            __M_writer('" ')
            __M_writer(str(selected))
            __M_writer('>')
            __M_writer(str(na_status))
            __M_writer('</option>\n')
        __M_writer('                    </select>\n                    <span class="help-block">Status for new downloads and items found on scan</span>\n                  </div>\n                  <div class="form-group">\n                    <label for="newseries_status">New Series Status:</label>\n                    <select id="newseries_status" name="newseries_status" class="form-control">\n')
        for na_status in ['Active', 'Paused', 'Wanted']:
            __M_writer('                      ')

            selected = ''
            if na_status == lazylibrarian.CONFIG['NEWSERIES_STATUS']:
                selected = 'selected="selected"'
                                  
            
            __M_writer('\n                      <option value="')
            __M_writer(str(na_status))
            __M_writer('" ')
            __M_writer(str(selected))
            __M_writer('>')
            __M_writer(str(na_status))
            __M_writer('</option>\n')
        __M_writer('                    </select>\n                    <span class="help-block">Should we monitor/download new books in the series</span>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['NEWAUTHOR_BOOKS'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="newauthor_books" class="control-label">\n                      <input type="checkbox" id="newauthor_books" name="newauthor_books" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Include other books by new authors</label>\n                    <span class="help-block">This will include details for other books by new authors found in wishlists or csv files,<br>\n                      or when manually importing a book by a new author</span>\n                  </div>\n                  <fieldset>\n                  <legend>External Programs</legend>\n                  <div class="form-group">\n                    <label for="ext_preprocess">Additional PreProcessor program:</label>\n                    <input type="text" id="ext_preprocess" name="ext_preprocess" value="')
        __M_writer(str(lazylibrarian.CONFIG['EXT_PREPROCESS']))
        __M_writer('" class="form-control">\n                    <span class="help-block">Path to additional preprocessor to run before importing books into the library</span>\n                    <input type="button" value="Test preprocessor" id="testpreprocessor" class="btn btn-default" />\n                  </div>\n                  <div class="form-group">\n                    <label for="ebook_convert">ebook-convert program:</label>\n                    <input type="text" id="ebook_convert" name="ebook_convert" value="')
        __M_writer(str(lazylibrarian.CONFIG['EBOOK_CONVERT']))
        __M_writer('" class="form-control" placeholder="ebook-convert program">\n                    <span class="help-block">Path to "ebook-convert" to convert book formats</span>\n                    <input type="button" value="Test ebook-convert" id="testebookconvert" class="btn btn-default" />\n                  </div>\n                  <div class="form-group">\n                    <label for="ffmpeg">ffmpeg program:</label>\n                    <input type="text" id="ffmpeg" name="ffmpeg" value="')
        __M_writer(str(lazylibrarian.CONFIG['FFMPEG']))
        __M_writer('" class="form-control" placeholder="ffmpeg program">\n                    <span class="help-block">Path to "ffmpeg" to merge audiobook parts or add tags</span>\n                  </div>\n                  <div class="form-group">\n                    <label for="ffmpeg">ffmpeg output extension:</label>\n                    <input type="text" id="ffmpeg_out" name="ffmpeg_out" value="')
        __M_writer(str(lazylibrarian.CONFIG['FFMPEG_OUT']))
        __M_writer('" class="form-control" placeholder="leave blank to use input extension">\n                    <span class="help-block">If you need to force a particular output type</span>\n                    <input type="button" value="Test ffmpeg" id="testffmpeg" class="btn btn-default" />\n                  </div>\n                  <div class="form-group">\n                    <label for="git_program">git program:</label>\n                    <input type="text" placeholder="git program" id="git_program" name="git_program" value="')
        __M_writer(str(lazylibrarian.CONFIG['GIT_PROGRAM']))
        __M_writer('" class="form-control">\n                    <span class="help-block">Git program unless already in your path. Usually leave this blank</span>\n                  </div>\n                  </fieldset>\n                  <legend>Calibre</legend>\n                  <fieldset>\n                  <div class="form-group">\n                    <label for="imp_calibredb">Calibredb import program:</label>\n                    <input type="text" id="imp_calibredb" name="imp_calibredb" value="')
        __M_writer(str(lazylibrarian.CONFIG['IMP_CALIBREDB']))
        __M_writer('" class="form-control" placeholder="calibredb program">\n                    <span class="help-block">Path to "calibredb" to import books into a calibre library</span>\n                    <input type="button" value="Test calibredb" id="testCalibredb" class="btn btn-default" />\n                  </div>\n                  <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['CALIBRE_USE_SERVER'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="calibre_use_server" class="control-label">\n                        <input type="checkbox" id="calibre_use_server" name="calibre_use_server" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Use Calibre Content Server</label>\n                  </div>\n                  </fieldset>\n                  <fieldset id="calibre_options">\n                  <div class="form-group">\n                    <label for="calibre_server">Calibre Server:</label>\n                    <input type="text" id="calibre_server" name="calibre_server" value="')
        __M_writer(str(lazylibrarian.CONFIG['CALIBRE_SERVER']))
        __M_writer('" class="form-control">\n                    <span class="help-block">eg http://my_calibre_server:9000</span>\n                  </div>\n                  <div class="form-group">\n                    <label for="calibre_user">Calibre Username:</label>\n                    <input type="text" id="calibre_user" name="calibre_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['CALIBRE_USER']))
        __M_writer('" class="form-control">\n                  </div>\n                  <div class="form-group">\n                    <label for="calibre_pass">Calibre Password:</label>\n                    <input type="password" id="calibre_pass" name="calibre_pass" value="')
        __M_writer(str(lazylibrarian.CONFIG['CALIBRE_PASS']))
        __M_writer('" class="form-control">\n                  </div>\n                  </fieldset>\n                  <fieldset>\n                  <div class="form-group">\n                    <label for="imp_autoadd">Calibre Books Auto Add Directory:</label>\n                    <input type="text" id="imp_autoadd" name="imp_autoadd" value="')
        __M_writer(str(lazylibrarian.CONFIG['IMP_AUTOADD']))
        __M_writer('" class="form-control">\n                    <span class="help-block">Directory for a copy to be placed for auto add process</span>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_CALIBRE_EBOOK'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="imp_calibre_ebook">\n                      <input type="checkbox" id="imp_calibre_ebook" name="imp_calibre_ebook" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Use calibredb to import ebooks</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_CALIBRE_COMIC'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="imp_calibre_comic">\n                      <input type="checkbox" id="imp_calibre_comic" name="imp_calibre_comic" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Use calibredb to import comics</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_CALIBRE_MAGAZINE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="imp_calibre_magazine">\n                      <input type="checkbox" id="imp_calibre_magazine" name="imp_calibre_magazine" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Use calibredb to import magazines</label>\n                  </div>\n                 <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_CALIBRE_MAGTITLE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="imp_calibre_magtitle">\n                      <input type="checkbox" id="imp_calibre_magtitle" name="imp_calibre_magtitle" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Use magazine title as author</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_CALIBRE_MAGISSUE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="imp_calibre_magissue">\n                      <input type="checkbox" id="imp_calibre_magissue" name="imp_calibre_magissue" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Use magazine issue as title</label>\n                  </div>\n                   <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_AUTOADD_COPY'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="imp_autoadd_copy">\n                      <input type="checkbox" id="imp_autoadd_copy" name="imp_autoadd_copy" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Keep a copy of the book in the local library</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_AUTOADD_BOOKONLY'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="imp_autoadd_bookonly">\n                      <input type="checkbox" id="imp_autoadd_bookonly" name="imp_autoadd_bookonly" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Only send calibre the eBook, not opf or jpg</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['OPF_TAGS'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="opf_tags">\n                      <input type="checkbox" id="opf_tags" name="opf_tags" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Add tags included with download to Calibre</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['GENRE_TAGS'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="genre_tags">\n                      <input type="checkbox" id="genre_tags" name="genre_tags" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Add genres as tags to Calibre</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['WISHLIST_TAGS'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="wishlist_tags">\n                      <input type="checkbox" id="wishlist_tags" name="wishlist_tags" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Add wishlist name as tag to Calibre</label>\n                  </div>\n                  </fieldset>\n                  <fieldset>\n                  <div class="form-group">\n                    <label for="imp_autoadd">Calibre Magazines Auto Add Directory:</label>\n                    <input type="text" id="imp_autoaddmag" name="imp_autoaddmag" value="')
        __M_writer(str(lazylibrarian.CONFIG['IMP_AUTOADDMAG']))
        __M_writer('" class="form-control">\n                    <span class="help-block">Directory for a copy to be placed for auto add process</span>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_AUTOADDMAG_COPY'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="imp_autoaddmag_copy">\n                      <input type="checkbox" id="imp_autoaddmag_copy" name="imp_autoaddmag_copy" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Keep a copy of the magazine in the local library</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_AUTOADD_MAGONLY'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="imp_autoadd_magonly">\n                      <input type="checkbox" id="imp_autoadd_magonly" name="imp_autoadd_magonly" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Only add magazine, not opf or jpg</label>\n                  </div>\n                  </fieldset>\n              </div>\n              <div class="col-md-4">\n                <fieldset>\n                  <legend>Name Formatting</legend>\n                  <div class="form-group">\n                    <label for="name_postfix">Author Name suffix</label>\n                    <input type="text" id="name_postfix" name="name_postfix" value="')
        __M_writer(str(lazylibrarian.CONFIG['NAME_POSTFIX']))
        __M_writer('" class="form-control" placeholder="eg snr, jnr">\n                    <span class="help-block">Comma separated list of suffixes to ignore when showing surname first</span>\n                  </div>\n                  <div class="form-group">\n                    <label for="name_postfix">Definite Articles</label>\n                    <input type="text" id="name_definite" name="name_definite" value="')
        __M_writer(str(lazylibrarian.CONFIG['NAME_DEFINITE']))
        __M_writer('" class="form-control" placeholder="eg The, A, Les">\n                    <span class="help-block">Comma separated list of definite articles for sorting titles</span>\n                  </div>\n                  <div class="form-group">\n                    <label for="name_postfix">Title prefix stripping</label>\n                    <input type="text" id="imp_nosplit" name="imp_nosplit" value="')
        __M_writer(str(lazylibrarian.CONFIG['IMP_NOSPLIT']))
        __M_writer('" class="form-control" placeholder="eg Doctor Who">\n                    <span class="help-block">Comma separated list of prefixes to ignore when splitting titles</span>\n                  </div>\n                  <legend>Filename Formatting</legend>\n                    <span class="help-block">Note: Calibre may override ebook folder and filename patterns</span>\n                  <div class="form-group">\n                    <label for="fmt_series">Series Pattern: ($Series variable)</label>\n                    <input type="text" id="fmt_series" name="fmt_series" value="')
        __M_writer(str(lazylibrarian.CONFIG['FMT_SERIES']))
        __M_writer('" class="form-control" placeholder="eg ($SerName #$SerNum)">\n                    <span class="help-block">Options: $SerName, $FmtName, $SerNum, $FmtNum, $PadNum, $PubYear, $SerYear, $$, any string.</span>\n                    <small>Example:  <mark>')
        __M_writer(str(config['namevars']['Series']))
        __M_writer('</mark></small>\n                  </div>\n                  <div class="form-group">\n                    <label for="fmt_sername">Series Name Pattern: ($FmtName variable)</label>\n                    <input type="text" id="fmt_sername" name="fmt_sername" value="')
        __M_writer(str(lazylibrarian.CONFIG['FMT_SERNAME']))
        __M_writer('" class="form-control" placeholder="eg $SerName">\n                    <span class="help-block">Options: $SerName, $PubYear, $SerYear, $$, any string.</span>\n                    <small>Example:  <mark>')
        __M_writer(str(config['namevars']['FmtName']))
        __M_writer('</mark></small>\n                  </div>\n                  <div class="form-group">\n                    <label for="fmt_sernum">Series Number Pattern: ($FmtNum variable)</label>\n                    <input type="text" id="fmt_sernum" name="fmt_sernum" value="')
        __M_writer(str(lazylibrarian.CONFIG['FMT_SERNUM']))
        __M_writer('" class="form-control" placeholder="eg Book #$SerNum">\n                    <span class="help-block">Options: $SerNum, $PadNum, $PubYear, $SerYear, $$, any string.</span>\n                    <small>Example:  <mark>')
        __M_writer(str(config['namevars']['FmtNum']))
        __M_writer('</mark></small>\n                  </div>\n                  <div class="form-group">\n                    <label for="ebook_dest_folder">eBook Foldername Pattern:</label>\n                    <input type="text" id="ebook_dest_folder" name="ebook_dest_folder" value="')
        __M_writer(str(lazylibrarian.CONFIG['EBOOK_DEST_FOLDER']))
        __M_writer('" class="form-control" placeholder="eBook Destination Folder">\n                    <span class="help-block">Options: $Author, $SortAuthor, $Title, $SortTitle, $Series, $SerName, $SerNum, $FmtName, $FmtNum, $PadNum, $PubYear, $SerYear, $Abridged, $$, any string.<br/>\n                      <strong>Current limitation: Each title has to be in unique subfolder</strong></span>\n                    <small>Example:  <mark>')
        __M_writer(str(config['namevars']['FolderName']))
        __M_writer('</mark></small>\n                  </div>\n                  <div class="form-group">\n                    <label for="ebook_dest_file">eBook Filename Pattern:</label>\n                    <input type="text" id="ebook_dest_file" name="ebook_dest_file" value="')
        __M_writer(str(lazylibrarian.CONFIG['EBOOK_DEST_FILE']))
        __M_writer('" class="form-control" placeholder="eBook Destination File">\n                    <span class="help-block">Options: $Author, $SortAuthor, $Title, $SortTitle, $Series, $SerName, $SerNum, $FmtName, $FmtNum, $PadNum, $PubYear, $SerYear, $Abridged, $$, any string.<br/>\n                      <strong>Current limitation: Each title has to be in unique subfolder</strong></span>\n                      <small>Example:  <mark>')
        __M_writer(str(config['namevars']['BookFile']))
        __M_writer('</mark></small>\n                  </div>\n')
        if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="audiobook_dest_folder">AudioBook Foldername Pattern:</label>\n                    <input type="text" id="audiobook_dest_folder" name="audiobook_dest_folder" value="')
            __M_writer(str(lazylibrarian.CONFIG['AUDIOBOOK_DEST_FOLDER']))
            __M_writer('" class="form-control" placeholder="AudioBook Destination Folder">\n                    <span class="help-block">Options: $Author, $SortAuthor, $Title, $SortTitle, $Series, $SerName, $SerNum, $FmtName, $FmtNum, $PadNum, $PubYear, $SerYear, $Abridged, $$, any string.<br/>\n                      <strong>Current limitation: Each title has to be in unique subfolder</strong></span>\n                    <small>Example:  <mark>')
            __M_writer(str(config['namevars']['AudioFolderName']))
            __M_writer('</mark></small>\n                  </div>\n                  <div class="form-group">\n                    <label for="audiobook_dest_file">AudioBook Filename Pattern:</label>\n                    <input type="text" id="audiobook_dest_file" name="audiobook_dest_file" value="')
            __M_writer(str(lazylibrarian.CONFIG['AUDIOBOOK_DEST_FILE']))
            __M_writer('" class="form-control" placeholder="audioBook Destination File">\n                    <span class="help-block">Options: $Author, $SortAuthor, $Title, $SortTitle, $Series, $SerName, $SerNum, $FmtName, $FmtNum, $PadNum, $PubYear, $SerYear, $Abridged, $Part, $Total, $$, any string.<br/>\n                      <strong>Current limitation: Has to include $Title or $SortTitle and $Part</strong></span>\n                      <small>Example:  <mark>')
            __M_writer(str(config['namevars']['AudioFile']))
            __M_writer('</mark></small>\n                  </div>\n                  <div class="form-group">\n                    <label for="audiobook_single_file">AudioBook Filename Pattern for single file:</label>\n                    <input type="text" id="audiobook_single_file" name="audiobook_single_file" value="')
            __M_writer(str(lazylibrarian.CONFIG['AUDIOBOOK_SINGLE_FILE']))
            __M_writer('" class="form-control" placeholder="Single file audioBook">\n                    <span class="help-block">Options: $Author, $SortAuthor, $Title, $SortTitle, $Series, $SerName, $SerNum, $FmtName, $FmtNum, $PadNum, $PubYear, $SerYear, $Abridged $$, any string.<br/>\n                      <strong>Current limitation: Has to include $Title or $SortTitle</strong></span>\n                      <small>Example:  <mark>')
            __M_writer(str(config['namevars']['AudioSingleFile']))
            __M_writer('</mark></small>\n                  </div>\n')
        __M_writer('                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['DESTINATION_COPY'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="destination_copy">\n                      <input type="checkbox" id="destination_copy" name="destination_copy" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Keep original files</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['ONE_FORMAT'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                            
        
        __M_writer('\n                    <label for="one_format">\n                      <input type="checkbox" id="one_format" name="one_format" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Only import one format of an ebook if multiple formats downloaded</label>\n                  </div>\n')
        if lazylibrarian.CONFIG['MAG_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="mag_dest_folder">Magazine Foldername Pattern:</label>\n                    <input type="text" id="mag_dest_folder" name="mag_dest_folder" value="')
            __M_writer(str(lazylibrarian.CONFIG['MAG_DEST_FOLDER']))
            __M_writer('" class="form-control" placeholder="Magazines Destination Folder">\n                    <span class="help-block">Absolute path, or inside book folder</span>\n                  </div>\n                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['MAG_RELATIVE'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                    <label for="mag_relative" class="control-label">\n                      <input type="checkbox" id="mag_relative" name="mag_relative" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Magazines inside book folder</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['MAG_DELFOLDER'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                    <label for="mag_delfolder" class="control-label">\n                      <input type="checkbox" id="mag_delfolder" name="mag_delfolder" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Delete folder and magazine details when last issue is removed</label>\n                  </div>\n                  <div class="form-group">\n                    <label for="mag_dest_file">Magazine Filename Pattern:</label>\n                    <input type="text" id="mag_dest_file" name="mag_dest_file" value="')
            __M_writer(str(lazylibrarian.CONFIG['MAG_DEST_FILE']))
            __M_writer('" class="form-control" placeholder="Magazine Issue Filename">\n                    <span class="help-block">Options: $Title, $IssueDate, any string\n                      <BR><strong>Current limitation: Filename must contain IssueDate</strong></span>\n                  </div>\n')
        if lazylibrarian.CONFIG['COMIC_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="comic_dest_folder">Comic Foldername Pattern:</label>\n                    <input type="text" id="comic_dest_folder" name="comic_dest_folder" value="')
            __M_writer(str(lazylibrarian.CONFIG['COMIC_DEST_FOLDER']))
            __M_writer('" class="form-control" placeholder="Comics Destination Folder">\n                    <span class="help-block">Absolute path, or inside book folder<br>Options: $Title, $Issue, $Publisher, any string</span>\n                  </div>\n                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['COMIC_RELATIVE'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                    <label for="comic_relative" class="control-label">\n                      <input type="checkbox" id="comic_relative" name="comic_relative" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Comics inside book folder</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['COMIC_DELFOLDER'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                    <label for="comic_delfolder" class="control-label">\n                      <input type="checkbox" id="comic_delfolder" name="comic_delfolder" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Delete folder and comic details when last issue is removed</label>\n                  </div>\n')
        __M_writer('                </fieldset>\n              </div>\n              <div class="col-md-4">\n                <fieldset>\n                  <legend>Folders</legend>\n                  <div class="form-group">\n                    <label for="download_dir" class="control-label">Download Directories:</label>\n                    <input type="text" id="download_dir" name="download_dir" value="')
        __M_writer(str(lazylibrarian.CONFIG['DOWNLOAD_DIR']))
        __M_writer('" class="form-control" placeholder="Download Directory">\n                    <span class="help-block">Comma separated list of folders where downloaders place books</span>\n                  </div>\n')
        if lazylibrarian.CONFIG['EBOOK_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="ebook_dir" class="control-label">eBook Library Folder:</label>\n                    <input type="text" id="ebook_dir" name="ebook_dir" value="')
            __M_writer(str(lazylibrarian.CONFIG['EBOOK_DIR']))
            __M_writer('" class="form-control" placeholder="eBook Library Folder">\n                  </div>\n')
        if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="audio_dir" class="control-label">AudioBook Library Folder:</label>\n                    <input type="text" id="audio_dir" name="audio_dir" value="')
            __M_writer(str(lazylibrarian.CONFIG['AUDIO_DIR']))
            __M_writer('" class="form-control" placeholder="AudioBook Library Folder">\n                  </div>\n')
        __M_writer('                  <div class="form-group">\n                    <label for="alternate_dir" class="control-label">Alternate Import/Export Folder:</label>\n                    <input type="text" id="alternate_dir" name="alternate_dir" value="')
        __M_writer(str(lazylibrarian.CONFIG['ALTERNATE_DIR']))
        __M_writer('" class="form-control" placeholder="Alternate Directory">\n                    <span class="help-block">Directory for wishlists and manually importing books<br>\n                      <strong>If "keep original files" is not set, LazyLibrarian can delete this folder after import</strong></span>\n                  </div>\n                  <legend>Permissions</legend>\n                  <div class="input-group">\n                    <span class="input-group-addon">File</span>\n                    <input type="text" id="file_perm" name="file_perm" value="')
        __M_writer(str(lazylibrarian.CONFIG['FILE_PERM'][2:]))
        __M_writer('" class="form-control" placeholder="644">\n                    <span class="input-group-addon">Directory</span>\n                    <input type="text" id="dir_perm" name="dir_perm" value="')
        __M_writer(str(lazylibrarian.CONFIG['DIR_PERM'][2:]))
        __M_writer('" class="form-control" placeholder="755">\n                    </div>\n                    <span class="help-block">Permissions should be 3 or 4 digits<br>Defaults are File:644 Directory:755</span>\n                  <legend>Miscellaneous</legend>\n                  <div class="form-group">\n                    <label for="cache_age" class="control-label">Cache expire after:</label>\n                    <div class="input-group">\n                      <input type="number" id="cache_age" name="cache_age" value="')
        __M_writer(str(lazylibrarian.CONFIG['CACHE_AGE']))
        __M_writer('" class="form-control" placeholder="0 to disable">\n                      <span class="input-group-addon">Days</span>\n                    </div>\n                  </div>\n')
        if lazylibrarian.CONFIG['MAG_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="mag_age" class="control-label">Max Magazine Issue Age:</label>\n                    <div class="input-group">\n                      <input type="number" id="mag_age" name="mag_age" value="')
            __M_writer(str(lazylibrarian.CONFIG['MAG_AGE']))
            __M_writer('" class="form-control" placeholder="0 to disable">\n                      <span class="input-group-addon">Days</span>\n                    </div>\n                  </div>\n')
        __M_writer('                  <div class="form-group">\n                    <label for="task_age" class="control-label">Remove failed tasks after:</label>\n                    <div class="input-group">\n                      <input type="number" id="task_age" name="task_age" value="')
        __M_writer(str(lazylibrarian.CONFIG['TASK_AGE']))
        __M_writer('" class="form-control" placeholder="0 to disable">\n                      <span class="input-group-addon">Hours</span>\n                    </div>\n                  </div>\n                  <div class="form-group">\n                    <label for="match_ratio">Search Match Ratio:</label>\n                    <div class="input-group">\n                      <input type="number" id="match_ratio" name="match_ratio" value="')
        __M_writer(str(lazylibrarian.CONFIG['MATCH_RATIO']))
        __M_writer('" class="form-control" placeholder="Search Match Ratio (percent)">\n                      <span class="input-group-addon">%</span>\n                    </div>\n                  </div>\n                  <div class="form-group">\n                    <label for="dload_ratio">Download Match Ratio:</label>\n                    <div class="input-group">\n                      <input type="number" id="dload_ratio" name="dload_ratio" value="')
        __M_writer(str(lazylibrarian.CONFIG['DLOAD_RATIO']))
        __M_writer('" class="form-control" placeholder="Download Match Ratio (percent)">\n                      <span class="input-group-addon">%</span>\n                    </div>\n                  </div>\n                  <div class="form-group">\n                    <label for="max_pages">Maximum Search Pages:</label>\n                    <input type="number" id="max_pages" name="max_pages" value="')
        __M_writer(str(lazylibrarian.CONFIG['MAX_PAGES']))
        __M_writer('" class="form-control" placeholder="0 for no limit">\n                  </div>\n                  <div class="form-group">\n                    <label for="max_bookpages">Maximum Author Pages:</label>\n                    <input type="number" id="max_bookpages" name="max_bookpages" value="')
        __M_writer(str(lazylibrarian.CONFIG['MAX_BOOKPAGES']))
        __M_writer('" class="form-control" placeholder="0 for no limit">\n                  </div>\n                  <div class="form-group">\n                    <label for="dload_ratio">Maximum Coverwall Images:</label>\n                    <input type="number" id="max_wall" name="max_wall" value="')
        __M_writer(str(lazylibrarian.CONFIG['MAX_WALL']))
        __M_writer('" class="form-control" placeholder="0 for no limit">\n                  </div>\n                </fieldset>\n                <fieldset>\n')
        if lazylibrarian.CONFIG['MAG_TAB'] == True:
            __M_writer('                  <div class="form-group">\n                    <label for="imp_convert">Cover creation program:</label>\n                    <input type="text" placeholder="Cover creation program" id="imp_convert" name="imp_convert" value="')
            __M_writer(str(lazylibrarian.CONFIG['IMP_CONVERT']))
            __M_writer('" class="form-control">\n                    <span class="help-block">Program for creating magazine covers (see wiki for details)  Leave blank to use a local copy of ghostscript, or PythonMagick or Wand interfaces to ImageMagick</span>\n                  </div>\n                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['IMP_MAGCOVER'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                    <label for="imp_magcover" class="control-label">\n                      <input type="checkbox" id="imp_magcover" name="imp_magcover" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Create cover files for magazines</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['IMP_MAGOPF'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                    <label for="imp_magopf" class="control-label">\n                      <input type="checkbox" id="imp_magopf" name="imp_magopf" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Create opf files for magazines</label>\n                  </div>\n')
        __M_writer('                </fieldset>\n                <fieldset>\n')
        if lazylibrarian.CONFIG['COMIC_TAB'] == True:
            __M_writer('                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['IMP_COMICCOVER'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                    <label for="imp_comiccover" class="control-label">\n                      <input type="checkbox" id="imp_comiccover" name="imp_comiccover" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Create cover files for comics</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['IMP_COMICOPF'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                    <label for="imp_comicopf" class="control-label">\n                      <input type="checkbox" id="imp_comicopf" name="imp_comicopf" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Create opf files for comics</label>\n                  </div>\n')
        __M_writer('                </fieldset>\n                <fieldset>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['FULL_SCAN'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="full_scan" class="control-label">\n                      <input type="checkbox" id="full_scan" name="full_scan" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Full scan</label>\n                    <span class="help-block">This will remove database entries for books removed from the download location or no longer listed at goodreads/googlebooks</span>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_SINGLEBOOK'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="imp_singlebook" class="control-label">\n                      <input type="checkbox" id="imp_singlebook" name="imp_singlebook" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Import one book per directory</label>\n                    <span class="help-block">Tick this if you keep multiple formats of the same book in the same directory</span>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_RENAME'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="imp_rename" class="control-label">\n                      <input type="checkbox" id="imp_rename" name="imp_rename" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Rename existing books on libraryscan</label>\n                  </div>\n')
        if lazylibrarian.CONFIG['MAG_TAB'] == True:
            __M_writer('                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['MAG_RENAME'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                    <label for="mag_rename" class="control-label">\n                      <input type="checkbox" id="mag_rename" name="mag_rename" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Rename existing magazines on libraryscan</label>\n                  </div>\n')
        __M_writer('                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['ADD_AUTHOR'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="add_author" class="control-label">\n                      <input type="checkbox" id="add_author" name="add_author" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Add New Authors</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['ADD_SERIES'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="add_series" class="control-label">\n                      <input type="checkbox" id="add_series" name="add_series" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Add Series Info</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['NO_SINGLE_BOOK_SERIES'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="no_single_book_series" class="control-label">\n                      <input type="checkbox" id="no_single_book_series" name="no_single_book_series" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Ignore single-book series</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['NO_NONINTEGER_SERIES'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="no_noninteger_series" class="control-label">\n                      <input type="checkbox" id="no_noninteger_series" name="no_noninteger_series" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Ignore non-integer series members</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['IMP_AUTOSEARCH'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="imp_autosearch" class="control-label">\n                      <input type="checkbox" id="imp_autosearch" name="imp_autosearch" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Search when added</label>\n                  </div>\n')
        if lazylibrarian.CONFIG['MAG_TAB'] == True:
            __M_writer('                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['MAG_SINGLE'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
                                
            
            __M_writer('\n                    <label for="mag_single" class="control-label">\n                      <input type="checkbox" id="mag_single" name="mag_single" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Quick open single issues of magazines</label>\n                  </div>\n')
        if lazylibrarian.CONFIG['COMIC_TAB'] == True:
            __M_writer('                  <div class="checkbox">\n                    ')

            if lazylibrarian.CONFIG['COMIC_SINGLE'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
                                
            
            __M_writer('\n                    <label for="comic_single" class="control-label">\n                      <input type="checkbox" id="comic_single" name="comic_single" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                      Quick open single issues of comics</label>\n                  </div>\n')
        __M_writer('                </fieldset>\n                <fieldset>\n                  <legend>eBook Conversions</legend>\n                  <div class="form-group">\n                    <label for="ebook_wanted_formats">eBook wanted formats:</label>\n                    <input type="text" id="ebook_wanted_formats" name="ebook_wanted_formats" value="')
        __M_writer(str(lazylibrarian.CONFIG['EBOOK_WANTED_FORMATS']))
        __M_writer('" class="form-control" placeholder="wanted formats">\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['KEEP_OPF'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="keep_opf" class="control-label">\n                      <input type="checkbox" id="keep_opf" name="keep_opf" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Keep downloaded opf</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['KEEP_JPG'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="keep_jpg" class="control-label">\n                      <input type="checkbox" id="keep_jpg" name="keep_jpg" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Keep downloaded jpg</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['DELETE_OTHER_FORMATS'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="delete_other_formats" class="control-label">\n                      <input type="checkbox" id="delete_other_formats" name="delete_other_formats" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Delete unwanted filetypes</label>\n                  </div>\n                  <legend>AudioBook Conversions</legend>\n                  <div class="form-group">\n                    <label for="audio_options">ffmpeg options:</label>\n                    <input type="text" id="audio_options" name="audio_options" value="')
        __M_writer(str(lazylibrarian.CONFIG['AUDIO_OPTIONS']))
        __M_writer('" class="form-control" placeholder="audio options">\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['CREATE_SINGLEAUDIO'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="create_singleaudio" class="control-label">\n                      <input type="checkbox" id="create_singleaudio" name="create_singleaudio" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Merge audiobook parts into one file</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['KEEP_SEPARATEAUDIO'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="keep_separateaudio" class="control-label">\n                      <input type="checkbox" id="keep_separateaudio" name="keep_separateaudio" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Also keep separate parts</label>\n                  </div>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['WRITE_AUDIOTAGS'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="write_audiotags" class="control-label">\n                      <input type="checkbox" id="write_audiotags" name="write_audiotags" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Write audio tags</label>\n                  </div>\n                  <legend>Magazine Conversions</legend>\n                  <div class="checkbox">\n                    ')

        if lazylibrarian.CONFIG['SWAP_COVERPAGE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                    <label for="swap_coverpage" class="control-label">\n                      <input type="checkbox" id="swap_coverpage" name="swap_coverpage" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                      Swap Coverpage</label>\n                  </div>\n                  <div class="form-group">\n                    <label for="shrink_mag">Resolution (dpi):</label>\n                    <input type="number" id="shrink_mag" name="shrink_mag" value="')
        __M_writer(str(lazylibrarian.CONFIG['SHRINK_MAG']))
        __M_writer('" class="form-control" placeholder="0 for no change">\n                  </div>\n                 </fieldset>\n              </div>\n            </div>\n            <br>\n          </div>\n        </div>\n        <div role="tabpanel" class="tab-pane" id="notifications">\n          <div class="configtable">\n            <div class="row">\n              <div class="col-md-6">\n')
        if lazylibrarian.CONFIG['HIDE_OLD_NOTIFIERS'] == False:
            __M_writer('                <div class="checkbox">\n                  ')

            if lazylibrarian.CONFIG['USE_TWITTER'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                  <label for="use_twitter">\n                    <input type="checkbox" id="use_twitter" name="use_twitter" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                    Enable Twitter Notifications</label>\n                </div>\n                <div id="twitteroptions">\n                  <fieldset>\n                    <legend>Twitter</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['TWITTER_NOTIFY_ONSNATCH'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="twitter_notify_onsnatch" class="control-label">\n                        <input type="checkbox" id="twitter_notify_onsnatch" name="twitter_notify_onsnatch" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on snatch</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['TWITTER_NOTIFY_ONDOWNLOAD'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="twitter_notify_ondownload">\n                        <input type="checkbox" id="twitter_notify_ondownload" name="twitter_notify_ondownload" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on download</label>\n                    </div>\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Request Authorization" id="twitterStep1" class="btn btn-default" />\n                    </div>\n                    <div class="form-group">\n                      <label for="twitter_key" class="control-label">Twitter Key</label>\n                      <input type="text" id="twitter_key" name="twitter_key" value="" placeholder="Twitter Authorization Key" class="form-control" />\n                      <span class="help-block">Enter the key from the twitter authorization page here, DO NOT press Enter or save the config. The key is single-use and will not be saved. Press [Verify Key] to complete authorization.</span>\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Verify Key" id="twitterStep2" class="btn btn-default" />\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Test Twitter" id="testTwitter" class="btn btn-default" />\n                    </div>\n                  </fieldset>\n                </div>\n                <div class="checkbox">\n                  ')

            if lazylibrarian.CONFIG['USE_BOXCAR'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                  <label for="use_boxcar" class="control-label">\n                    <input type="checkbox" id="use_boxcar" name="use_boxcar" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                    Enable boxcar Notifications</label>\n                </div>\n                <div id="boxcaroptions">\n                  <fieldset>\n                    <legend>Boxcar2</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['BOXCAR_NOTIFY_ONSNATCH'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="boxcar_notify_onsnatch" class="control-label">\n                        <input type="checkbox" id="boxcar_notify_onsnatch" name="boxcar_notify_onsnatch" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on snatch</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['BOXCAR_NOTIFY_ONDOWNLOAD'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="boxcar_notify_ondownload">\n                        <input type="checkbox" id="boxcar_notify_ondownload" name="boxcar_notify_ondownload" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on download</label>\n                    </div>\n                    </div>\n                    <div class="form-group">\n                      <label for="boxcar_token" class="control-label">Boxcar Token</label>\n                      <input type="text" id="boxcar_token" name="boxcar_token" value="')
            __M_writer(str(lazylibrarian.CONFIG['BOXCAR_TOKEN']))
            __M_writer('" placeholder="Boxcar token" class="form-control">\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Test Boxcar" id="testBoxcar" class="btn btn-default">\n                    </div>\n                  </fieldset>\n                </div>\n                <div class="checkbox">\n                  ')

            if lazylibrarian.CONFIG['USE_PUSHBULLET'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                  <label for="use_pushbullet" class="control-label">\n                    <input type="checkbox" id="use_pushbullet" name="use_pushbullet" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                    Enable Pushbullet Notifications</label>\n                </div>\n                <div id="pushbulletoptions">\n                  <fieldset>\n                    <legend>Pushbullet</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['PUSHBULLET_NOTIFY_ONSNATCH'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="pushbullet_notify_onsnatch">\n                        <input type="checkbox" id="pushbullet_notify_onsnatch" name="pushbullet_notify_onsnatch" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on snatch</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['PUSHBULLET_NOTIFY_ONDOWNLOAD'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="pushbullet_notify_ondownload">\n                        <input type="checkbox" id="pushbullet_notify_ondownload" name="pushbullet_notify_ondownload" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on download</label>\n                    </div>\n                    </div>\n                    <div class="form-group">\n                      <label for="pushbullet_token">Pushbullet API</label>\n                      <input type="text" id="pushbullet_token" name="pushbullet_token" value="')
            __M_writer(str(lazylibrarian.CONFIG['PUSHBULLET_TOKEN']))
            __M_writer('" class="form-control" placeholder="Pushbullet API">\n                    </div>\n                    <div class="form-group">\n                      <label for="pushbullet_deviceid" class="control-label">Device ID</label>\n                      <input type="text" id="pushbullet_deviceid" name="pushbullet_deviceid" value="')
            __M_writer(str(lazylibrarian.CONFIG['PUSHBULLET_DEVICEID']))
            __M_writer('" class="form-control" placeholder="Pushbullet DeviceID">\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Test Pushbullet" id="testPushbullet" class="btn btn-default">\n                    </div>\n                  </fieldset>\n                </div>\n                <div class="checkbox">\n                  ')

            if lazylibrarian.CONFIG['USE_PUSHOVER'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                  <label for="use_pushover" class="control-label">\n                    <input type="checkbox" id="use_pushover" name="use_pushover" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                    Enable Pushover Notifications</label>\n                </div>\n                <div id="pushoveroptions">\n                  <fieldset>\n                    <legend>Pushover</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['PUSHOVER_ONSNATCH'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="pushover_onsnatch">\n                        <input type="checkbox" id="pushover_onsnatch" name="pushover_onsnatch" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on snatch</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['PUSHOVER_ONDOWNLOAD'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="pushover_ondownload" class="control-label">\n                        <input type="checkbox" id="pushover_ondownload" name="pushover_ondownload" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on download</label>\n                    </div>\n                    </div>\n                    <div class="form-group">\n                      <label for="pushover_apitoken">Pushover API</label>\n                      <input type="text" id="pushover_apitoken" name="pushover_apitoken" value="')
            __M_writer(str(lazylibrarian.CONFIG['PUSHOVER_APITOKEN']))
            __M_writer('" class="form-control" placeholder="Pushover API Token">\n                    </div>\n                    <div class="form-group">\n                      <label for="pushover_keys" class="control-label">Pushover Keys</label>\n                      <input type="text" id="pushover_keys" name="pushover_keys" value="')
            __M_writer(str(lazylibrarian.CONFIG['PUSHOVER_KEYS']))
            __M_writer('" class="form-control" placeholder="Pushover Keys">\n                    </div>\n                    <div class="form-group">\n                      <label for="pushover_device" class="control-label">Pushover Device</label>\n                      <input type="text" id="pushover_device" name="pushover_device" value="')
            __M_writer(str(lazylibrarian.CONFIG['PUSHOVER_DEVICE']))
            __M_writer('" class="form-control" placeholder="Pushover Device">\n                    </div>\n                    <div class="form-group">\n                      <label for="pushover_priority" class="control-label">Pushover Priority</label>\n                      <input type="number" id="pushover_priority" name="pushover_priority" min=-2 max=1 value="')
            __M_writer(str(lazylibrarian.CONFIG['PUSHOVER_PRIORITY']))
            __M_writer('" class="form-control" placeholder="Pushover Priority">\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Test Pushover" id="testPushover" class="btn btn-default">\n                    </div>\n                  </fieldset>\n                </div>\n                <div class="checkbox">\n                  ')

            if lazylibrarian.CONFIG['USE_ANDROIDPN'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                  <label for="use_androidpn" class="control-label">\n                    <input type="checkbox" id="use_androidpn" name="use_androidpn" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                    Enable AndroidPN Notifications</label>\n                </div>\n                <div id="androidpnoptions">\n                  <fieldset>\n                    <legend>AndroidPN</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['ANDROIDPN_NOTIFY_ONSNATCH'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="androidpn_notify_onsnatch" class="control-label">\n                        <input type="checkbox" id="androidpn_notify_onsnatch" name="androidpn_notify_onsnatch" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on snatch</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['ANDROIDPN_NOTIFY_ONDOWNLOAD'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="androidpn_notify_ondownload" class="control-label">\n                        <input type="checkbox" id="androidpn_notify_ondownload" name="androidpn_notify_ondownload" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on download</label>\n                    </div>\n                    </div>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['ANDROIDPN_BROADCAST'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="androidpn_broadcast" class="control-label">\n                        <input type="checkbox" id="androidpn_broadcast" name="androidpn_broadcast" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Broadcast notification</label>\n                    </div>\n                    </div>\n                    <div class="form-group">\n                      <label for="androidpn_url" class="control-label">AndroidPN Notification URL</label>\n                      <input type="text" id="androidpn_url" name="androidpn_url" value="')
            __M_writer(str(lazylibrarian.CONFIG['ANDROIDPN_URL']))
            __M_writer('" class="form-control" placeholder="AndroidPN Notification URL" />\n                    </div>\n                    <div class="form-group">\n                      <label for="androidpn_username" class="control-label">Username</label>\n                      <input type="text" id="androidpn_username" name="androidpn_username"  value="')
            __M_writer(str(lazylibrarian.CONFIG['ANDROIDPN_USERNAME']))
            __M_writer('" class="form-control" placeholder="AndroidPN Username" />\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Test AndroidPN" id="testAndroidPN" class="btn btn-default" />\n                    </div>\n                  </fieldset>\n                </div>\n')
        __M_writer('                <div class="checkbox">\n                  ')

        if lazylibrarian.CONFIG['USE_EMAIL'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                  <label for="use_email" class="control-label">\n                    <input type="checkbox" id="use_email" name="use_email" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                    Enable Email Notifications</label>\n                </div>\n                <div id="emailoptions">\n                  <fieldset>\n                    <legend>Email</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['EMAIL_NOTIFY_ONSNATCH'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                              
        
        __M_writer('\n                      <label for="email_notify_onsnatch">\n                        <input type="checkbox" id="email_notify_onsnatch" name="email_notify_onsnatch" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Notify on snatch</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['EMAIL_NOTIFY_ONDOWNLOAD'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                      <label for="email_notify_ondownload">\n                        <input type="checkbox" id="email_notify_ondownload" name="email_notify_ondownload" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Notify on download</label>\n                    </div>\n                    </div>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['EMAIL_SENDFILE_ONDOWNLOAD'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                      <label for="email_sendfile_ondownload">\n                        <input type="checkbox" id="email_sendfile_ondownload" name="email_sendfile_ondownload" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Attach book on download</label>\n                    </div>\n                    </div>\n                    <div class="row form-group">\n                    <div class="col-md-6">\n                      <label for="email_from">Email From</label>\n                      <input type="text" id="email_from" name="email_from" value="')
        __M_writer(str(lazylibrarian.CONFIG['EMAIL_FROM']))
        __M_writer('" class="form-control" placeholder="Email From Address">\n                    </div>\n                    <div class="col-md-6">\n                      <label for="email_to">Email To</label>\n                      <input type="text" id="email_to" name="email_to" value="')
        __M_writer(str(lazylibrarian.CONFIG['EMAIL_TO']))
        __M_writer('" class="form-control" placeholder="Email To Address">\n                    </div>\n                    </div>\n                    <div class="row form-group">\n                    <div class="col-md-6">\n                      <label for="email_smtp_server">SMTP Server</label>\n                      <input type="text" id="email_smtp_server" name="email_smtp_server" value="')
        __M_writer(str(lazylibrarian.CONFIG['EMAIL_SMTP_SERVER']))
        __M_writer('" class="form-control" placeholder="SMTP Server">\n                    </div>\n                    <div class="col-md-6">\n                      <label for="email_smtp_port">SMTP Port</label>\n                      <input type="number" id="email_smtp_port" name="email_smtp_port" value="')
        __M_writer(str(lazylibrarian.CONFIG['EMAIL_SMTP_PORT']))
        __M_writer('" class="form-control" placeholder="SMTP Port">\n                    </div>\n                    </div>\n                    <div class="row form-group">\n                    <div class="col-md-6">\n                      <label for="email_smtp_user">SMTP User</label>\n                      <input type="text" id="email_smtp_user" name="email_smtp_user" value="')
        __M_writer(str(lazylibrarian.CONFIG['EMAIL_SMTP_USER']))
        __M_writer('" class="form-control" placeholder="SMTP User">\n                    </div>\n                    <div class="col-md-6">\n                      <label for="email_smtp_password">SMTP Password</label>\n                      <input type="password" id="email_smtp_password" name="email_smtp_password" value="')
        __M_writer(str(lazylibrarian.CONFIG['EMAIL_SMTP_PASSWORD']))
        __M_writer('" class="form-control" placeholder="SMTP Password">\n                    </div>\n                    </div>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['EMAIL_SSL'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                      <label for="email_ssl">\n                        <input type="checkbox" id="email_ssl" name="email_ssl" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        SSL</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['EMAIL_TLS'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                      <label for="email_tls">\n                        <input type="checkbox" id="email_tls" name="email_tls" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        TLS</label>\n                    </div>\n                    </div>\n                    <div class="checkbox">\n                      ')

        if lazylibrarian.CONFIG['USE_EMAIL_CUSTOM_FORMAT'] == True:
          checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                      <label for="use_email_custom_format" class="control-label">\n                        <input type="checkbox" id="use_email_custom_format" name="use_email_custom_format" value="1"\n                               ')
        __M_writer(str(checked))
        __M_writer('/>\n                        Enable Email Custom Type (requires full Calibre install)</label>\n                    </div>\n                    <div id="email_custom_format_options">\n                      <span class="help-block">Send a different file type than the one downloaded and convert if necessary. Useful if you download ePUB files but need to send a MOBI to a Kindle. Only file types listed here will be converted.</span>\n                      <fieldset>\n                        <div class="row form-group">\n                          <div class="col-md-6">\n                            <label for="email_send_type">Filetype to send</label>\n                            <input type="text" id="email_send_type" name="email_send_type"\n                                   value="')
        __M_writer(str(lazylibrarian.CONFIG['EMAIL_SEND_TYPE']))
        __M_writer('" class="form-control"\n                                   placeholder="mobi">\n                          </div>\n                          <div class="col-md-6">\n                            <label for="email_convert_from">Filetypes to convert from</label>\n                            <input type="text" id="email_convert_from" name="email_convert_from"\n                                   value="')
        __M_writer(str(lazylibrarian.CONFIG['EMAIL_CONVERT_FROM']))
        __M_writer('" class="form-control"\n                                   placeholder="epub">\n                          </div>\n                        </div>\n                      </fieldset>\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Test Email" id="testEmail" class="btn btn-default">\n                    </div>\n                  </fieldset>\n                </div>\n              </div>\n              <div class="col-md-6">\n')
        if lazylibrarian.CONFIG['HIDE_OLD_NOTIFIERS'] == False:
            __M_writer('                <div class="checkbox">\n                  ')

            if lazylibrarian.CONFIG['USE_PROWL'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                  <label for="use_prowl" class="control-label">\n                    <input type="checkbox" name="use_prowl" id="use_prowl" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                    Enable Prowl</label>\n                </div>\n                <div id="prowloptions">\n                  <fieldset>\n                    <legend>Prowl</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['PROWL_ONSNATCH'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="prowl_onsnatch" class="control-label">\n                        <input type="checkbox" id="prowl_onsnatch" name="prowl_onsnatch" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on snatch</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['PROWL_ONDOWNLOAD'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="prowl_ondownload" class="control-label">\n                        <input type="checkbox" id="prowl_ondownload" name="prowl_ondownload" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on download</label>\n                    </div>\n                    </div>\n                    <div class="form-group">\n                      <label for="prowl_apikey" class="control-label">Prowl API Key</label>\n                      <input type="text" id="prowl_apikey" name="prowl_apikey" value="')
            __M_writer(str(lazylibrarian.CONFIG['PROWL_APIKEY']))
            __M_writer('" class="form-control" placeholder="Prowl API Key">\n                      <span class="help-block">Separate multiple api keys with commas</span>\n                    </div>\n                    <div class="form-group">\n                      <label for="prowl_priority" class="control-label">Priority</label>\n                      <select id="prowl_priority" name="prowl_priority" class="form-control">\n')
            for x in [-2,-1,0,1,2]:
                __M_writer('                        ')

                if lazylibrarian.CONFIG['PROWL_PRIORITY'] == x:
                    prowl_priority_selected = 'selected'
                else:
                    prowl_priority_selected = ''
                
                if x == -2:
                    prowl_priority_value = 'Very Low'
                elif x == -1:
                    prowl_priority_value = 'Moderate'
                elif x == 0:
                    prowl_priority_value = 'Normal'
                elif x == 1:
                    prowl_priority_value = 'High'
                else:
                    prowl_priority_value = 'Emergency'
                                        
                
                __M_writer('\n                        <option value="')
                __M_writer(str(x))
                __M_writer('" ')
                __M_writer(str(prowl_priority_selected))
                __M_writer('>')
                __M_writer(str(prowl_priority_value))
                __M_writer('</option>\n')
            __M_writer('                      </select>\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Test Prowl" id="testProwl" class="btn btn-default" />\n                    </div>\n                  </fieldset>\n                </div>\n                <div class="checkbox">\n                  ')

            if lazylibrarian.CONFIG['USE_GROWL'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                  <label for="use_growl" class="control-label">\n                    <input type="checkbox" name="use_growl" id="use_growl" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                    Enable Growl</label>\n                </div>\n                <div id="growloptions">\n                  <fieldset>\n                    <legend>Growl</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['GROWL_ONSNATCH'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="growl_onsnatch" class="control-label">\n                        <input type="checkbox" id="growl_onsnatch" name="growl_onsnatch" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on snatch</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['GROWL_ONDOWNLOAD'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="growl_ondownload" class="control-label">\n                        <input type="checkbox" id="growl_ondownload" name="growl_ondownload" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on download</label>\n                    </div>\n                    </div>\n                    <div class="input-group">\n                      <span class="input-group-addon">Host</span>\n                      <input type="text" id="growl_host" name="growl_host" value="')
            __M_writer(str(lazylibrarian.CONFIG['GROWL_HOST']))
            __M_writer('" class="form-control" placeholder="eg localhost:23053">\n                      <span class="input-group-addon">Password</span>\n                      <input type="number" id="growl_password" name="growl_password" value="')
            __M_writer(str(lazylibrarian.CONFIG['GROWL_PASSWORD']))
            __M_writer('" class="form-control" placeholder="none">\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Test Growl" id="testGrowl" class="btn btn-default" />\n                    </div>\n                  </fieldset>\n                </div>\n                <div class="checkbox">\n                  ')

            if lazylibrarian.CONFIG['USE_TELEGRAM'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                  <label for="use_telegram" class="control-label">\n                    <input type="checkbox" name="use_telegram" id="use_telegram" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                    Enable Telegram</label>\n                </div>\n                <div id="telegramoptions">\n                  <fieldset>\n                    <legend>Telegram</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['TELEGRAM_ONSNATCH'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="telegram_onsnatch" class="control-label">\n                        <input type="checkbox" id="telegram_onsnatch" name="telegram_onsnatch" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on snatch</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['TELEGRAM_ONDOWNLOAD'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="telegram_ondownload" class="control-label">\n                        <input type="checkbox" id="telegram_ondownload" name="telegram_ondownload" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on download</label>\n                    </div>\n                    </div>\n                    <div class="form-group">\n                      <label for="telegram_token" class="control-label">Telegram Token</label>\n                      <input type="text" id="telegram_token" name="telegram_token" value="')
            __M_writer(str(lazylibrarian.CONFIG['TELEGRAM_TOKEN']))
            __M_writer('" class="form-control" placeholder="Telegram Token"><small>Contact <a href="http://telegram.me/BotFather">@BotFather</a> to create a bot and get its token\n                      <br>After creating the bot, send it a message from telegram to activate it</small>\n                    </div>\n                    <div class="form-group">\n                      <label for="telegram_userid" class="control-label">Telegram UserID</label>\n                      <input type="text" id="telegram_userid" name="telegram_userid" value="')
            __M_writer(str(lazylibrarian.CONFIG['TELEGRAM_USERID']))
            __M_writer('" class="form-control" placeholder="Telegram UserID"><small>Contact <a href="http://telegram.me/myidbot">@myidbot</a> to get your user ID</small>\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Test Telegram" id="testTelegram" class="btn btn-default" />\n                    </div>\n                  </fieldset>\n                </div>\n                <div class="checkbox">\n                  ')

            if lazylibrarian.CONFIG['USE_SLACK'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                  <label for="use_slack" class="control-label">\n                    <input type="checkbox" id="use_slack" name="use_slack" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                    Enable Slack Notifications</label>\n                </div>\n                <div id="slackoptions">\n                  <fieldset>\n                    <legend>Slack</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['SLACK_NOTIFY_ONSNATCH'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="slack_notify_onsnatch">\n                        <input type="checkbox" id="slack_notify_onsnatch" name="slack_notify_onsnatch" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on snatch</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

            if lazylibrarian.CONFIG['SLACK_NOTIFY_ONDOWNLOAD'] == True:
                checked = 'checked="checked"'
            else:
                checked = ''
            
            
            __M_writer('\n                      <label for="slack_notify_ondownload">\n                        <input type="checkbox" id="slack_notify_ondownload" name="slack_notify_ondownload" value="1" ')
            __M_writer(str(checked))
            __M_writer(' />\n                        Notify on download</label>\n                    </div>\n                    </div>\n                    <div class="form-group">\n                      <label for="slack_url">Slack Webhook URL (usually https://hooks.slack.com/services/)</label>\n                      <input type="text" id="slack_url" name="slack_url" value="')
            __M_writer(str(lazylibrarian.CONFIG['SLACK_URL']))
            __M_writer('" class="form-control" placeholder="Slack Webhook URL">\n                    </div>\n                    <div class="form-group">\n                      <label for="slack_token">Slack Webhook Token (everything after https://hooks.slack.com/services/)</label>\n                      <input type="text" id="slack_token" name="slack_token" value="')
            __M_writer(str(lazylibrarian.CONFIG['SLACK_TOKEN']))
            __M_writer('" class="form-control" placeholder="Slack Webhook Token">\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Test Slack" id="testSlack" class="btn btn-default">\n                    </div>\n                  </fieldset>\n                </div>\n')
        __M_writer('                <div class="checkbox">\n                  ')

        if lazylibrarian.CONFIG['USE_CUSTOM'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                  <label for="use_custom" class="control-label">\n                    <input type="checkbox" id="use_custom" name="use_custom" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                    Enable Custom Notifications</label>\n                </div>\n                <div id="customoptions">\n                  <fieldset>\n                    <legend>Custom</legend>\n                    <div class="row checkbox">\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['CUSTOM_NOTIFY_ONSNATCH'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                      <label for="custom_notify_onsnatch">\n                        <input type="checkbox" id="custom_notify_onsnatch" name="custom_notify_onsnatch" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Notify on snatch</label>\n                    </div>\n                    <div class="col-md-6">\n                      ')

        if lazylibrarian.CONFIG['CUSTOM_NOTIFY_ONDOWNLOAD'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
        
        
        __M_writer('\n                      <label for="custom_notify_ondownload">\n                        <input type="checkbox" id="custom_notify_ondownload" name="custom_notify_ondownload" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                        Notify on download</label>\n                    </div>\n                    </div>\n                    <div class="form-group">\n                      <label for="custom_script">Custom script to run</label>\n                      <input type="text" id="custom_script" name="custom_script" value="')
        __M_writer(str(lazylibrarian.CONFIG['CUSTOM_SCRIPT']))
        __M_writer('" class="form-control" placeholder="Custom Script">\n                    </div>\n                    <div class="form-group">\n                      <input type="button" value="Test Custom" id="testCustom" class="btn btn-default">\n                    </div>\n                  </fieldset>\n                </div>\n              </div>\n')
        if lazylibrarian.APPRISE and lazylibrarian.APPRISE[0].isdigit():
            __M_writer('                <div id="apprise">\n                  <div class="col-md-12">\n                    <legend>Apprise Notifiers\n                    <button class="button btn btn-sm btn-primary" type="button" value="Supported Types" id="show_apprise"><i class="fa fa-list-ul"></i> Supported Types</button>\n                    </legend>\n                  </div>\n')
            loop = __M_loop._enter(lazylibrarian.APPRISE_PROV)
            try:
                for provider in loop:
                    if provider['DISPNAME'] != '':
                        __M_writer('                  ')

                        onsnatch = ''
                        if provider['SNATCH'] == True:
                            onsnatch = 'checked="checked"'
                        ondownload = ''
                        if provider['DOWNLOAD'] == True:
                            ondownload = 'checked="checked"'
                                          
                        
                        __M_writer('\n                  <div class="col-md-6 form-group">\n                    <div class="input-group">\n                      <span class="input-group-addon">Name</span>\n                      <input type="text" id="apprise_')
                        __M_writer(str(loop.index))
                        __M_writer('_dispname" name="apprise_')
                        __M_writer(str(loop.index))
                        __M_writer('_dispname" value="')
                        __M_writer(str(provider['DISPNAME']))
                        __M_writer('" class="form-control" placeholder="name">\n                      <span class="input-group-addon">S\n                        &nbsp;<input type="checkbox" id="apprise_')
                        __M_writer(str(loop.index))
                        __M_writer('_snatch" data-toggle="tooltip" title="Notify Snatch" name="apprise_')
                        __M_writer(str(loop.index))
                        __M_writer('_snatch" value="1" ')
                        __M_writer(str(onsnatch))
                        __M_writer(' />&nbsp;\n                      </span>\n                      <span class="input-group-addon">D\n                        &nbsp;<input type="checkbox" id="apprise_')
                        __M_writer(str(loop.index))
                        __M_writer('_download" data-toggle="tooltip" title="Notify Download" name="apprise_')
                        __M_writer(str(loop.index))
                        __M_writer('_download" value="1" ')
                        __M_writer(str(ondownload))
                        __M_writer(' />&nbsp;\n                      </span>\n                    </div>\n                    <div class="input-group">\n                      <span class="input-group-addon"></span>\n                      <label for="apprise_')
                        __M_writer(str(loop.index))
                        __M_writer('_url" class="sr-only">URL</label>\n                      <input type="text" placeholder="URL #')
                        __M_writer(str(loop.index))
                        __M_writer(' see docs for format" id="apprise_')
                        __M_writer(str(loop.index))
                        __M_writer('_url" name="apprise_')
                        __M_writer(str(loop.index))
                        __M_writer('_url" value="')
                        __M_writer(str(provider['URL']))
                        __M_writer('" class="form-control" />\n                      <span class="input-group-addon">\n                        <button role="testprov" class="button btn btn-xs btn-warning btn-primary" type="button" value="apprise_')
                        __M_writer(str(loop.index))
                        __M_writer('"> Test</button>\n                      </span>\n                    </div>\n                  </div>\n')
            finally:
                loop = __M_loop._exit()
            __M_writer('                </div>\n')
        __M_writer('              <div id="notifieroptions">\n                <div class="col-md-12">\n                  <legend>Options</legend>\n                    <div class="row checkbox">\n                      <div class="col-md-6">\n                        ')

        if lazylibrarian.CONFIG['NOTIFY_WITH_TITLE'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="notify_with_title" class="control-label">\n                          <input type="checkbox" id="notify_with_title" name="notify_with_title" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Show title in download notification</label>\n                      </div>\n                      <div class="col-md-6">\n                         ')

        if lazylibrarian.CONFIG['NOTIFY_WITH_URL'] == True:
            checked = 'checked="checked"'
        else:
            checked = ''
                                
        
        __M_writer('\n                        <label for="notify_with_url" class="control-label">\n                          <input type="checkbox" id="notify_with_url" name="notify_with_url" value="1" ')
        __M_writer(str(checked))
        __M_writer(' />\n                          Show url in download notification<br><small>(WARNING may contain api key)</small></label>\n                      </div>\n                    </div>\n                  </div>\n                </div>\n              </div>\n          </div>\n        </div>\n        <div role="tabpanel" class="tab-pane" id="capabilities">\n          <div class="configtable">\n              <div>\n              You only need to alter category settings if auto-detection fails or returns incorrect values. If you make any alterations, tick the lock button to prevent reloading values from the provider. API limit is not read from the provider and is not affected by lock.\n              </div>\n            <div class="row">\n')
        loop = __M_loop._enter(lazylibrarian.NEWZNAB_PROV)
        try:
            for provider in loop:
                __M_writer('                ')

                if provider['HOST'] == "":
                  hidden = 'hidden="hidden"'
                else:
                  hidden = ''
                                
                
                __M_writer('\n                ')

                if 'APILIMIT' in provider:
                  apilimit = provider['APILIMIT']
                else:
                  apilimit = 0
                                
                
                __M_writer('\n                <div class="col-md-6">\n                <legend ')
                __M_writer(str(hidden))
                __M_writer('>')
                __M_writer(str(provider['DISPNAME']))
                __M_writer('</legend>\n                <input type="text" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_name" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_name" value="')
                __M_writer(str(provider['NAME']))
                __M_writer('" class="hidden">\n                <input type="text" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_updated" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_updated" value="')
                __M_writer(str(provider['UPDATED']))
                __M_writer('" class="hidden">\n                <div class="row form-group" ')
                __M_writer(str(hidden))
                __M_writer('>\n                <div class="col-md-6">\n                  <label for="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_generalsearch" class="control-label">General Search:</label>\n                  <input type="text" placeholder="General Search" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_generalsearch" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_generalsearch" value="')
                __M_writer(str(provider['GENERALSEARCH']))
                __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_extended" class="control-label">Extended Search:</label>\n                  <input type="text" placeholder="Extended Search" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_extended" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_extended" value="')
                __M_writer(str(provider['EXTENDED']))
                __M_writer('" class="form-control">\n                </div>\n                </div>\n')
                if lazylibrarian.CONFIG['EBOOK_TAB'] == True:
                    __M_writer('                <div class="row form-group" ')
                    __M_writer(str(hidden))
                    __M_writer('>\n                <div class="col-md-6">\n                  <label for="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_booksearch" class="control-label">eBook Search:</label>\n                  <input type="text" placeholder="none" id="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_booksearch" name="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_booksearch" value="')
                    __M_writer(str(provider['BOOKSEARCH']))
                    __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_bookcat" class="control-label">eBook Categories:</label>\n                  <input type="text" id="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_bookcat" name="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_bookcat" value="')
                    __M_writer(str(provider['BOOKCAT']))
                    __M_writer('" class="form-control">\n                </div>\n                </div>\n')
                if lazylibrarian.CONFIG['MAG_TAB'] == True:
                    __M_writer('                <div class="row form-group" ')
                    __M_writer(str(hidden))
                    __M_writer('>\n                <div class="col-md-6">\n                  <label for="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magsearch" class="control-label">Magazine Search:</label>\n                  <input type="text" placeholder="none" id="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magsearch" name="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magsearch" value="')
                    __M_writer(str(provider['MAGSEARCH']))
                    __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magcat" class="control-label">Magazine Categories:</label>\n                  <input type="text" id="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magcat" name="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magcat" value="')
                    __M_writer(str(provider['MAGCAT']))
                    __M_writer('" class="form-control">\n                </div>\n                </div>\n')
                if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
                    __M_writer('                <div class="row form-group" ')
                    __M_writer(str(hidden))
                    __M_writer('>\n                <div class="col-md-6">\n                  <label for="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiosearch" class="control-label">AudioBook Search:</label>\n                  <input type="text" placeholder="none" id="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiosearch" name="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiosearch" value="')
                    __M_writer(str(provider['AUDIOSEARCH']))
                    __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiocat" class="control-label">AudioBook Categories:</label>\n                  <input type="text" id="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiocat" name="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiocat" value="')
                    __M_writer(str(provider['AUDIOCAT']))
                    __M_writer('" class="form-control">\n                </div>\n                </div>\n')
                if lazylibrarian.CONFIG['COMIC_TAB'] == True:
                    __M_writer('                <div class="row form-group" ')
                    __M_writer(str(hidden))
                    __M_writer('>\n                <div class="col-md-6">\n                  <label for="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comicsearch" class="control-label">Comic Search:</label>\n                  <input type="text" placeholder="none" id="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comicsearch" name="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comicsearch" value="')
                    __M_writer(str(provider['COMICSEARCH']))
                    __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comiccat" class="control-label">Comic Categories:</label>\n                  <input type="text" id="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comiccat" name="newznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comiccat" value="')
                    __M_writer(str(provider['COMICCAT']))
                    __M_writer('" class="form-control">\n                </div>\n                </div>\n')
                __M_writer('                <div class="row form-group" ')
                __M_writer(str(hidden))
                __M_writer('>\n                <div class="col-md-6">\n                  <label for="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_apilimit" class="control-label">Daily API Limit: (used ')
                __M_writer(str(provider['APICOUNT']))
                __M_writer(')</label>\n                  <input type="number" placeholder="API Limit" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_apilimit" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_apilimit" value="')
                __M_writer(str(provider['APILIMIT']))
                __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_ratelimit" class="control-label">Rate Limit:</label>\n                  <input type="number" placeholder="Rate Limit" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_ratelimit" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_ratelimit" value="')
                __M_writer(str(provider['RATELIMIT']))
                __M_writer('" class="form-control">\n                </div>\n                <div class="checkbox col-md-6">\n                  ')

                if provider['MANUAL'] == True:
                    checked = 'checked="checked"'
                else:
                    checked = ''
                
                
                __M_writer('\n                  <label for="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_manual" class="control-label" ')
                __M_writer(str(hidden))
                __M_writer('>\n                    <input type="checkbox" id="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_manual" name="newznab_')
                __M_writer(str(loop.index))
                __M_writer('_manual" value="1" ')
                __M_writer(str(checked))
                __M_writer('  ')
                __M_writer(str(hidden))
                __M_writer('/>\n                    Tick to lock settings</label>\n                </div>\n                </div>\n                </div>\n')
        finally:
            loop = __M_loop._exit()
        __M_writer('            </div>\n            <div class="row">\n')
        loop = __M_loop._enter(lazylibrarian.TORZNAB_PROV)
        try:
            for provider in loop:
                __M_writer('                ')

                if provider['HOST'] == "":
                    hidden = 'hidden="hidden"'
                else:
                    hidden = ''
                                
                
                __M_writer('\n                <div class="col-md-6">\n                <legend ')
                __M_writer(str(hidden))
                __M_writer('>')
                __M_writer(str(provider['DISPNAME']))
                __M_writer('</legend>\n                <input type="text" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_name" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_name" value="')
                __M_writer(str(provider['NAME']))
                __M_writer('" class="hidden">\n                <input type="text" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_updated" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_updated" value="')
                __M_writer(str(provider['UPDATED']))
                __M_writer('" class="hidden">\n                <div class="row form-group" ')
                __M_writer(str(hidden))
                __M_writer('>\n                <div class="col-md-6">\n                  <label for="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_generalsearch" class="control-label">General Search:</label>\n                  <input type="text" placeholder="General Search" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_generalsearch" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_generalsearch" value="')
                __M_writer(str(provider['GENERALSEARCH']))
                __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_extended" class="control-label">Extended Search:</label>\n                  <input type="text" placeholder="Extended Search" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_extended" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_extended" value="')
                __M_writer(str(provider['EXTENDED']))
                __M_writer('" class="form-control">\n                </div>\n                </div>\n')
                if lazylibrarian.CONFIG['EBOOK_TAB'] == True:
                    __M_writer('                <div class="row form-group" ')
                    __M_writer(str(hidden))
                    __M_writer('>\n                <div class="col-md-6">\n                  <label for="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_booksearch" class="control-label">eBook Search:</label>\n                  <input type="text" placeholder="none" id="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_booksearch" name="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_booksearch" value="')
                    __M_writer(str(provider['BOOKSEARCH']))
                    __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_bookcat" class="control-label">eBook Categories:</label>\n                  <input type="text" id="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_bookcat" name="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_bookcat" value="')
                    __M_writer(str(provider['BOOKCAT']))
                    __M_writer('" class="form-control">\n                </div>\n                </div>\n')
                if lazylibrarian.CONFIG['MAG_TAB'] == True:
                    __M_writer('                <div class="row form-group" ')
                    __M_writer(str(hidden))
                    __M_writer('>\n                <div class="col-md-6">\n                  <label for="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magsearch" class="control-label">Magazine Search:</label>\n                  <input type="text" placeholder="none" id="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magsearch" name="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magsearch" value="')
                    __M_writer(str(provider['MAGSEARCH']))
                    __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magcat" class="control-label">Magazine Categories:</label>\n                  <input type="text" id="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magcat" name="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_magcat" value="')
                    __M_writer(str(provider['MAGCAT']))
                    __M_writer('" class="form-control">\n                </div>\n                </div>\n')
                if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
                    __M_writer('                <div class="row form-group" ')
                    __M_writer(str(hidden))
                    __M_writer('>\n                <div class="col-md-6">\n                  <label for="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiosearch" class="control-label">AudioBook Search:</label>\n                  <input type="text" placeholder="none" id="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiosearch" name="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiosearch" value="')
                    __M_writer(str(provider['AUDIOSEARCH']))
                    __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiocat" class="control-label">AudioBook Categories:</label>\n                  <input type="text" id="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiocat" name="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_audiocat" value="')
                    __M_writer(str(provider['AUDIOCAT']))
                    __M_writer('" class="form-control">\n                </div>\n                </div>\n')
                if lazylibrarian.CONFIG['COMIC_TAB'] == True:
                    __M_writer('                <div class="row form-group" ')
                    __M_writer(str(hidden))
                    __M_writer('>\n                <div class="col-md-6">\n                  <label for="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comicsearch" class="control-label">Comic Search:</label>\n                  <input type="text" placeholder="none" id="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comicsearch" name="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comicsearch" value="')
                    __M_writer(str(provider['COMICSEARCH']))
                    __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comiccat" class="control-label">Comic Categories:</label>\n                  <input type="text" id="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comiccat" name="torznab_')
                    __M_writer(str(loop.index))
                    __M_writer('_comiccat" value="')
                    __M_writer(str(provider['COMICCAT']))
                    __M_writer('" class="form-control">\n                </div>\n                </div>\n')
                __M_writer('                <div class="row form-group" ')
                __M_writer(str(hidden))
                __M_writer('>\n                <div class="col-md-6">\n                  <label for="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_apilimit" class="control-label">Daily API Limit: (used ')
                __M_writer(str(provider['APICOUNT']))
                __M_writer(')</label>\n                  <input type="number" placeholder="API Limit" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_apilimit" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_apilimit" value="')
                __M_writer(str(provider['APILIMIT']))
                __M_writer('" class="form-control">\n                </div>\n                <div class="col-md-6">\n                  <label for="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_ratelimit" class="control-label">Rate Limit:</label>\n                  <input type="number" placeholder="Rate Limit" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_ratelimit" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_ratelimit" value="')
                __M_writer(str(provider['RATELIMIT']))
                __M_writer('" class="form-control">\n                </div>\n                <div class="checkbox col-md-6">\n                  ')

                if provider['MANUAL'] == True:
                    checked = 'checked="checked"'
                else:
                    checked = ''
                                  
                
                __M_writer('\n                  <label for="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_manual" class="control-label" ')
                __M_writer(str(hidden))
                __M_writer('>\n                    <input type="checkbox" id="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_manual" name="torznab_')
                __M_writer(str(loop.index))
                __M_writer('_manual" value="1" ')
                __M_writer(str(checked))
                __M_writer(' ')
                __M_writer(str(hidden))
                __M_writer('/>\n                    Tick to lock settings</label>\n                </div>\n                </div>\n              </div>\n')
        finally:
            loop = __M_loop._exit()
        __M_writer('            </div>\n          </div>\n        </div>\n        <div role="tabpanel" class="tab-pane" id="filters">\n          <div class="configtable">\n            <div class="row">\n')
        if lazylibrarian.CONFIG['EBOOK_TAB'] == True:
            __M_writer('                <div class="col-md-6">\n                <legend>Book Reject List</legend>\n                <div class="form-group">\n                  <input type="text" id="reject_words" name="reject_words" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_WORDS']))
            __M_writer('" class="form-control" placeholder="Reject word list">\n                  <span class="help-block">Comma separated list of words to reject:<br/>\n                    Search results with any of these words in the title or filenames<br>\n                    (where available) will be ignored<br/>\n                  </span>\n                </div>\n                </div>\n                <div class="col-md-6">\n                <legend>Publisher Reject List</legend>\n                <div class="form-group">\n                  <input type="text" id="reject_publisher" name="reject_publisher" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_PUBLISHER']))
            __M_writer('" class="form-control" placeholder="Reject publishers">\n                  <span class="help-block">Comma separated list of publishers to reject:<br/>\n                    Libraryscan will ignore books by these publishers on import<br>\n                    if found in opf files or goodreads info<br/>\n                  </span>\n                </div>\n                </div>\n                <br>\n')
        if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
            __M_writer('                <div class="col-md-6">\n                <legend>AudioBook Reject List</legend>\n                <div class="form-group">\n                  <input type="text" id="reject_audio" name="reject_audio" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_AUDIO']))
            __M_writer('" class="form-control" placeholder="Reject word list">\n                  <span class="help-block">Comma separated list of words to reject:<br/>\n                    Search results with any of these words in the title or filenames<br>\n                    (where available) will be ignored<br/>\n                  </span>\n                </div>\n                </div>\n')
        if lazylibrarian.CONFIG['MAG_TAB'] == True:
            __M_writer('                <div class="col-md-6">\n                <legend>Magazine Reject List (all titles)</legend>\n                <div class="form-group">\n                  <input type="text" id="reject_mags" name="reject_mags" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_MAGS']))
            __M_writer('" class="form-control" placeholder="Reject word list">\n                  <span class="help-block">Comma separated list of words to reject:<br/>\n                    Search results with any of these words in the title or filenames<br>\n                    (where available) will be ignored<br/>\n                  </span>\n                </div>\n                </div>\n')
        if lazylibrarian.CONFIG['COMIC_TAB'] == True:
            __M_writer('                <div class="col-md-6">\n                <legend>Comic Reject List (all titles)</legend>\n                <div class="form-group">\n                  <input type="text" id="reject_comic" name="reject_comic" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_COMIC']))
            __M_writer('" class="form-control" placeholder="Reject word list">\n                  <span class="help-block">Comma separated list of words to reject:<br/>\n                    Search results with any of these words in the title will be ignored<br/>\n                  </span>\n                </div>\n                </div>\n')
        __M_writer('                <div class="col-md-6">\n                <legend>Extension Reject List (all types)</legend>\n                <div class="form-group">\n                  <input type="text" id="banned_ext" name="banned_ext" value="')
        __M_writer(str(lazylibrarian.CONFIG['BANNED_EXT']))
        __M_writer('" class="form-control" placeholder="Reject extensions list">\n                  <span class="help-block">Comma separated list of extensions to reject:<br/>\n                    Results with any of these extensions in the filenames will be rejected<br/>\n                    (where info is available)<br/>\n                  </span>\n                </div>\n                </div>\n')
        if lazylibrarian.CONFIG['EBOOK_TAB'] == True:
            __M_writer('                <div class="col-md-6">\n                <legend>eBook Size Limits</legend>\n                  <div class="input-group">\n                    <label for="reject_minsize" class="input-group-addon">Min size</label>\n                    <input type="number" id="reject_minsize" name="reject_minsize" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_MINSIZE']))
            __M_writer('" class="form-control" placeholder="Reject minimum size">\n                    <label for="reject_maxsize" class="input-group-addon">Max size</label>\n                    <input type="number" id="reject_maxsize" name="reject_maxsize" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_MAXSIZE']))
            __M_writer('" class="form-control" placeholder="Reject maximum size">\n                    <span class="input-group-addon">Mb</span>\n                  </div>\n                </div>\n')
        if lazylibrarian.CONFIG['AUDIO_TAB'] == True:
            __M_writer('                <div class="col-md-6">\n                <legend>AudioBook Size Limits</legend>\n                 <div class="input-group">\n                    <label for="reject_minaudio" class="input-group-addon">Min size</label>\n                    <input type="number" id="reject_minaudio" name="reject_minaudio" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_MINAUDIO']))
            __M_writer('" class="form-control" placeholder="Reject minimum size">\n                    <label for="reject_maxaudio" class="input-group-addon">Max size</label>\n                    <input type="number" id="reject_maxaudio" name="reject_maxaudio" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_MAXAUDIO']))
            __M_writer('" class="form-control" placeholder="Reject maximum size">\n                    <span class="input-group-addon">Mb</span>\n                  </div>\n                </div>\n')
        if lazylibrarian.CONFIG['COMIC_TAB'] == True:
            __M_writer('                <div class="col-md-6">\n                <legend>Comic Size Limits</legend>\n                 <div class="input-group">\n                    <label for="reject_mincomic" class="input-group-addon">Min size</label>\n                    <input type="number" id="reject_mincomic" name="reject_mincomic" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_MINCOMIC']))
            __M_writer('" class="form-control" placeholder="Reject minimum size">\n                    <label for="reject_maxcomic" class="input-group-addon">Max size</label>\n                    <input type="number" id="reject_maxcomic" name="reject_maxcomic" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_MAXCOMIC']))
            __M_writer('" class="form-control" placeholder="Reject maximum size">\n                    <span class="input-group-addon">Mb</span>\n                  </div>\n                </div>\n')
        if lazylibrarian.CONFIG['MAG_TAB'] == True:
            __M_writer('                <div class="col-md-6">\n                <br>\n                <legend>Magazine Size Limits</legend>\n                  <div class="input-group">\n                    <label for="reject_magmin" class="input-group-addon">Min size</label>\n                    <input type="number" id="reject_magmin" name="reject_magmin" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_MAGMIN']))
            __M_writer('" class="form-control" placeholder="Reject minimum size">\n                    <label for="reject_magsize" class="input-group-addon">Max size</label>\n                    <input type="number" id="reject_magsize" name="reject_magsize" value="')
            __M_writer(str(lazylibrarian.CONFIG['REJECT_MAGSIZE']))
            __M_writer('" class="form-control" placeholder="Reject maximum size">\n                    <span class="input-group-addon">Mb</span>\n                  </div>\n                </div>\n                <div class="col-md-12">\n                <br>\n                <legend>Magazine Options (per title)</legend>\n                </div>\n')
            for mag in config['magazines_list']:
                __M_writer('                <div class="col-md-6">\n                <label>')
                __M_writer(str(mag['Title']))
                __M_writer('</label>\n                  <div class="input-group">\n                    <label for="reject_list[')
                __M_writer(str(mag['Title']))
                __M_writer(']" class="input-group-addon">Reject&nbsp;</label>\n                    <input type="text" id="reject_list[')
                __M_writer(str(mag['Title']))
                __M_writer(']" name="reject_list[')
                __M_writer(str(mag['Title']))
                __M_writer(']" value="')
                __M_writer(str(mag['Reject']))
                __M_writer('" class="form-control" placeholder="Reject word list">\n                  </div>\n                  <div class="input-group">\n                    <label for="regex[')
                __M_writer(str(mag['Title']))
                __M_writer(']" class="input-group-addon">Search</label>\n                    <input type="text" id="regex[')
                __M_writer(str(mag['Title']))
                __M_writer(']" name="regex[')
                __M_writer(str(mag['Title']))
                __M_writer(']" value="')
                __M_writer(str(mag['Regex']))
                __M_writer('" class="form-control" placeholder="Search expression">\n                  </div>\n                  <div class="input-group">\n                    <label for="datetype[')
                __M_writer(str(mag['Title']))
                __M_writer(']" class="input-group-addon">Date Style</label>\n                    <input type="text" id="datetype[')
                __M_writer(str(mag['Title']))
                __M_writer(']" name="datetype[')
                __M_writer(str(mag['Title']))
                __M_writer(']" value="')
                __M_writer(str(mag['DateType']))
                __M_writer('" class="form-control" placeholder="auto">\n                    <label for="coverpage[')
                __M_writer(str(mag['Title']))
                __M_writer(']" class="input-group-addon">Cover Page</label>\n                    <input type="number" id="coverpage[')
                __M_writer(str(mag['Title']))
                __M_writer(']" name="coverpage[')
                __M_writer(str(mag['Title']))
                __M_writer(']" value="')
                __M_writer(str(mag['CoverPage']))
                __M_writer('" min=1 class="form-control" placeholder="1">\n                  </div>\n                </div>\n')
        __M_writer('                <div class="col-md-6">\n                <label>Settings:</label><br>\n                <input type="button" value="Export Filters" id="savefilters" class="btn btn-default" />\n                <input type="button" value="Import Filters" id="loadfilters" class="btn btn-default" />\n                  <div class="pull-right table_wrapper_button">\n                    <input type="submit" value="Save changes" id="add" class="btn btn-primary">\n                  </div>\n                </div>\n            </div>\n            <br>\n          </div>\n        </div>\n        <div role="tabpanel" class="tab-pane" id="genres">\n          <div class="configtable">\n            <div class="row">\n              <div class="col-md-6">\n                <legend>Genre Settings</legend>\n                <div class="input-group">\n                  <span class="input-group-addon">Genres per book</span>\n                  <input type="number" id="genrelimit" name="genrelimit" value="')
        __M_writer(str(lazylibrarian.GRGENRES['genreLimit']))
        __M_writer('" class="form-control">\n                  <span class="input-group-addon">Genre Users</span>\n                  <input type="number" id="genreusers" name="genreusers" value="')
        __M_writer(str(lazylibrarian.GRGENRES['genreUsers']))
        __M_writer('" class="form-control">\n                </div>\n              </div>\n            </div>\n            <p>\n            <div class="row">\n              <div class="col-md-12">\n                <legend>Reject Genres</legend>\n                <div class="form-group">\n                  <input type="text" id="genreexclude" name="genreexclude" value="')
        __M_writer(str(', '.join(i for i in sorted(lazylibrarian.GRGENRES['genreExclude']))))
        __M_writer('" class="form-control" placeholder="Reject word list">\n                  <span class="help-block">Comma separated list of genres to reject: Results that match any of these words will be ignored<br/>\n                  </span>\n                </div>\n                <legend>Reject Parts</legend>\n                <div class="form-group">\n                  <input type="text" id="genreexcludeparts" name="genreexcludeparts" value="')
        __M_writer(str(', '.join(i for i in sorted(lazylibrarian.GRGENRES['genreExcludeParts']))))
        __M_writer('" class="form-control" placeholder="Reject word list">\n                  <span class="help-block">Comma separated list of part-words in genres to reject: Results that contain any of these part-words will be ignored<br/>\n                  </span>\n                </div>\n                <legend>Replace Genre</legend>\n                  <span class="help-block">Replace one genre name with another (replace happens <i>before</i> processing reject lists)<br/>\n                  </span>\n                  <div class="input-group col-md-6">\n                    <span class="input-group-addon">Replace genre</span>\n                    <input type="text" id="genreold" name="genreold" value="" class="form-control">\n                    <span class="input-group-addon">with</span>\n                    <input type="text" id="genrenew" name="genrenew" value="" class="form-control">\n                  </div>\n                  <br>\n                  <span class="help-block">To remove an existing entry leave the text box below it empty<br/>\n                  </span>\n')
        for item in sorted(lazylibrarian.GRGENRES['genreReplace']):
            __M_writer('                  <div class="col-md-4">\n                    <label>')
            __M_writer(str(item))
            __M_writer('</label>\n                    <input type="text" id="genrereplace[')
            __M_writer(str(item))
            __M_writer(']" name="genrereplace[')
            __M_writer(str(item))
            __M_writer(']" value="')
            __M_writer(str(lazylibrarian.GRGENRES['genreReplace'][item]))
            __M_writer('" class="form-control" placeholder="<delete>">\n                  </div>\n')
        __M_writer('              </div>\n            </div>\n          </div>\n        </div>\n      </div>\n    <!-- tabs content -->\n    </div>\n    <!-- tabs -->\n    <p>&nbsp;</p>\n    <p style="text-align:center;color:grey">Repo: https://')
        __M_writer(str(lazylibrarian.CONFIG['GIT_HOST']))
        __M_writer('/')
        __M_writer(str(lazylibrarian.CONFIG['GIT_USER']))
        __M_writer('/')
        __M_writer(str(lazylibrarian.CONFIG['GIT_REPO']))
        __M_writer('  :     Branch: ')
        __M_writer(str(lazylibrarian.CONFIG['GIT_BRANCH']))
        __M_writer('  :  Updated: ')
        __M_writer(str(config['updated']))
        __M_writer('<br>\n    Current Version: ')
        __M_writer(str(lazylibrarian.CONFIG['CURRENT_VERSION']))
        __M_writer('  : Latest  Version:    ')
        __M_writer(str(lazylibrarian.CONFIG['LATEST_VERSION']))
        __M_writer('</p>\n  </div>\n<!-- form -->\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascriptIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n  ')
        runtime._include_file(context, 'config_functions.js', _template_uri)
        __M_writer('\n  <script type="text/javascript">\n    $(document).ready(function() {\n        initThisPage();\n    });\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/app/lazylibrarian/data/interfaces/bookstrap/config.html", "uri": "config.html", "source_encoding": "utf-8", "line_map": {"16": 2, "17": 3, "18": 4, "19": 5, "31": 0, "36": 1, "37": 4, "38": 25, "39": 4337, "40": 4345, "46": 5, "50": 5, "51": 8, "52": 9, "53": 11, "54": 16, "55": 17, "56": 19, "57": 20, "58": 22, "64": 26, "72": 26, "73": 30, "74": 30, "75": 49, "76": 50, "77": 52, "78": 60, "79": 60, "80": 63, "81": 63, "82": 65, "83": 65, "84": 69, "85": 69, "86": 73, "87": 73, "88": 79, "89": 80, "90": 81, "91": 82, "92": 83, "93": 84, "94": 85, "95": 84, "96": 86, "97": 86, "98": 90, "99": 91, "100": 92, "101": 93, "102": 94, "103": 95, "104": 96, "105": 95, "106": 97, "107": 97, "108": 105, "109": 105, "110": 109, "111": 109, "112": 114, "113": 115, "114": 116, "115": 117, "116": 118, "117": 119, "118": 120, "119": 119, "120": 121, "121": 121, "122": 128, "123": 128, "124": 135, "125": 135, "126": 140, "127": 141, "128": 142, "129": 143, "130": 144, "131": 145, "132": 146, "133": 145, "134": 146, "135": 146, "136": 147, "137": 148, "138": 149, "139": 150, "140": 151, "141": 152, "142": 153, "143": 152, "144": 153, "145": 153, "146": 154, "147": 155, "148": 156, "149": 157, "150": 158, "151": 159, "152": 160, "153": 159, "154": 160, "155": 160, "156": 163, "157": 163, "158": 167, "159": 167, "160": 169, "161": 169, "162": 171, "163": 172, "164": 177, "165": 178, "166": 179, "167": 180, "168": 181, "169": 182, "170": 183, "171": 182, "172": 184, "173": 184, "174": 188, "175": 189, "176": 190, "177": 191, "178": 192, "179": 193, "180": 194, "181": 193, "182": 195, "183": 195, "184": 201, "185": 202, "186": 203, "187": 204, "188": 205, "189": 206, "190": 207, "191": 206, "192": 208, "193": 208, "194": 212, "195": 213, "196": 214, "197": 215, "198": 216, "199": 217, "200": 218, "201": 217, "202": 219, "203": 219, "204": 225, "205": 226, "206": 227, "207": 228, "208": 229, "209": 230, "210": 231, "211": 230, "212": 232, "213": 232, "214": 236, "215": 237, "216": 238, "217": 239, "218": 240, "219": 241, "220": 242, "221": 241, "222": 243, "223": 243, "224": 249, "225": 250, "226": 251, "227": 252, "228": 253, "229": 254, "230": 255, "231": 254, "232": 256, "233": 256, "234": 260, "235": 261, "236": 262, "237": 263, "238": 264, "239": 265, "240": 266, "241": 265, "242": 267, "243": 267, "244": 273, "245": 274, "246": 275, "247": 276, "248": 277, "249": 278, "250": 279, "251": 278, "252": 280, "253": 280, "254": 284, "255": 285, "256": 286, "257": 287, "258": 288, "259": 289, "260": 290, "261": 289, "262": 291, "263": 291, "264": 297, "265": 298, "266": 299, "267": 300, "268": 301, "269": 302, "270": 303, "271": 302, "272": 304, "273": 304, "274": 308, "275": 309, "276": 310, "277": 311, "278": 312, "279": 313, "280": 314, "281": 313, "282": 315, "283": 315, "284": 321, "285": 322, "286": 323, "287": 324, "288": 325, "289": 326, "290": 327, "291": 326, "292": 328, "293": 328, "294": 333, "295": 340, "296": 340, "297": 344, "298": 344, "299": 351, "300": 352, "301": 353, "302": 354, "303": 355, "304": 356, "305": 357, "306": 356, "307": 358, "308": 358, "309": 364, "310": 364, "311": 367, "312": 368, "313": 369, "314": 370, "315": 371, "316": 372, "317": 373, "318": 374, "319": 375, "320": 374, "321": 376, "322": 376, "323": 380, "324": 385, "325": 386, "326": 387, "327": 388, "328": 389, "329": 390, "330": 391, "331": 390, "332": 392, "333": 392, "334": 398, "335": 399, "336": 400, "337": 401, "338": 402, "339": 403, "340": 404, "341": 403, "342": 405, "343": 405, "344": 412, "345": 412, "346": 414, "347": 414, "348": 419, "349": 420, "350": 421, "351": 422, "352": 423, "353": 424, "354": 425, "355": 424, "356": 426, "357": 426, "358": 431, "359": 431, "360": 441, "361": 442, "362": 443, "363": 444, "364": 445, "365": 446, "366": 447, "367": 446, "368": 448, "369": 448, "370": 452, "371": 453, "372": 454, "373": 455, "374": 456, "375": 457, "376": 458, "377": 457, "378": 459, "379": 459, "380": 468, "381": 468, "382": 475, "383": 475, "384": 477, "385": 477, "386": 483, "387": 484, "388": 485, "389": 486, "390": 487, "391": 488, "392": 489, "393": 488, "394": 489, "395": 489, "396": 490, "397": 491, "398": 492, "399": 493, "400": 494, "401": 495, "402": 496, "403": 495, "404": 496, "405": 496, "406": 507, "407": 508, "408": 509, "409": 510, "410": 511, "411": 512, "412": 513, "413": 512, "414": 514, "415": 514, "416": 518, "417": 519, "418": 520, "419": 521, "420": 522, "421": 523, "422": 524, "423": 523, "424": 525, "425": 525, "426": 534, "427": 534, "428": 537, "429": 537, "430": 546, "431": 547, "432": 547, "433": 548, "434": 549, "435": 550, "436": 551, "437": 552, "438": 553, "439": 552, "440": 553, "441": 553, "442": 553, "443": 553, "444": 553, "445": 553, "446": 555, "447": 559, "448": 559, "449": 566, "450": 567, "451": 567, "452": 568, "453": 569, "454": 570, "455": 571, "456": 572, "457": 573, "458": 572, "459": 573, "460": 573, "461": 573, "462": 573, "463": 573, "464": 573, "465": 575, "466": 580, "467": 581, "468": 582, "469": 583, "470": 584, "471": 585, "472": 586, "473": 585, "474": 587, "475": 587, "476": 591, "477": 592, "478": 593, "479": 594, "480": 595, "481": 596, "482": 597, "483": 596, "484": 598, "485": 598, "486": 604, "487": 605, "488": 606, "489": 607, "490": 608, "491": 609, "492": 610, "493": 609, "494": 611, "495": 611, "496": 615, "497": 616, "498": 617, "499": 618, "500": 619, "501": 620, "502": 621, "503": 620, "504": 622, "505": 622, "506": 628, "507": 629, "508": 630, "509": 631, "510": 632, "511": 633, "512": 634, "513": 633, "514": 635, "515": 635, "516": 638, "517": 639, "518": 640, "519": 641, "520": 642, "521": 643, "522": 644, "523": 645, "524": 646, "525": 645, "526": 647, "527": 647, "528": 651, "529": 654, "530": 655, "531": 656, "532": 657, "533": 658, "534": 659, "535": 660, "536": 659, "537": 661, "538": 661, "539": 664, "540": 665, "541": 666, "542": 667, "543": 668, "544": 669, "545": 670, "546": 671, "547": 672, "548": 671, "549": 673, "550": 673, "551": 677, "552": 680, "553": 681, "554": 682, "555": 683, "556": 684, "557": 685, "558": 686, "559": 685, "560": 687, "561": 687, "562": 691, "563": 692, "564": 693, "565": 694, "566": 695, "567": 696, "568": 697, "569": 696, "570": 698, "571": 698, "572": 704, "573": 705, "574": 706, "575": 707, "576": 708, "577": 709, "578": 710, "579": 709, "580": 711, "581": 711, "582": 715, "583": 716, "584": 717, "585": 718, "586": 719, "587": 720, "588": 721, "589": 720, "590": 722, "591": 722, "592": 728, "593": 729, "594": 730, "595": 731, "596": 732, "597": 733, "598": 734, "599": 733, "600": 735, "601": 735, "602": 738, "603": 739, "604": 740, "605": 741, "606": 742, "607": 743, "608": 744, "609": 745, "610": 746, "611": 745, "612": 747, "613": 747, "614": 753, "615": 754, "616": 755, "617": 756, "618": 757, "619": 758, "620": 759, "621": 760, "622": 759, "623": 761, "624": 761, "625": 765, "626": 766, "627": 767, "628": 768, "629": 769, "630": 770, "631": 771, "632": 770, "633": 772, "634": 772, "635": 788, "636": 789, "637": 790, "638": 791, "639": 792, "640": 793, "641": 794, "642": 795, "643": 796, "644": 797, "645": 798, "646": 799, "647": 800, "648": 801, "649": 802, "650": 801, "651": 804, "652": 804, "653": 805, "654": 805, "655": 806, "656": 806, "657": 812, "658": 812, "659": 816, "660": 816, "661": 823, "662": 823, "663": 825, "664": 826, "665": 827, "666": 828, "667": 829, "668": 830, "669": 831, "670": 830, "671": 832, "672": 832, "673": 837, "674": 838, "675": 839, "676": 840, "677": 841, "678": 842, "679": 843, "680": 842, "681": 844, "682": 844, "683": 848, "684": 848, "685": 850, "686": 850, "687": 852, "688": 852, "689": 854, "690": 855, "691": 856, "692": 857, "693": 858, "694": 859, "695": 860, "696": 859, "697": 861, "698": 861, "699": 863, "700": 864, "701": 866, "702": 870, "703": 870, "704": 873, "705": 874, "706": 875, "707": 875, "708": 877, "709": 877, "710": 879, "711": 880, "712": 882, "713": 882, "714": 884, "715": 884, "716": 887, "717": 888, "718": 889, "719": 890, "720": 891, "721": 892, "722": 893, "723": 894, "724": 893, "725": 895, "726": 895, "727": 902, "728": 902, "729": 918, "730": 918, "731": 922, "732": 923, "733": 925, "734": 925, "735": 928, "736": 929, "737": 930, "738": 931, "739": 932, "740": 933, "741": 934, "742": 933, "743": 935, "744": 935, "745": 939, "746": 944, "747": 945, "748": 947, "749": 947, "750": 951, "751": 952, "752": 954, "753": 954, "754": 958, "755": 959, "756": 961, "757": 961, "758": 965, "759": 966, "760": 968, "761": 968, "762": 972, "763": 973, "764": 974, "765": 975, "766": 976, "767": 977, "768": 978, "769": 979, "770": 978, "771": 980, "772": 980, "773": 984, "774": 985, "775": 986, "776": 987, "777": 988, "778": 989, "779": 990, "780": 989, "781": 991, "782": 991, "783": 995, "784": 996, "785": 997, "786": 998, "787": 999, "788": 1000, "789": 1001, "790": 1000, "791": 1002, "792": 1002, "793": 1006, "794": 1007, "795": 1008, "796": 1009, "797": 1010, "798": 1011, "799": 1012, "800": 1011, "801": 1013, "802": 1013, "803": 1017, "804": 1018, "805": 1019, "806": 1020, "807": 1021, "808": 1022, "809": 1023, "810": 1022, "811": 1024, "812": 1024, "813": 1028, "814": 1029, "815": 1030, "816": 1031, "817": 1032, "818": 1033, "819": 1034, "820": 1033, "821": 1035, "822": 1035, "823": 1039, "824": 1040, "825": 1041, "826": 1042, "827": 1043, "828": 1044, "829": 1045, "830": 1044, "831": 1046, "832": 1046, "833": 1050, "834": 1051, "835": 1052, "836": 1053, "837": 1054, "838": 1055, "839": 1056, "840": 1055, "841": 1057, "842": 1057, "843": 1061, "844": 1062, "845": 1063, "846": 1064, "847": 1065, "848": 1066, "849": 1067, "850": 1066, "851": 1068, "852": 1068, "853": 1072, "854": 1073, "855": 1074, "856": 1075, "857": 1076, "858": 1077, "859": 1078, "860": 1077, "861": 1079, "862": 1079, "863": 1083, "864": 1084, "865": 1085, "866": 1086, "867": 1087, "868": 1088, "869": 1089, "870": 1088, "871": 1090, "872": 1090, "873": 1100, "874": 1100, "875": 1109, "876": 1109, "877": 1118, "878": 1118, "879": 1122, "880": 1122, "881": 1139, "882": 1140, "883": 1141, "884": 1142, "885": 1143, "886": 1144, "887": 1145, "888": 1144, "889": 1146, "890": 1146, "891": 1154, "892": 1154, "893": 1158, "894": 1158, "895": 1164, "896": 1164, "897": 1168, "898": 1168, "899": 1173, "900": 1173, "901": 1178, "902": 1178, "903": 1182, "904": 1182, "905": 1189, "906": 1189, "907": 1199, "908": 1200, "909": 1201, "910": 1202, "911": 1203, "912": 1204, "913": 1205, "914": 1204, "915": 1206, "916": 1206, "917": 1211, "918": 1212, "919": 1213, "920": 1214, "921": 1215, "922": 1216, "923": 1217, "924": 1216, "925": 1218, "926": 1218, "927": 1226, "928": 1226, "929": 1230, "930": 1230, "931": 1236, "932": 1236, "933": 1240, "934": 1240, "935": 1246, "936": 1246, "937": 1250, "938": 1250, "939": 1262, "940": 1263, "941": 1264, "942": 1265, "943": 1266, "944": 1267, "945": 1268, "946": 1267, "947": 1269, "948": 1269, "949": 1277, "950": 1277, "951": 1281, "952": 1281, "953": 1285, "954": 1285, "955": 1289, "956": 1289, "957": 1293, "958": 1293, "959": 1298, "960": 1299, "961": 1300, "962": 1301, "963": 1302, "964": 1303, "965": 1304, "966": 1303, "967": 1305, "968": 1305, "969": 1309, "970": 1310, "971": 1311, "972": 1312, "973": 1313, "974": 1314, "975": 1315, "976": 1314, "977": 1316, "978": 1316, "979": 1329, "980": 1330, "981": 1331, "982": 1332, "983": 1333, "984": 1334, "985": 1335, "986": 1334, "987": 1336, "988": 1336, "989": 1343, "990": 1343, "991": 1348, "992": 1348, "993": 1359, "994": 1360, "995": 1361, "996": 1362, "997": 1363, "998": 1364, "999": 1365, "1000": 1364, "1001": 1366, "1002": 1366, "1003": 1374, "1004": 1374, "1005": 1378, "1006": 1378, "1007": 1384, "1008": 1384, "1009": 1388, "1010": 1388, "1011": 1394, "1012": 1394, "1013": 1398, "1014": 1398, "1015": 1402, "1016": 1402, "1017": 1406, "1018": 1406, "1019": 1416, "1020": 1417, "1021": 1418, "1022": 1419, "1023": 1420, "1024": 1421, "1025": 1422, "1026": 1421, "1027": 1423, "1028": 1423, "1029": 1431, "1030": 1431, "1031": 1435, "1032": 1435, "1033": 1439, "1034": 1439, "1035": 1443, "1036": 1443, "1037": 1447, "1038": 1447, "1039": 1451, "1040": 1451, "1041": 1463, "1042": 1464, "1043": 1465, "1044": 1466, "1045": 1467, "1046": 1468, "1047": 1469, "1048": 1468, "1049": 1470, "1050": 1470, "1051": 1478, "1052": 1478, "1053": 1482, "1054": 1482, "1055": 1486, "1056": 1486, "1057": 1490, "1058": 1490, "1059": 1494, "1060": 1494, "1061": 1506, "1062": 1507, "1063": 1508, "1064": 1509, "1065": 1510, "1066": 1511, "1067": 1512, "1068": 1511, "1069": 1513, "1070": 1513, "1071": 1521, "1072": 1521, "1073": 1525, "1074": 1525, "1075": 1529, "1076": 1529, "1077": 1533, "1078": 1533, "1079": 1537, "1080": 1537, "1081": 1541, "1082": 1541, "1083": 1553, "1084": 1554, "1085": 1555, "1086": 1556, "1087": 1557, "1088": 1558, "1089": 1559, "1090": 1558, "1091": 1560, "1092": 1560, "1093": 1568, "1094": 1568, "1095": 1572, "1096": 1572, "1097": 1576, "1098": 1576, "1099": 1580, "1100": 1580, "1101": 1584, "1102": 1584, "1103": 1588, "1104": 1588, "1105": 1592, "1106": 1592, "1107": 1604, "1108": 1605, "1109": 1606, "1110": 1607, "1111": 1608, "1112": 1609, "1113": 1610, "1114": 1609, "1115": 1611, "1116": 1611, "1117": 1618, "1118": 1618, "1119": 1621, "1120": 1622, "1121": 1623, "1122": 1624, "1123": 1625, "1124": 1626, "1125": 1627, "1126": 1626, "1127": 1628, "1128": 1628, "1129": 1633, "1130": 1634, "1131": 1635, "1132": 1636, "1133": 1637, "1134": 1638, "1135": 1639, "1136": 1638, "1137": 1640, "1138": 1640, "1139": 1644, "1140": 1645, "1141": 1646, "1142": 1647, "1143": 1648, "1144": 1649, "1145": 1650, "1146": 1649, "1147": 1651, "1148": 1651, "1149": 1655, "1150": 1656, "1151": 1657, "1152": 1658, "1153": 1659, "1154": 1660, "1155": 1661, "1156": 1660, "1157": 1662, "1158": 1662, "1159": 1666, "1160": 1667, "1161": 1668, "1162": 1669, "1163": 1670, "1164": 1671, "1165": 1672, "1166": 1671, "1167": 1673, "1168": 1673, "1169": 1677, "1170": 1678, "1171": 1679, "1172": 1680, "1173": 1681, "1174": 1682, "1175": 1683, "1176": 1682, "1177": 1684, "1178": 1684, "1179": 1701, "1182": 1702, "1183": 1702, "1184": 1703, "1185": 1704, "1186": 1705, "1187": 1706, "1188": 1707, "1189": 1706, "1190": 1710, "1191": 1710, "1192": 1711, "1193": 1711, "1194": 1711, "1195": 1711, "1196": 1711, "1197": 1711, "1198": 1713, "1199": 1713, "1200": 1713, "1201": 1713, "1202": 1713, "1203": 1713, "1204": 1718, "1205": 1718, "1206": 1719, "1207": 1719, "1208": 1719, "1209": 1719, "1210": 1719, "1211": 1719, "1212": 1719, "1213": 1719, "1214": 1724, "1215": 1724, "1216": 1725, "1217": 1725, "1218": 1725, "1219": 1725, "1220": 1725, "1221": 1725, "1222": 1725, "1223": 1725, "1224": 1730, "1225": 1730, "1226": 1730, "1227": 1730, "1228": 1730, "1229": 1730, "1230": 1732, "1231": 1732, "1232": 1732, "1233": 1732, "1234": 1732, "1235": 1732, "1236": 1734, "1237": 1734, "1240": 1739, "1241": 1746, "1244": 1747, "1245": 1747, "1246": 1748, "1247": 1749, "1248": 1750, "1249": 1751, "1250": 1752, "1251": 1751, "1252": 1755, "1253": 1755, "1254": 1756, "1255": 1756, "1256": 1756, "1257": 1756, "1258": 1756, "1259": 1756, "1260": 1758, "1261": 1758, "1262": 1758, "1263": 1758, "1264": 1758, "1265": 1758, "1266": 1763, "1267": 1763, "1268": 1764, "1269": 1764, "1270": 1764, "1271": 1764, "1272": 1764, "1273": 1764, "1274": 1764, "1275": 1764, "1276": 1769, "1277": 1769, "1278": 1770, "1279": 1770, "1280": 1770, "1281": 1770, "1282": 1770, "1283": 1770, "1284": 1770, "1285": 1770, "1286": 1775, "1287": 1775, "1288": 1775, "1289": 1775, "1290": 1775, "1291": 1775, "1292": 1777, "1293": 1777, "1294": 1777, "1295": 1777, "1296": 1777, "1297": 1777, "1298": 1779, "1299": 1779, "1300": 1784, "1301": 1784, "1302": 1784, "1303": 1784, "1304": 1784, "1305": 1784, "1308": 1788, "1309": 1795, "1312": 1796, "1313": 1796, "1314": 1797, "1315": 1798, "1316": 1799, "1317": 1800, "1318": 1801, "1319": 1800, "1320": 1804, "1321": 1804, "1322": 1805, "1323": 1805, "1324": 1805, "1325": 1805, "1326": 1805, "1327": 1805, "1328": 1807, "1329": 1807, "1330": 1807, "1331": 1807, "1332": 1807, "1333": 1807, "1334": 1812, "1335": 1812, "1336": 1813, "1337": 1813, "1338": 1813, "1339": 1813, "1340": 1813, "1341": 1813, "1342": 1813, "1343": 1813, "1344": 1816, "1345": 1817, "1346": 1818, "1347": 1819, "1348": 1820, "1349": 1821, "1350": 1822, "1351": 1823, "1352": 1824, "1353": 1825, "1354": 1824, "1355": 1826, "1356": 1826, "1357": 1827, "1358": 1827, "1359": 1827, "1360": 1827, "1361": 1827, "1362": 1827, "1363": 1829, "1364": 1829, "1365": 1829, "1366": 1829, "1367": 1829, "1368": 1829, "1369": 1831, "1370": 1831, "1373": 1836, "1374": 1842, "1375": 1843, "1376": 1844, "1377": 1845, "1378": 1846, "1379": 1847, "1380": 1848, "1381": 1847, "1382": 1851, "1383": 1851, "1384": 1853, "1385": 1853, "1386": 1858, "1387": 1858, "1388": 1860, "1389": 1860, "1390": 1864, "1391": 1864, "1392": 1870, "1393": 1871, "1394": 1872, "1395": 1873, "1396": 1874, "1397": 1875, "1398": 1876, "1399": 1875, "1400": 1879, "1401": 1879, "1402": 1881, "1403": 1881, "1404": 1886, "1405": 1886, "1406": 1888, "1407": 1888, "1408": 1892, "1409": 1892, "1410": 1898, "1411": 1899, "1412": 1900, "1413": 1901, "1414": 1902, "1415": 1903, "1416": 1904, "1417": 1903, "1418": 1907, "1419": 1907, "1420": 1909, "1421": 1909, "1422": 1914, "1423": 1914, "1424": 1916, "1425": 1916, "1426": 1920, "1427": 1920, "1428": 1926, "1429": 1927, "1430": 1928, "1431": 1929, "1432": 1930, "1433": 1931, "1434": 1932, "1435": 1931, "1436": 1935, "1437": 1935, "1438": 1937, "1439": 1937, "1440": 1942, "1441": 1942, "1442": 1944, "1443": 1944, "1444": 1948, "1445": 1948, "1446": 1954, "1447": 1955, "1448": 1956, "1449": 1957, "1450": 1958, "1451": 1959, "1452": 1960, "1453": 1959, "1454": 1963, "1455": 1963, "1456": 1965, "1457": 1965, "1458": 1970, "1459": 1970, "1460": 1972, "1461": 1972, "1462": 1976, "1463": 1976, "1464": 1982, "1465": 1983, "1466": 1984, "1467": 1985, "1468": 1986, "1469": 1987, "1470": 1988, "1471": 1987, "1472": 1991, "1473": 1991, "1474": 1993, "1475": 1993, "1476": 1998, "1477": 1998, "1478": 2000, "1479": 2000, "1480": 2004, "1481": 2004, "1482": 2010, "1483": 2011, "1484": 2012, "1485": 2013, "1486": 2014, "1487": 2015, "1488": 2016, "1489": 2015, "1490": 2019, "1491": 2019, "1492": 2021, "1493": 2021, "1494": 2026, "1495": 2026, "1496": 2028, "1497": 2028, "1498": 2032, "1499": 2032, "1500": 2045, "1503": 2046, "1504": 2046, "1505": 2047, "1506": 2048, "1507": 2049, "1508": 2050, "1509": 2051, "1510": 2050, "1511": 2054, "1512": 2054, "1513": 2055, "1514": 2055, "1515": 2055, "1516": 2055, "1517": 2055, "1518": 2055, "1519": 2057, "1520": 2057, "1521": 2057, "1522": 2057, "1523": 2057, "1524": 2057, "1525": 2062, "1526": 2062, "1527": 2063, "1528": 2063, "1529": 2063, "1530": 2063, "1531": 2063, "1532": 2063, "1533": 2063, "1534": 2063, "1535": 2068, "1536": 2068, "1537": 2069, "1538": 2069, "1539": 2069, "1540": 2069, "1541": 2069, "1542": 2069, "1543": 2069, "1544": 2069, "1545": 2074, "1546": 2074, "1547": 2075, "1548": 2075, "1549": 2075, "1550": 2075, "1551": 2075, "1552": 2075, "1553": 2075, "1554": 2075, "1555": 2080, "1556": 2080, "1557": 2081, "1558": 2081, "1559": 2081, "1560": 2081, "1561": 2081, "1562": 2081, "1563": 2081, "1564": 2081, "1565": 2086, "1566": 2086, "1567": 2086, "1568": 2086, "1569": 2086, "1570": 2086, "1571": 2088, "1572": 2088, "1573": 2088, "1574": 2088, "1575": 2088, "1576": 2088, "1577": 2090, "1578": 2090, "1581": 2095, "1582": 2102, "1583": 2103, "1584": 2104, "1585": 2105, "1586": 2106, "1587": 2107, "1588": 2108, "1589": 2107, "1590": 2112, "1591": 2112, "1592": 2114, "1593": 2114, "1594": 2119, "1595": 2119, "1596": 2121, "1597": 2121, "1598": 2127, "1599": 2127, "1600": 2128, "1601": 2128, "1602": 2131, "1603": 2132, "1604": 2133, "1605": 2134, "1606": 2135, "1607": 2136, "1608": 2137, "1609": 2136, "1610": 2141, "1611": 2141, "1612": 2143, "1613": 2143, "1614": 2148, "1615": 2148, "1616": 2150, "1617": 2150, "1618": 2156, "1621": 2157, "1622": 2157, "1623": 2158, "1624": 2159, "1625": 2160, "1626": 2161, "1627": 2162, "1628": 2161, "1629": 2165, "1630": 2165, "1631": 2166, "1632": 2166, "1633": 2166, "1634": 2166, "1635": 2166, "1636": 2166, "1637": 2168, "1638": 2168, "1639": 2168, "1640": 2168, "1641": 2168, "1642": 2168, "1643": 2173, "1644": 2173, "1645": 2174, "1646": 2174, "1647": 2174, "1648": 2174, "1649": 2174, "1650": 2174, "1651": 2174, "1652": 2174, "1653": 2179, "1654": 2179, "1655": 2180, "1656": 2180, "1657": 2180, "1658": 2180, "1659": 2180, "1660": 2180, "1661": 2180, "1662": 2180, "1663": 2185, "1664": 2185, "1665": 2185, "1666": 2185, "1667": 2185, "1668": 2185, "1669": 2187, "1670": 2187, "1671": 2187, "1672": 2187, "1673": 2187, "1674": 2187, "1675": 2189, "1676": 2189, "1679": 2194, "1680": 2212, "1681": 2212, "1682": 2216, "1683": 2217, "1684": 2220, "1685": 2220, "1686": 2225, "1687": 2226, "1688": 2229, "1689": 2229, "1690": 2234, "1691": 2237, "1692": 2237, "1693": 2244, "1694": 2244, "1695": 2251, "1696": 2251, "1697": 2258, "1698": 2258, "1699": 2265, "1700": 2265, "1701": 2268, "1702": 2269, "1703": 2270, "1704": 2271, "1705": 2272, "1706": 2273, "1707": 2274, "1708": 2273, "1709": 2275, "1710": 2275, "1711": 2285, "1712": 2286, "1713": 2286, "1714": 2287, "1715": 2288, "1716": 2289, "1717": 2290, "1718": 2291, "1719": 2290, "1720": 2291, "1721": 2291, "1722": 2291, "1723": 2291, "1724": 2291, "1725": 2291, "1726": 2293, "1727": 2296, "1728": 2297, "1729": 2300, "1730": 2301, "1731": 2301, "1732": 2302, "1733": 2303, "1734": 2304, "1735": 2305, "1736": 2306, "1737": 2305, "1738": 2306, "1739": 2306, "1740": 2306, "1741": 2306, "1742": 2306, "1743": 2306, "1744": 2308, "1745": 2312, "1746": 2313, "1747": 2316, "1748": 2317, "1749": 2317, "1750": 2318, "1751": 2319, "1752": 2320, "1753": 2321, "1754": 2322, "1755": 2321, "1756": 2322, "1757": 2322, "1758": 2322, "1759": 2322, "1760": 2322, "1761": 2322, "1762": 2324, "1763": 2328, "1764": 2329, "1765": 2332, "1766": 2333, "1767": 2333, "1768": 2334, "1769": 2335, "1770": 2336, "1771": 2337, "1772": 2338, "1773": 2337, "1774": 2338, "1775": 2338, "1776": 2338, "1777": 2338, "1778": 2338, "1779": 2338, "1780": 2340, "1781": 2344, "1782": 2345, "1783": 2348, "1784": 2349, "1785": 2349, "1786": 2350, "1787": 2351, "1788": 2352, "1789": 2353, "1790": 2354, "1791": 2353, "1792": 2354, "1793": 2354, "1794": 2354, "1795": 2354, "1796": 2354, "1797": 2354, "1798": 2356, "1799": 2360, "1800": 2363, "1801": 2364, "1802": 2364, "1803": 2365, "1804": 2366, "1805": 2367, "1806": 2368, "1807": 2369, "1808": 2368, "1809": 2369, "1810": 2369, "1811": 2369, "1812": 2369, "1813": 2369, "1814": 2369, "1815": 2371, "1816": 2377, "1817": 2378, "1818": 2378, "1819": 2379, "1820": 2380, "1821": 2381, "1822": 2382, "1823": 2383, "1824": 2382, "1825": 2383, "1826": 2383, "1827": 2383, "1828": 2383, "1829": 2383, "1830": 2383, "1831": 2385, "1832": 2389, "1833": 2390, "1834": 2391, "1835": 2392, "1836": 2393, "1837": 2394, "1838": 2395, "1839": 2394, "1840": 2396, "1841": 2396, "1842": 2405, "1843": 2405, "1844": 2411, "1845": 2411, "1846": 2417, "1847": 2417, "1848": 2422, "1849": 2422, "1850": 2428, "1851": 2428, "1852": 2436, "1853": 2436, "1854": 2441, "1855": 2442, "1856": 2443, "1857": 2444, "1858": 2445, "1859": 2446, "1860": 2447, "1861": 2446, "1862": 2448, "1863": 2448, "1864": 2455, "1865": 2455, "1866": 2460, "1867": 2460, "1868": 2464, "1869": 2464, "1870": 2470, "1871": 2470, "1872": 2474, "1873": 2475, "1874": 2476, "1875": 2477, "1876": 2478, "1877": 2479, "1878": 2480, "1879": 2479, "1880": 2481, "1881": 2481, "1882": 2485, "1883": 2486, "1884": 2487, "1885": 2488, "1886": 2489, "1887": 2490, "1888": 2491, "1889": 2490, "1890": 2492, "1891": 2492, "1892": 2496, "1893": 2497, "1894": 2498, "1895": 2499, "1896": 2500, "1897": 2501, "1898": 2502, "1899": 2501, "1900": 2503, "1901": 2503, "1902": 2507, "1903": 2508, "1904": 2509, "1905": 2510, "1906": 2511, "1907": 2512, "1908": 2513, "1909": 2512, "1910": 2514, "1911": 2514, "1912": 2518, "1913": 2519, "1914": 2520, "1915": 2521, "1916": 2522, "1917": 2523, "1918": 2524, "1919": 2523, "1920": 2525, "1921": 2525, "1922": 2529, "1923": 2530, "1924": 2531, "1925": 2532, "1926": 2533, "1927": 2534, "1928": 2535, "1929": 2534, "1930": 2536, "1931": 2536, "1932": 2540, "1933": 2541, "1934": 2542, "1935": 2543, "1936": 2544, "1937": 2545, "1938": 2546, "1939": 2545, "1940": 2547, "1941": 2547, "1942": 2551, "1943": 2552, "1944": 2553, "1945": 2554, "1946": 2555, "1947": 2556, "1948": 2557, "1949": 2556, "1950": 2558, "1951": 2558, "1952": 2562, "1953": 2563, "1954": 2564, "1955": 2565, "1956": 2566, "1957": 2567, "1958": 2568, "1959": 2567, "1960": 2569, "1961": 2569, "1962": 2573, "1963": 2574, "1964": 2575, "1965": 2576, "1966": 2577, "1967": 2578, "1968": 2579, "1969": 2578, "1970": 2580, "1971": 2580, "1972": 2587, "1973": 2587, "1974": 2591, "1975": 2592, "1976": 2593, "1977": 2594, "1978": 2595, "1979": 2596, "1980": 2597, "1981": 2596, "1982": 2598, "1983": 2598, "1984": 2602, "1985": 2603, "1986": 2604, "1987": 2605, "1988": 2606, "1989": 2607, "1990": 2608, "1991": 2607, "1992": 2609, "1993": 2609, "1994": 2619, "1995": 2619, "1996": 2624, "1997": 2624, "1998": 2629, "1999": 2629, "2000": 2636, "2001": 2636, "2002": 2638, "2003": 2638, "2004": 2642, "2005": 2642, "2006": 2644, "2007": 2644, "2008": 2648, "2009": 2648, "2010": 2650, "2011": 2650, "2012": 2654, "2013": 2654, "2014": 2657, "2015": 2657, "2016": 2661, "2017": 2661, "2018": 2664, "2019": 2664, "2020": 2666, "2021": 2667, "2022": 2669, "2023": 2669, "2024": 2672, "2025": 2672, "2026": 2676, "2027": 2676, "2028": 2679, "2029": 2679, "2030": 2683, "2031": 2683, "2032": 2686, "2033": 2686, "2034": 2689, "2035": 2690, "2036": 2691, "2037": 2692, "2038": 2693, "2039": 2694, "2040": 2695, "2041": 2696, "2042": 2695, "2043": 2697, "2044": 2697, "2045": 2701, "2046": 2702, "2047": 2703, "2048": 2704, "2049": 2705, "2050": 2706, "2051": 2707, "2052": 2706, "2053": 2708, "2054": 2708, "2055": 2711, "2056": 2712, "2057": 2714, "2058": 2714, "2059": 2718, "2060": 2719, "2061": 2720, "2062": 2721, "2063": 2722, "2064": 2723, "2065": 2724, "2066": 2723, "2067": 2725, "2068": 2725, "2069": 2729, "2070": 2730, "2071": 2731, "2072": 2732, "2073": 2733, "2074": 2734, "2075": 2735, "2076": 2734, "2077": 2736, "2078": 2736, "2079": 2741, "2080": 2741, "2081": 2746, "2082": 2747, "2083": 2749, "2084": 2749, "2085": 2753, "2086": 2754, "2087": 2755, "2088": 2756, "2089": 2757, "2090": 2758, "2091": 2759, "2092": 2758, "2093": 2760, "2094": 2760, "2095": 2764, "2096": 2765, "2097": 2766, "2098": 2767, "2099": 2768, "2100": 2769, "2101": 2770, "2102": 2769, "2103": 2771, "2104": 2771, "2105": 2775, "2106": 2782, "2107": 2782, "2108": 2785, "2109": 2786, "2110": 2788, "2111": 2788, "2112": 2791, "2113": 2792, "2114": 2794, "2115": 2794, "2116": 2797, "2117": 2799, "2118": 2799, "2119": 2806, "2120": 2806, "2121": 2808, "2122": 2808, "2123": 2815, "2124": 2815, "2125": 2819, "2126": 2820, "2127": 2823, "2128": 2823, "2129": 2828, "2130": 2831, "2131": 2831, "2132": 2838, "2133": 2838, "2134": 2845, "2135": 2845, "2136": 2851, "2137": 2851, "2138": 2855, "2139": 2855, "2140": 2859, "2141": 2859, "2142": 2863, "2143": 2864, "2144": 2866, "2145": 2866, "2146": 2870, "2147": 2871, "2148": 2872, "2149": 2873, "2150": 2874, "2151": 2875, "2152": 2876, "2153": 2875, "2154": 2877, "2155": 2877, "2156": 2881, "2157": 2882, "2158": 2883, "2159": 2884, "2160": 2885, "2161": 2886, "2162": 2887, "2163": 2886, "2164": 2888, "2165": 2888, "2166": 2892, "2167": 2894, "2168": 2895, "2169": 2896, "2170": 2897, "2171": 2898, "2172": 2899, "2173": 2900, "2174": 2901, "2175": 2902, "2176": 2901, "2177": 2903, "2178": 2903, "2179": 2907, "2180": 2908, "2181": 2909, "2182": 2910, "2183": 2911, "2184": 2912, "2185": 2913, "2186": 2912, "2187": 2914, "2188": 2914, "2189": 2918, "2190": 2921, "2191": 2922, "2192": 2923, "2193": 2924, "2194": 2925, "2195": 2926, "2196": 2927, "2197": 2926, "2198": 2928, "2199": 2928, "2200": 2933, "2201": 2934, "2202": 2935, "2203": 2936, "2204": 2937, "2205": 2938, "2206": 2939, "2207": 2938, "2208": 2940, "2209": 2940, "2210": 2945, "2211": 2946, "2212": 2947, "2213": 2948, "2214": 2949, "2215": 2950, "2216": 2951, "2217": 2950, "2218": 2952, "2219": 2952, "2220": 2955, "2221": 2956, "2222": 2957, "2223": 2958, "2224": 2959, "2225": 2960, "2226": 2961, "2227": 2962, "2228": 2963, "2229": 2962, "2230": 2964, "2231": 2964, "2232": 2968, "2233": 2969, "2234": 2970, "2235": 2971, "2236": 2972, "2237": 2973, "2238": 2974, "2239": 2975, "2240": 2974, "2241": 2976, "2242": 2976, "2243": 2980, "2244": 2981, "2245": 2982, "2246": 2983, "2247": 2984, "2248": 2985, "2249": 2986, "2250": 2985, "2251": 2987, "2252": 2987, "2253": 2991, "2254": 2992, "2255": 2993, "2256": 2994, "2257": 2995, "2258": 2996, "2259": 2997, "2260": 2996, "2261": 2998, "2262": 2998, "2263": 3002, "2264": 3003, "2265": 3004, "2266": 3005, "2267": 3006, "2268": 3007, "2269": 3008, "2270": 3007, "2271": 3009, "2272": 3009, "2273": 3013, "2274": 3014, "2275": 3015, "2276": 3016, "2277": 3017, "2278": 3018, "2279": 3019, "2280": 3018, "2281": 3020, "2282": 3020, "2283": 3023, "2284": 3024, "2285": 3025, "2286": 3026, "2287": 3027, "2288": 3028, "2289": 3029, "2290": 3030, "2291": 3031, "2292": 3030, "2293": 3032, "2294": 3032, "2295": 3036, "2296": 3037, "2297": 3038, "2298": 3039, "2299": 3040, "2300": 3041, "2301": 3042, "2302": 3043, "2303": 3044, "2304": 3043, "2305": 3045, "2306": 3045, "2307": 3049, "2308": 3054, "2309": 3054, "2310": 3057, "2311": 3058, "2312": 3059, "2313": 3060, "2314": 3061, "2315": 3062, "2316": 3063, "2317": 3062, "2318": 3064, "2319": 3064, "2320": 3068, "2321": 3069, "2322": 3070, "2323": 3071, "2324": 3072, "2325": 3073, "2326": 3074, "2327": 3073, "2328": 3075, "2329": 3075, "2330": 3079, "2331": 3080, "2332": 3081, "2333": 3082, "2334": 3083, "2335": 3084, "2336": 3085, "2337": 3084, "2338": 3086, "2339": 3086, "2340": 3092, "2341": 3092, "2342": 3095, "2343": 3096, "2344": 3097, "2345": 3098, "2346": 3099, "2347": 3100, "2348": 3101, "2349": 3100, "2350": 3102, "2351": 3102, "2352": 3106, "2353": 3107, "2354": 3108, "2355": 3109, "2356": 3110, "2357": 3111, "2358": 3112, "2359": 3111, "2360": 3113, "2361": 3113, "2362": 3117, "2363": 3118, "2364": 3119, "2365": 3120, "2366": 3121, "2367": 3122, "2368": 3123, "2369": 3122, "2370": 3124, "2371": 3124, "2372": 3129, "2373": 3130, "2374": 3131, "2375": 3132, "2376": 3133, "2377": 3134, "2378": 3135, "2379": 3134, "2380": 3136, "2381": 3136, "2382": 3141, "2383": 3141, "2384": 3153, "2385": 3154, "2386": 3155, "2387": 3156, "2388": 3157, "2389": 3158, "2390": 3159, "2391": 3160, "2392": 3161, "2393": 3160, "2394": 3162, "2395": 3162, "2396": 3170, "2397": 3171, "2398": 3172, "2399": 3173, "2400": 3174, "2401": 3175, "2402": 3176, "2403": 3175, "2404": 3177, "2405": 3177, "2406": 3181, "2407": 3182, "2408": 3183, "2409": 3184, "2410": 3185, "2411": 3186, "2412": 3187, "2413": 3186, "2414": 3188, "2415": 3188, "2416": 3209, "2417": 3210, "2418": 3211, "2419": 3212, "2420": 3213, "2421": 3214, "2422": 3215, "2423": 3214, "2424": 3216, "2425": 3216, "2426": 3224, "2427": 3225, "2428": 3226, "2429": 3227, "2430": 3228, "2431": 3229, "2432": 3230, "2433": 3229, "2434": 3231, "2435": 3231, "2436": 3235, "2437": 3236, "2438": 3237, "2439": 3238, "2440": 3239, "2441": 3240, "2442": 3241, "2443": 3240, "2444": 3242, "2445": 3242, "2446": 3248, "2447": 3248, "2448": 3256, "2449": 3257, "2450": 3258, "2451": 3259, "2452": 3260, "2453": 3261, "2454": 3262, "2455": 3261, "2456": 3263, "2457": 3263, "2458": 3271, "2459": 3272, "2460": 3273, "2461": 3274, "2462": 3275, "2463": 3276, "2464": 3277, "2465": 3276, "2466": 3278, "2467": 3278, "2468": 3282, "2469": 3283, "2470": 3284, "2471": 3285, "2472": 3286, "2473": 3287, "2474": 3288, "2475": 3287, "2476": 3289, "2477": 3289, "2478": 3295, "2479": 3295, "2480": 3299, "2481": 3299, "2482": 3307, "2483": 3308, "2484": 3309, "2485": 3310, "2486": 3311, "2487": 3312, "2488": 3313, "2489": 3312, "2490": 3314, "2491": 3314, "2492": 3322, "2493": 3323, "2494": 3324, "2495": 3325, "2496": 3326, "2497": 3327, "2498": 3328, "2499": 3327, "2500": 3329, "2501": 3329, "2502": 3333, "2503": 3334, "2504": 3335, "2505": 3336, "2506": 3337, "2507": 3338, "2508": 3339, "2509": 3338, "2510": 3340, "2511": 3340, "2512": 3346, "2513": 3346, "2514": 3350, "2515": 3350, "2516": 3354, "2517": 3354, "2518": 3358, "2519": 3358, "2520": 3366, "2521": 3367, "2522": 3368, "2523": 3369, "2524": 3370, "2525": 3371, "2526": 3372, "2527": 3371, "2528": 3373, "2529": 3373, "2530": 3381, "2531": 3382, "2532": 3383, "2533": 3384, "2534": 3385, "2535": 3386, "2536": 3387, "2537": 3386, "2538": 3388, "2539": 3388, "2540": 3392, "2541": 3393, "2542": 3394, "2543": 3395, "2544": 3396, "2545": 3397, "2546": 3398, "2547": 3397, "2548": 3399, "2549": 3399, "2550": 3405, "2551": 3406, "2552": 3407, "2553": 3408, "2554": 3409, "2555": 3410, "2556": 3411, "2557": 3410, "2558": 3412, "2559": 3412, "2560": 3418, "2561": 3418, "2562": 3422, "2563": 3422, "2564": 3430, "2565": 3431, "2566": 3432, "2567": 3433, "2568": 3434, "2569": 3435, "2570": 3436, "2571": 3437, "2572": 3436, "2573": 3438, "2574": 3438, "2575": 3446, "2576": 3447, "2577": 3448, "2578": 3449, "2579": 3450, "2580": 3451, "2581": 3452, "2582": 3451, "2583": 3453, "2584": 3453, "2585": 3457, "2586": 3458, "2587": 3459, "2588": 3460, "2589": 3461, "2590": 3462, "2591": 3463, "2592": 3462, "2593": 3464, "2594": 3464, "2595": 3470, "2596": 3471, "2597": 3472, "2598": 3473, "2599": 3474, "2600": 3475, "2601": 3476, "2602": 3475, "2603": 3477, "2604": 3477, "2605": 3484, "2606": 3484, "2607": 3488, "2608": 3488, "2609": 3494, "2610": 3494, "2611": 3498, "2612": 3498, "2613": 3504, "2614": 3504, "2615": 3508, "2616": 3508, "2617": 3513, "2618": 3514, "2619": 3515, "2620": 3516, "2621": 3517, "2622": 3518, "2623": 3519, "2624": 3518, "2625": 3520, "2626": 3520, "2627": 3524, "2628": 3525, "2629": 3526, "2630": 3527, "2631": 3528, "2632": 3529, "2633": 3530, "2634": 3529, "2635": 3531, "2636": 3531, "2637": 3536, "2638": 3537, "2639": 3538, "2640": 3539, "2641": 3540, "2642": 3541, "2643": 3542, "2644": 3541, "2645": 3544, "2646": 3544, "2647": 3554, "2648": 3554, "2649": 3560, "2650": 3560, "2651": 3573, "2652": 3574, "2653": 3575, "2654": 3576, "2655": 3577, "2656": 3578, "2657": 3579, "2658": 3580, "2659": 3581, "2660": 3580, "2661": 3582, "2662": 3582, "2663": 3590, "2664": 3591, "2665": 3592, "2666": 3593, "2667": 3594, "2668": 3595, "2669": 3596, "2670": 3595, "2671": 3597, "2672": 3597, "2673": 3601, "2674": 3602, "2675": 3603, "2676": 3604, "2677": 3605, "2678": 3606, "2679": 3607, "2680": 3606, "2681": 3608, "2682": 3608, "2683": 3614, "2684": 3614, "2685": 3620, "2686": 3621, "2687": 3621, "2688": 3622, "2689": 3623, "2690": 3624, "2691": 3625, "2692": 3626, "2693": 3627, "2694": 3628, "2695": 3629, "2696": 3630, "2697": 3631, "2698": 3632, "2699": 3633, "2700": 3634, "2701": 3635, "2702": 3636, "2703": 3637, "2704": 3638, "2705": 3637, "2706": 3638, "2707": 3638, "2708": 3638, "2709": 3638, "2710": 3638, "2711": 3638, "2712": 3640, "2713": 3648, "2714": 3649, "2715": 3650, "2716": 3651, "2717": 3652, "2718": 3653, "2719": 3654, "2720": 3653, "2721": 3655, "2722": 3655, "2723": 3663, "2724": 3664, "2725": 3665, "2726": 3666, "2727": 3667, "2728": 3668, "2729": 3669, "2730": 3668, "2731": 3670, "2732": 3670, "2733": 3674, "2734": 3675, "2735": 3676, "2736": 3677, "2737": 3678, "2738": 3679, "2739": 3680, "2740": 3679, "2741": 3681, "2742": 3681, "2743": 3687, "2744": 3687, "2745": 3689, "2746": 3689, "2747": 3697, "2748": 3698, "2749": 3699, "2750": 3700, "2751": 3701, "2752": 3702, "2753": 3703, "2754": 3702, "2755": 3704, "2756": 3704, "2757": 3712, "2758": 3713, "2759": 3714, "2760": 3715, "2761": 3716, "2762": 3717, "2763": 3718, "2764": 3717, "2765": 3719, "2766": 3719, "2767": 3723, "2768": 3724, "2769": 3725, "2770": 3726, "2771": 3727, "2772": 3728, "2773": 3729, "2774": 3728, "2775": 3730, "2776": 3730, "2777": 3736, "2778": 3736, "2779": 3741, "2780": 3741, "2781": 3749, "2782": 3750, "2783": 3751, "2784": 3752, "2785": 3753, "2786": 3754, "2787": 3755, "2788": 3754, "2789": 3756, "2790": 3756, "2791": 3764, "2792": 3765, "2793": 3766, "2794": 3767, "2795": 3768, "2796": 3769, "2797": 3770, "2798": 3769, "2799": 3771, "2800": 3771, "2801": 3775, "2802": 3776, "2803": 3777, "2804": 3778, "2805": 3779, "2806": 3780, "2807": 3781, "2808": 3780, "2809": 3782, "2810": 3782, "2811": 3788, "2812": 3788, "2813": 3792, "2814": 3792, "2815": 3800, "2816": 3801, "2817": 3802, "2818": 3803, "2819": 3804, "2820": 3805, "2821": 3806, "2822": 3807, "2823": 3806, "2824": 3808, "2825": 3808, "2826": 3816, "2827": 3817, "2828": 3818, "2829": 3819, "2830": 3820, "2831": 3821, "2832": 3822, "2833": 3821, "2834": 3823, "2835": 3823, "2836": 3827, "2837": 3828, "2838": 3829, "2839": 3830, "2840": 3831, "2841": 3832, "2842": 3833, "2843": 3832, "2844": 3834, "2845": 3834, "2846": 3840, "2847": 3840, "2848": 3848, "2849": 3849, "2850": 3855, "2853": 3856, "2854": 3857, "2855": 3857, "2856": 3858, "2857": 3859, "2858": 3860, "2859": 3861, "2860": 3862, "2861": 3863, "2862": 3864, "2863": 3865, "2864": 3864, "2865": 3868, "2866": 3868, "2867": 3868, "2868": 3868, "2869": 3868, "2870": 3868, "2871": 3870, "2872": 3870, "2873": 3870, "2874": 3870, "2875": 3870, "2876": 3870, "2877": 3873, "2878": 3873, "2879": 3873, "2880": 3873, "2881": 3873, "2882": 3873, "2883": 3878, "2884": 3878, "2885": 3879, "2886": 3879, "2887": 3879, "2888": 3879, "2889": 3879, "2890": 3879, "2891": 3879, "2892": 3879, "2893": 3881, "2894": 3881, "2897": 3887, "2898": 3889, "2899": 3894, "2900": 3895, "2901": 3896, "2902": 3897, "2903": 3898, "2904": 3899, "2905": 3900, "2906": 3899, "2907": 3901, "2908": 3901, "2909": 3905, "2910": 3906, "2911": 3907, "2912": 3908, "2913": 3909, "2914": 3910, "2915": 3911, "2916": 3910, "2917": 3912, "2918": 3912, "2919": 3927, "2922": 3928, "2923": 3928, "2924": 3929, "2925": 3930, "2926": 3931, "2927": 3932, "2928": 3933, "2929": 3934, "2930": 3933, "2931": 3934, "2932": 3935, "2933": 3936, "2934": 3937, "2935": 3938, "2936": 3939, "2937": 3940, "2938": 3939, "2939": 3941, "2940": 3941, "2941": 3941, "2942": 3941, "2943": 3942, "2944": 3942, "2945": 3942, "2946": 3942, "2947": 3942, "2948": 3942, "2949": 3943, "2950": 3943, "2951": 3943, "2952": 3943, "2953": 3943, "2954": 3943, "2955": 3944, "2956": 3944, "2957": 3946, "2958": 3946, "2959": 3947, "2960": 3947, "2961": 3947, "2962": 3947, "2963": 3947, "2964": 3947, "2965": 3950, "2966": 3950, "2967": 3951, "2968": 3951, "2969": 3951, "2970": 3951, "2971": 3951, "2972": 3951, "2973": 3954, "2974": 3955, "2975": 3955, "2976": 3955, "2977": 3957, "2978": 3957, "2979": 3958, "2980": 3958, "2981": 3958, "2982": 3958, "2983": 3958, "2984": 3958, "2985": 3961, "2986": 3961, "2987": 3962, "2988": 3962, "2989": 3962, "2990": 3962, "2991": 3962, "2992": 3962, "2993": 3966, "2994": 3967, "2995": 3967, "2996": 3967, "2997": 3969, "2998": 3969, "2999": 3970, "3000": 3970, "3001": 3970, "3002": 3970, "3003": 3970, "3004": 3970, "3005": 3973, "3006": 3973, "3007": 3974, "3008": 3974, "3009": 3974, "3010": 3974, "3011": 3974, "3012": 3974, "3013": 3978, "3014": 3979, "3015": 3979, "3016": 3979, "3017": 3981, "3018": 3981, "3019": 3982, "3020": 3982, "3021": 3982, "3022": 3982, "3023": 3982, "3024": 3982, "3025": 3985, "3026": 3985, "3027": 3986, "3028": 3986, "3029": 3986, "3030": 3986, "3031": 3986, "3032": 3986, "3033": 3990, "3034": 3991, "3035": 3991, "3036": 3991, "3037": 3993, "3038": 3993, "3039": 3994, "3040": 3994, "3041": 3994, "3042": 3994, "3043": 3994, "3044": 3994, "3045": 3997, "3046": 3997, "3047": 3998, "3048": 3998, "3049": 3998, "3050": 3998, "3051": 3998, "3052": 3998, "3053": 4002, "3054": 4002, "3055": 4002, "3056": 4004, "3057": 4004, "3058": 4004, "3059": 4004, "3060": 4005, "3061": 4005, "3062": 4005, "3063": 4005, "3064": 4005, "3065": 4005, "3066": 4008, "3067": 4008, "3068": 4009, "3069": 4009, "3070": 4009, "3071": 4009, "3072": 4009, "3073": 4009, "3074": 4012, "3075": 4013, "3076": 4014, "3077": 4015, "3078": 4016, "3079": 4017, "3080": 4018, "3081": 4017, "3082": 4018, "3083": 4018, "3084": 4018, "3085": 4018, "3086": 4019, "3087": 4019, "3088": 4019, "3089": 4019, "3090": 4019, "3091": 4019, "3092": 4019, "3093": 4019, "3096": 4025, "3097": 4027, "3100": 4028, "3101": 4028, "3102": 4029, "3103": 4030, "3104": 4031, "3105": 4032, "3106": 4033, "3107": 4034, "3108": 4033, "3109": 4035, "3110": 4035, "3111": 4035, "3112": 4035, "3113": 4036, "3114": 4036, "3115": 4036, "3116": 4036, "3117": 4036, "3118": 4036, "3119": 4037, "3120": 4037, "3121": 4037, "3122": 4037, "3123": 4037, "3124": 4037, "3125": 4038, "3126": 4038, "3127": 4040, "3128": 4040, "3129": 4041, "3130": 4041, "3131": 4041, "3132": 4041, "3133": 4041, "3134": 4041, "3135": 4044, "3136": 4044, "3137": 4045, "3138": 4045, "3139": 4045, "3140": 4045, "3141": 4045, "3142": 4045, "3143": 4048, "3144": 4049, "3145": 4049, "3146": 4049, "3147": 4051, "3148": 4051, "3149": 4052, "3150": 4052, "3151": 4052, "3152": 4052, "3153": 4052, "3154": 4052, "3155": 4055, "3156": 4055, "3157": 4056, "3158": 4056, "3159": 4056, "3160": 4056, "3161": 4056, "3162": 4056, "3163": 4060, "3164": 4061, "3165": 4061, "3166": 4061, "3167": 4063, "3168": 4063, "3169": 4064, "3170": 4064, "3171": 4064, "3172": 4064, "3173": 4064, "3174": 4064, "3175": 4067, "3176": 4067, "3177": 4068, "3178": 4068, "3179": 4068, "3180": 4068, "3181": 4068, "3182": 4068, "3183": 4072, "3184": 4073, "3185": 4073, "3186": 4073, "3187": 4075, "3188": 4075, "3189": 4076, "3190": 4076, "3191": 4076, "3192": 4076, "3193": 4076, "3194": 4076, "3195": 4079, "3196": 4079, "3197": 4080, "3198": 4080, "3199": 4080, "3200": 4080, "3201": 4080, "3202": 4080, "3203": 4084, "3204": 4085, "3205": 4085, "3206": 4085, "3207": 4087, "3208": 4087, "3209": 4088, "3210": 4088, "3211": 4088, "3212": 4088, "3213": 4088, "3214": 4088, "3215": 4091, "3216": 4091, "3217": 4092, "3218": 4092, "3219": 4092, "3220": 4092, "3221": 4092, "3222": 4092, "3223": 4096, "3224": 4096, "3225": 4096, "3226": 4098, "3227": 4098, "3228": 4098, "3229": 4098, "3230": 4099, "3231": 4099, "3232": 4099, "3233": 4099, "3234": 4099, "3235": 4099, "3236": 4102, "3237": 4102, "3238": 4103, "3239": 4103, "3240": 4103, "3241": 4103, "3242": 4103, "3243": 4103, "3244": 4106, "3245": 4107, "3246": 4108, "3247": 4109, "3248": 4110, "3249": 4111, "3250": 4112, "3251": 4111, "3252": 4112, "3253": 4112, "3254": 4112, "3255": 4112, "3256": 4113, "3257": 4113, "3258": 4113, "3259": 4113, "3260": 4113, "3261": 4113, "3262": 4113, "3263": 4113, "3266": 4119, "3267": 4125, "3268": 4126, "3269": 4129, "3270": 4129, "3271": 4139, "3272": 4139, "3273": 4148, "3274": 4149, "3275": 4152, "3276": 4152, "3277": 4160, "3278": 4161, "3279": 4164, "3280": 4164, "3281": 4172, "3282": 4173, "3283": 4176, "3284": 4176, "3285": 4183, "3286": 4186, "3287": 4186, "3288": 4193, "3289": 4194, "3290": 4198, "3291": 4198, "3292": 4200, "3293": 4200, "3294": 4205, "3295": 4206, "3296": 4210, "3297": 4210, "3298": 4212, "3299": 4212, "3300": 4217, "3301": 4218, "3302": 4222, "3303": 4222, "3304": 4224, "3305": 4224, "3306": 4229, "3307": 4230, "3308": 4235, "3309": 4235, "3310": 4237, "3311": 4237, "3312": 4245, "3313": 4246, "3314": 4247, "3315": 4247, "3316": 4249, "3317": 4249, "3318": 4250, "3319": 4250, "3320": 4250, "3321": 4250, "3322": 4250, "3323": 4250, "3324": 4253, "3325": 4253, "3326": 4254, "3327": 4254, "3328": 4254, "3329": 4254, "3330": 4254, "3331": 4254, "3332": 4257, "3333": 4257, "3334": 4258, "3335": 4258, "3336": 4258, "3337": 4258, "3338": 4258, "3339": 4258, "3340": 4259, "3341": 4259, "3342": 4260, "3343": 4260, "3344": 4260, "3345": 4260, "3346": 4260, "3347": 4260, "3348": 4265, "3349": 4284, "3350": 4284, "3351": 4286, "3352": 4286, "3353": 4295, "3354": 4295, "3355": 4301, "3356": 4301, "3357": 4317, "3358": 4318, "3359": 4319, "3360": 4319, "3361": 4320, "3362": 4320, "3363": 4320, "3364": 4320, "3365": 4320, "3366": 4320, "3367": 4323, "3368": 4332, "3369": 4332, "3370": 4332, "3371": 4332, "3372": 4332, "3373": 4332, "3374": 4332, "3375": 4332, "3376": 4332, "3377": 4332, "3378": 4333, "3379": 4333, "3380": 4333, "3381": 4333, "3387": 4338, "3391": 4338, "3392": 4339, "3393": 4339, "3399": 3393}}
__M_END_METADATA
"""
