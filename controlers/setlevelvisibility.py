# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:02:39 2021

@author: Nima
"""

class SetLevelVisibility():
    
    def setVisibility(self,resultLevel):
        
        if resultLevel == 1:
            
            self.ui.tabWidget.setTabEnabled(2,True)
            self.ui.tabWidget.setTabEnabled(3,True)
            self.ui.tabWidget.setTabEnabled(4,True)
        elif resultLevel == 0:
            
            self.ui.tabWidget.setTabEnabled(2,False)
            self.ui.tabWidget.setTabEnabled(3,False)
            self.ui.tabWidget.setTabEnabled(4,False)
        
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        
    
    def show_update_gp(self, numberComDatbase):
        
        
        if numberComDatbase == 0:
            self.ui.gp_update_agenacy.setVisible(False)
            self.ui.gp_update_customer.setVisible(False)
            self.ui.gp_update_account.setVisible(False)
            self.ui.gp_update_loan.setVisible(False)
            self.ui.gp_update_user.setVisible(False)
        elif numberComDatbase == 1:
            self.ui.gp_update_agenacy.setVisible(True)
            self.ui.gp_update_customer.setVisible(False)
            self.ui.gp_update_account.setVisible(False)
            self.ui.gp_update_loan.setVisible(False)
            self.ui.gp_update_user.setVisible(False)
        
        elif numberComDatbase == 2:
            self.ui.gp_update_agenacy.setVisible(False)
            self.ui.gp_update_customer.setVisible(True)
            self.ui.gp_update_account.setVisible(False)
            self.ui.gp_update_loan.setVisible(False)
            self.ui.gp_update_user.setVisible(False)
              
        elif numberComDatbase == 3:
            self.ui.gp_update_agenacy.setVisible(False)
            self.ui.gp_update_customer.setVisible(False)
            self.ui.gp_update_account.setVisible(True)
            self.ui.gp_update_loan.setVisible(False)
            self.ui.gp_update_user.setVisible(False)
            
        elif numberComDatbase == 4:
            self.ui.gp_update_agenacy.setVisible(False)
            self.ui.gp_update_customer.setVisible(False)
            self.ui.gp_update_account.setVisible(False)
            self.ui.gp_update_loan.setVisible(True)
            self.ui.gp_update_user.setVisible(False)
            
        elif numberComDatbase == 5:
            self.ui.gp_update_agenacy.setVisible(False)
            self.ui.gp_update_customer.setVisible(False)
            self.ui.gp_update_account.setVisible(False)
            self.ui.gp_update_loan.setVisible(False)
            self.ui.gp_update_user.setVisible(True)
            
    def show_delete_gp(self, numberComDatbase):
        
        self.ui.btn_save_excel.setText('Truncate table')
        if numberComDatbase == 0:
            self.ui.gp_delete_agency.setVisible(False)
            self.ui.gp_delete_customer.setVisible(False)
            self.ui.gp_delete_account.setVisible(False)
            self.ui.gp_delete_loan.setVisible(False)
            self.ui.gp_delete_user.setVisible(False)
            
        elif numberComDatbase == 1:
            self.ui.gp_delete_agency.setVisible(True)
            self.ui.gp_delete_customer.setVisible(False)
            self.ui.gp_delete_account.setVisible(False)
            self.ui.gp_delete_loan.setVisible(False)
            self.ui.gp_delete_user.setVisible(False)
        
        elif numberComDatbase == 2:
            self.ui.gp_delete_agency.setVisible(False)
            self.ui.gp_delete_customer.setVisible(True)
            self.ui.gp_delete_account.setVisible(False)
            self.ui.gp_delete_loan.setVisible(False)
            self.ui.gp_delete_user.setVisible(False)
              
        elif numberComDatbase == 3:
            self.ui.gp_delete_agency.setVisible(False)
            self.ui.gp_delete_customer.setVisible(False)
            self.ui.gp_delete_account.setVisible(True)
            self.ui.gp_delete_loan.setVisible(False)
            self.ui.gp_delete_user.setVisible(False)
            
        elif numberComDatbase == 4:
            self.ui.gp_delete_agency.setVisible(False)
            self.ui.gp_delete_customer.setVisible(False)
            self.ui.gp_delete_account.setVisible(False)
            self.ui.gp_delete_loan.setVisible(True)
            self.ui.gp_delete_user.setVisible(False)
        
        elif numberComDatbase == 5:
            self.ui.gp_delete_agency.setVisible(False)
            self.ui.gp_delete_customer.setVisible(False)
            self.ui.gp_delete_account.setVisible(False)
            self.ui.gp_delete_loan.setVisible(False)
            self.ui.gp_delete_user.setVisible(True)
            
    def show_insert_gp(self, numberComDatbase):

        if numberComDatbase == 0:
            self.ui.gp_agency.setVisible(False)
            self.ui.gp_customer.setVisible(False)
            self.ui.gp_account.setVisible(False)
            self.ui.gp_loan.setVisible(False)
            self.ui.gp_insert_user.setVisible(False)
        elif numberComDatbase == 1:
            self.ui.gp_agency.setVisible(True)
            self.ui.gp_customer.setVisible(False)
            self.ui.gp_account.setVisible(False)
            self.ui.gp_loan.setVisible(False)
            self.ui.gp_insert_user.setVisible(False)
        
        elif numberComDatbase == 2:
            self.ui.gp_agency.setVisible(False)
            self.ui.gp_customer.setVisible(True)
            self.ui.gp_account.setVisible(False)
            self.ui.gp_loan.setVisible(False)   
            self.ui.gp_insert_user.setVisible(False)
              
        elif numberComDatbase == 3:
            self.ui.gp_agency.setVisible(False)
            self.ui.gp_customer.setVisible(False)
            self.ui.gp_account.setVisible(True)
            self.ui.gp_loan.setVisible(False)
            self.ui.gp_insert_user.setVisible(False)
            
        elif numberComDatbase == 4:
            self.ui.gp_agency.setVisible(False)
            self.ui.gp_customer.setVisible(False)
            self.ui.gp_account.setVisible(False)
            self.ui.gp_loan.setVisible(True) 
            self.ui.gp_insert_user.setVisible(False)
            
        elif numberComDatbase == 5:
            self.ui.gp_agency.setVisible(False)
            self.ui.gp_customer.setVisible(False)
            self.ui.gp_account.setVisible(False)
            self.ui.gp_loan.setVisible(False) 
            self.ui.gp_insert_user.setVisible(True) 
            
    def set_visible_findbyid(self, numberComDatbase):
        if numberComDatbase == 0:
            self.ui.lb_find_id.setVisible(True)
            self.ui.et_find_by_id.setVisible(True)
            self.ui.lb_find_name.setVisible(True)
            self.ui.et_find_name.setVisible(True)
            self.ui.lb_find_name.setText('Name')
            
        elif numberComDatbase == 1:
            self.ui.lb_find_id.setVisible(True)
            self.ui.et_find_by_id.setVisible(True)
            self.ui.lb_find_name.setVisible(True)
            self.ui.et_find_name.setVisible(True)
            self.ui.lb_find_name.setText('Agency name')
            
        elif numberComDatbase == 2:
            self.ui.lb_find_id.setVisible(True)
            self.ui.et_find_by_id.setVisible(True)
            self.ui.lb_find_name.setVisible(True)
            self.ui.et_find_name.setVisible(True)
            self.ui.lb_find_name.setText('Customer name')
            
        elif numberComDatbase == 3:
            self.ui.lb_find_id.setVisible(True)
            self.ui.et_find_by_id.setVisible(True)
            self.ui.lb_find_name.setVisible(False)
            self.ui.et_find_name.setVisible(False)
            
        elif numberComDatbase == 4:
            self.ui.lb_find_id.setVisible(True)
            self.ui.et_find_by_id.setVisible(True)
            self.ui.lb_find_name.setVisible(False)
            self.ui.et_find_name.setVisible(False)
            
        elif numberComDatbase == 5:
            self.ui.lb_find_id.setVisible(True)
            self.ui.et_find_by_id.setVisible(True)
            self.ui.lb_find_name.setVisible(True)
            self.ui.et_find_name.setVisible(True)
            self.ui.lb_find_name.setText('Login name')
            
        
        
            