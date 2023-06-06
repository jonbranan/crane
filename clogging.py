def cont_log(self):
    """Setting up the log file, if self.use_log is set to true and self.loglevel is DEBUG OR INFO"""
    if self.use_log:
        if self.log_level.lower() == 'debug':
            self.tl.basicConfig(filename=self.log_path, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.DEBUG)
        elif self.log_level.lower() == 'info':
            self.tl.basicConfig(filename=self.log_path, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.INFO)
        elif self.log_level.lower() == 'warn':
            self.tl.basicConfig(filename=self.log_path, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.WARN)
        elif self.log_level.lower() == 'error':
            self.tl.basicConfig(filename=self.log_path, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.ERROR)

def cont_notify(self):
    """Seting up to use pushover, if self.use_pushover is set to true and 
    if valid self.po_key and self.po_token is provided in the config file"""
    if self.use_pushover:
        self.poc = self.po.Pushover(self.po_token)

def cont_notify_summary(self, app_obj, req_obj):
    """Main notification method when the app is used in an automated fashion"""
    title = "--- crane summary ---"
    body = f'{self.extm}'
    if self.use_pushover:
        #TODO figure out why the flip it thinks its getting 4 pos args
        self.poc.message(self.po_key, message=body, title=title)
    if self.use_apprise:
        app_obj(req_obj, self.apprise_host, self.apprise_port, self.apprise_aurls, title, body)

def list_first_cont(self, index=0):
    """Only lists the first torrent"""
    self.tl.debug('First torrent in the list:')
    torrent = self.torrent_list[index]
    for k,v in torrent.items():
         self.tl.debug(f'{k}:  {v}')
    self.tl.debug('\n')

def get_script_runtime(self):
    elapsed_time = self.et - self.st
    if self.use_log:
        self.tl.info(f'Execution time: [{elapsed_time}]')
    if self.use_pushover:
        self.extm = f"Execution time: [{elapsed_time}]"
    if self.use_apprise:
        self.extm = f"Execution time: [{elapsed_time}]"

def send_ping(self, req_obj, healthcheck_url):
    try:
        req_obj.get(healthcheck_url, timeout=10)
    except req_obj.RequestException as e:
        self.tl.info(f"Ping failed: {e}")