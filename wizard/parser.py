# -*- encoding: utf-8 -*-
##############################################################################
#
#
##############################################################################
import jasper_reports
from osv import osv,fields 
import pooler
import datetime

def jasper_order_fornit( cr, uid, ids, data, context ):
    return {
        'parameters': {	
            'from_date': data['form']['from_date'],
            'to_date': data['form']['to_date'],
            'lingua': data['lang'],
            'company_id': data['form']['company_id'],
            'company_name': data['form']['company_name'],
        },
   }

jasper_reports.report_jasper(
    'report.ordinef',
    'purchase.order',
    parser=jasper_order_fornit
)