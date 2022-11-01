def cont_log(self):
    """Setting up the log file, if self.use_log is set to true and self.loglevel is DEBUG OR INFO"""
    if self.use_log:
        if self.log_level == 'DEBUG':
            self.tl.basicConfig(filename=self.log_path, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.DEBUG)
        elif self.log_level == 'INFO':
            self.tl.basicConfig(filename=self.log_path, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.INFO)

def cont_notify(self):
    """Seting up to use pushover, if self.use_pushover is set to true and 
    if valid self.po_key and self.po_token is provided in the config file"""
    if self.use_pushover:
        self.poc = self.po.Pushover(self.po_token)

def cont_notify_summary(self):
    """Main notification method when the app is used in an automated fashion"""
    if self.use_pushover:
        self.poc.message(self.po_key,f"   \
        {self.extm}", title="--- crane summary ---")

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