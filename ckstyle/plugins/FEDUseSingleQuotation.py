from Base import *

class FEDUseSingleQuotation(RuleChecker):
    def __init__(self):
        self.id = 'single-quotation'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'replace " with \' in "${selector}"'

    def check(self, rule):
        if rule.value.find('"') != -1:
            return False

        return True
