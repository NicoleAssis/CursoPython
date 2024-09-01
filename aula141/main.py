from log import LogFileMixin,LogPrintMixin

lp = LogPrintMixin()
lp.log_error('Error')
lp.log_sucess('Sucess')
lf = LogFileMixin()
lf.log_error('Qualquer Coisa')
lf.log_sucess('Que legal')


